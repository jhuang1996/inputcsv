#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 15 11:58:48 2017

@author: Johnny
"""
'''
Day to ten section
'''
import pandas as pd
import csv

input_csv = 'ten.csv'
full_df = pd.read_csv(input_csv, sep=',', skipinitialspace = True)

Q90 = full_df.Q90
Q95 = full_df.Q95
OutBase = full_df.OutBase
ino = full_df.InandOut
pwn = full_df.PWN
ul = full_df.UpperLimit
ml = full_df.MidLimit
ll = full_df.LowerLimit
sll = full_df.SeriousLowerLimit

#Create ten days list
def daytotenloop(Q90,Q95,OutBase,ino,pwn,ul,ml,ll,sll):
    Ten90=[]
    Ten95=[]
    out=[]
    inandout=[]
    tenpwn=[]
    tenul=[]
    tenml=[]
    tenll=[]
    tensll=[]
    
    for i in range(13):
        if i == 1:
            Ten90.append(sum(Q90[0:10]))
            Ten90.append(sum(Q90[10:20]))
            Ten90.append(sum(Q90[20:31]))
            Ten95.append(sum(Q95[0:10]))
            Ten95.append(sum(Q95[10:20]))
            Ten95.append(sum(Q95[20:31]))
            out.append(sum(OutBase[0:10]))
            out.append(sum(OutBase[10:20]))
            out.append(sum(OutBase[20:31]))
            inandout.append(sum(ino[0:10]))
            inandout.append(sum(ino[10:20]))
            inandout.append(sum(ino[20:31]))
            tenpwn.append(sum(pwn[0:10]))
            tenpwn.append(sum(pwn[10:20]))
            tenpwn.append(sum(pwn[20:31]))
            tenul.append(sum(ul[0:10]))
            tenul.append(sum(ul[10:20]))
            tenul.append(sum(ul[20:31]))
            tenml.append(sum(ml[0:10]))
            tenml.append(sum(ml[10:20]))
            tenml.append(sum(ml[20:31]))
            tenll.append(sum(ll[0:10]))
            tenll.append(sum(ll[10:20]))
            tenll.append(sum(ll[20:31]))
            tensll.append(sum(sll[0:10]))
            tensll.append(sum(sll[10:20]))
            tensll.append(sum(sll[20:31]))
        elif i==2:
            a=31;b=41;c=51;d=59
            Ten90.append(sum(Q90[31:41]))
            Ten90.append(sum(Q90[41:51]))
            Ten90.append(sum(Q90[51:59]))
            Ten95.append(sum(Q95[31:41]))
            Ten95.append(sum(Q95[41:51]))
            Ten95.append(sum(Q95[51:59]))
            out.append(sum(OutBase[31:41]))
            out.append(sum(OutBase[41:51]))
            out.append(sum(OutBase[51:59]))
            inandout.append(sum(ino[31:41]))
            inandout.append(sum(ino[41:51]))
            inandout.append(sum(ino[51:59]))
            tenpwn.append(sum(pwn[31:41]))
            tenpwn.append(sum(pwn[41:51]))
            tenpwn.append(sum(pwn[51:59]))
            tenul.append(sum(ul[a:b]))
            tenul.append(sum(ul[b:c]))
            tenul.append(sum(ul[c:d]))
            tenml.append(sum(ml[a:b]))
            tenml.append(sum(ml[b:c]))
            tenml.append(sum(ml[c:d]))
            tenll.append(sum(ll[a:b]))
            tenll.append(sum(ll[b:c]))
            tenll.append(sum(ll[c:d]))
            tensll.append(sum(sll[a:b]))
            tensll.append(sum(sll[b:c]))
            tensll.append(sum(sll[c:d]))
        elif i==3:
            a=59;b=69;c=79;d=90;
            Ten90.append(sum(Q90[59:69]))
            Ten90.append(sum(Q90[69:79]))
            Ten90.append(sum(Q90[79:90]))
            Ten95.append(sum(Q95[59:69]))
            Ten95.append(sum(Q95[69:79]))
            Ten95.append(sum(Q95[79:90]))
            out.append(sum(OutBase[59:69]))
            out.append(sum(OutBase[69:79]))
            out.append(sum(OutBase[79:90]))
            inandout.append(sum(ino[59:69]))
            inandout.append(sum(ino[69:79]))
            inandout.append(sum(ino[79:90]))
            tenpwn.append(sum(pwn[59:69]))
            tenpwn.append(sum(pwn[69:79]))
            tenpwn.append(sum(pwn[79:90]))
            tenul.append(sum(ul[a:b]))
            tenul.append(sum(ul[b:c]))
            tenul.append(sum(ul[c:d]))
            tenml.append(sum(ml[a:b]))
            tenml.append(sum(ml[b:c]))
            tenml.append(sum(ml[c:d]))
            tenll.append(sum(ll[a:b]))
            tenll.append(sum(ll[b:c]))
            tenll.append(sum(ll[c:d]))
            tensll.append(sum(sll[a:b]))
            tensll.append(sum(sll[b:c]))
            tensll.append(sum(sll[c:d]))
        elif i==4:
            a=90;b=100;c=110;d=120;
            Ten90.append(sum(Q90[90:100]))
            Ten90.append(sum(Q90[100:110]))
            Ten90.append(sum(Q90[110:120]))
            Ten95.append(sum(Q95[90:100]))
            Ten95.append(sum(Q95[100:110]))
            Ten95.append(sum(Q95[110:120]))
            out.append(sum(OutBase[90:100]))
            out.append(sum(OutBase[100:110]))
            out.append(sum(OutBase[110:120]))
            inandout.append(sum(ino[90:100]))
            inandout.append(sum(ino[100:110]))
            inandout.append(sum(ino[110:120]))
            tenpwn.append(sum(pwn[90:100]))
            tenpwn.append(sum(pwn[100:110]))
            tenpwn.append(sum(pwn[110:120]))
            tenul.append(sum(ul[a:b]))
            tenul.append(sum(ul[b:c]))
            tenul.append(sum(ul[c:d]))
            tenml.append(sum(ml[a:b]))
            tenml.append(sum(ml[b:c]))
            tenml.append(sum(ml[c:d]))
            tenll.append(sum(ll[a:b]))
            tenll.append(sum(ll[b:c]))
            tenll.append(sum(ll[c:d]))
            tensll.append(sum(sll[a:b]))
            tensll.append(sum(sll[b:c]))
            tensll.append(sum(sll[c:d]))
        elif i==5:
            a=120;b=130;c=140;d=151;
            Ten90.append(sum(Q90[120:130]))
            Ten90.append(sum(Q90[130:140]))
            Ten90.append(sum(Q90[140:151]))
            Ten95.append(sum(Q95[120:130]))
            Ten95.append(sum(Q95[130:140]))
            Ten95.append(sum(Q95[140:151]))
            out.append(sum(OutBase[120:130]))
            out.append(sum(OutBase[130:140]))
            out.append(sum(OutBase[140:151]))
            inandout.append(sum(ino[120:130]))
            inandout.append(sum(ino[130:140]))
            inandout.append(sum(ino[140:151]))
            tenpwn.append(sum(pwn[120:130]))
            tenpwn.append(sum(pwn[130:140]))
            tenpwn.append(sum(pwn[140:151]))
            tenul.append(sum(ul[a:b]))
            tenul.append(sum(ul[b:c]))
            tenul.append(sum(ul[c:d]))
            tenml.append(sum(ml[a:b]))
            tenml.append(sum(ml[b:c]))
            tenml.append(sum(ml[c:d]))
            tenll.append(sum(ll[a:b]))
            tenll.append(sum(ll[b:c]))
            tenll.append(sum(ll[c:d]))
            tensll.append(sum(sll[a:b]))
            tensll.append(sum(sll[b:c]))
            tensll.append(sum(sll[c:d]))
        elif i==6:
            a=151;b=161;c=171;d=181;
            Ten90.append(sum(Q90[151:161]))
            Ten90.append(sum(Q90[161:171]))
            Ten90.append(sum(Q90[171:181]))
            Ten95.append(sum(Q95[151:161]))
            Ten95.append(sum(Q95[161:171]))
            Ten95.append(sum(Q95[171:181]))
            out.append(sum(OutBase[151:161]))
            out.append(sum(OutBase[161:171]))
            out.append(sum(OutBase[171:181]))
            inandout.append(sum(ino[151:161]))
            inandout.append(sum(ino[161:171]))
            inandout.append(sum(ino[171:181]))
            tenpwn.append(sum(pwn[151:161]))
            tenpwn.append(sum(pwn[161:171]))
            tenpwn.append(sum(pwn[171:181]))
            tenul.append(sum(ul[a:b]))
            tenul.append(sum(ul[b:c]))
            tenul.append(sum(ul[c:d]))
            tenml.append(sum(ml[a:b]))
            tenml.append(sum(ml[b:c]))
            tenml.append(sum(ml[c:d]))
            tenll.append(sum(ll[a:b]))
            tenll.append(sum(ll[b:c]))
            tenll.append(sum(ll[c:d]))
            tensll.append(sum(sll[a:b]))
            tensll.append(sum(sll[b:c]))
            tensll.append(sum(sll[c:d]))
        elif i==7:
            a=181;b=191;c=201;d=212;
            Ten90.append(sum(Q90[181:191]))
            Ten90.append(sum(Q90[191:201]))
            Ten90.append(sum(Q90[201:212]))
            Ten95.append(sum(Q95[181:191]))
            Ten95.append(sum(Q95[191:201]))
            Ten95.append(sum(Q95[201:212]))
            out.append(sum(OutBase[181:191]))
            out.append(sum(OutBase[191:201]))
            out.append(sum(OutBase[201:212]))
            inandout.append(sum(ino[181:191]))
            inandout.append(sum(ino[191:201]))
            inandout.append(sum(ino[201:212]))
            tenpwn.append(sum(pwn[181:191]))
            tenpwn.append(sum(pwn[191:201]))
            tenpwn.append(sum(pwn[201:212]))
            tenul.append(sum(ul[a:b]))
            tenul.append(sum(ul[b:c]))
            tenul.append(sum(ul[c:d]))
            tenml.append(sum(ml[a:b]))
            tenml.append(sum(ml[b:c]))
            tenml.append(sum(ml[c:d]))
            tenll.append(sum(ll[a:b]))
            tenll.append(sum(ll[b:c]))
            tenll.append(sum(ll[c:d]))
            tensll.append(sum(sll[a:b]))
            tensll.append(sum(sll[b:c]))
            tensll.append(sum(sll[c:d]))
        elif i==8:
            a=212;b=222;c=232;d=243;
            Ten90.append(sum(Q90[212:222]))
            Ten90.append(sum(Q90[222:232]))
            Ten90.append(sum(Q90[232:243]))
            Ten95.append(sum(Q95[212:222]))
            Ten95.append(sum(Q95[222:232]))
            Ten95.append(sum(Q95[232:243]))
            out.append(sum(OutBase[212:222]))
            out.append(sum(OutBase[222:232]))
            out.append(sum(OutBase[232:243]))
            inandout.append(sum(ino[212:222]))
            inandout.append(sum(ino[222:232]))
            inandout.append(sum(ino[232:243]))
            tenpwn.append(sum(pwn[212:222]))
            tenpwn.append(sum(pwn[222:232]))
            tenpwn.append(sum(pwn[232:243]))
            tenul.append(sum(ul[a:b]))
            tenul.append(sum(ul[b:c]))
            tenul.append(sum(ul[c:d]))
            tenml.append(sum(ml[a:b]))
            tenml.append(sum(ml[b:c]))
            tenml.append(sum(ml[c:d]))
            tenll.append(sum(ll[a:b]))
            tenll.append(sum(ll[b:c]))
            tenll.append(sum(ll[c:d]))
            tensll.append(sum(sll[a:b]))
            tensll.append(sum(sll[b:c]))
            tensll.append(sum(sll[c:d]))
        elif i==9:
            a=243;b=253;c=263;d=273;
            Ten90.append(sum(Q90[243:253]))
            Ten90.append(sum(Q90[253:263]))
            Ten90.append(sum(Q90[263:273]))
            Ten95.append(sum(Q95[243:253]))
            Ten95.append(sum(Q95[253:263]))
            Ten95.append(sum(Q95[263:273]))
            out.append(sum(OutBase[243:253]))
            out.append(sum(OutBase[253:263]))
            out.append(sum(OutBase[263:273]))
            inandout.append(sum(ino[243:253]))
            inandout.append(sum(ino[253:263]))
            inandout.append(sum(ino[263:273]))
            tenpwn.append(sum(pwn[243:253]))
            tenpwn.append(sum(pwn[253:263]))
            tenpwn.append(sum(pwn[263:273]))
            tenul.append(sum(ul[a:b]))
            tenul.append(sum(ul[b:c]))
            tenul.append(sum(ul[c:d]))
            tenml.append(sum(ml[a:b]))
            tenml.append(sum(ml[b:c]))
            tenml.append(sum(ml[c:d]))
            tenll.append(sum(ll[a:b]))
            tenll.append(sum(ll[b:c]))
            tenll.append(sum(ll[c:d]))
            tensll.append(sum(sll[a:b]))
            tensll.append(sum(sll[b:c]))
            tensll.append(sum(sll[c:d]))
        elif i==10:
            a=273;b=283;c=293;d=304;
            Ten90.append(sum(Q90[273:283]))
            Ten90.append(sum(Q90[283:293]))
            Ten90.append(sum(Q90[293:304]))
            Ten95.append(sum(Q95[273:283]))
            Ten95.append(sum(Q95[283:293]))
            Ten95.append(sum(Q95[293:304]))
            out.append(sum(OutBase[273:283]))
            out.append(sum(OutBase[283:293]))
            out.append(sum(OutBase[293:304]))
            inandout.append(sum(ino[273:283]))
            inandout.append(sum(ino[283:293]))
            inandout.append(sum(ino[293:304]))
            tenpwn.append(sum(pwn[273:283]))
            tenpwn.append(sum(pwn[283:293]))
            tenpwn.append(sum(pwn[293:304]))
            tenul.append(sum(ul[a:b]))
            tenul.append(sum(ul[b:c]))
            tenul.append(sum(ul[c:d]))
            tenml.append(sum(ml[a:b]))
            tenml.append(sum(ml[b:c]))
            tenml.append(sum(ml[c:d]))
            tenll.append(sum(ll[a:b]))
            tenll.append(sum(ll[b:c]))
            tenll.append(sum(ll[c:d]))
            tensll.append(sum(sll[a:b]))
            tensll.append(sum(sll[b:c]))
            tensll.append(sum(sll[c:d]))
        elif i==11:
            a=304;b=314;c=324;d=334;
            Ten90.append(sum(Q90[304:314]))
            Ten90.append(sum(Q90[314:324]))
            Ten90.append(sum(Q90[324:334]))
            Ten95.append(sum(Q95[304:314]))
            Ten95.append(sum(Q95[314:324]))
            Ten95.append(sum(Q95[324:334]))
            out.append(sum(OutBase[304:314]))
            out.append(sum(OutBase[314:324]))
            out.append(sum(OutBase[324:334]))
            inandout.append(sum(ino[304:314]))
            inandout.append(sum(ino[314:324]))
            inandout.append(sum(ino[324:334]))
            tenpwn.append(sum(pwn[304:314]))
            tenpwn.append(sum(pwn[314:324]))
            tenpwn.append(sum(pwn[324:334]))
            tenul.append(sum(ul[a:b]))
            tenul.append(sum(ul[b:c]))
            tenul.append(sum(ul[c:d]))
            tenml.append(sum(ml[a:b]))
            tenml.append(sum(ml[b:c]))
            tenml.append(sum(ml[c:d]))
            tenll.append(sum(ll[a:b]))
            tenll.append(sum(ll[b:c]))
            tenll.append(sum(ll[c:d]))
            tensll.append(sum(sll[a:b]))
            tensll.append(sum(sll[b:c]))
            tensll.append(sum(sll[c:d]))
        elif i==12:
            a=334;b=344;c=354;d=365;
            Ten90.append(sum(Q90[334:344]))
            Ten90.append(sum(Q90[344:354]))
            Ten90.append(sum(Q90[354:365]))
            Ten95.append(sum(Q95[334:344]))
            Ten95.append(sum(Q95[344:354]))
            Ten95.append(sum(Q95[354:365]))
            out.append(sum(OutBase[334:344]))
            out.append(sum(OutBase[344:354]))
            out.append(sum(OutBase[354:365]))
            inandout.append(sum(ino[334:344]))
            inandout.append(sum(ino[344:354]))
            inandout.append(sum(ino[354:365]))
            tenpwn.append(sum(pwn[334:344]))
            tenpwn.append(sum(pwn[344:354]))
            tenpwn.append(sum(pwn[354:365]))
            tenul.append(sum(ul[a:b]))
            tenul.append(sum(ul[b:c]))
            tenul.append(sum(ul[c:d]))
            tenml.append(sum(ml[a:b]))
            tenml.append(sum(ml[b:c]))
            tenml.append(sum(ml[c:d]))
            tenll.append(sum(ll[a:b]))
            tenll.append(sum(ll[b:c]))
            tenll.append(sum(ll[c:d]))
            tensll.append(sum(sll[a:b]))
            tensll.append(sum(sll[b:c]))
            tensll.append(sum(sll[c:d]))
    return Ten90,Ten95,out,inandout,tenpwn,tenul,tenml,tenll,tensll

cor_df = daytotenloop(Q90,Q95,OutBase,ino,pwn,ul,ml,ll,sll)

#cor_df = [Ten90,Ten95,out,inandout,pwn]
#output_csv = 'output.csv'
#cor_df.to_csv(output_csv, sep=',', encoding='utf-8')
with open('output.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerows(cor_df)

'''
DB section
'''
import MySQLdb
import MySQLdb.cursors
try:
    conn = MySQLdb.connect(host='localhost',
                            user='demouser',
                            passwd='demo1234',
                            db='demo',
                            charset='utf8')
    print("Connect to mysql through demouser.")
except:
    print("Can't Connect Database via demouser: ", sys.exc_info()[0])
    sys.exit()
    
cursor = conn.cursor()  

#insert into database
ten90=cor_df[0]
ten95=cor_df[1]
out=cor_df[2]
inandout=cor_df[3]
pwn=cor_df[4]
insert90 = '\"' + '\",\"'.join(map(str, ten90)) + '\"'
insert95 = '\"' + '\",\"'.join(map(str, ten95)) + '\"'
insertout = '\"' + '\",\"'.join(map(str, out)) + '\"'
insertinandout = '\"' + '\",\"'.join(map(str, inandout)) + '\"'
insertpwn = '\"' + '\",\"'.join(map(str, pwn)) + '\"'

#print('Q90 = '+insert90)
#print('Q95 = '+insert95)
#print('In and out = '+insertinandout)
#print('pwn = '+insertpwn)

#insert to DB
sql90 = "INSERT INTO Q90 (Ten_1, Ten_2, Ten_3, Ten_4, Ten_5, Ten_6, Ten_7, \
Ten_8, Ten_9, Ten_10, Ten_11, Ten_12, Ten_13, Ten_14, Ten_15, Ten_16, Ten_17, \
Ten_18, Ten_19, Ten_20, Ten_21, Ten_22, Ten_23, Ten_24, Ten_25, Ten_26, Ten_27,\
Ten_28, Ten_29, Ten_30, Ten_31, Ten_32, Ten_33, Ten_34, Ten_35, Ten_36) \
values ("+insert90+");"

sql95 = "INSERT INTO Q95 (Ten_1, Ten_2, Ten_3, Ten_4, Ten_5, Ten_6, Ten_7, \
Ten_8, Ten_9, Ten_10, Ten_11, Ten_12, Ten_13, Ten_14, Ten_15, Ten_16, Ten_17, \
Ten_18, Ten_19, Ten_20, Ten_21, Ten_22, Ten_23, Ten_24, Ten_25, Ten_26, Ten_27,\
Ten_28, Ten_29, Ten_30, Ten_31, Ten_32, Ten_33, Ten_34, Ten_35, Ten_36) values \
("+insert95+");"

sqlinandout = "INSERT INTO IrrigationWaterDemand (IrrigationWaterDemand_1,\
IrrigationWaterDemand_2,IrrigationWaterDemand_3,IrrigationWaterDemand_4,\
IrrigationWaterDemand_5,IrrigationWaterDemand_6,IrrigationWaterDemand_7,\
IrrigationWaterDemand_8,IrrigationWaterDemand_9,IrrigationWaterDemand_10,\
IrrigationWaterDemand_11,IrrigationWaterDemand_12,IrrigationWaterDemand_13,\
IrrigationWaterDemand_14,IrrigationWaterDemand_15,IrrigationWaterDemand_16,\
IrrigationWaterDemand_17,IrrigationWaterDemand_18,IrrigationWaterDemand_19,\
IrrigationWaterDemand_20,IrrigationWaterDemand_21,IrrigationWaterDemand_22,\
IrrigationWaterDemand_23,IrrigationWaterDemand_24,IrrigationWaterDemand_25,\
IrrigationWaterDemand_26,IrrigationWaterDemand_27,IrrigationWaterDemand_28,\
IrrigationWaterDemand_29,IrrigationWaterDemand_30,IrrigationWaterDemand_31,\
IrrigationWaterDemand_32,IrrigationWaterDemand_33,IrrigationWaterDemand_34,\
IrrigationWaterDemand_35,IrrigationWaterDemand_36) values ("+insertinandout+");"

sqlpwn = "INSERT INTO PeoplesLivelihoodWater (PeoplesLivelihoodWater_1,\
PeoplesLivelihoodWater_2,PeoplesLivelihoodWater_3,PeoplesLivelihoodWater_4,\
PeoplesLivelihoodWater_5,PeoplesLivelihoodWater_6,PeoplesLivelihoodWater_7,\
PeoplesLivelihoodWater_8,PeoplesLivelihoodWater_9,PeoplesLivelihoodWater_10,\
PeoplesLivelihoodWater_11,PeoplesLivelihoodWater_12,PeoplesLivelihoodWater_13,\
PeoplesLivelihoodWater_14,PeoplesLivelihoodWater_15,PeoplesLivelihoodWater_16,\
PeoplesLivelihoodWater_17,PeoplesLivelihoodWater_18,PeoplesLivelihoodWater_19,\
PeoplesLivelihoodWater_20,PeoplesLivelihoodWater_21,PeoplesLivelihoodWater_22,\
PeoplesLivelihoodWater_23,PeoplesLivelihoodWater_24,PeoplesLivelihoodWater_25,\
PeoplesLivelihoodWater_26,PeoplesLivelihoodWater_27,PeoplesLivelihoodWater_28,\
PeoplesLivelihoodWater_29,PeoplesLivelihoodWater_30,PeoplesLivelihoodWater_31,\
PeoplesLivelihoodWater_32,PeoplesLivelihoodWater_33,PeoplesLivelihoodWater_34,\
PeoplesLivelihoodWater_35,PeoplesLivelihoodWater_36) values ("+insertpwn+");"

#outbase table is not created
cursor.execute(sql90)
cursor.execute(sql95)
cursor.execute(sqlinandout)
cursor.execute(sqlpwn)

print('successfully import csv file to mysql!')


conn.commit()

# Close DB link
cursor.close()
conn.close()
