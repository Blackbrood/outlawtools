import asyncio
import os
import sys
import random
import time
from datetime import datetime
from telethon import TelegramClient, functions, types, errors
from colorama import init, Fore, Back, Style

# ================================================
# 🚀 Tool developed by REDX_64 🚀
# 💎 Updates channel: https://t.me/REDX_64 💎
# ================================================

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

# ==================== YAHAN APNI API CREDENTIALS DALO ====================
# my.telegram.org se leke aao
api_id = 12345678  # ← YAHAN APNA API ID DALO (7-8 digits)
api_hash = 'abcdef1234567890abcdef1234567890'  # ← YAHAN APNA API HASH DALO (32 chars)
# =========================================================================

session_name = 'redx_reporter'

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_banner():
    clear_screen()
    print(f"{Colors.RED}{'═' * 60}")
    print(f"{Colors.RED}╔{'═' * 58}╗")
    print(f"{Colors.RED}║{Colors.WHITE}{'🚀 REDX64 REPORT BOT 🚀'.center(58)}{Colors.RED}║")
    print(f"{Colors.RED}║{Colors.WHITE}{'💀 ACCOUNT DESTROYER MODE 💀'.center(58)}{Colors.RED}║")
    print(f"{Colors.RED}║{Colors.WHITE}{'👤 Developer: @REDX_64'.center(58)}{Colors.RED}║")
    print(f"{Colors.RED}╚{'═' * 58}╝")
    print(f"{Colors.RED}{'═' * 60}\n")

def print_status(msg, status="info"):
    timestamp = datetime.now().strftime("%H:%M:%S")
    if status == "success":
        print(f"{Colors.GREEN}[{timestamp}] ✅ {msg}")
    elif status == "error":
        print(f"{Colors.RED}[{timestamp}] ❌ {msg}")
    elif status == "warning":
        print(f"{Colors.YELLOW}[{timestamp}] ⚠️  {msg}")
    else:
        print(f"{Colors.CYAN}[{timestamp}] ℹ️  {msg}")

async def check_account_status(client, target_id):
    """Check if target account still exists"""
    try:
        entity = await client.get_entity(target_id)
        return True, entity
    except errors.rpcerrorlist.UserIdInvalidError:
        return False, None
    except errors.rpcerrorlist.PeerIdInvalidError:
        return False, None
    except Exception:
        return True, None

async def send_single_report(client, target_entity, report_type, comment):
    """Send single report with error handling"""
    try:
        # Map report types
        reason_map = {
            "1": types.InputReportReasonSpam(),
            "2": types.InputReportReasonViolence(),
            "3": types.InputReportReasonPornography(),
            "4": types.InputReportReasonChildAbuse(),
            "5": types.InputReportReasonCopyright(),
            "6": types.InputReportReasonFake(),
            "7": types.InputReportReasonGeoIrrelevant(),
            "8": types.InputReportReasonOther()
        }
        
        reason = reason_map.get(report_type, types.InputReportReasonSpam())
        
        # Send report
        result = await client(functions.account.ReportPeerRequest(
            peer=target_entity,
            reason=reason,
            message=comment
        ))
        
        return True, "Report sent successfully"
        
    except errors.FloodWaitError as e:
        return False, f"Flood wait: {e.seconds} seconds"
    except errors.rpcerrorlist.PeerIdInvalidError:
        return False, "Account not found (possibly banned)"
    except Exception as e:
        return False, str(e)

