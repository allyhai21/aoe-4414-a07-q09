# max_bitrate.py
#
# Usage: python3 script_name.py arg1 arg2 ...
#  Text explaining script usage
# Parameters:
#  arg1: description of argument 1
#  arg2: description of argument 2
#  ...
# Output:
#  A description of the script output
#
# Written by Brad Denby
# Other contributors: Allison Hai
#
# Optional license statement, e.g., See the LICENSE file for the license.

# import Python modules
import sys
import math

# "constants"
c = 299792458
L_l = math.pow(10,-1/10)
L_a = math.pow(10,0/10)

# helper functions

## function description
# def calc_something(param1, param2):
#   pass

# initialize script arguments
tx_w       = float('nan') #input channel count
tx_gain_db = float('nan') #input height count 
freq_hz    = float('nan') # input width count 
dist_km    = float('nan') #avergae pooling kernel height count 
rx_gain_db = float('nan') #avergae pooling kernal width count 
n0_j       = float('nan') #stride of average pooling kernel 
bw_hz      = float('nan') #amount of padding on each of the four input map sides 

# parse script arguments
if len(sys.argv)==8:
    tx_w       = float(sys.argv[1])
    tx_gain_db = float(sys.argv[2])
    freq_hz    = float(sys.argv[3])
    dist_km    = float(sys.argv[4])
    rx_gain_db = float(sys.argv[5])
    n0_j       = float(sys.argv[6])
    bw_hz      = float(sys.argv[7])
else:
    print(\
        'Usage: '\
        'max_bitrate.py tx_w tx_gain_db freq_hz dist_km rx_gain_db n0_j bw_hz'\
    )
    exit()

# write script below this line
tx_gain = 10**(tx_gain_db/10)
rx_gain = 10**(rx_gain_db/10) 

wavelength = c/freq_hz
C = tx_w*L_l*tx_gain*L_a*rx_gain*(wavelength/(4*math.pi*dist_km))**2
N = n0_j*bw_hz
r_max = bw_hz*math.log((1+C/N),2)


print(math.floor(r_max))