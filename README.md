Scrapy
===
```
+-------------------------+
| Tables_in_demo          |
+-------------------------+
| City                    |
| FlowObservatory         |
| Forecast                |
| IrrigationArea          |
| Light                   |
| Location                |
| NextReservoirLights     |
| NextWeekP               |
| PreWaterLevel           |
| PreWaterStorageCapacity |
| Q90                     |
| Q95                     |
| RegionalWaterRegime     |
| Reservoir               |
| ReservoirState          |
| RuleCurve               |
| SimReservoirFlow        |
| WaterIntakeStructures   |
| WaterSupply             |
| a136                    |
+-------------------------+
```

output documentation
1st row = Q90 旬
2nd row = Q95 旬
3rd row = OutBase 旬

```
mysql> INSERT INTO <table name> VALUES (val1, val2,...)
```
For example:
```
INSERT INTO Light (C_ID, FT_ID, Light_1, Light_2, Light_3, Light_4, Light_5, Light_6, Light_7, Light_8, Light_9, Light_10, Light_11,Light_12) VALUES (1,2,'藍','藍','綠','綠','綠','綠','綠','綠','綠','黃','黃','黃')
```
```
mysql> insert into Q90 (Ten_1, Ten_2, Ten_3, Ten_4, Ten_5, Ten_6, Ten_7, Ten_8, Ten_9, Ten_10, Ten_11, Ten_12, Ten_13, Ten_14, Ten_15, Ten_16, Ten_17, Ten_18, Ten_19, Ten_20, Ten_21, Ten_22, Ten_23, Ten_24, Ten_25, Ten_26, Ten_27, Ten_28, Ten_29, Ten_30, Ten_31, Ten_32, Ten_33, Ten_34, Ten_35, Ten_36) values (170.5798224,162.6796656,185.6082817,180.6139296,174.3936912,139.5694368,236.1874464,267.197832,339.615936,502.159392,404.542512,329.1732,309.9676464,505.1106,440.8196689,605.5878816,789.1530192,643.0001184,461.1148992,439.1397504,514.9630944,440.184024,403.9522704,664.702848,536.5750176,536.1209856,608.1304608,477.0968256,345.3367392,304.0652304,241.9082496,222.021648,221.8400352,181.4765904,167.9464368,169.4901456)
```

insert
===
```
insert into Location values("1","test");
insert into City (CityName,L_ID) values ("test", 1);
insert into FlowObservatory (C_ID,BasinIdentifier,ObservatoryName) values ("5",1,2);
```