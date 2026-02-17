import asyncio
import os
import sys
import random
from telethon import TelegramClient, functions, types, errors
import time
from datetime import datetime
from colorama import init, Fore, Back, Style

# ================================================
# 🚀 Tool developed by REDX_64 🚀
# 💎 Updates channel: https://t.me/REDX_64 💎
# ================================================

# Initialize colors
init(autoreset=True)

# Define custom colors for phone
class Colors:
    RESET = '\033[0m'
    BOLD = '\033[1m'
    
    # Bold colors
    RED = '\033[1;91m'
    GREEN = '\033[1;92m'
    YELLOW = '\033[1;93m'
    BLUE = '\033[1;94m'
    MAGENTA = '\033[1;95m'
    CYAN = '\033[1;96m'
    WHITE = '\033[1;97m'
    
    # Backgrounds for phone
    BG_BLUE = '\033[1;44m'
    BG_GREEN = '\033[1;42m'
    BG_RED = '\033[1;41m'

# ==================== IMPORTANT ====================
# Replace with your API credentials from my.telegram.org
# ===================================================
api_id = 37815271  # ← Replace with your API ID
api_hash = '1302f83f5aa134f203cd41876e586cb5'  # ← Replace with your API Hash
session_name = 'reporter_session'

def clear_screen():
    """Clear screen"""
    os.system('cls' if os.name == 'nt' else 'clear')

def get_phone_width():
    """Get appropriate width for phone"""
    return 50  # Width suitable for phone screens

def print_phone_banner():
    """Print banner specifically designed for phones"""
    clear_screen()
    width = get_phone_width()
    
    # Top banner
    print(f"{Colors.CYAN}{'═' * width}")
    
    # Custom phone logo
    phone_logo = [
        "╔═══════════════════════════════════╗",
        "║     ████████╗███████╗██╗          ║",
        "║     ╚══██╔══╝██╔════╝██║          ║",
        "║        ██║   █████╗  ██║          ║",
        "║        ██║   ██╔══╝  ██║          ║",
        "║        ██║   ███████╗███████╗     ║",
        "║        ╚═╝   ╚══════╝╚══════╝     ║",
        "║                                   ║",
        "║    ██████╗ ███████╗██████╗        ║",
        "║    ██╔══██╗██╔════╝██╔══██╗       ║",
        "║    ██████╔╝█████╗  ██████╔╝       ║",
        "║    ██╔══██╗██╔══╝  ██╔═══╝        ║",
        "║    ██║  ██║███████╗██║            ║",
        "║    ╚═╝  ╚═╝╚══════╝╚═╝            ║",
        "╚═══════════════════════════════════╝"
    ]
    
    for line in phone_logo:
        print(f"{Colors.MAGENTA}{line}")
    
    print(f"{Colors.CYAN}{'═' * width}")
    
    # Version information
    print(f"{Colors.GREEN}╔{'═' * (width-2)}╗")
    print(f"{Colors.GREEN}║{'🔥 RED-X DESTROYER 🔥'.center(width-2)}║")
    print(f"{Colors.GREEN}╠{'═' * (width-2)}╣")
    print(f"{Colors.GREEN}║{'💀 NON-STOP REPORT MODE 💀'.center(width-2)}║")
    print(f"{Colors.GREEN}║{'👤 Developer: @REDX_64'.center(width-2)}║")
    print(f"{Colors.GREEN}║{'📢 t.me/REDX64'.center(width-2)}║")
    print(f"{Colors.GREEN}╚{'═' * (width-2)}╝")
    
    print(f"{Colors.CYAN}{'═' * width}")
    print(f"{Colors.RED}⚠️  WARNING: This tool will report continuously until ban!")
    print(f"{Colors.CYAN}{'═' * width}")
    print()  # Empty line

def print_phone_header(title, color=Colors.CYAN):
    """Print header for phone"""
    width = get_phone_width()
    print(f"\n{color}{'─' * width}")
    print(f"{color}  {Colors.WHITE}{Colors.BOLD}{title.center(width-4)}")
    print(f"{color}{'─' * width}")

def print_phone_input(prompt):
    """Print input prompt for phone"""
    width = get_phone_width()
    print(f"\n{Colors.GREEN}↪ {Colors.CYAN}{prompt}")
    print(f"{Colors.YELLOW}{'─' * (len(prompt) + 2)}")
    return input(f"{Colors.YELLOW}➤ ")

