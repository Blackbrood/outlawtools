import asyncio
import os
import sys
import json
import random
import time
import logging
import threading
from datetime import datetime
from queue import Queue
from telethon import TelegramClient, functions, types, errors
from telegram import Update, Bot
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from colorama import init, Fore, Back, Style

# ================================================
# 🚀 REDX64 TELEGRAM REPORT BOT - COMPLETE SYSTEM
# 💎 One File Solution - Just Run and Use
# 👤 Developer: @REDX_64
# ================================================

# Initialize colors
init(autoreset=True)

class Colors:
    RESET = '\033[0m'
    BOLD = '\033[1m'
    RED = '\033[1;91m'
    GREEN = '\033[1;92m'
    YELLOW = '\033[1;93m'
    BLUE = '\033[1;94m'
    MAGENTA = '\033[1;95m'
    CYAN = '\033[1;96m'
    WHITE = '\033[1;97m'

# ==================== CONFIGURATION ====================
# Bot Token - @BotFather se le lo
BOT_TOKEN = "YOUR_BOT_TOKEN_HERE"  # ← YAHAN APNA BOT TOKEN DALO

# Accounts file
ACCOUNTS_FILE = "report_accounts.json"

# Session directory
SESSION_DIR = "telegram_sessions"

# Global variables
report_queue = Queue()
active_attacks = {}
attack_status = {}
accounts_list = []

# ==================== FILE MANAGEMENT ====================

def load_accounts():
    """Load reporting accounts from file"""
    global accounts_list
    try:
        if os.path.exists(ACCOUNTS_FILE):
            with open(ACCOUNTS_FILE, 'r', encoding='utf-8') as f:
                accounts_list = json.load(f)
                print(f"{Colors.GREEN}✅ Loaded {len(accounts_list)} reporting accounts")
                return True
        else:
            print(f"{Colors.YELLOW}⚠️  No accounts file found. Creating new one...")
            with open(ACCOUNTS_FILE, 'w', encoding='utf-8') as f:
                json.dump([], f)
            return False
    except Exception as e:
        print(f"{Colors.RED}❌ Error loading accounts: {e}")
        return False

def save_accounts():
    """Save accounts to file"""
    try:
        with open(ACCOUNTS_FILE, 'w', encoding='utf-8') as f:
            json.dump(accounts_list, f, indent=2, ensure_ascii=False)
        print(f"{Colors.GREEN}✅ Accounts saved to {ACCOUNTS_FILE}")
        return True
    except Exception as e:
        print(f"{Colors.RED}❌ Error saving accounts: {e}")
        return False

def add_account_interactive():
    """Interactive function to add new account"""
    print(f"\n{Colors.CYAN}{'='*50}")
    print(f"{Colors.WHITE}📱 ADD NEW REPORTING ACCOUNT")
    print(f"{Colors.CYAN}{'='*50}")
    
    print(f"\n{Colors.YELLOW}📝 Note: You need API credentials from my.telegram.org")
    print(f"{Colors.YELLOW}      (Not from @BotFather)")
    
    api_id = input(f"{Colors.GREEN}➤ API ID (7-8 digits): {Colors.WHITE}").strip()
    api_hash = input(f"{Colors.GREEN}➤ API Hash (32 chars): {Colors.WHITE}").strip()
    phone = input(f"{Colors.GREEN}➤ Phone (+countrycode): {Colors.WHITE}").strip()
    name = input(f"{Colors.GREEN}➤ Account nickname: {Colors.WHITE}").strip() or f"Account {len(accounts_list)+1}"
    
    # Validate
    if not api_id.isdigit() or len(api_id) < 7:
        print(f"{Colors.RED}❌ Invalid API ID")
        return False
    
    if len(api_hash) != 32:
        print(f"{Colors.RED}❌ Invalid API Hash (must be 32 characters)")
        return False
    
    if not phone.startswith('+'):
        print(f"{Colors.RED}❌ Phone must start with +countrycode")
        return False
    
    # Create account dict
    account = {
        "api_id": int(api_id),
        "api_hash": api_hash,
        "phone": phone,
        "name": name,
        "added_date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "reports_sent": 0,
        "status": "active"
    }
    
    # Test the account
    print(f"{Colors.YELLOW}🔄 Testing account credentials...")
    
    try:
        # Quick test
        async def test_acc():
            client = TelegramClient(
                os.path.join(SESSION_DIR, f"test_{phone}"),
                account['api_id'],
                account['api_hash']
            )
            await client.start(phone=phone)
            me = await client.get_me()
            await client.disconnect()
            return me.bot
        
        is_bot = asyncio.run(test_acc())
        
        if is_bot:
            print(f"{Colors.RED}❌ ERROR: This is a BOT account!")
            print(f"{Colors.YELLOW}ℹ️  Bot accounts cannot report users.")
            print(f"{Colors.YELLOW}ℹ️  Get USER API from my.telegram.org")
            return False
        
        print(f"{Colors.GREEN}✅ Account test successful!")
        
    except Exception as e:
        print(f"{Colors.RED}❌ Account test failed: {e}")
        retry = input(f"{Colors.YELLOW}➤ Add anyway? (y/n): {Colors.WHITE}").lower()
        if retry != 'y':
            return False
    
    # Add to list
    accounts_list.append(account)
    save_accounts()
    
    print(f"{Colors.GREEN}✅ Account '{name}' added successfully!")
    print(f"{Colors.CYAN}📊 Total accounts: {len(accounts_list)}")
    return True

