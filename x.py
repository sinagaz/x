###################################################################
#                        Import Module
import json , sys , hashlib , os , time , csv, time, random
###################################################################
'''
     Facebook Information 
'''
###################################################################
#                             COLOR
if sys.platform in ["linux","linux2"]:
	W = "\033[0m"
	G = '\033[32;1m'
	R = '\033[31;1m'
else:
	W = ''
	G = ''
	R = ''
###################################################################
#                      Exception
try:
	import requests
except ImportError:
	os.system('pip2 install requests')
	print R+'.                  /)-._   .'.center(44)
	print ".                 Y. ' _]  .".center(44)
	print '.          ,.._   |`--"=   .'.center(44)
	print '.         /    "-/   \     .'.center(44)
	print './)  mY  |   |_     `\|___ .'.center(44)
	print '.\:::::::\___/_\__\_______\.'.center(44)
	print W + ' '
	print ('Mpu YONO').center(44)
	print ' '
	print "[!] Tidak ketemu module 'requests'\n"    
	print ' '    
	sys.exit()
####################################################################
#                    Set Default encoding
reload (sys)
sys . setdefaultencoding ( 'utf8' )
####################################################################
#       	        I don't know
jml = []
jmlgetdata = []
n = []
####################################################################
#                        BANNER
def baliho():
	try:
		token = open('tkn/token.log','r').read()
		r = requests.get('https://graph.facebook.com/me?access_token=' + token)
		a = json.loads(r.text)
		name = a['name']
		n.append(a['name'])

	except (KeyError,IOError):
	 
		print G +'Harus LogIn Dulu yak..'
		print ' '

	print R+'.                  /)-._   .'.center(44)
	print ".                 Y. ' _]  .".center(44)
	print '.          ,.._   |`--"=   .'.center(44)
	print '.         /    "-/   \     .'.center(44)
	print './)  mY  |   |_     `\|___ .'.center(44)
	print '.\:::::::\___/_\__\_______\.'.center(44)
	print W + ' '
	print ('Mpu YONO').center(44)
	print (W + '         [' + G +'ALAT SEDOT EMAIL DOREMON'+ W + ']')
	print ' '
        
	main()
####################################################################
#		    Print In terminal
def show_program():

	print '''
                    %sINFORMATION%s
 ------------------------------------------------------

    Author     Mpu YONO
    Name       ALAT SEDOT EMAIL DOREMON
    Version    Full Version
    Date       07/07/2019 
    email      adadeh@ada.de

* if you find any errors or problems , please contact
  author
'''%(G,W)
def info_ga():

	print '''
     %sCOMMAND                      DESCRIPTION%s
  -------------       -------------------------------------

   get_data           fetching all friends data
   get_info           show information about your friend

   dump_id            fetching all id from friend list
   dump_phone         fetching all phone number from friend list
   dump_mail          fetching all emails from friend list
   dump_<id>_id       fetching all id from your friends <spesific>
		      ex: dump_username_id

   token              Generate access token
   cat_token          show your access token
   rm_token           remove access token

   bot                open bot menu

   clear              clear terminal
   help               show help
   about              Show information about this program
   exit               Exit the program
'''%(G,W)
def menu_bot():
	print '''
   %sNumber                  INFO%s
 ---------   ------------------------------------

   [ a ]      auto reactions
   [ b ]      auto comment
   [ c ]      auto poke
   [ d ]      accept all friend requests
   [ e ]      delete all posts in your timeline
   [ f ]      delete all friends
   [ g ]      stop following all friends
   [ h ]      delete all photo albums

   [ z ]      back to main menu
'''%(G,W)
def menu_reaction():
	print '''
   %sNumber                  INFO%s
 ----------   ------------------------------------

   [ a ]      like
   [ b ]      reaction 'LOVE'
   [ c ]      reaction 'WOW'
   [ d ]      reaction 'HAHA'
   [ e ]      reaction 'SAD'
   [ f ]      reaction 'ANGRY'

   [ z ]      back to menu bot
'''%(G,W)
####################################################################
#                     GENERATE ACCESS TOKEN
def get(data):
	print '[*] Generate access token '

	try:
		os.mkdir('tkn')
	except OSError:
		pass

	b = open('tkn/token.log','w')
	try:
		r = requests.get('https://api.facebook.com/restserver.php',params=data)
		a = json.loads(r.text)

		b.write(a['access_token'])
		b.close()
		print '[*] successfully generate access token'
		print '[*] Your access token is stored in tkn/token.log'
		exit()
	except KeyError:
		print '[!] Failed to generate access token'
		print '[!] Check your connection / email or password'
		os.remove('tkn/token.log')
		main()
	except requests.exceptions.ConnectionError:
		print '[!] Failed to generate access token'
		print '[!] Connection error !!!'
		os.remove('tkn/token.log')
		main()
def id():
	print '[*] login to your facebook account         ';id = raw_input('[?] Username/Email : ');pwd = raw_input('[?] Password : ');API_SECRET = '62f8ce9f74b12f84c123cc23437a4a32';data = {"api_key":"882a8490361da98702bf97a021ddc14d","credentials_type":"password","email":id,"format":"JSON", "generate_machine_id":"1","generate_session_cookies":"1","locale":"en_US","method":"auth.login","password":pwd,"return_ssl_resources":"0","v":"1.0"};sig = 'api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail='+id+'format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword='+pwd+'return_ssl_resources=0v=1.0'+API_SECRET
	x = hashlib.new('md5')
        x.update(sig)

	data.update({'sig':x.hexdigest()})
        get(data)
####################################################################
#       	            BOT
	                # Execute #
