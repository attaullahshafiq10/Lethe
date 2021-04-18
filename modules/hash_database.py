import os
import requests
from colorama import Fore
logo = f"""{Fore.MAGENTA}
 .S    S.    .S_SSSs      sSSs   .S    S.           sSSs   .S_sSSs     .S_SSSs      sSSs   .S    S.     sSSs   .S_sSSs    
.SS    SS.  .SS~SSSSS    d%%SP  .SS    SS.         d%%SP  .SS~YS%%b   .SS~SSSSS    d%%SP  .SS    SS.   d%%SP  .SS~YS%%b   
S%S    S%S  S%S   SSSS  d%S'    S%S    S%S        d%S'    S%S   `S%b  S%S   SSSS  d%S'    S%S    S&S  d%S'    S%S   `S%b  
S%S    S%S  S%S    S%S  S%|     S%S    S%S        S%S     S%S    S%S  S%S    S%S  S%S     S%S    d*S  S%S     S%S    S%S  
S%S SSSS%S  S%S SSSS%S  S&S     S%S SSSS%S        S&S     S%S    d*S  S%S SSSS%S  S&S     S&S   .S*S  S&S     S%S    d*S  
S&S  SSS&S  S&S  SSS%S  Y&Ss    S&S  SSS&S        S&S     S&S   .S*S  S&S  SSS%S  S&S     S&S_sdSSS   S&S_Ss  S&S   .S*S  
S&S    S&S  S&S    S&S  `S&&S   S&S    S&S        S&S     S&S_sdSSS   S&S    S&S  S&S     S&S~YSSY%b  S&S~SP  S&S_sdSSS   
S&S    S&S  S&S    S&S    `S*S  S&S    S&S        S&S     S&S~YSY%b   S&S    S&S  S&S     S&S    `S%  S&S     S&S~YSY%b   
S*S    S*S  S*S    S&S     l*S  S*S    S*S        S*b     S*S   `S%b  S*S    S&S  S*b     S*S     S%  S*b     S*S   `S%b  
S*S    S*S  S*S    S*S    .S*P  S*S    S*S        S*S.    S*S    S%S  S*S    S*S  S*S.    S*S     S&  S*S.    S*S    S%S  
S*S    S*S  S*S    S*S  sSS*S   S*S    S*S         SSSbs  S*S    S&S  S*S    S*S   SSSbs  S*S     S&   SSSbs  S*S    S&S  
SSS    S*S  SSS    S*S  YSS'    SSS    S*S          YSSP  S*S    SSS  SSS    S*S    YSSP  S*S     SS    YSSP  S*S    SSS  
       SP          SP                  SP                 SP                 SP           SP                  SP          
       Y           Y                   Y                  Y                  Y            Y                   Y           
                                                                                                                                                                  
"""
print(logo)
hashvalue = input("Please enter the hash: ")
hashtype = input("What type of hash is it (e.g. md5, sha1): ")
response = requests.get("https://md5decrypt.net/Api/api.php?hash=" + hashvalue + "&hash_type=" + hashtype + "&email=deanna_abshire@proxymail.eu&code=1152464b80a61728").text
if len(response) != 0:
    print("Cracked: " + response)
else:
    print("Hash wasnt found ):")