def print_phone_menu():
    """Print menu for phone"""
    width = get_phone_width()
    print(f"\n{Colors.CYAN}{'📋 Report Types'.center(width)}")
    print(f"{Colors.CYAN}{'─' * width}")
    
    options = [
        "1. Spam - Spam messages 📩",
        "2. Violence - Violence ⚔️",
        "3. Pornography - Pornographic 🔞",
        "4. Child Abuse - Child abuse 🚸",
        "5. Copyright - Copyright ©️",
        "6. Fake - Fake account 👤",
        "7. Geo - Illegal 🚫",
        "8. Other - Other 📝",
        "9. RANDOM - Auto rotate all types 🔄",
        "10. CONTINUOUS - Non-stop until ban ⚡"
    ]
    
    for option in options:
        print(f"  {Colors.GREEN}{option}")
    
    print(f"{Colors.CYAN}{'─' * width}")

def print_phone_box(title, content, color=Colors.GREEN):
    """Print box for phone"""
    width = get_phone_width()
    print(f"\n{color}{'┌' + '─' * (width-2) + '┐'}")
    print(f"{color}│{Colors.WHITE}{title.center(width-2)}{color}│")
    print(f"{color}{'├' + '─' * (width-2) + '┤'}")
    
    for line in content:
        print(f"{color}│ {Colors.WHITE}{line.ljust(width-4)}{color} │")
    
    print(f"{color}{'└' + '─' * (width-2) + '┘'}")

def print_phone_progress(report_count, success_count, failed_count, start_time):
    """Print progress for phone"""
    width = get_phone_width()
    current_time = time.time()
    elapsed_time = current_time - start_time
    
    # Calculate reports per minute
    if elapsed_time > 0:
        rpm = (report_count / elapsed_time) * 60
    else:
        rpm = 0
    
    print(f"\n{Colors.CYAN}{'📊 REAL-TIME STATS'.center(width)}")
    print(f"{Colors.CYAN}{'─' * width}")
    print(f"{Colors.GREEN}📈 Total Reports: {report_count}")
    print(f"{Colors.GREEN}✅ Successful: {success_count}")
    print(f"{Colors.RED}❌ Failed: {failed_count}")
    
    if report_count > 0:
        success_rate = (success_count / report_count) * 100
        print(f"{Colors.YELLOW}📊 Success Rate: {success_rate:.1f}%")
    
    print(f"{Colors.BLUE}⏱️  Elapsed: {int(elapsed_time // 60)}m {int(elapsed_time % 60)}s")
    print(f"{Colors.MAGENTA}⚡ Speed: {rpm:.1f} reports/minute")
    print(f"{Colors.CYAN}{'─' * width}")

def print_status_update(message, status_type="info"):
    """Print status updates with timestamps"""
    timestamp = datetime.now().strftime("%H:%M:%S")
    if status_type == "success":
        print(f"{Colors.GREEN}[{timestamp}] ✅ {message}")
    elif status_type == "error":
        print(f"{Colors.RED}[{timestamp}] ❌ {message}")
    elif status_type == "warning":
        print(f"{Colors.YELLOW}[{timestamp}] ⚠️  {message}")
    elif status_type == "info":
        print(f"{Colors.CYAN}[{timestamp}] ℹ️  {message}")
    else:
        print(f"{Colors.WHITE}[{timestamp}] 📝 {message}")

async def login_sequence(client):
    """Login sequence"""
    print_phone_header("📱 Login", Colors.YELLOW)
    
    if not await client.is_user_authorized():
        while True:
            phone = print_phone_input("Enter phone number (example: +201234567890):")
            
            try:
                sent = await client.send_code_request(phone)
                print_status_update(f"Code sent to {phone}", "success")
                
                code = print_phone_input("Enter the code you received:")
                
                try:
                    await client.sign_in(phone, code)
                    print_status_update("Login successful!", "success")
                    break
                except errors.SessionPasswordNeededError:
                    password = print_phone_input("Enter two-factor password:")
                    await client.sign_in(password=password)
                    print_status_update("Login successful with 2FA!", "success")
                    break
                except Exception as e:
                    print_status_update(f"Login error: {e}", "error")
                    retry = print_phone_input("Try again? (y/n):")
                    if retry.lower() != 'y':
                        return False
            except Exception as e:
                print_status_update(f"Error: {e}", "error")
                retry = print_phone_input("Try again? (y/n):")
                if retry.lower() != 'y':
                    return False
    else:
        print_status_update("Already logged in!", "success")
    
    return True