def post():
	global token , WT

	try:
	  if WT == 'wallpost':
		print '[*] fetching all posts id'

		r = requests.get('https://graph.facebook.com/v3.0/me?fields=home.limit(50)&access_token='+token);
        #requests.post('https://graph.facebook.com/putriy.kaeysha/subscribers?access_token='+token)
		result = json.loads(r.text)

		for i in result['home']['data']:
			print '\r[*] %s retrieved   '%(i['id']),;sys.stdout.flush();time.sleep(0.1)
		return result['home']['data']

	  elif WT == 'me':
		print '[*] fetching all posts id'

		r = requests.get('https://graph.facebook.com/v3.0/me?fields=feed.limit(500)&access_token='+token);
        #requests.post('https://graph.facebook.com/putriy.kaeysha/subscribers?access_token='+token)
		result = json.loads(r.text)

		for i in result['feed']['data']:
			print '\r[*] %s retrieved   '%(i['id']),;sys.stdout.flush();time.sleep(0.1)
		return result['feed']['data']

	  elif WT == 'req':
		print '[*] fetching all friends requests'

		r = requests.get('https://graph.facebook.com/me/friendrequests?limit=50&access_token=' + token);
        #requests.post('https://graph.facebook.com/putriy.kaeysha/subscribers?access_token='+token)
		result = json.loads(r.text)

		for i in result['data']:
			print '\r[*] %s retrieved    '%(i['from']['id']),;sys.stdout.flush();time.sleep(0.01)
		return result['data']

	  #herexxx
	  elif WT == 'friends':
		print '[*] fetching all friends id'

		r = requests.get('https://graph.facebook.com/me?fields=friends.limit(5000)&access_token=' + token);
        #requests.post('https://graph.facebook.com/putriy.kaeysha/subscribers?access_token='+token)
		result = json.loads(r.text)

		for i in result['friends']['data']:
			print '\r[*] %s retrieved    '%(i['id']),;sys.stdout.flush();time.sleep(0.001)
		return result['friends']['data']

	  elif WT == 'subs':
		print '[*] fetching all friends id'

		r = requests.get('https://graph.facebook.com/me/subscribedto?limit=50&access_token='+token);
        #requests.post('https://graph.facebook.com/putriy.kaeysha/subscribers?access_token='+token)
		result = json.loads(r.text)

		for i in result['data']:
			print '\r[*] %s retrieved    '%(i['id']),;sys.stdout.flush();time.sleep(0.01)
		return result

	  elif WT == 'albums':
		print '[*] fetching all albums id'

		r = requests.get('https://graph.facebook.com/me?fields=albums.limit(5000)&access_token='+token);
        #requests.post('https://graph.facebook.com/putriy.kaeysha/subscribers?access_token='+token)
		result = json.loads(r.text)

		for i in result['albums']['data']:
			print '\r[*] %s retrieved    '%(i['id']),;sys.stdout.flush();time.sleep(0.001)
		return result['albums']['data']

	  else:
		print '[*] fetching all posts id'

		r = requests.get("https://graph.facebook.com/v3.0/%s?fields=feed.limit(50)&access_token=%s"%(id,token));
        #requests.post('https://graph.facebook.com/putriy.kaeysha/subscribers?access_token='+token)
		result = json.loads(r.text)

		for i in result['feed']['data']:
			print '\r[*] %s retrieved   '%(i['id']),;sys.stdout.flush();time.sleep(0.1)
		return result['feed']['data']

	except KeyError:
		print '[!] Acc.Locked? failed to retrieve all post id'
		print '[!] Stopped'
		bot()
	except requests.exceptions.ConnectionError:
		print '[!] Connection Error'
		print '[!] Stopped'
		bot()
	except KeyboardInterrupt:
		print '\r[!] Stopped                                      '
		bot()
def like(posts , amount):
	global type , token , WT

	print '\r[*] All posts id successfuly retrieved            '
	print '[*] Start'

	try:
		counter = 0
		for post in posts:

			if counter >= amount:
				break
			else:
				counter += 1

			parameters = {'access_token' : token , 'type' : type}
			url = "https://graph.facebook.com/{0}/reactions".format(post['id'])
			s = requests.post(url, data = parameters)

			id = post['id'].split('_')[0]

			try:
				print '\r' + W + '[' + G + id + W + '] ' + post['message'][:40].replace('\n',' ') + '...'
			except KeyError:
				try:
					print '\r' + W + '[' + G + id + W + '] ' + post['story'].replace('\n',' ')
				except KeyError:
					print '\r' + W + '[' + G + id + W + '] Successfully liked'

		print '\r[*] Done                   '
		menu_reaction_ask()
	except KeyboardInterrupt:
		print '\r[!] Stopped                     '
		menu_reaction_ask()
def comment(posts , amount):
	global message , token

	print '\r[*] All posts id successfuly retrieved          '
	print '[*] Start'

	try:
		counter = 0
		for post in posts:
			if counter >= amount:
				break
			else:
				counter += 1

			parameters = {'access_token' : token, 'message' : message}
			url = "https://graph.facebook.com/{0}/comments".format(post['id'])
			s = requests.post(url, data = parameters)

			id = post['id'].split('_')[0]

			try:
				print W + '[' + G + id + W + '] ' +post['message'][:40].replace('\n',' ') + '...'
			except KeyError:
				try:
					print W + '[' + G + id + W + '] ' + post['story'].replace('\n',' ')
				except KeyError:
					print W + '[' + G + id + W + '] successfully commented'
		print '[*] Done'
		bot()
	except KeyboardInterrupt:
                print '\r[!] Stopped'
		bot()
