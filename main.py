from AggregateModel import Aggregation
from Anamoly import Anamoly
import time

TABLES_NAMES = ['heart_table','spo2_table','temperature_table']
DEVICE_ID = ['BSM_G101','BSM_G102']

aggregation1 = Aggregation(DEVICE_ID[0])
aggregation1.aggregate()
print(f'Aggregating data for {DEVICE_ID[0]} ')


aggregation2 = Aggregation(DEVICE_ID[1])
aggregation2.aggregate()
print(f'Aggregating data for {DEVICE_ID[1]}')

time.sleep(2)

print('-------ANAMOLY DETECTION-------------------')


for i in TABLES_NAMES:
    anamoly_device1 = Anamoly(DEVICE_ID[0],i)
    anamoly_device2 = Anamoly(DEVICE_ID[1],i)

    print(f'Processing rules for {DEVICE_ID[0]} ')
    anamoly_device1.Anamoly_detected()
    print(f'Processing rules for {DEVICE_ID[1]}')
    anamoly_device2.Anamoly_detected()
    break
    



