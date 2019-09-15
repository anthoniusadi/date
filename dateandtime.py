from datetime import datetime
import time
import dbintegrate as db

#print(db.time)
i=1
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
    def konversi(jam):
        if(jam=="22"):
            jam="1"
            return jam
        if(jam=="6"):
            jam="2"
            return jam
        if(jam=="10"):
            jam="3"
            return jam
        if(jam=="19"):
            jam="4"
            return jam
        if(jam=="21"):
            jam="5"
            return jam
    t=db.time
    print(t)
#    print(t)
    
    #db.timeStart(1)
    if((jam in t)and i==1):
        print("berhasil")
        X=konversi(jam)
        db.timeStart(X)
        #print(sat)
        i+=1
##!
    if(menit>69):
        print("system will be break soon")
        break
    else:
        print("belom")
        #print(date)
        #print(jam)
        
#    print ("{}-{}-{} \n {}:{}:{}".format(hari, bulan, tahun,jam, menit, detik))
    time.sleep(2)