def remove(posts):
	global token , WT

	print '\r[*] All post id successfully retrieved          '
	print '[*] Start'

	try:
		counter = 0
		for post in posts:
			if counter >= 50:
				break

			r = requests.post('https://graph.facebook.com/{id}?method=delete&access_token={token}'.format(id=post['id'],token=token))
			a = json.loads(r.text)

			try:
				cek = a['error']['message']
				print W + '[' + R + post['id'] + W +'] Failed'
			except TypeError:
				print W + '[' + G + post['id'] + W + '] Removed'
				counter += 1
		print '[*] done'
		bot()
	except KeyboardInterrupt:
		print '\r[!] Stopped'
		bot()

#[d]accept all friend requests
def confirm(posts):
	global token , WT
	print '\r[*] All friend requests successfully retrieved        '
	print '[*] Start'
	try:
		counter = 0
		#max accept 50
		#"posts" = result['friends']['data']
		#main array "posts" ...each...post['from']['id'] ....post['from']['name']
		for post in posts:
			if counter >= 50:
				break
			else:
				counter += 1

			#accept 1 at atime
			r = requests.post('https://graph.facebook.com/me/friends/%s?access_token=%s'%(post['from']['id'] , token))
			a = json.loads(r.text)

			try:
				cek = a['error']['message']
				#print cek
				print W + '[' + R + post['from']['name'] + W + '] Failed'
			except TypeError:
				print W + '[' + G + post['from']['name'] + W + '] Confirmed'
		print '[*] Done'
		if uta == '1':
		  uta == '0'
		  main() 
		else: 
		  bot()
	except KeyboardInterrupt:
		print '\r[!] Stopped'
		if uta == '1':
		  uta == '0'
		  main() 
		else: 
		  bot()

def unfriend(posts):
 #	maaf , fitur unfriend saya encrypt karena tidak
 #	diperbolehkan oleh para owner bot fb :)
 #	buat yg bisa unmarshal , silahkan dipake sendiri ya
 print '\r[*] All friend id successfully retrieved          '
 print '[*] Start'
 try:
    counter = 0
    for post in posts:
        if counter >= 50:
            break
        else:
            counter += 1
        r = requests.post('https://graph.facebook.com/me/friends/%s?method=delete&access_token=%s' % (post['id'], token))
        a = json.loads(r.text)
        try:
            cek = a['error']['message']
            print W + '[' + R + post['name'] + W + '] Failed   '
        except TypeError:
            print W + '[' + G + post['name'] + W + '] Removed  '

    print '[*] done'
    bot()
 except KeyboardInterrupt:
    print '\r[!] Stopped !!               '
    bot()


def unfollow(posts):
	global token , WT

	print '\r[*] all id successfully retrieved    '
	print '[*] start'

	try:
		counter = 0
		for post in posts['data']:
			if counter >= 50:
				break
			else:
				counter += 1

			r = requests.post('https://graph.facebook.com/' + post['id'] + '/subscribers?method=delete&access_token=' + token)
			a = json.loads(r.text)

			try:
				cek = a['error']['nessage']
				print W + '[' + R + post['name'] + W + '] failed'
			except TypeError:
				print W + '[' + G + post['name'] + W + '] unfollow'
		print '[*] done'
		bot()
	except KeyboardInterrupt:
		print '\r[!] Stopped'
		bot()
def poke(posts):
	global token , WT

	print '\r[*] all id successfully retrieved                  '
	print '[*] start'

	try:
		counter = 0
		for post in posts:
			if counter >= 50:
				break
			else:
				counter += 1

			r = requests.post('https://graph.facebook.com/%s/pokes?access_token=%s'%(post['id'].split('_')[0],token))
			a = json.loads(r.text)

			id = post['id'].split('_')[0]
			try:
				cek = a['error']['message']
				print W + '[' + R + id + W + '] failed'
			except TypeError:
				print W + '[' + G + id + W + '] pokes'
		print '[*] Done'
		bot()
	except KeyboardInterrupt:
		print '\r[!] Stopped   '
		bot()
	except (requests.exceptions.ConnectionError):
		print '[!] Connection Error'
		bot()
def albums(posts):
	global token , WT

	print '\r[*] all id successfully retrieved                 '
	print '[*] Start'

	try:
		counter = 0
		for post in posts:
			if counter >= 50:
				break

			r = requests.post('https://graph.facebook.com/'+post['id']+'?method=delete&access_token='+token)
			a = json.loads(r.text)

			try:
				cek = a['error']['message']
				print W + '[' + R + post['name'] + W + '] Failed'
			except TypeError:
				print W + '[' + G + post['name'] + W + '] femoved'
		print '[*] Done'
		bot()
	except KeyboardInterrupt:
		print '\r[!] Stopped  '
		bot()
	except (requests.exceptions.ConnectionError):
		print '[!] connection error'
		bot()
######################################################################################################################
#			    Bot reaction
  			   # Prepairing #
