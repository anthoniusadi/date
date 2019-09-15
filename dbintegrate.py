from datetime import datetime
import time
import mqtt
import modulderive as md
import sqlite3
import base64
conn = sqlite3.connect('/root/dev/proyek/newsatpam.sq3')
print ("Opened database successfully");
print ("==========================================")
global timework
timework=[]
def konversi(jam):
      ptr=conn.execute("select id,start from  times ")
      for n in ptr:
            convert_id=(str(n[0]))
            convert_jam=(str(n[1]))
            if(jam in convert_jam):
                  return convert_id
      # if(jam=="14"):
      #       jam="1"
      #       return jam
      # if(jam=="20"):
      #       jam="2"
      #       return jam
      # if(jam=="10"):
      #       jam="3"
      #       return jam
      # if(jam=="11"):
      #       jam="4"
      #       return jam
      # if(jam=="21"):
      #       jam="5"
      #       return jam
def fungsi1():
   cursor = conn.execute("select s.date,s.time_id ,s.user_id,u.name,s.room_id from shifts as s,users as u where s.user_id=u.id AND s.time_id=1 AND s.user_id=7;")
   for row in cursor:
      x=(row[0], row[1], row[2], row[3], row[4])
     # string=bytes(x,encoding='utf-8')
 #    x.replace(" ","_") 
      print(x)
      #print (str(string,encoding='ascii',error='ignore'))
     # print (str(x,encoding='ascii',error='ignore'))
 #  print ("date = ", row[0])
 #  print ("time_shift = ", row[1])
 #  print ("no_satpam = ", row[2]) 
 #  print ("nama = ", row[3])
 #  print ("room_id = ", row[4])
###! ambil timeshift
def timeShift():
   cursor = conn.execute("select start from times ")
   for s in cursor:
      x=str(s[0])
      print(x)
      timework.append(x)
      
###! FIND ALL TIMESTART FROM parameter time
def timeStart(times):
   
   cursor = conn.execute("select u.name,s.user_id,s.time_id, t.start ,s.room_id from users as u,times as t,shifts as s where t.id=s.time_id AND u.id=s.user_id AND s.time_id=(%s)" %(times)  )
   for e in cursor:
      x = str("{} # {} # {} # {} # {}".format(e[0],e[1],e[2],e[3],e[4]))
      ##! ambil masterkey dari tabel users
      z = str(e[1])
      ruang=str(e[4])
      ##! kemudian s.user_id  akan di derive dan langsung dikirim ke roomnya 
      
      r=masterkey(z)
      print(r)
      pswd=md.enkrip(r,z)
      print(pswd)
      strpswd = base64.b64encode(pswd)
      
      print(strpswd)
      jk='ruang/'+ruang
      print("kirim ke "+jk)
      
      ##!kirim ke stiap node sesuai room_id
      mqtt.client.publish(jk,strpswd)
      time.sleep(2)
      
def masterkey(key):
      curs= conn.execute("select master_key from users where id=(%s)"%key)
      for j in curs:
            mkey=str(j[0])
            #print(mkey)
            return mkey
def getSalt(timeid):
   cursor = conn.execute("select u.name , u.password from users as u ,shifts as s WHERE u.id=s.user_id AND s.time_id=(%s)"%timeid)
   for e in cursor:
      x = str("{} # {}".format(e[0],e[1]))
      print(x)
      
###! menemukan orang yang bekerja pada start tertentu ####
def workstart():
   cursor = conn.execute("select s.date,s.time_id ,s.user_id,u.name,s.room_id from shifts as s,users as u where u.id=s.user_id AND s.time_id=1")
   
   for e in cursor:
      
     # data=(e[0],e[1],e[2],e[3],e[4])
      #data=("{}#{}#{}#{}#{}".format(e[0],e[1],e[2],e[3],e[4]))
      x=str("{}#{}#{}#{}#{}".format(e[0],e[1],e[2],e[3],e[4]))
      #x=str(data)
      print((x))
      #final=(Replace(x))   
     # print(final.replace(" ","_"))
      # print(type(x))
      ##*data string dikirim pada mqtt##
      ## !kirim ke MQTT ##
     # print ('kirim ke MQTT')
#fungsi1()
#workstart()
i=1
timeShift()
while(True):
   current = datetime.now()
   tahun = current.year
   bulan = current.month
   hari = current.day
   jam = str(current.hour)
   menit = current.minute
   detik = current.second
   now = ("{}".format(jam,menit))
   date = ("{}-{}-{}".format(tahun,bulan,hari))
   
   t=timework
   print(jam)
   
   time.sleep(3)
#    print(t)
   #db.timeStart(1)
   if((jam in t)and i==1):
      print("berhasil")
      print(jam)
      X=konversi(jam)
      print(X)
      timeStart(X)
      #print(sat)
      i+=1
##!
   if(menit>69):
      print("system will be break soon")
      break
   else:
      print("....")
      #print(date)
      #print(jam)
#    print ("{}-{}-{} \n {}:{}:{}".format(hari, bulan, tahun,jam, menit, detik))
   time.sleep(2)
   print("===========================================")
   #?FIND TIME START time_id= 1
   #timeStart(1)
   #?FINDSALT 
   #getSalt(1)
   #?get all time shift
   print ("==========================================")
   print ("scanning time");
   #conn.close()