# ==================== REPORT WORKER ====================

class ReportWorker:
    def __init__(self, bot_token):
        self.bot_token = bot_token
        self.running = True
        self.current_tasks = {}
        
    async def send_bot_message(self, chat_id, text):
        """Send message through bot"""
        try:
            bot = Bot(token=self.bot_token)
            await bot.send_message(chat_id=chat_id, text=text, parse_mode='HTML')
            return True
        except Exception as e:
            print(f"{Colors.RED}❌ Bot message error: {e}")
            return False
    
    async def process_single_report(self, account, target_username, reason_type, comment):
        """Send single report using an account"""
        try:
            # Create session name
            session_name = os.path.join(SESSION_DIR, account['phone'].replace('+', ''))
            
            # Create client
            client = TelegramClient(
                session_name,
                account['api_id'],
                account['api_hash']
            )
            
            # Connect
            await client.start(phone=account['phone'])
            
            # Get target
            target = await client.get_entity(target_username)
            
            # Map reason type to Telegram reason
            reason_map = {
                '1': types.InputReportReasonSpam(),
                '2': types.InputReportReasonViolence(),
                '3': types.InputReportReasonPornography(),
                '4': types.InputReportReasonChildAbuse(),
                '5': types.InputReportReasonCopyright(),
                '6': types.InputReportReasonFake(),
                '7': types.InputReportReasonGeoIrrelevant(),
                '8': types.InputReportReasonOther()
            }
            
            reason = reason_map.get(reason_type, types.InputReportReasonSpam())
            
            # Random comment if not provided
            if not comment:
                comments = [
                    "This account violates Telegram's Terms of Service",
                    "Spamming and harassing behavior detected",
                    "Sharing inappropriate and harmful content",
                    "Fake account impersonating someone",
                    "Promoting illegal activities and content",
                    "Mass messaging and advertisement spam",
                    "Sharing copyrighted material without permission",
                    "Engaging in hate speech and harassment"
                ]
                comment = f"{random.choice(comments)} | Ref: {random.randint(10000, 99999)}"
            
            # Send report
            result = await client(functions.account.ReportPeerRequest(
                peer=target,
                reason=reason,
                message=comment
            ))
            
            # Update account stats
            account['reports_sent'] = account.get('reports_sent', 0) + 1
            
            # Disconnect
            await client.disconnect()
            
            return True, "Report sent successfully"
            
        except errors.FloodWaitError as e:
            return False, f"Flood wait: {e.seconds} seconds"
        except errors.PeerIdInvalidError:
            return False, "Account not found (may be banned)"
        except errors.UserBannedError:
            return False, "Target account is banned"
        except Exception as e:
            return False, str(e)
    
    async def execute_attack(self, attack_id, target, report_type, count, chat_id):
        """Execute complete attack"""
        print(f"{Colors.GREEN}🚀 Starting attack {attack_id} on {target}")
        
        # Initialize status
        attack_status[attack_id] = {
            'target': target,
            'type': report_type,
            'total': count,
            'completed': 0,
            'successful': 0,
            'failed': 0,
            'start_time': time.time(),
            'active': True
        }
        
        # Notify start
        await self.send_bot_message(
            chat_id,
            f"⚡ <b>ATTACK STARTED</b>\n"
            f"🎯 Target: <code>{target}</code>\n"
            f"📊 Type: {report_type}\n"
            f"🔢 Reports: {count}\n"
            f"📈 Accounts: {len(accounts_list)}\n"
            f"⏱️ Estimated: {count*5} seconds"
        )
        
        # Execute reports
        for i in range(count):
            if not attack_status[attack_id]['active']:
                break
            
            # Select random account
            if not accounts_list:
                await self.send_bot_message(chat_id, "❌ No reporting accounts available!")
                break
            
            account = random.choice(accounts_list)
            
            # Update status
            attack_status[attack_id]['completed'] = i + 1
            
            # Send report
            success, message = await self.process_single_report(
                account, target, report_type, ""
            )
            
            if success:
                attack_status[attack_id]['successful'] += 1
                status_msg = f"✅ Report {i+1}/{count} successful"
            else:
                attack_status[attack_id]['failed'] += 1
                status_msg = f"❌ Report {i+1}/{count} failed: {message}"
            
            # Send progress every 10 reports
            if (i + 1) % 10 == 0 or (i + 1) == count:
                progress = attack_status[attack_id]
                elapsed = time.time() - progress['start_time']
                
                await self.send_bot_message(
                    chat_id,
                    f"📊 <b>PROGRESS UPDATE</b>\n"
                    f"🎯 Target: <code>{target}</code>\n"
                    f"✅ Completed: {progress['completed']}/{progress['total']}\n"
                    f"📈 Success: {progress['successful']}\n"
                    f"❌ Failed: {progress['failed']}\n"
                    f"⏱️ Time: {int(elapsed)}s\n"
                    f"⚡ Speed: {(progress['completed']/elapsed*60 if elapsed>0 else 0):.1f}/min"
                )
            
            # Random delay (2-8 seconds)
            await asyncio.sleep(random.uniform(2, 8))
        
        # Final report
        progress = attack_status[attack_id]
        elapsed = time.time() - progress['start_time']
        success_rate = (progress['successful'] / progress['completed'] * 100) if progress['completed'] > 0 else 0
        
        await self.send_bot_message(
            chat_id,
            f"🎯 <b>ATTACK COMPLETED</b>\n"
            f"Target: <code>{target}</code>\n"
            f"✅ Successful: {progress['successful']}\n"
            f"❌ Failed: {progress['failed']}\n"
            f"📊 Success Rate: {success_rate:.1f}%\n"
            f"⏱️ Total Time: {int(elapsed//60)}m {int(elapsed%60)}s\n"
            f"⚡ Avg Speed: {(progress['completed']/elapsed*60 if elapsed>0 else 0):.1f} reports/min\n\n"
            f"{'🎉 HIGH IMPACT! Account should be restricted!' if progress['successful'] > 20 else '⚠️  Moderate impact'}"
        )
        
        # Save accounts stats
        save_accounts()
        
        # Mark as inactive
        attack_status[attack_id]['active'] = False
    
    async def worker_loop(self):
        """Main worker loop to process attack queue"""
        while self.running:
            try:
                if not report_queue.empty():
                    task = report_queue.get()
                    
                    attack_id = task['attack_id']
                    target = task['target']
                    report_type = task['type']
                    count = task['count']
                    chat_id = task['chat_id']
                    
                    # Execute attack
                    await self.execute_attack(attack_id, target, report_type, count, chat_id)
                    
                    report_queue.task_done()
                
                await asyncio.sleep(1)
                
            except Exception as e:
                print(f"{Colors.RED}❌ Worker error: {e}")
                await asyncio.sleep(5)
    
    def start(self):
        """Start worker in background"""
        thread = threading.Thread(target=lambda: asyncio.run(self.worker_loop()))
        thread.daemon = True
        thread.start()
        print(f"{Colors.GREEN}✅ Report Worker started")
    
    def stop(self):
        """Stop worker"""
        self.running = False