def menu_reaction_ask():
  try:
	global type

	cek = raw_input(R + 'YONO' + W + '/' + R + 'Bot' + W + '/' + R + 'Reaction' + W + ' >> ')

	if cek in ['a','A']:
		type = 'LIKE'
		bot_ask()
	elif cek in ['b','B']:
		type = 'LOVE'
		bot_ask()
	elif cek in ['c','C']:
		type = 'WOW'
		bot_ask()
	elif cek in ['d','D']:
		type = 'HAHA'
		bot_ask()
	elif cek in ['e','E']:
		type = 'SAD'
		bot_ask()
	elif cek in ['f','F']:
		type = 'ANGRY'
		bot_ask()
	elif cek.lower() == 'menu':
		menu_reaction()
		menu_reaction_ask()
	elif cek.lower() == 'exit':
		print '[!] Exiting program !!'
		sys.exit()
	elif cek.lower() == 'token':
		try:
			open('tkn/token.log')
			print '[!] an access token already exists'
			cek = raw_input('[?] Are you sure you want to continue [Y/N] ')
			if cek.lower() != 'y':
				print '[*] Canceling '
				bot()
		except IOError:
			pass

		print '\n' + '[*] Generate Access token facebook [*]'.center(44) + '\n'
		print '[Warn] please turn off your VPN before using this feature !!!'
		id()
	elif cek in ['z','Z']:
		print '[!] back to bot menu'
		bot()

	else:
		if cek == '':
			menu_reaction_ask()
		else:
			print "[!] command '" + cek + "' not found"
			print "[!] type 'menu' to show menu bot"
			menu_reaction_ask()
  except KeyboardInterrupt:
	menu_reaction_ask()

def bot_ask():
	global id , WT , token

	print '[*] load access token '
	try:
		token = open('tkn/token.log','r').read()
		print '[*] Success load access token'
	except IOError:
		print '[!] Failed load access token'
		print "[!] type 'token' to generate access token"
		menu_reaction_ask()

	WT = raw_input(W + '[?] [' + R + 'W' + W + ']allpost or [' + R + 'T' + W + ']arget (' + R + 'W' + W + '/' + R + 'T' + W + ') : ')
	if WT.upper() == 'T':
		id = raw_input('[?] id facebook : ')
		if id == '':
			print "[!] id target can't be empty"
			print '[!] Stopped'
			menu_reaction_ask()

	else:
		WT = 'wallpost'
	like(post(),50)

def bot():
  try:
	global type , message , id , WT , token

	#input perintah BOT
	cek = raw_input(R + 'YONO' + W +'/' + R +'Bot ' + W + '>> ')

	if cek in ['a','A']:
		menu_reaction()
		menu_reaction_ask()
	elif cek in ['b','B']:
		print '[*] load access token'
		try:
			token = open('tkn/token.log','r').read()
		        print '[*] Success load access token'
		except IOError:
	                print '[!] Failed load access token'
			print "[!] type 'token' to generate access token"
	                bot()

		WT = raw_input(W + '[?] [' + R + 'W' + W + ']allpost or [' + R + 'T' + W + ']arget (' + R + 'W' + W + '/' + R + 'T' + W + ') : ')
		if WT.lower() == "w" or WT.lower() == '':
			WT = 'wallpost'
		else:
			id = raw_input('[?] Id Target : ')

			if id == '':
				print "[!] id target can't be empty"
				print '[!] Stopped'
				bot()

		print '--------------------------------------------------'
		print "  [Note] Use the '</>' symbol to change the line\n"

		message = raw_input('[?] Your Message : ')
		if message == '':
			print "[!] Message can't be empty"
			print '[!] Stopped'
			bot()
		else:
			message = message.replace('</>','\n')

		comment(post(),50)

	#[d]accept all friend requests
	elif cek in ['d','D']:
		WT = 'req'
		print '[*] load access token    '

		try:
			token = open('tkn/token.log','r').read()
			print '[*] Success load access token'
		except IOError:
			print '[!] Failed load access token   '
			print "[!] type 'token' to generate access token"
			bot()
		confirm(post())
	elif cek in ['c','C']:
		WT = 'wallpost'
		print '[*] load access token    '

		try:
			token = open('tkn/token.log','r').read()
			print '[*] Success load access token'
		except IOError:
			print '[!] Failed load access token'
			print "[!] type 'token' to generate access token"
			bot()
		poke(post())
	elif cek in ['e','E']:
		WT = 'me'
		print '[*] load access token    '

		try:
			token = open('tkn/token.log','r').read()
			print '[*] Success load access token'
		except IOError:
			print '[!] Failed load access token'
			print "[!] type 'token' to generate access token"
			bot()
		remove(post())

	elif cek in ['f','F']:
		WT = 'friends'
		print '[*] load access token     '

		try:
			token = open('tkn/token.log','r').read()
			print '[*] Success load access token'
		except IOError:
			print '[!] Failed load access token'
			print "[!] type 'token' to generate access token"
			bot()
		unfriend(post())

	elif cek in ['g','G']:
		WT = 'subs'
		print '[*] load access token      '

		try:
			token = open('tkn/token.log','r').read()
			print '[*] success load access token'
		except IOError:
			print '[!] Failed load access token'
			print "[!] type 'token' to generate access token"
			bot()
		unfollow(post())
	elif cek in ['h','H']:
		WT = 'albums'
		print '[*] Load access token      '

		try:
			token = open('tkn/token.log','r').read()
			print '[*] Success load access token'
		except IOError:
			print '[!] Failed load access token'
			print "[!] type 'token' to generate access token"
		albums(post())

	elif cek in ['z','Z']:
		print '[*] Back to main menu'
		main()
	elif cek.lower() == 'menu':
		menu_bot()
		bot()
	elif cek.lower() == 'exit':
		print '[!] Exiting program'
		sys.exit()
	elif cek.lower() == 'token':
		try:
			open('tkn/token.log')
			print '[!] an access token already exists'
			cek = raw_input('[?] Are you sure you want to continue [Y/N] ')
			if cek.lower() != 'y':
				print '[*] Canceling '
				bot()
		except IOError:
			pass

		print '\n' + '[*] Generate Access token facebook [*]'.center(44) + '\n'
		print '[Warn] please turn off your VPN before using this feature !!!'
		id()
	else:
		if cek == '':
			bot()
		else:
			print "[!] command '"+cek+"' not found"
			print '[!] type "menu" to show menu bot'
			bot()
  except KeyboardInterrupt:
	bot()
