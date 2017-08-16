#!/home/ubuntu/.env/bin/python
# -*- coding: utf-8 -*-

import sys
import MySQLdb
import MySQLdb.cursors

try:
    r_conn = MySQLdb.connect(host='127.0.0.1',
                            user='root',
                            passwd='root1234',
                            charset='utf8')
except:
    print("Can't Connect Database via root: ", sys.exc_info()[0])
    sys.exit()

# drop db and user if exist
r_cursor = r_conn.cursor()

# create user and db, and grant privileges
r_cursor.execute("CREATE USER 'demouser'@'localhost' IDENTIFIED BY 'demo1234'")
r_cursor.execute("CREATE DATABASE demo CHARACTER SET UTF8")
r_cursor.execute("GRANT ALL PRIVILEGES ON demo.* to 'demouser'@'localhost'")
r_cursor.execute("FLUSH PRIVILEGES")
r_cursor.close()
r_conn.close()

# connect demo db
try:
    conn = MySQLdb.connect(host='127.0.0.1',
                            user='demouser',
                            passwd='demo1234',
                            db='demo',
                            charset='utf8')
except:
    print("Can't Connect Database via demouser: ", sys.exc_info()[0])
    sys.exit()

# create schema
cursor = conn.cursor()
# cursor.execute("DROP TABLE if EXISTS a136")
cursor.execute("USE demo")
cursor.execute("""CREATE TABLE a136 (
                pk INT(12) NOT NULL AUTO_INCREMENT PRIMARY KEY,
                name CHAR(10) NOT NULL,
                sid CHAR(5) NOT NULL,
                t_10m FLOAT(6,1) DEFAULT NULL,
                t_1h FLOAT(6,1) DEFAULT NULL,
                t_3h FLOAT(6,1) DEFAULT NULL,
                t_6h FLOAT(6,1) DEFAULT NULL,
                t_12h FLOAT(6,1) DEFAULT NULL,
                t_24h FLOAT(6,1) DEFAULT NULL,
                t_today FLOAT(6,1) DEFAULT NULL,
                t_yday FLOAT(6,1) DEFAULT NULL,
                t_2d FLOAT(6,1) DEFAULT NULL,
                Realtime CHAR(30) NOT NULL
                ) ENGINE=InnoDB""")


#cursor.execute("drop table if exists City")

# cursor.execute("drop table if exists FlowObservatory")

# cursor.execute("drop table if exists Forecast")

# cursor.execute("drop table if exists IrrigationArea")

# cursor.execute("drop table if exists Light")

# cursor.execute("drop table if exists Location")

# cursor.execute("drop table if exists PreWaterLevel")

# cursor.execute("drop table if exists PreWaterStorageCapacity")

# cursor.execute("drop table if exists Q90")

# cursor.execute("drop table if exists Q95")

# cursor.execute("drop table if exists RegionalWaterRegime")
# cursor.execute("drop table if exists NextReservoirLights")
# cursor.execute("drop table if exists NextWeekP")

# cursor.execute("drop table if exists ReservoirState")

# cursor.execute("drop table if exists Reservoir")

# cursor.execute("drop table if exists RuleCurve")

# cursor.execute("drop table if exists SimReservoirFlow")

# cursor.execute("drop table if exists Temperature")

# cursor.execute("drop table if exists WaterIntakeStructures")

# cursor.execute("drop table if exists WaterSupply")

cursor = conn.cursor()
#/*==============================================================*/
#/* Table: Location                                              */
#/*==============================================================*/
cursor.execute("""create table Location
(
   L_ID                 int not null auto_increment,
   LocationName         varchar(3),
   primary key (L_ID)
)ENGINE=InnoDB""")

cursor = conn.cursor()
#/*==============================================================*/
#/* Table: City                                                  */
#/*==============================================================*/
cursor.execute("""create table City(
                C_ID                 int not null auto_increment,
                CityName             varchar(10),
                L_ID                 int,
                PeoplesLivelihoodWater float,
                IndustrialWater   float default NULL,
                IrrigationWaterDemand float,
                primary key (C_ID),
                FOREIGN KEY (L_ID) REFERENCES Location (L_ID)
                )ENGINE=InnoDB""")
   
