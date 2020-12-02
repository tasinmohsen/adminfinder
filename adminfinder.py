import socket
import requests
import time
W = '\033[1;37m'
B = '\033[1;34m'
R = '\033[1;31m'
G = '\033[1;32m'
Y = '\033[1;33m'
C = '\033[1;36m'
print(f"{W}")
website = input("Give me your website:")
print('''[1]http\n[2]https''')
ht = input("Give me http/https(default:http://):")
if ht == "1":
    web = "http://"+website
elif ht == "":
    web = "http://"+website
elif ht == "2":
    web = "https://"+website
else:
    print("[X] Wrong options")
ip = socket.gethostbyname(website)
print(f"\n[+]Target: {web}")
print("[+]Finding the website admin pannel")
adminpannel_txt = ("%s_admin"%(website))
admin_list = open('adminpanel_list.txt')
print("[+]Remember admin page saved in [%s%s%s]"%(G,adminpannel_txt,W))
time.sleep(3)
for line in admin_list.readlines():
    adminpannel = line.strip('\n')
    try:
        webpannel = web+"/"+adminpannel
        r = requests.get(webpannel, timeout=5)
        if r.status_code == 404:
            print (f"%s[%s] error to connect [%s] host%s"%(R,r.status_code,webpannel,W))
        elif r.status_code == 200:
            print (f"%s[%s] connected to [%s] host succussfully%s"%(G,r.status_code,webpannel,W))
            file = open(adminpannel_txt,"a")
            file.write('%s \n'%(webpannel))
            file.close()
            print("This Admin Pannel found: %s%s%s"%(G,webpannel,W))
            print("Do you want to search more or exit")
            user = input("[y/n](default:y):")
            if user in ['Y','y']:
                pass
            elif user in ['N','n']:
                file = open(adminpannel_txt,"a")
                file.read()
                site = file
                print("Those admin pannel are found on this page[%s]"%(web))
                print(site)
                break
            elif user == "":
                pass
            else:
                print("[!]Error.Just press y/n")
              
        #print ('[*]Try to connect: '+web+'/'+adminpannel)
    except KeyboardInterrupt:
        pass
file = open(adminpannel_txt,"a")
file.read()
site = file
print("Those admin pannel are found on this page[%s]"%(web))
print(site) 