# ==================== TELEGRAM BOT ====================

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Start command handler"""
    user = update.effective_user
    welcome_text = f"""
🤖 <b>REDX64 REPORT BOT v2.0</b>
👤 Welcome <b>{user.first_name}</b>!

⚡ <b>FEATURES:</b>
• Mass reporting with multiple accounts
• Real-time progress tracking
• Multiple report types
• Auto account rotation
• Anti-detection delays

📊 <b>STATS:</b>
• Accounts Loaded: <b>{len(accounts_list)}</b>
• Active Attacks: <b>{len([a for a in attack_status.values() if a.get('active', False)])}</b>

📋 <b>COMMANDS:</b>
/report - Start new attack
/status - Check attack status
/stop - Stop all attacks
/accounts - Manage reporting accounts
/stats - Show statistics
/help - Show detailed help

⚠️  <b>WARNING:</b>
Only report accounts violating Telegram ToS!
Misuse may result in account bans.

👤 Developer: @REDX_64
    """
    await update.message.reply_text(welcome_text, parse_mode='HTML')

async def report_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Start reporting command"""
    if not context.args:
        await update.message.reply_text(
            "❌ Usage: <code>/report @username</code>\n"
            "Example: <code>/report @spammer123</code>",
            parse_mode='HTML'
        )
        return
    
    if len(accounts_list) == 0:
        await update.message.reply_text(
            "❌ No reporting accounts configured!\n"
            "Use /accounts to add reporting accounts first."
        )
        return
    
    target = context.args[0].replace('@', '')
    
    # Store target
    context.user_data['target'] = target
    context.user_data['step'] = 'awaiting_type'
    
    # Create inline keyboard for report types
    from telegram import InlineKeyboardButton, InlineKeyboardMarkup
    
    keyboard = [
        [
            InlineKeyboardButton("1️⃣ Spam", callback_data="type_1"),
            InlineKeyboardButton("2️⃣ Violence", callback_data="type_2"),
            InlineKeyboardButton("3️⃣ Porn", callback_data="type_3"),
        ],
        [
            InlineKeyboardButton("4️⃣ Child Abuse", callback_data="type_4"),
            InlineKeyboardButton("5️⃣ Copyright", callback_data="type_5"),
            InlineKeyboardButton("6️⃣ Fake", callback_data="type_6"),
        ],
        [
            InlineKeyboardButton("7️⃣ Illegal", callback_data="type_7"),
            InlineKeyboardButton("8️⃣ Other", callback_data="type_8"),
            InlineKeyboardButton("🔄 Random", callback_data="type_random"),
        ]
    ]
    
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await update.message.reply_text(
        f"🎯 <b>Target Selected:</b> @{target}\n\n"
        f"📋 <b>Select Report Type:</b>\n"
        f"Choose the violation type to report",
        reply_markup=reply_markup,
        parse_mode='HTML'
    )

