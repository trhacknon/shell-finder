#Tools Scan Shell
#!/usr/bin/python
# -*- coding: utf-8 -*


import requests, re ,os ,socket,sys,random,time
from colorama import init
from multiprocessing.dummy import Pool					     	
from colorama import Fore
import warnings
import subprocess
from requests.packages.urllib3.exceptions import InsecureRequestWarning
warnings.simplefilter('ignore',InsecureRequestWarning)
reload(sys)  
sys.setdefaultencoding('utf8')
init(autoreset=True)

def Banner():
	host_name = socket.gethostname()
	host_ip = socket.gethostbyname(host_name)
	print "==================================================="
	print Fore.RED + "[!] Contact : " + Fore.WHITE+"http://gfwkesarea.ml"
	print Fore.RED + "[!] Host : " + Fore.WHITE+"Py@"+host_name
	print Fore.RED + "[!] LocalHost : " + Fore.WHITE + host_ip
	print "===================================================" 
Banner()

def mek(url):
	try:
                Headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:28.0) Gecko/20100101 Firefox/72.0'}
		file = open("path.txt")
		# read all content
		content = file.read().splitlines()
		for line in content:
			kontol = requests.get(url+line,headers=Headers, timeout=5)
			if '-rw-r--r' in kontol.content or 'drwxr-xr-x' in kontol.text:
				print(url + Fore.GREEN + ' ' +'Vuln' + Fore.WHITE)
				open('shelo.txt','a').write(url+line+"\n")
			elif '<input type=file' in kontol.text or 'option value="chmod">' in kontol.content:
				open('shelo.txt','a').write(url+line+"\n")
			else:
				print(url + Fore.RED + ' ' + 'Not Vuln' + Fore.WHITE)
				open('domainalive.txt','a').write(url+"\n")
	except:
		pass

def Main():
	try:
		list = raw_input("\n\033[91mDomain List\033[97m:~# \033[97m")
		che = open(list, 'r').read().splitlines()
		pp = Pool(50)
		pr = pp.map(mek, che)
	except:
		pass

if __name__ == '__main__':
	Main()

      