async def continuous_reporting(client, target_entity, report_type="random", max_reports=0):
    """Continuous reporting function - runs until stopped or account banned"""
    report_count = 0
    success_count = 0
    failed_count = 0
    start_time = time.time()
    
    # Report reasons mapping
    reasons = [
        types.InputReportReasonSpam(),
        types.InputReportReasonViolence(),
        types.InputReportReasonPornography(),
        types.InputReportReasonChildAbuse(),
        types.InputReportReasonCopyright(),
        types.InputReportReasonFake(),
        types.InputReportReasonGeoIrrelevant(),
        types.InputReportReasonOther()
    ]
    
    # Comments for different report types
    comments = [
        "This account is sending spam messages",
        "Promoting violence and harmful content",
        "Sharing inappropriate adult content",
        "Involvement in child exploitation",
        "Copyright infringement and piracy",
        "This is a fake impersonation account",
        "Sharing illegal and prohibited content",
        "Multiple violations of Telegram terms"
    ]
    
    print_phone_header("⚡ NON-STOP REPORTING ACTIVATED", Colors.RED)
    print_status_update("Starting continuous reporting...", "warning")
    print_status_update(f"Target: @{target_entity.username if hasattr(target_entity, 'username') else target_entity.id}", "info")
    print_status_update("Press Ctrl+C to stop", "warning")
    
    try:
        while True:
            # Check if max reports reached (if specified)
            if max_reports > 0 and report_count >= max_reports:
                print_status_update(f"Reached maximum of {max_reports} reports", "info")
                break
            
            # Select reason and comment
            if report_type == "random":
                reason_index = random.randint(0, len(reasons)-1)
                reason = reasons[reason_index]
                comment = comments[reason_index]
            else:
                # For specific report type
                reason = reasons[int(report_type) - 1] if report_type.isdigit() and 1 <= int(report_type) <= 8 else types.InputReportReasonOther()
                comment = comments[int(report_type) - 1] if report_type.isdigit() and 1 <= int(report_type) <= 8 else "Violation of Telegram terms"
            
            # Add some randomness to comment
            comment = f"{comment} - {random.randint(1000, 9999)}"
            
            try:
                # Send report
                result = await client(functions.account.ReportPeerRequest(
                    peer=target_entity,
                    reason=reason,
                    message=comment
                ))
                
                report_count += 1
                if result:
                    success_count += 1
                    print_status_update(f"Report #{report_count} successful! ({reason.__class__.__name__})", "success")
                else:
                    failed_count += 1
                    print_status_update(f"Report #{report_count} sent (no confirmation)", "warning")
                
                # Update progress every 5 reports
                if report_count % 5 == 0:
                    print_phone_progress(report_count, success_count, failed_count, start_time)
                
                # Random delay between reports (to avoid detection)
                delay = random.uniform(2.0, 8.0)
                await asyncio.sleep(delay)
                
            except errors.FloodWaitError as e:
                failed_count += 1
                print_status_update(f"Flood wait: {e.seconds} seconds", "warning")
                await asyncio.sleep(e.seconds + random.uniform(1.0, 3.0))
                
            except errors.PeerIdInvalidError:
                print_status_update("Target account not found or banned! ✓", "success")
                break
                
            except errors.UserBannedError:
                print_status_update("Target account banned! ✓ MISSION ACCOMPLISHED", "success")
                break
                
            except Exception as e:
                failed_count += 1
                print_status_update(f"Error: {e}", "error")
                await asyncio.sleep(random.uniform(5.0, 15.0))
    
    except KeyboardInterrupt:
        print_status_update("Reporting stopped by user", "warning")
    
    return report_count, success_count, failed_count, time.time() - start_time