async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle inline button clicks"""
    query = update.callback_query
    await query.answer()
    
    user_id = update.effective_user.id
    data = query.data
    
    if data.startswith("type_"):
        report_type = data.split("_")[1]
        
        if 'target' not in context.user_data:
            await query.edit_message_text("❌ Session expired. Start again with /report")
            return
        
        target = context.user_data['target']
        context.user_data['report_type'] = report_type
        context.user_data['step'] = 'awaiting_count'
        
        # Ask for number of reports
        await query.edit_message_text(
            f"✅ <b>Type Selected:</b> {report_type}\n"
            f"🎯 <b>Target:</b> @{target}\n\n"
            f"🔢 <b>Enter number of reports (1-500):</b>\n"
            f"Recommended: 50-100 for good impact",
            parse_mode='HTML'
        )
    
    elif data == "confirm_yes":
        # Start the attack
        if all(key in context.user_data for key in ['target', 'report_type', 'count']):
            target = context.user_data['target']
            report_type = context.user_data['report_type']
            count = context.user_data['count']
            
            # Generate attack ID
            attack_id = f"{user_id}_{int(time.time())}"
            
            # Add to queue
            report_queue.put({
                'attack_id': attack_id,
                'target': target,
                'type': report_type,
                'count': count,
                'chat_id': query.message.chat_id
            })
            
            await query.edit_message_text(
                f"🚀 <b>ATTACK QUEUED!</b>\n"
                f"🎯 Target: @{target}\n"
                f"📊 Type: {report_type}\n"
                f"🔢 Reports: {count}\n"
                f"👥 Accounts: {len(accounts_list)}\n\n"
                f"⏳ <i>Processing will start shortly...</i>\n"
                f"Use /status to track progress",
                parse_mode='HTML'
            )
            
            # Clear user data
            context.user_data.clear()
        
    elif data == "confirm_no":
        await query.edit_message_text("🚫 Attack cancelled")
        context.user_data.clear()

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle text messages"""
    text = update.message.text
    user_id = update.effective_user.id
    
    # Check if waiting for report count
    if 'step' in context.user_data and context.user_data['step'] == 'awaiting_count':
        try:
            count = int(text)
            if 1 <= count <= 500:
                target = context.user_data['target']
                report_type = context.user_data['report_type']
                context.user_data['count'] = count
                context.user_data['step'] = 'awaiting_confirm'
                
                # Create confirmation keyboard
                from telegram import InlineKeyboardButton, InlineKeyboardMarkup
                
                keyboard = [
                    [
                        InlineKeyboardButton("✅ YES, START ATTACK", callback_data="confirm_yes"),
                        InlineKeyboardButton("❌ NO, CANCEL", callback_data="confirm_no")
                    ]
                ]
                reply_markup = InlineKeyboardMarkup(keyboard)
                
                estimated_time = count * 5
                minutes = estimated_time // 60
                seconds = estimated_time % 60
                
                await update.message.reply_text(
                    f"⚡ <b>ATTACK CONFIRMATION</b>\n\n"
                    f"🎯 <b>Target:</b> @{target}\n"
                    f"📊 <b>Type:</b> {report_type}\n"
                    f"🔢 <b>Reports:</b> {count}\n"
                    f"👥 <b>Accounts:</b> {len(accounts_list)}\n"
                    f"⏱️ <b>Est. Time:</b> {minutes}m {seconds}s\n\n"
                    f"⚠️  <b>WARNING:</b> This will send {count} reports!\n"
                    f"Are you sure you want to continue?",
                    reply_markup=reply_markup,
                    parse_mode='HTML'
                )
            else:
                await update.message.reply_text("❌ Please enter number between 1-500")
        except ValueError:
            await update.message.reply_text("❌ Please enter a valid number")
    
    # Handle other messages
    else:
        await update.message.reply_text(
            "🤖 Use /report to start an attack\n"
            "Use /help for all commands"
        )

