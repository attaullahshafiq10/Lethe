# tethe-python


## Table of contents
* [General info](#general-info)
* [Setup](#setup)
* [Modules](#Modules)

## General info
Lethe is a lightweight pentest framework. It includes modules for Information Gathering, Vulnerability analysis, Explotation and more.

## Setup

Lethe runs on any platform that has python3 and setting it up is very easy.

```
$ git clone https://github.com/hades921/Lethe.git
$ cd Lethe
$ pip3 install -r requirements.txt
$ python3 lethe.py
```
	
## Modules

### 1.Information Gathering: 
  *  WhoIS scan 
  *  Port scanner 
  *  Subdomain Scanner 
  *  Spider/Crawler
  *  OS fingerprinting
### 2.Vulnerability Analysis: 
  * SQLI scan 
  * SSL scan
  * XSS scan

### 3.Exploiting: 
  * SQL Injection
  * DOS
      * Slowloris
      * SYN flood 
  * Buffer Overflow
### 4.Password: 
  * Hashes 
	* Hash Identifier 
	* Hash cracker (supported hashes: md5, sha1, sha256, sha3 256)
		* Online Hash database lookup 
		* Hash dictionary attack 
  * Brute Force 
	* SSH cracker 
	* FTP cracker 

### 5.GeoIP 

### 6. Network
  * ARP scan
	


