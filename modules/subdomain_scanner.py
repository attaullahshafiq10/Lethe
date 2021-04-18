import requests
from threading import Thread, Lock
from queue import Queue
from colorama import init, Fore
init()

GREEN = Fore.GREEN
RED   = Fore.RED
RESET = Fore.RESET
BLUE  = Fore.BLUE
q = Queue()
list_lock = Lock()
discovered_domains = []
logo = (f"""{RED}
                                                  
              ('-.    .-') _     ('-. .-.    ('-.   
            _(  OO)  (  OO) )   ( OO )  /  _(  OO)  
 ,--.      (,------. /     '._  ,--. ,--. (,------. 
 |  |.-')   |  .---' |'--...__) |  | |  |  |  .---' 
 |  | OO )  |  |     '--.  .--' |   .|  |  |  |     
 |  |`-' | (|  '--.     |  |    |       | (|  '--.  
(|  '---.'  |  .--'     |  |    |  .-.  |  |  .--'  
 |      |   |  `---.    |  |    |  | |  |  |  `---. 
 `------'   `------'    `--'    `--' `--'  `------'
                                                
                            Subdomain Scanner v0.1
    {RESET}""")
print(logo)
def scan_subdomains(domain):
    global q
    while True:
        subdomain = q.get()
        url = f"http://{subdomain}.{domain}"
        try:
            requests.get(url)
        except requests.ConnectionError:
            pass
        else:
            print(f"{GREEN}[+] Discovered subdomain:", url)
            with list_lock:
                discovered_domains.append(url)
        q.task_done()
def main(domain, n_threads, subdomains):
    global q
    for subdomain in subdomains:
        q.put(subdomain)
    for t in range(n_threads):
        worker = Thread(target=scan_subdomains, args=(domain,))
        worker.daemon = True
        worker.start()
if __name__ == "__main__":
    import argparse
    domain = input(f"{RED}Which domain do you want to scan: {RESET}")
    wordlist = "sw.txt"
    num_threads = 10
    output_file = "result.txt"
    main(domain=domain, n_threads=num_threads, subdomains=open(wordlist).read().splitlines())
    q.join()
    with open(output_file, "w") as f:
        for url in discovered_domains:
            print(url, file=f)
if __name__ == '__main__':
    main()