async def status_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Check attack status"""
    user_id = update.effective_user.id
    
    # Find user's active attacks
    user_attacks = []
    for attack_id, attack in attack_status.items():
        if attack_id.startswith(str(user_id)) and attack.get('active', False):
            user_attacks.append((attack_id, attack))
    
    if not user_attacks:
        await update.message.reply_text("📭 No active attacks found")
        return
    
    status_text = "📊 <b>ACTIVE ATTACKS STATUS</b>\n\n"
    
    for attack_id, attack in user_attacks:
        elapsed = time.time() - attack['start_time']
        progress = (attack['completed'] / attack['total']) * 100 if attack['total'] > 0 else 0
        
        status_text += (
            f"🎯 <b>Target:</b> @{attack['target']}\n"
            f"📈 <b>Progress:</b> {attack['completed']}/{attack['total']} ({progress:.1f}%)\n"
            f"✅ <b>Success:</b> {attack['successful']}\n"
            f"❌ <b>Failed:</b> {attack['failed']}\n"
            f"⏱️ <b>Time:</b> {int(elapsed//60)}m {int(elapsed%60)}s\n"
            f"⚡ <b>Speed:</b> {(attack['completed']/elapsed*60 if elapsed>0 else 0):.1f}/min\n"
            f"{'─'*30}\n"
        )
    
    status_text += f"\n📈 <b>Total Active:</b> {len(user_attacks)} attack(s)"
    
    await update.message.reply_text(status_text, parse_mode='HTML')

async def stop_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Stop all attacks"""
    user_id = update.effective_user.id
    
    stopped = 0
    for attack_id in list(attack_status.keys()):
        if attack_id.startswith(str(user_id)):
            attack_status[attack_id]['active'] = False
            stopped += 1
    
    if stopped > 0:
        await update.message.reply_text(f"🛑 Stopped {stopped} active attack(s)")
    else:
        await update.message.reply_text("❌ No active attacks to stop")

