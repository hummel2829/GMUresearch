import numpy as np
import matplotlib
from matplotlib import pyplot as plt
from snAPI.Main import *

filename = r'C:\Users\johnh\Desktop\Stuff\Physics\Research GMU\picoquant\correlation measurments\data\thermal bulb t2  test 1 1-3-2024.ptu'




# reads `Unfold` data for measuretime (in millisec) in :obj:`.MeasMode.T2`
measuretime = 1 #(integer milliseconds)

sn = snAPI()
sn.getFileDevice(filename)
sn.initDevice(MeasMode.T2)

sn.unfold.measure(measuretime)

timetag, channel = sn.unfold.getData()
#sn.logPrint(f"{len(timetag)} records read")
#sn.logPrint(timetag)

nptimetag = np.array(timetag)
print(nptimetag[0:10])
print(len(nptimetag))
npchannel = np.array(channel)



sn.logPrint('end of code')


print('0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
