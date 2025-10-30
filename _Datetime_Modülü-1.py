from datetime import date

gecmis_tarih = date(2015,8,10)
bugun = date(2025,9,10)
gecen_zaman = bugun - gecmis_tarih
#print(gecen_zaman)
#print(type(gecen_zaman))

from datetime import datetime
bugun = date.today()
suan = datetime.now()
#print(suan.ctime())
#print(suan.date())
#print(suan.time())

gecmis_anı = datetime(2019,4,21,4,17,54,231)
#print(gecmis_anı)
#print(suan - gecmis_anı)
#print(bugun.strftime("%d-%m-%Y"))

from datetime import timedelta
suan = datetime.now()
tdelta = timedelta(days=10,hours=4,seconds=61)
print(suan + tdelta)
print(suan - tdelta)