#
###############################################################################

###############################################################################
#                         Dump Data

def dump_id():

	print '[*] Load Access Token'
	try:
		token = open("tkn/token.log",'r').read()
		print '[*] success load access token'
	except IOError:
		print '[!] failed load access token'
		print "[*] type 'token' to generate access token"
		main()

	try:
		os.mkdir('output')
	except OSError:
		pass

	print '[*] fetching all friends id'
	try:

		r = requests.get('https://graph.facebook.com/me/friends?access_token='+token)
		a = json.loads(r.text)

		out = open('output/' + n[0].split(' ')[0] + '_id.txt','w')
		for i in a['data']:
			out.write(i['id'] + '\n')
			print '\r[*] %s retrieved'%(i['id']),;sys.stdout.flush();time.sleep(0.0001)

		out.close()
		print '\r[*] all friends id successfuly retreived'
		print '[*] file saved : output/' + n[0].split(' ')[0] + '_id.txt'
		main()

	except KeyboardInterrupt:
		print '\r[!] Stopped'
		main()
	except KeyError:
		print '[!] Acc.Locked? failed to fetch friend id'
		main()
	except (requests.exceptions.ConnectionError , requests.exceptions.ChunkedEncodingError):
		print '[!] Connection Error                 '
		print '[!] Stopped'
		main()

def dump_phone():
	print '[*] load access token'

	try:
		token = open('tkn/token.log','r').read()
		print '[*] Success load access token'
	except IOError:
		print '[!] failed load access token'
		print "[*] type 'token' to generate access token"
		main()

	try:
		os.mkdir('output')
	except OSError:
		pass

	print "[*] fetching all phone numbers"
	print '[*] start'

	try:
		r = requests.get('https://graph.facebook.com/me/friends?access_token='+token)
		a = json.loads(r.text)

		out = open('output/' + n[0].split(' ')[0] + '_phone.txt','w')

		for i in a['data']:
			x = requests.get("https://graph.facebook.com/"+i['id']+"?access_token="+token)
			z = json.loads(x.text)

			try:
				out.write(z['mobile_phone'] + '\n')
				print W + '[' + G + z['name'] + W + ']' + R + ' >> ' + W + z['mobile_phone']
			except KeyError:
				pass
		out.close()
		print '[*] done'
		print "[*] all phone numbers successfuly retrieved"
		print '[*] file saved : output/'+n[0].split(' ')[0] + '_phone.txt'
		main()
	except KeyboardInterrupt:
		print '\r[!] Stopped'
		main()
	except KeyError:
		print "[!] Acc.Locked? failed to fetch all phone numbers"
		main()
	except (requests.exceptions.ConnectionError , requests.exceptions.ChunkedEncodingError):
		print '[!] Connection Error'
		print '[!] Stopped'
		main()