async def accounts_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Manage accounts"""
    if not context.args:
        # Show accounts list
        if len(accounts_list) == 0:
            await update.message.reply_text(
                "❌ No accounts configured!\n\n"
                "To add account:\n"
                "<code>/accounts add</code>\n\n"
                "You need API credentials from my.telegram.org",
                parse_mode='HTML'
            )
            return
        
        accounts_text = f"📱 <b>REPORTING ACCOUNTS</b>\n\n"
        accounts_text += f"📊 Total: <b>{len(accounts_list)}</b> accounts\n\n"
        
        for i, acc in enumerate(accounts_list[:10], 1):  # Show first 10
            accounts_text += (
                f"<b>{i}. {acc['name']}</b>\n"
                f"   📞 {acc['phone']}\n"
                f"   📨 Reports: {acc.get('reports_sent', 0)}\n"
                f"   📅 Added: {acc.get('added_date', 'N/A')}\n\n"
            )
        
        if len(accounts_list) > 10:
            accounts_text += f"... and {len(accounts_list)-10} more accounts\n\n"
        
        accounts_text += (
            f"🔧 <b>Commands:</b>\n"
            f"<code>/accounts add</code> - Add new account\n"
            f"<code>/accounts remove 1</code> - Remove account #1\n"
            f"<code>/accounts test</code> - Test all accounts\n"
            f"<code>/accounts stats</code> - Detailed statistics"
        )
        
        await update.message.reply_text(accounts_text, parse_mode='HTML')
        return
    
    # Handle subcommands
    subcommand = context.args[0].lower()
    
    if subcommand == "add":
        # Send instructions
        await update.message.reply_text(
            "📝 <b>ADDING NEW ACCOUNT</b>\n\n"
            "1. Go to <b>my.telegram.org</b>\n"
            "2. Login with your Telegram account\n"
            "3. Click <b>API Development Tools</b>\n"
            "4. Create new application\n"
            "5. Copy <b>api_id</b> and <b>api_hash</b>\n\n"
            "⚠️  <b>IMPORTANT:</b>\n"
            "• Use REAL user account (not bot)\n"
            "• Platform: Desktop\n"
            "• Account should be at least 1 week old\n\n"
            "Send me the details in this format:\n"
            "<code>api_id api_hash phone name</code>\n\n"
            "Example:\n"
            "<code>12345678 abcdef1234567890abcdef1234567890 +919876543210 MyAccount</code>",
            parse_mode='HTML'
        )
        
        context.user_data['awaiting_account'] = True
    
    elif subcommand == "remove" and len(context.args) > 1:
        try:
            index = int(context.args[1]) - 1
            if 0 <= index < len(accounts_list):
                removed = accounts_list.pop(index)
                save_accounts()
                await update.message.reply_text(
                    f"✅ Removed account: {removed['name']}\n"
                    f"📞 Phone: {removed['phone']}"
                )
            else:
                await update.message.reply_text("❌ Invalid account number")
        except ValueError:
            await update.message.reply_text("❌ Please enter valid number")
    
    elif subcommand == "test":
        await update.message.reply_text("🔄 Testing all accounts...")
        
        # Test in background
        async def test_accounts():
            results = []
            for acc in accounts_list:
                try:
                    client = TelegramClient(
                        os.path.join(SESSION_DIR, f"test_{acc['phone'].replace('+', '')}"),
                        acc['api_id'],
                        acc['api_hash']
                    )
                    await client.start(phone=acc['phone'])
                    me = await client.get_me()
                    await client.disconnect()
                    
                    if me.bot:
                        results.append(f"❌ {acc['name']} - BOT (cannot report)")
                    else:
                        results.append(f"✅ {acc['name']} - OK")
                except Exception as e:
                    results.append(f"❌ {acc['name']} - Error: {str(e)[:50]}")
            
            # Send results
            result_text = "🧪 <b>ACCOUNT TEST RESULTS</b>\n\n"
            result_text += "\n".join(results[:20])  # Limit to 20
            
            if len(results) > 20:
                result_text += f"\n\n... and {len(results)-20} more"
            
            await context.bot.send_message(
                chat_id=update.effective_chat.id,
                text=result_text,
                parse_mode='HTML'
            )
        
        # Run in background
        asyncio.create_task(test_accounts())
    
    elif subcommand == "stats":
        total_reports = sum(acc.get('reports_sent', 0) for acc in accounts_list)
        avg_reports = total_reports / len(accounts_list) if accounts_list else 0
        
        stats_text = (
            f"📊 <b>ACCOUNTS STATISTICS</b>\n\n"
            f"📈 Total Accounts: {len(accounts_list)}\n"
            f"📨 Total Reports Sent: {total_reports}\n"
            f"📊 Avg Reports/Account: {avg_reports:.1f}\n\n"
            f"🏆 <b>Top Performers:</b>\n"
        )
        
        # Sort by reports sent
        sorted_accounts = sorted(accounts_list, key=lambda x: x.get('reports_sent', 0), reverse=True)
        
        for i, acc in enumerate(sorted_accounts[:5], 1):
            stats_text += f"{i}. {acc['name']}: {acc.get('reports_sent', 0)} reports\n"
        
        await update.message.reply_text(stats_text, parse_mode='HTML')

async def stats_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Show bot statistics"""
    total_attacks = len(attack_status)
    active_attacks_count = len([a for a in attack_status.values() if a.get('active', False)])
    
    total_reports_sent = 0
    total_reports_success = 0
    
    for attack in attack_status.values():
        total_reports_sent += attack.get('completed', 0)
        total_reports_success += attack.get('successful', 0)
    
    success_rate = (total_reports_success / total_reports_sent * 100) if total_reports_sent > 0 else 0
    
    stats_text = (
        f"📈 <b>BOT STATISTICS</b>\n\n"
        f"🤖 Bot Status: <b>Online</b>\n"
        f"📊 Total Attacks: {total_attacks}\n"
        f"⚡ Active Attacks: {active_attacks_count}\n"
        f"📨 Total Reports Sent: {total_reports_sent}\n"
        f"✅ Successful Reports: {total_reports_success}\n"
        f"📈 Success Rate: {success_rate:.1f}%\n"
        f"📱 Available Accounts: {len(accounts_list)}\n\n"
        f"👤 Developer: @REDX_64\n"
        f"🕒 Uptime: {int(time.time() - start_time)} seconds"
    )
    
    await update.message.reply_text(stats_text, parse_mode='HTML')

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Help command"""
    help_text = """
