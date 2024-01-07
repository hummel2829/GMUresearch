import matplotlib.pyplot as plt
import numpy as np
from math import ceil
from io import StringIO



filename = r'C:\Users\johnh\Desktop\Stuff\Physics\Research GMU\picoquant\correlation measurments\data\thor laser test 1 1-2-2024.out'
#file path for thor laser test 1 1-2-2024
#assumed T2 data

photons = np.genfromtxt(filename, skip_header=2, invalid_raise=False, dtype=str)
#print(photons)

recordstring = photons[:,0]
record = recordstring.astype(np.int64)
#record of detection

Channelstring = photons[:,2]
Channel = Channelstring.astype(np.int64)
#detector that made measurement

TimeTagstring = photons[:,3]
TimeTag = TimeTagstring.astype(np.int64)

TrueTimestring = np.char.strip(photons[:,4], chars='(')
TrueTime = TrueTimestring.astype(np.float64)


T2datareconstruct = np.vstack((record, Channel, TimeTag, TrueTime)).T
print(T2datareconstruct)