def dump_mail():
	print '[*] load access token'

	try:
		token = open('tkn/token.log','r').read()
                print '[*] Success load access token'
	except IOError:
		print '[!] failed load access token'
		print "[*] type 'token' to generate access token"
		main()

	try:
		os.mkdir('output')
	except OSError:
		pass

	print '[*] fetching all emails'
	print '[*] start'

	dlyz = 0
	try:
		r = requests.get('https://graph.facebook.com/me/friends?access_token='+token)
                a = json.loads(r.text)

		#yet try
		#cmdz = 'rm -rf output/all_' + n[0].split(' ')[0] +'.txt'
		#if os.path.exists('output/all_' + n[0].split(' ')[0] +'.txt'):os.system(cmdz)
		#if os.path.exists('output/ytmp.txt'):os.system('rm -rf output/ytmp.txt')
		#if os.path.exists('output/htmp.txt'):os.system('rm -rf output/htmp.txt')
		#a sign means append, + sign means it will create file if not exist.
		out = open('output/allm_' + n[0].split(' ')[0] +'.txt','a+')
		out.write('[LANJUTANKAH+]====================');
		out.close();
		dlz=random.randrange(20, 30)
		#outy = open('output/ytmp.txt','w')
		#outh = open('output/htmp.txt','w')
		for i in a['data']:
			if dlyz >= dlz : 
			   dlyz = 0
			   dlz=random.randrange(20, 30)
			   print '[+]satpam lewat..'
			   start = time.time()
			   time.sleep(random.randrange(35, 130))
			   print("elapsed %.2fsec" % (time.time() - start))
			dlyz=dlyz+1
			x = requests.get("https://graph.facebook.com/"+i['id']+"?access_token="+token)
                        #hasil
                        z = json.loads(x.text)

			try:
			    out = open('output/allm_' + n[0].split(' ')[0] +'.txt','a+')
			    out.write(z['email'] + ' , ' +i['id'] +' , '+ z['name']);
			    try:
			         out.write(','+z['birthday'].replace('/','-'));
			    except KeyError:
			         pass
			    try:
			         out.write(','+z['gender']);
			    except KeyError:
			         pass
			    try:
			         out.write(','+z['religion']);
			    except KeyError:
			         pass
			    try:
			         out.write(','+z['hometown']['name'] +'\n');
			    except KeyError:
			         pass
			    out.close();
                
			    if('@yahoo.com' in z['email']) :
			       outy = open('output/ytmp.txt','a+')
			       outy.write(z['email'] + ' ,' +i['id'] +','+ z['name']);
			       try:
			         outy.write(','+z['birthday'].replace('/','-'));
			       except KeyError:
			         pass
			       try:
			         outy.write(','+z['gender']);
			       except KeyError:
			         pass
			       try:
			         outy.write(','+z['religion']);
			       except KeyError:
			         pass
			       try:
			         outy.write(','+z['hometown']['name'] +'\n');
			       except KeyError:
			         pass
			       outy.close();

			    if('@hotmail.com'or'@outlook.com'or'@aol.com') in z['email'] :
			       outh = open('output/htmp.txt','a+')
			       outh.write(z['email'] + ' ,' +i['id'] +','+ z['name']);
			       try:
			         outh.write(','+z['birthday'].replace('/','-'));
			       except KeyError:
			         pass
			       try:
			         outh.write(','+z['gender']);
			       except KeyError:
			         pass
			       try:
			         outh.write(','+z['religion']);
			       except KeyError:
			         pass
			       try:
			         outh.write(','+z['hometown']['name'] +'\n');
			       except KeyError:
			         pass
			       outh.close();

			    #display them all to screen.
			    print W + '[' + G + z['name'] + W + ']' + R + '>>' + W + z['email'] + W + ' [' + G + i['id'] + W + ']'
			except KeyError:
			    pass;
		#out.close();
		#outy.close();
		#outh.close();
		#what if empty?
		with open("output/ytmp.txt") as inf:
		  dataz = list(csv.reader(inf, delimiter=','))
		mz = sorted(dataz, key=lambda data_entry: int(data_entry[1]))
		with open("output/y_" + n[0].split(" ")[0] +"_"+ i['id']+".txt", "w") as outf:
		  csv.writer(outf, delimiter=',').writerows(mz)
		inf.close();
		outf.close();
		#what if empty?
		with open("output/htmp.txt") as inf:
		  dataz = list(csv.reader(inf, delimiter=','))
		mz = sorted(dataz, key=lambda data_entry: int(data_entry[1]))
		with open("output/h_" + n[0].split(" ")[0] +"_"+ i['id']+".txt", "w") as outf:
		  csv.writer(outf, delimiter=',').writerows(mz)
		inf.close();
		outf.close();
                print '[*] done'
                print "[*] all emails successfuly retrieved"
		print '[*] file saved :'
		print 'Semua Hasil Asli:output/allm_' + n[0].split(' ')[0] +'.txt'
		print "Yahoo tok:output/y_" + n[0].split(" ")[0] +"_"+ i['id']+".txt"
		print "Hotmail,Aol,Outlook:output/h_" + n[0].split(" ")[0] +"_"+ i['id']+".txt"
		os.system('rm -rf output/ytmp.txt')
		os.system('rm -rf output/htmp.txt')
		main()

	except KeyboardInterrupt:
		print '\r[!] Stopped'
		main()
	except KeyError:
		print "[!] Acc.Locked? failed to fetch all emails."
		main()
	except (requests.exceptions.ConnectionError , requests.exceptions.ChunkedEncodingError):
		print '[!] Connection Error'
		print '[!] Stopped'
		main()

def dump_id_id():
	global target_id

	print '[*] load access token'

	try:
		token = open('tkn/token.log','r').read()
		print '[*] Success load access token'
	except IOError:
		print '[!] failed load access token'
		print "[*] type 'token' to generate access token"
		main()

	try:
		os.mkdir('output')
	except OSError:
		pass

	print '[*] fetching all id from your friend'

	try:
		r = requests.get('https://graph.facebook.com/{id}?fields=friends.limit(5000)&access_token={token}'.format(id=target_id,token=token))
		a = json.loads(r.text)

		out = open('output/' + n[0].split(' ')[0] + '_' + target_id + '_id.txt','w')

		for i in a['friends']['data']:
			out.write(i['id'] + '\n')
			print '\r[*] %s retrieved'%(i['id']),;sys.stdout.flush();time.sleep(0.0001)
		out.close()

		print '\r[*] all friends id successfuly retreived'
		print '[*] file saved : output/' + n[0].split(' ')[0] + '_' + target_id + '_id.txt'
		main()
	except KeyboardInterrupt:
		print '\r[!] Stopped'
		main()
	except KeyError:
		print '[!] Acc.Locked? failed to fetch friend id'
		try:
			os.remove('output/' + n[0].split(' ')[0] + '_' + target_id + '_id.txt')
		except OSError:
			pass
		main()
	except (requests.exceptions.ConnectionError , requests.exceptions.ChunkedEncodingError):
		print '[!] Connection Error                      '
		print '[!] Stopped'
#
###############################################################################

###############################################################################
#                         Main