🤖 <b>REDX64 REPORT BOT - HELP GUIDE</b>

⚡ <b>MAIN COMMANDS:</b>
<code>/report @username</code> - Start reporting attack
<code>/status</code> - Check attack progress
<code>/stop</code> - Stop all attacks
<code>/stats</code> - Show bot statistics

📱 <b>ACCOUNT MANAGEMENT:</b>
<code>/accounts</code> - List all accounts
<code>/accounts add</code> - Add new account
<code>/accounts remove 1</code> - Remove account #1
<code>/accounts test</code> - Test all accounts
<code>/accounts stats</code> - Account statistics

🎯 <b>REPORT TYPES:</b>
1. Spam - Unwanted messages
2. Violence - Threats/Harm
3. Porn - Adult content
4. Child Abuse - Minor exploitation
5. Copyright - Content theft
6. Fake - Impersonation
7. Illegal - Illegal activities
8. Other - Miscellaneous
9. Random - Mix all types

⚠️ <b>IMPORTANT NOTES:</b>
• Only report violating accounts
• Use multiple accounts for better effect
• Accounts need API from my.telegram.org
• Bot accounts cannot report users
• False reporting may get your accounts banned

🔧 <b>SETUP GUIDE:</b>
1. Get Bot Token from @BotFather
2. Add to BOT_TOKEN in code
3. Add reporting accounts with /accounts add
4. Start attacks with /report

👤 <b>Developer:</b> @REDX_64
📢 <b>Channel:</b> t.me/REDX64
    """
    await update.message.reply_text(help_text, parse_mode='HTML')

async def error_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Error handler"""
    print(f"{Colors.RED}❌ Update {update} caused error {context.error}")
    
    try:
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="❌ An error occurred. Please try again."
        )
    except:
        pass

# ==================== MAIN SYSTEM ====================

def setup_directories():
    """Create necessary directories"""
    if not os.path.exists(SESSION_DIR):
        os.makedirs(SESSION_DIR)
        print(f"{Colors.GREEN}✅ Created session directory: {SESSION_DIR}")

