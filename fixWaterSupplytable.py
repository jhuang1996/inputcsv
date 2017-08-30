#!/home/drfuser/pyvenv/bin/python
# -*- coding: utf-8 -*-
import sys
sys.path.append("/home/drfuser/prototype-demo/")
from  dbhelper import dbuser_connect
conn = dbuser_connect()                                                        
cursor = conn.cursor()
cursor.execute("select R_ID from Reservoir where ReservoirName='寶山水庫'")
RID1=cursor.fetchall()
cursor.execute("select R_ID from Reservoir where ReservoirName='寶山第二水庫'")
RID2=cursor.fetchall()
print(RID1[0][0])
print(RID2[0][0])
sql = "INSERT INTO WaterSupply (R_ID,C_ID) VALUES (%s,%s);"
cursor.execute(sql,(RID1[0][0],1))
cursor.execute(sql,(RID2[0][0],1)) 
conn.commit()
cursor.execute("update Q90 set FO_ID='1' where Q90_ID='1';")
cursor.execute("update Q95 set FO_ID='1' where Q95_ID='1';") 
cursor.execute("update ReservedWater set R_ID=%s where RW_ID='1';",RID1[0][0])
cursor.execute("update PeoplesLivelihoodWater set R_ID=%s where PLW_ID='1';",RID1[0][0])
cursor.execute("update IrrigationWaterDemand set R_ID=%s where IWD_ID ='1';",RID1[0][0])
cursor.execute("update RuleCurve set R_ID=%s;",RID1[0][0])
conn.commit()

cursor.close()
conn.close()