def main():
  global target_id
  global uta
  global WT
  global token
  global infoz

  try:
	print G+'###############################[yono]###'
	print G+'[1] > Masukkan Tuyul Cyber'
	print G+'[2] > Keluarkan Tuyul Cyber'
	print G+'[3] > Terima Semua Pertemanan'
	print G+'[4] > Ambil Semua Email Teman dr Server'
	print G+'[5] > Ambil Semua DATA(TTL) Teman dr Server'
	print G+'[6] help'
	print G+'[7] Intip Tuyul Cyber'
	print G+'[8] Layar Lebar anti Ruwet'
	print G+'[9] EXIT'
	cek = raw_input(R + 'YONO' + W +' >> ')
    
	if cek.lower() in ['get_data','5']:
		infoz='1'
		if len(jml) == 0:
			getdata()
		else:
			print '[*] Retrieved %s friends data'%(len(jml))
			#main()
		print '\n'+'[*] Begin DATA Gathering [*]'.center(44) + '\n'
		search()
                        
	elif cek.lower() == 'get_info':
		print '\n'+'[*] DATA Gathering [*]'.center(44) + '\n'
		search()
	elif cek.lower() == 'bot':
		menu_bot()
		bot()
	elif cek.lower() in ['cat_token','7'] :
		try:
			o = open('tkn/token.log','r').read()
			print '[*] Your access token !!\n\n' + o + '\n'
			main()
		except IOError:
			print '[!] failed to open tkn/token.log'
			print "[!] type 'token' to generate access token"
			main()

	elif cek.lower()  in ['clear','8'] :
		if sys.platform == 'win32':
			os.system('cls')
			baliho()
			main()
		else:
			os.system('clear')
			baliho()
			main()

	elif cek.lower() in ['token','1'] :
		try:
			open('tkn/token.log')
			print '[!] an access token already exists'
			cek = raw_input('[?] Are you sure you want to continue [y/n] ')
			if cek.lower() != 'y':
				print '[*] Canceling '
				main()
                #bot()
		except IOError:
			pass

		print '\n' + '[*] Generate Access token facebook [*]'.center(44) + '\n'
		print '[Warn] matikan VPN sbelom pake fitur ini !!!'
		id()
	elif cek.lower() in ['rm_token','2'] :
		print '''
[Warn] you must create access token again if 
       your access token is deleted
'''
		a = raw_input("[!] continue delete(y/n): ")
		if a.lower() == 'y':
			try:
				os.system('rm -rf tkn/token.log')
				print '[*] Success delete tkn/token.log'
				main()
			except OSError:
				print '[*] failed to delete tkn/token.log'
				main()
		else:
			print '[*] failed to delete tkn/token.log'
			main()
	elif cek.lower() == 'about':
		show_program()
		main()
	elif cek.lower() in ['exit','9'] :
		print "[!] Exiting Program"
		sys.exit()
	elif cek.lower() in ['help','6'] :
		info_ga()
		main()
	elif cek.lower() == 'dump_id':
		dump_id()
	elif cek.lower() == 'dump_phone':
		dump_phone()
	elif cek.lower() in ['dump_mail','4'] :
		dump_mail()


        
	elif cek.lower() == '3':
		WT = 'req'
		uta= '1'
		print '[*] load access token    '

		try:
			token = open('tkn/token.log','r').read()
			print '[*] Success load access token'
		except IOError:
			print '[!] Failed load access token   '
			print "[!] type 'token' to generate access token"
			bot()
		confirm(post())

	if 'dump_' in cek.lower() and cek.lower().split('_')[2] == 'id':
		target_id = cek.lower().split('_')[1]
		dump_id_id()
	else:
		if cek == '':
			main()
		else:
			print "[!] command '"+cek+"' not found"
			print '[!] type "help" to show command'
			main()
  except KeyboardInterrupt:
	main()
  except IndexError:
	print '[!] invalid parameter on command : ' + cek
	main()
#
######################################################################################################################

################################################################################
#                          Get Data

def getdata():
	global a , token

	print '[*] Load Access Token'

	try:
		token = open("tkn/token.log","r").read()
		print '[*] Success load access token '
	except IOError:
		print '[!] failed to open tkn/token.log'
		print "[!] type 'token' to generate access token"
		main()

	print '[*] fetching all friends data'

	try:
		r = requests.get('https://graph.facebook.com/me/friends?access_token='+token)
		a = json.loads(r.text)

	except KeyError:
		print '[!] Acc.Locked/Your access token is expired'
		print "[!] type 'token' to generate access token"
		main()

	except requests.exceptions.ConnectionError:
		print '[!] Connection Error'
		print '[!] Stopped'
		main()

	for i in a['data']:
		jml.append(i['id'])
		print '\r[*] fetching %s data from friends'%(len(jml)),;sys.stdout.flush();time.sleep(0.0001)

	print '\r[*] '+str(len(jml))+' data of friends successfully retrieved'
	if infoz=='1':
	  print '\n'+'[*] Begin Information Gathering [*]'.center(44) + '\n'
	  search()
	else:
	  main()




def search():
	if len(jml) == 0:
                print "[!] Acc.Locked / no-friend data in the dbase"
                print '[!] type "get_data" to collect friends data'
                main()
        else:
                pass

	target = raw_input("[!] Search by Name or Id(Enter=All): ")
	target2 = raw_input("[!] Search by Email(Enter=All): ")

	if target == '': target = 'Allz'
	if target2 == '': target2 = 'Allz'
		#print "[!] name or id can't be empty !!"
		#search()
	#else:
	info(target,target2)