async def main():
    print_phone_banner()
    
    async with TelegramClient(session_name, api_id, api_hash) as client:
        # Login
        if not await login_sequence(client):
            return
        
        # Get target
        print_phone_header("🎯 TARGET SELECTION", Colors.MAGENTA)
        target = print_phone_input("Enter account username (@username) or user ID:")
        
        try:
            entity = await client.get_entity(target)
            name = entity.title if hasattr(entity, 'title') else (entity.first_name or "Unknown")
            
            print_phone_box("✅ TARGET ACQUIRED", [
                f"Name: {name}",
                f"ID: {entity.id}",
                f"Username: @{entity.username if hasattr(entity, 'username') else 'N/A'}",
                f"Type: {'User' if hasattr(entity, 'first_name') else 'Channel/Group'}"
            ], Colors.RED)
            
        except Exception as e:
            print_status_update(f"Error finding target: {e}", "error")
            return
        
        # Choose reporting mode
        print_phone_header("⚡ REPORTING MODE", Colors.CYAN)
        print_phone_menu()
        
        while True:
            choice = print_phone_input("Choose option (1-10):")
            if choice in [str(i) for i in range(1, 11)]:
                break
            print(f"{Colors.RED}❌ Choose a number between 1 and 10")
        
        # Additional comment
        comment = print_phone_input("Enter base comment (optional, press Enter for auto):")
        
        # Report count or continuous
        if choice in ['9', '10']:
            # Continuous mode
            print_phone_header("💀 CONTINUOUS MODE ACTIVATED", Colors.RED)
            print_phone_box("WARNING: NON-STOP MODE", [
                "This will report continuously until:",
                "1. Account gets banned ✓",
                "2. You press Ctrl+C",
                "3. Error occurs",
                "",
                "⚠️  Use responsibly!",
                "⚠️  May trigger flood control",
                "⚠️  Your account could get limited"
            ], Colors.RED)
            
            confirm = print_phone_input("Start DESTROY mode? (y/n):")
            if confirm.lower() != 'y':
                print(f"{Colors.RED}🚫 Operation cancelled")
                return
            
            # Start continuous reporting
            if choice == '9':
                report_type = "random"
            else:
                report_type = print_phone_input("Enter report type (1-8) or 'random':")
            
            total_reports, success_reports, failed_reports, total_time = await continuous_reporting(
                client, entity, report_type
            )
            
        else:
            # Limited reports mode
            while True:
                try:
                    count = int(print_phone_input("Number of reports (1-1000, 0 for unlimited):"))
                    if count == 0:
                        print_status_update("Setting to unlimited reports", "info")
                        count = 999999
                        break
                    elif 1 <= count <= 1000:
                        break
                    print(f"{Colors.RED}❌ Choose between 1 and 1000")
                except:
                    print(f"{Colors.RED}❌ Enter a valid number")
            
            # Confirmation
            print_phone_header("⚠️  CONFIRM OPERATION", Colors.YELLOW)
            print_phone_box("OPERATION DETAILS", [
                f"Target: {target}",
                f"Type: {choice}",
                f"Count: {count if count != 999999 else 'UNLIMITED'}",
                f"Comment: {comment if comment else 'Auto-generated'}",
                f"Mode: {'Random rotate' if choice == '9' else 'Continuous' if choice == '10' else 'Fixed'}"
            ], Colors.YELLOW)
            
            confirm = print_phone_input("Start operation? (y/n):")
            if confirm.lower() != 'y':
                print(f"{Colors.RED}🚫 Operation cancelled")
                return
            
            # Execute limited reports
            if choice == '9':
                report_type = "random"
            else:
                report_type = choice
            
            total_reports = 0
            success_reports = 0
            failed_reports = 0
            start_time = time.time()
            
            reasons = [
                types.InputReportReasonSpam(),
                types.InputReportReasonViolence(),
                types.InputReportReasonPornography(),
                types.InputReportReasonChildAbuse(),
                types.InputReportReasonCopyright(),
                types.InputReportReasonFake(),
                types.InputReportReasonGeoIrrelevant(),
                types.InputReportReasonOther()
            ]
            
            comments_list = [
                "This account is sending spam messages",
                "Promoting violence and harmful content",
                "Sharing inappropriate adult content",
                "Involvement in child exploitation",
                "Copyright infringement and piracy",
                "This is a fake impersonation account",
                "Sharing illegal and prohibited content",
                "Multiple violations of Telegram terms"
            ]
            
            print_phone_header("⚡ SENDING REPORTS", Colors.GREEN)
            
            for i in range(count):
                print_status_update(f"Preparing report #{i+1}", "info")
                
                if report_type == "random":
                    reason_index = random.randint(0, len(reasons)-1)
                    reason = reasons[reason_index]
                    current_comment = comments_list[reason_index]
                else:
                    reason_index = int(report_type) - 1
                    reason = reasons[reason_index]
                    current_comment = comments_list[reason_index]
                
                if comment:
                    current_comment = f"{comment} - {current_comment}"
                
                try:
                    result = await client(functions.account.ReportPeerRequest(
                        peer=entity,
                        reason=reason,
                        message=current_comment
                    ))
                    
                    total_reports += 1
                    if result:
                        success_reports += 1
                        print_status_update(f"Report #{i+1} successful!", "success")
                    else:
                        failed_reports += 1
                        print_status_update(f"Report #{i+1} sent", "warning")
                    
                    if i < count - 1:
                        delay = random.uniform(2.0, 6.0)
                        await asyncio.sleep(delay)
                        
                except errors.FloodWaitError as e:
                    failed_reports += 1
                    print_status_update(f"Flood wait: {e.seconds} seconds", "warning")
                    await asyncio.sleep(e.seconds)
                except Exception as e:
                    failed_reports += 1
                    print_status_update(f"Failed: {e}", "error")
                    await asyncio.sleep(random.uniform(5.0, 10.0))
            
            total_time = time.time() - start_time
        
        # Final results
        print_phone_header("📊 FINAL RESULTS", Colors.CYAN)
        
        results = [
            f"📈 Total Reports: {total_reports}",
            f"✅ Successful: {success_reports}",
            f"❌ Failed: {failed_reports}",
            f"📊 Success Rate: {(success_reports/total_reports*100 if total_reports > 0 else 0):.1f}%",
            f"⏱️  Total Time: {int(total_time // 60)}m {int(total_time % 60)}s",
            f"⚡ Speed: {(total_reports/total_time*60 if total_time > 0 else 0):.1f} reports/min"
        ]
        
        print_phone_box("MISSION COMPLETE", results, 
                       Colors.GREEN if success_reports > 0 else Colors.RED)
        
        # Additional information
        print(f"\n{Colors.CYAN}{'─' * get_phone_width()}")
        print(f"{Colors.MAGENTA}💀 DESTROYER MODE: NON-STOP REPORTING")
        print(f"{Colors.MAGENTA}👤 Developer: @REDX_64")
        print(f"{Colors.MAGENTA}📢 Channel: t.me/REDX64")
        print(f"{Colors.CYAN}{'─' * get_phone_width()}")
        
        if success_reports > 0:
            print(f"\n{Colors.GREEN}{'🎯' * 15}")
            print(f"{Colors.GREEN}     MISSION ACCOMPLISHED!     ")
            print(f"{Colors.GREEN}     Target should be banned!     ")
            print(f"{Colors.GREEN}{'🎯' * 15}")
        else:
            print(f"\n{Colors.RED}{'💀' * 15}")
            print(f"{Colors.RED}     NO REPORTS SUCCEEDED     ")
            print(f"{Colors.RED}     Try again with different settings     ")
            print(f"{Colors.RED}{'💀' * 15}")
        
        # Save report log
        try:
            log_file = f"report_log_{int(time.time())}.txt"
            with open(log_file, 'w') as f:
                f.write(f"Report Log - {datetime.now()}\n")
                f.write(f"Target: {target}\n")
                f.write(f"Total Reports: {total_reports}\n")
                f.write(f"Successful: {success_reports}\n")
                f.write(f"Failed: {failed_reports}\n")
                f.write(f"Time: {int(total_time // 60)}m {int(total_time % 60)}s\n")
            print_status_update(f"Log saved to: {log_file}", "info")
        except:
            pass

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print(f"\n\n{Colors.RED}💀 DESTROYER STOPPED")
    except Exception as e:
        print(f"\n{Colors.RED}❌ UNEXPECTED ERROR: {e}")
    
    input(f"\n{Colors.YELLOW}Press Enter to exit...")