def print_banner():
    """Print startup banner"""
    clear = lambda: os.system('cls' if os.name == 'nt' else 'clear')
    clear()
    
    banner = f"""
{Colors.RED}{'═'*60}
{Colors.RED}╔{'═'*58}╗
{Colors.RED}║{Colors.WHITE}{'🚀 REDX64 TELEGRAM REPORT SYSTEM 🚀'.center(58)}{Colors.RED}║
{Colors.RED}║{Colors.WHITE}{'💀 COMPLETE ONE-FILE SOLUTION 💀'.center(58)}{Colors.RED}║
{Colors.RED}║{Colors.WHITE}{'👤 Developer: @REDX_64'.center(58)}{Colors.RED}║
{Colors.RED}╚{'═'*58}╝
{Colors.RED}{'═'*60}

{Colors.CYAN}📊 STATUS:{Colors.WHITE}
• Bot Token: {'✅ SET' if BOT_TOKEN != "YOUR_BOT_TOKEN_HERE" else '❌ NOT SET'}
• Accounts: {len(accounts_list)} loaded
• Session Dir: {SESSION_DIR}

{Colors.YELLOW}⚡ INSTRUCTIONS:{Colors.WHITE}
1. Replace BOT_TOKEN with your token
2. Add accounts with /accounts add command
3. Start attacks with /report @username

{Colors.GREEN}📱 BOT COMMANDS:{Colors.WHITE}
/report - Start attack
/status - Check progress
/accounts - Manage accounts
/help - Show help

{Colors.MAGENTA}⚠️  WARNING: Use responsibly! Only report violating accounts.
{Colors.RED}{'═'*60}
    """
    print(banner)

def start_bot():
    """Start the Telegram bot"""
    print(f"{Colors.YELLOW}🚀 Starting Telegram Bot...")
    
    # Create application
    app = Application.builder().token(BOT_TOKEN).build()
    
    # Add handlers
    app.add_handler(CommandHandler("start", start_command))
    app.add_handler(CommandHandler("report", report_command))
    app.add_handler(CommandHandler("status", status_command))
    app.add_handler(CommandHandler("stop", stop_command))
    app.add_handler(CommandHandler("accounts", accounts_command))
    app.add_handler(CommandHandler("stats", stats_command))
    app.add_handler(CommandHandler("help", help_command))
    
    # Add callback query handler
    from telegram.ext import CallbackQueryHandler
    app.add_handler(CallbackQueryHandler(button_handler))
    
    # Add message handler
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    
    # Add error handler
    app.add_error_handler(error_handler)
    
    print(f"{Colors.GREEN}✅ Bot started successfully!")
    print(f"{Colors.CYAN}📱 Open Telegram and search for your bot")
    print(f"{Colors.YELLOW}⚡ Use /help for commands")
    
    # Start polling
    app.run_polling(allowed_updates=Update.ALL_TYPES)

def main():
    """Main function"""
    global start_time
    start_time = time.time()
    
    # Setup
    setup_directories()
    load_accounts()
    print_banner()
    
    # Check bot token
    if BOT_TOKEN == "YOUR_BOT_TOKEN_HERE":
        print(f"{Colors.RED}❌ ERROR: Bot token not set!")
        print(f"{Colors.YELLOW}ℹ️  Get token from @BotFather and replace in code")
        print(f"{Colors.CYAN}1. Search @BotFather in Telegram")
        print(f"{Colors.CYAN}2. Send /newbot")
        print(f"{Colors.CYAN}3. Follow instructions")
        print(f"{Colors.CYAN}4. Copy token and paste in BOT_TOKEN variable")
        input(f"\n{Colors.YELLOW}Press Enter to exit...")
        return
    
    # Check accounts
    if len(accounts_list) == 0:
        print(f"{Colors.YELLOW}⚠️  No reporting accounts found!")
        print(f"{Colors.CYAN}Add accounts using /accounts add command in bot")
    
    # Start report worker
    worker = ReportWorker(BOT_TOKEN)
    worker.start()
    
    # Start bot
    try:
        start_bot()
    except KeyboardInterrupt:
        print(f"\n{Colors.RED}🛑 Bot stopped by user")
    except Exception as e:
        print(f"\n{Colors.RED}❌ Error: {e}")
    
    worker.stop()
    
    # Save before exit
    save_accounts()
    print(f"{Colors.GREEN}✅ System shutdown complete")

if __name__ == "__main__":
    main()