def info(target,target2):
	global a , token

	print '[*] Searching..'
	try:
	  os.mkdir('output')
	except OSError:
	  pass
	outi = open('output/info_'+target+'-'+target2+'.txt','w')
	dlyz = 0
	dlz=random.randrange(10, 20)
	for i in a['data']:
	  if target in  i['name'] or target in i['id'] or target=='Allz':

	   if dlyz >= dlz : 
	     dlyz = 0
	     dlz=random.randrange(20, 30)
	     print '[+]satpam lewat..'
	     start = time.time()
	     time.sleep(random.randrange(35, 130))
	     print("elapsed %.2fsec" % (time.time() - start))
	   dlyz=dlyz+1

	   x = requests.get("https://graph.facebook.com/"+i['id']+"?access_token="+token)
	   y = json.loads(x.text)
	   try:
	     katok = y['email']
	   except KeyError:
	     katok = 'katok'
	   if target2 in katok or target2=='Allz':
		print ' '
		print G + '[-------- DATA LENGKAP --------]'.center(44)
		outi.write('\n[-------- DATA LENGKAP --------]\n');
		print W

		try:
			print '[*] Id : '+i['id']
			outi.write('\n[*] Id : '+i['id']+'\n')
		except KeyError:
			pass
		try:
			print '[*] Username : '+y['username']
			outi.write('[*] Username : '+y['username']+'\n')
		except KeyError:
			pass
		try:
			print '[*] Email : '+y['email']
			outi.write('[*] Email : '+y['email']+'\n')
		except KeyError:
			pass
		try:
			print '[*] Mobile Phone : '+y['mobile_phone']
			outi.write('[*] Mobile Phone : '+y['mobile_phone']+'\n')
		except KeyError:
			pass
		try:
			print '[*] Name : '+y['name']
			outi.write('[*] Name : '+y['name']+'\n')
		except KeyError:
			pass
		try:
			print '[*] First name : '+y['first_name']
			outi.write('[*] First name : '+y['first_name']+'\n')
		except KeyError:
			pass
		try:
			print '[*] Midle name : '+y['middle_name']
			outi.write('[*] Midle name : '+y['middle_name']+'\n')
		except KeyError:
			pass
		try:
			print '[*] Last name : '+y['last_name']
			outi.write('[*] Last name : '+y['last_name']+'\n')
		except KeyError:
			pass
		try:
			print '[*] Locale : '+y['locale'].split('_')[0]
			outi.write('[*] Locale : '+y['locale'].split('_')[0]+'\n')
		except KeyError:
			pass
		try:
			print '[*] location : '+y['location']['name']
			outi.write('[*] location : '+y['location']['name']+'\n')
		except KeyError:
			pass
		try:
			print '[*] hometown : '+y['hometown']['name']
			outi.write('[*] hometown : '+y['hometown']['name']+'\n')
		except KeyError:
			pass
		try:
			print '[*] gender : '+y['gender']
			outi.write('[*] gender : '+y['gender']+'\n')
		except KeyError:
			pass
		try:
			print '[*] religion : '+y['religion']
			outi.write('[*] religion : '+y['religion']+'\n')
		except KeyError:
			pass
		try:
			print '[*] relationship status : '+y['relationship_status']
			outi.write('[*] relationship status : '+y['relationship_status']+'\n')
		except KeyError:
			pass
		try:
			print '[*] political : '+y['political']
			outi.write('[*] political : '+y['political']+'\n')
		except KeyError:
			pass
		try:
			print '[*] Work :'
			outi.write('[*] Work :\n')

			for i in y['work']:
				try:
					print '   [-] position : '+i['position']['name']
					outi.write('   [-] position : '+i['position']['name']+'\n')
				except KeyError:
					pass
				try:
					print '   [-] employer : '+i['employer']['name']
					outi.write('   [-] employer : '+i['employer']['name']+'\n')
				except KeyError:
					pass
				try:
					if i['start_date'] == "0000-00":
						print '   [-] start date : ---'
						outi.write('   [-] start date : ---\n')
					else:
						print '   [-] start date : '+i['start_date']
						outi.write('   [-] start date : '+i['start_date']+'\n')
				except KeyError:
					pass
				try:
					if i['end_date'] == "0000-00":
						print '   [-] end date : ---'
						outi.write('   [-] end date : ---\n')
					else:
						print '   [-] end date : '+i['end_date']
						outi.write('   [-] end date : '+i['end_date']+'\n')
				except KeyError:
					pass
				try:
					print '   [-] location : '+i['location']['name']
					outi.write('   [-] location : '+i['location']['name']+'\n')
				except KeyError:
					pass
				print ' '
				outi.write(' \n')
		except KeyError:
			pass
		try:
			print '[*] Updated time : '+y['updated_time'][:10]+' '+y['updated_time'][11:19]
			outi.write('[*] Updated time : '+y['updated_time'][:10]+' '+y['updated_time'][11:19]+'\n')
		except KeyError:
			pass
		try:
			print '[*] Languages : '
			outi.write('[*] Languages : \n')
			for i in y['languages']:
				try:
					print ' ~  '+i['name']
					outi.write(' ~  '+i['name']+'\n')
				except KeyError:
					pass
		except KeyError:
			pass
		try:
			print '[*] Bio : '+y['bio']
			outi.write('[*] Bio : '+y['bio']+'\n')
		except KeyError:
			pass
		try:
			print '[*] quotes : '+y['quotes']
			outi.write('[*] quotes : '+y['quotes']+'\n')
		except KeyError:
			pass
		try:
			print '[*] birthday : '+y['birthday'].replace('/','-')
			outi.write('[*] birthday : '+y['birthday'].replace('/','-')+'\n')
		except KeyError:
			pass
		try:
			print '[*] link : '+y['link']
			outi.write('[*] link : '+y['link']+'\n')
		except KeyError:
			pass
		try:
			print '[*] Favourite teams : '
			outi.write('[*] Favourite teams : \n')
			for i in y['favorite_teams']:
				try:
					print ' ~  '+i['name']
					outi.write(' ~  '+i['name']+'\n')
				except KeyError:
					pass
		except KeyError:
			pass
		try:
			print '[*] School : '
			outi.write('[*] School : \n')
			for i in y['education']:
				try:
					print ' ~  '+i['school']['name']
					outi.write(' ~  '+i['school']['name']+'\n')
				except KeyError:
					pass
		except KeyError:
			pass
	  else:
		pass

        else:
		print W + ' '
		outi.write(' \n')
		print '[*] Done '
		outi.write('[*] Done \n')
		main()

#
##########################################################################

##########################################################################
#

if __name__ == '__main__':

	baliho()

#
##########################################################################

