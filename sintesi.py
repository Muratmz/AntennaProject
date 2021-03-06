import antenna_package
import math
from pylab import*

r = float(20)
f0 = 5.8*10**9
file_gain = open("gain.txt",'r')
file_angles = open("angles.txt",'r')

gain = []
angles = []
while True:
    line = file_gain.readline()
    if not line:
        break
    gain.append(float(line))
file_gain.close()

while True:
    line = file_angles.readline()
    if not line:
        break
    angles.append(float(line))
file_angles.close()

for item in gain:
    item = 10**item/10

n = [ 5,7,9 ]
array_factors = zeros((len(n),len(gain)))
array_factors_gain = zeros((len(n),len(gain)))
system_gain = zeros((len(n),len(gain)))
max_gain = zeros(len(n))
beam_width = zeros(len(n))
output = open("beamwidth.txt",'wa')
for item in range(0,len(n)):
    synthesis_result = antenna_package.chebyshevSynthesis( f0, r , angles , gain, n[item] )
    array_factors[item] = synthesis_result[0]
    array_factors_gain[item] = synthesis_result[1]
    system_gain[item] = synthesis_result[2]
    max_gain[item] = synthesis_result[3]
    beam_width[item] = synthesis_result[4]

for item in range(0,len(n)):
    output.write("N = " + str(n[item]) + " bw = " + str(beam_width[item]) + "\n")
output.close()
max_gain_db = 10*log10(max_gain)
array_factors_abs = abs(array_factors)
array_factors_abs_db = 20*log10(array_factors_abs)
array_factors_gain_db = 10*log10(array_factors_gain)
system_gain_db = 10*log10(system_gain)

g = []
for item in angles:
    g.append(-1*item)
g=g[::-1]
axes = g + angles
a = list(array_factors_abs_db[2][::-1]) + list(array_factors_abs_db[2])

for item in range(0,len(n)):
    names_array_factors = [ "db","angle","Array factor absolute value for " + str(n[item]) + " elements"]    
    figure()
    antenna_package.plot_function(angles,array_factors_abs_db[item],names_array_factors)
    show()
    names_system_gain = ["db","angle"," Gain of the " + str(n[item]) + " elements array patch antenna"]
    figure()
    antenna_package.plot_function(angles,system_gain_db[item],names_system_gain)
    show()