async def continuous_report_attack(client, target_input):
    """Main attack function - reports continuously"""
    print_banner()
    
    # Get target entity
    try:
        target_entity = await client.get_entity(target_input)
        target_name = target_entity.first_name if hasattr(target_entity, 'first_name') else target_entity.title
        target_id = target_entity.id
        
        print_status(f"Target found: {target_name} (ID: {target_id})", "success")
        
    except Exception as e:
        print_status(f"Error finding target: {e}", "error")
        return
    
    # Get reporting parameters
    print(f"\n{Colors.YELLOW}{'═' * 60}")
    print(f"{Colors.CYAN}⚡ REPORTING CONFIGURATION")
    print(f"{Colors.YELLOW}{'═' * 60}")
    
    print(f"\n{Colors.GREEN}Report Types:")
    print(f"1. Spam 📩    2. Violence ⚔️    3. Pornography 🔞")
    print(f"4. Child Abuse 🚸  5. Copyright ©️  6. Fake 👤")
    print(f"7. Illegal 🚫     8. Other 📝    9. Random 🔄")
    
    report_type = input(f"\n{Colors.YELLOW}➤ Select report type (1-9, default 9): ") or "9"
    
    comment = input(f"{Colors.YELLOW}➤ Custom comment (press Enter for auto): ")
    
    print(f"\n{Colors.RED}⚠️  WARNING: This is DESTROY MODE")
    print(f"{Colors.RED}⚠️  Will report continuously until account banned")
    
    confirm = input(f"\n{Colors.YELLOW}➤ Start DESTROY mode? (y/n): ")
    if confirm.lower() != 'y':
        print_status("Operation cancelled", "warning")
        return
    
    # Start attack
    print(f"\n{Colors.RED}{'═' * 60}")
    print(f"{Colors.RED}🚀 STARTING DESTROY ATTACK")
    print(f"{Colors.RED}{'═' * 60}")
    
    total_reports = 0
    successful_reports = 0
    failed_reports = 0
    start_time = time.time()
    
    # Predefined comments for each report type
    comments = {
        "1": ["Spamming links", "Mass messaging", "Advertising", "Bot behavior"],
        "2": ["Threats of violence", "Promoting terrorism", "Harmful content", "Extremist"],
        "3": ["Adult content", "Pornographic material", "NSFW", "Explicit content"],
        "4": ["Child exploitation", "Minor abuse", "Underage content", "Pedophilic"],
        "5": ["Copyright infringement", "Piracy", "Stolen content", "Illegal sharing"],
        "6": ["Fake account", "Impersonation", "Scammer", "Identity theft"],
        "7": ["Illegal activities", "Drugs selling", "Weapons trading", "Crime"],
        "8": ["Harassment", "Hate speech", "Scam", "Fraud"]
    }
    
    try:
        attack_number = 0
        while True:
            attack_number += 1
            
            # Check if account still exists
            account_exists, _ = await check_account_status(client, target_id)
            if not account_exists:
                print_status(f"🎯 TARGET BANNED! MISSION ACCOMPLISHED!", "success")
                print_status(f"Total attacks: {attack_number-1}", "success")
                break
            
            # Select random report type if needed
            if report_type == "9":
                current_type = str(random.randint(1, 8))
            else:
                current_type = report_type
            
            # Generate comment
            if comment:
                current_comment = f"{comment} - Ref: {random.randint(1000, 9999)}"
            else:
                comment_list = comments.get(current_type, ["Violation of Telegram rules"])
                current_comment = f"{random.choice(comment_list)} - ID: {random.randint(10000, 99999)}"
            
            # Send report
            print_status(f"Attack #{attack_number}: Sending {current_type} report...")
            
            success, message = await send_single_report(
                client, target_entity, current_type, current_comment
            )
            
            if success:
                successful_reports += 1
                print_status(f"✅ Attack #{attack_number} successful!", "success")
            else:
                failed_reports += 1
                print_status(f"❌ Attack #{attack_number} failed: {message}", "error")
            
            total_reports += 1
            
            # Display statistics every 10 attacks
            if attack_number % 10 == 0:
                elapsed = time.time() - start_time
                hours = int(elapsed // 3600)
                minutes = int((elapsed % 3600) // 60)
                seconds = int(elapsed % 60)
                
                print(f"\n{Colors.CYAN}{'═' * 60}")
                print(f"{Colors.GREEN}📊 ATTACK STATISTICS (Every 10 attacks)")
                print(f"{Colors.CYAN}{'═' * 60}")
                print(f"{Colors.YELLOW}Total Attacks: {attack_number}")
                print(f"{Colors.GREEN}Successful: {successful_reports}")
                print(f"{Colors.RED}Failed: {failed_reports}")
                print(f"{Colors.BLUE}Duration: {hours:02d}:{minutes:02d}:{seconds:02d}")
                print(f"{Colors.MAGENTA}Success Rate: {(successful_reports/total_reports*100):.1f}%")
                print(f"{Colors.CYAN}{'═' * 60}\n")
            
            # Random delay between attacks (2-10 seconds)
            delay = random.uniform(2, 10)
            await asyncio.sleep(delay)
            
    except KeyboardInterrupt:
        print_status("Attack stopped by user", "warning")
    
    except Exception as e:
        print_status(f"Unexpected error: {e}", "error")
    
    finally:
        # Final statistics
        elapsed = time.time() - start_time
        hours = int(elapsed // 3600)
        minutes = int((elapsed % 3600) // 60)
        seconds = int(elapsed % 60)
        
        print(f"\n{Colors.RED}{'═' * 60}")
        print(f"{Colors.RED}🎯 ATTACK COMPLETED")
        print(f"{Colors.RED}{'═' * 60}")
        print(f"{Colors.GREEN}✅ Final Statistics:")
        print(f"{Colors.YELLOW}Total Attacks: {total_reports}")
        print(f"{Colors.GREEN}Successful: {successful_reports}")
        print(f"{Colors.RED}Failed: {failed_reports}")
        print(f"{Colors.BLUE}Duration: {hours:02d}:{minutes:02d}:{seconds:02d}")
        
        if total_reports > 0:
            success_rate = (successful_reports / total_reports) * 100
            print(f"{Colors.MAGENTA}Success Rate: {success_rate:.1f}%")
        
        if successful_reports > 50:
            print(f"\n{Colors.GREEN}{'🎯' * 20}")
            print(f"{Colors.GREEN}   HIGH CHANCE OF ACCOUNT BAN!   ")
            print(f"{Colors.GREEN}   Target should be restricted    ")
            print(f"{Colors.GREEN}{'🎯' * 20}")
        
        print(f"\n{Colors.CYAN}{'─' * 60}")
        print(f"{Colors.WHITE}👤 Developer: @REDX_64")
        print(f"{Colors.WHITE}📢 Channel: t.me/REDX64")
        print(f"{Colors.CYAN}{'─' * 60}")

async def main():
    print_banner()
    
    # Check API credentials
    if api_id == 12345678 or api_hash == 'abcdef1234567890abcdef1234567890':
        print_status("❌ API credentials not set!", "error")
        print_status("Get API ID and Hash from my.telegram.org", "warning")
        input(f"\n{Colors.YELLOW}Press Enter to exit...")
        return
    
    # Create client
    client = TelegramClient(session_name, api_id, api_hash)
    
    try:
        await client.start()
        print_status("✅ Connected to Telegram", "success")
        
        me = await client.get_me()
        print_status(f"Logged in as: {me.first_name} (@{me.username})", "success")
        
        # Get target
        print(f"\n{Colors.YELLOW}{'═' * 60}")
        target = input(f"{Colors.CYAN}➤ Enter target username (@username) or user ID: {Colors.WHITE}")
        
        if not target:
            print_status("No target specified", "error")
            return
        
        # Start attack
        await continuous_report_attack(client, target)
        
    except errors.rpcerrorlist.ApiIdInvalidError:
        print_status("❌ Invalid API credentials", "error")
        print_status("Get correct credentials from my.telegram.org", "warning")
    except errors.rpcerrorlist.PhoneNumberInvalidError:
        print_status("❌ Invalid phone number", "error")
    except errors.rpcerrorlist.PhoneCodeInvalidError:
        print_status("❌ Invalid verification code", "error")
    except Exception as e:
        print_status(f"❌ Error: {e}", "error")
    finally:
        await client.disconnect()

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print(f"\n{Colors.RED}🚫 Program stopped")
    except Exception as e:
        print(f"\n{Colors.RED}❌ Fatal error: {e}")
    
    input(f"\n{Colors.YELLOW}Press Enter to exit...")