cursor = conn.cursor()
#/*==============================================================*/
#/* Table: FlowObservatory                                       */
#/*==============================================================*/
cursor.execute("""create table FlowObservatory
(
   FO_ID                int not null auto_increment,
   C_ID                 int,
   BasinIdentifier      varchar(10),
   ObservatoryName      varchar(10),
   primary key (FO_ID),
   FOREIGN KEY (C_ID) REFERENCES City (C_ID)
)ENGINE=InnoDB""")
cursor = conn.cursor()
#/*==============================================================*/
#/* Table: Forecast                                              */
#/*==============================================================*/
cursor.execute("""create table Forecast
(
   F_ID                 int not null,
   L_ID                 int,
   TimeStamp            datetime,
   ElementValue         varchar(10),
   ForecastP            float,
   ForecastT            float,
   primary key (F_ID),
   FOREIGN KEY (L_ID) REFERENCES Location (L_ID)
)ENGINE=InnoDB""")
cursor = conn.cursor()
#/*==============================================================*/
#/* Table: IrrigationArea                                        */
#/*==============================================================*/
cursor.execute("""create table IrrigationArea
(
   IRR_ID               int not null auto_increment,
   IrrigationName       varchar(10),
   IrrigationArea       float,
   Fallow               int,
   primary key (IRR_ID)
)ENGINE=InnoDB""")
cursor = conn.cursor()
#/*==============================================================*/
#/* Table: Light                                                 */
#/*==============================================================*/
cursor.execute("""create table Light
(
   Light_ID             int not null auto_increment,
   C_ID                 int,
   TimeStamp            datetime,
   Light                varchar(10),
   primary key (Light_ID),
   FOREIGN KEY (C_ID) REFERENCES City (C_ID)
)ENGINE=InnoDB""")

cursor = conn.cursor()
#/*==============================================================*/
#/* Table: Reservoir                                              */
#/*==============================================================*/
cursor.execute("""create table Reservoir
(
   R_ID                 int not null auto_increment,
   ReservoirIdentifier  varchar(8) not null,
   ReservoirName         varchar(10),
   primary key (R_ID)
)ENGINE=InnoDB""")

cursor = conn.cursor()
#/*==============================================================*/
#/* Table: PreWaterLevel                                         */
#/*==============================================================*/
cursor.execute("""create table PreWaterLevel
(
   PWL_ID               int not null auto_increment,
   R_ID                 int,
   PredictionWaterLevel float,
   primary key (PWL_ID),
   foreign key (R_ID) references Reservoir (R_ID)
)ENGINE=InnoDB""")

cursor = conn.cursor()
#/*==============================================================*/
#/* Table: PreWaterStorageCapacity                               */
#/*==============================================================*/
cursor.execute("""create table PreWaterStorageCapacity
(
   PWSC_ID               int not null,
   R_ID                 int,
   PredictionWaterStorageCapacity float,
   primary key (PWSC_ID),
   foreign key (R_ID) references Reservoir (R_ID)
)ENGINE=InnoDB""")

cursor = conn.cursor()
#/*==============================================================*/
#/* Table: Q90                                                   */
#/*==============================================================*/
cursor.execute("""create table Q90
(
   Q90_ID               int not null auto_increment,
   FO_ID                int,
   Ten_1                float,
   Ten_2                float,
   Ten_3                float,
   Ten_4                float,
   Ten_5                float,
   Ten_6                float,
   Ten_7                float,
   Ten_8                float,
   Ten_9                float,
   Ten_10               float,
   Ten_11               float,
   Ten_12               float,
   Ten_13               float,
   Ten_14               float,
   Ten_15               float,
   Ten_16               float,
   Ten_17               float,
   Ten_18               float,
   Ten_19               float,
   Ten_20               float,
   Ten_21               float,
   Ten_22               float,
   Ten_23               float,
   Ten_24               float,
   Ten_25               float,
   Ten_26               float,
   Ten_27               float,
   Ten_28               float,
   Ten_29               float,
   Ten_30               float,
   Ten_31               float,
   Ten_32               float,
   Ten_33               float,
   Ten_34               float,
   Ten_35               float,
   Ten_36               float,
   primary key (Q90_ID),
   FOREIGN KEY (FO_ID) REFERENCES FlowObservatory (FO_ID)
)ENGINE=InnoDB""")
cursor = conn.cursor()
#/*==============================================================*/
#/* Table: Q95                                                   */
#/*==============================================================*/
cursor.execute("""create table Q95
(
   Q95_ID               int not null auto_increment,
   FO_ID                int,
   Ten_1                float,
   Ten_2                float,
   Ten_3                float,
   Ten_4                float,
   Ten_5                float,
   Ten_6                float,
   Ten_7                float,
   Ten_8                float,
   Ten_9                float,
   Ten_10               float,
   Ten_11               float,
   Ten_12               float,
   Ten_13               float,
   Ten_14               float,
   Ten_15               float,
   Ten_16               float,
   Ten_17               float,
   Ten_18               float,
   Ten_19               float,
   Ten_20               float,
   Ten_21               float,
   Ten_22               float,
   Ten_23               float,
   Ten_24               float,
   Ten_25               float,
   Ten_26               float,
   Ten_27               float,
   Ten_28               float,
   Ten_29               float,
   Ten_30               float,
   Ten_31               float,
   Ten_32               float,
   Ten_33               float,
   Ten_34               float,
   Ten_35               float,
   Ten_36               float,
   primary key (Q95_ID),
   FOREIGN KEY (FO_ID) REFERENCES FlowObservatory (FO_ID)
)ENGINE=InnoDB""")

