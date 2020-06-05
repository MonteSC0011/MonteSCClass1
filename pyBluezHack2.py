#Class Libraries for the bluetooth application

import time #<---Class Library. 1st 

from bluetooth.ble import BeaconService #<---3rd Party module 

service = BeaconService() #<--Creating an instance object of the class library. 

service.start_advertising("11111111-2222-3333-4444-555555555555", 1, 1, 1, 200) #<---Advertise the UUID and different ports for spoofing devices.

time.sleep(15)
service.stop_advertise()

print("Done.")


