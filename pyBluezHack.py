

#This script that advertises a bluetooth low energy beacon for 15 seconds


import time #<----1st party class module 

from bluetooth.ble import BeaconService #<----3rd party module 

#Create an instance of the object from the 3rd party class

service = BeaconService()


service.start_advertising("11111111-2222-3333-4444-555555555555", 1, 1,1, 200) #<----

time.sleep(15)

service.stop_advertising()

print("Done.")