cursor = conn.cursor()
#/*==============================================================*/
#/* Table: RegionalWaterRegime                                   */
#/*==============================================================*/
cursor.execute("""create table RegionalWaterRegime
(
   RWR_ID               int not null,
   C_ID                 int,
   TimeStamp            datetime,
   ReservoirLightsNow   varchar(10),
   primary key (RWR_ID),
   FOREIGN KEY (C_ID) REFERENCES City (C_ID)
)ENGINE=InnoDB""")

cursor = conn.cursor()
#/*==============================================================*/
#/* Table: NextReservoirLights                                   */
#/*==============================================================*/
cursor.execute("""create table NextReservoirLights
(
   NRL_ID               int not null,
   C_ID                 int,
   NextReservoirLights  varchar(10),
   ReleaseTime          datetime,
   primary key (NRL_ID),
   FOREIGN KEY (C_ID) REFERENCES City (C_ID)
)ENGINE=InnoDB""")

cursor = conn.cursor()
#/*==============================================================*/
#/* Table: NextWeekP                                   */
#/*==============================================================*/
cursor.execute("""create table NextWeekP
(
   NWP_ID               int not null,
   C_ID                 int,
   NextWeekP            int,
   primary key (NWP_ID),
   FOREIGN KEY (C_ID) REFERENCES City (C_ID)
)ENGINE=InnoDB""")




cursor = conn.cursor()
#/*==============================================================*/
#/* Table: ReservoirState                                        */
#/*==============================================================*/
cursor.execute("""create table ReservoirState
(
   RS_ID                int not null,
   R_ID                 int,
   TimeStamp            datetime,
   WaterLevel           float,
   EffectiveWaterStorageCapacity float,
   PercentageUsedInReservoirCapacity float,
   MaximumCapacity      float,
   primary key (RS_ID),
   FOREIGN KEY (R_ID) REFERENCES Reservoir (R_ID)
)ENGINE=InnoDB""")

cursor = conn.cursor()
#/*==============================================================*/
#/* Table: RuleCurve                                             */
#/*==============================================================*/
cursor.execute("""create table RuleCurve
(
   RC_ID                int not null auto_increment,
   R_ID                 int,
   TenDays_No           float,
   UpperLimit           float,
   MidLimit             float,
   LowerLimit           float,
   SeriousLowerLimit    float,
   primary key (RC_ID),
   FOREIGN KEY (R_ID) REFERENCES Reservoir (R_ID)
)ENGINE=InnoDB""")
cursor = conn.cursor()
#/*==============================================================*/
#/* Table: SimReservoirFlow                                       */
#/*==============================================================*/
cursor.execute("""create table SimReservoirFlow
(
   SRF_ID               int not null,
   R_ID                 int,
   TimeStamp            datetime,
   StreamFlow           float,
   PlanWaterDemand      float,
   IrrigationRequirement float,
   WaterRight           float,
   primary key (SRF_ID),
   foreign key (R_ID) references Reservoir (R_ID)
)ENGINE=InnoDB""")

cursor = conn.cursor()
#/*==============================================================*/
#/* Table: WaterIntakeStructures                                 */
#/*==============================================================*/
cursor.execute("""create table WaterIntakeStructures
(
   WIS_ID               int not null auto_increment,
   StructuresName       varchar(10),
   Q_downstream         float,
   MaxQ                 float,
   primary key (WIS_ID)
)ENGINE=InnoDB""")
cursor = conn.cursor()
#/*==============================================================*/
#/* Table: WaterSupply                                           */
#/*==============================================================*/
cursor.execute("""create table WaterSupply
(
   WS_ID                int not null auto_increment,
   R_ID                 int,
   C_ID                 int,
   primary key (WS_ID),
   foreign key (C_ID) references City (C_ID),
   foreign key (R_ID) references Reservoir (R_ID)
)ENGINE=InnoDB""")


cursor.close()
conn.close()

