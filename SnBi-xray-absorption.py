import re,string,os,sys,scipy


from math import *
from pylab import *
import matplotlib
matplotlib.rc('text', usetex = True)
import scipy.optimize

from xraylib import *
import xrayhelp

XRayInit()
# print LineEnergy(26,0) 

DEGREES2RADIANS = pi/180.0
RADIANS2DEGREES = 180.0/pi


AVOGNUM = 0.602252

# Z_Br = 35
# Bromine 
# Edge K = 13.474 keV
# Emission Ka = 11.9230003 keV
# Emission Kb = 13.29 keV
#
# DCSP_Rayl
# //////////////////////////////////////////////////////////////////////
# //                                                                  //
# //         Differential Rayleigh scattering cross section           // 
# //                for polarized beam (cm2/g/sterad)                 //
# //                                                                  //
# //          Z : atomic number                                       //
# //          E : Energy (keV)                                        //
# //          theta : scattering polar angle (radians)                //
# //          phi : scattering azimuthal angle (radians)              //
# //                                                                  //
# //////////////////////////////////////////////////// /////////////////
# >>> float DCSP_Rayl(int Z, float E, float theta, float phi)
#

print DCSP_Rayl(35, 13.3,90.0*DEGREES2RADIANS,45.0*DEGREES2RADIANS)


Sn_Z = 50
Sn_atomic_wt = 118.690002
Sn_density = 5.30999994

Bi_Z = 83
Bi_atomic_wt = 209
Bi_density = 9.80000019

Au_Z = 79
Au_atomic_wt = 197.199997
Au_density = 19.3700008

energy = linspace(1,100,10000)

Sn_attenuation_len = []
Bi_attenuation_len = []
Au_attenuation_len = []


Sn_absorption = []
Bi_absorption = []
Au_absorption = []


thickness = 20.

for e in energy:
	Sn_attenuation_len.append( 10000*(Sn_density*CS_Total(Sn_Z,e))**-1  )# microns
	Bi_attenuation_len.append( 10000*(Bi_density*CS_Total(Bi_Z,e))**-1  )# microns
	Au_attenuation_len.append( 10000*(Au_density*CS_Total(Au_Z,e))**-1  )# microns

	Sn_absorption.append(1.0 - exp(-1*thickness/(10000*(Sn_density*CS_Total(Sn_Z,e))**-1)))
	Bi_absorption.append(1.0 - exp(-1*thickness/(10000*(Bi_density*CS_Total(Bi_Z,e))**-1)))
	Au_absorption.append(1.0 - exp(-1*thickness/(10000*(Au_density*CS_Total(Au_Z,e))**-1)))


semilogy(energy,Sn_attenuation_len,'k-')
semilogy(energy,Bi_attenuation_len,'r-')
semilogy(energy,Au_attenuation_len,'y-')

xlabel('Energy (keV)', fontsize = 18)
ylabel('Attenuation length (microns)', fontsize = 18)
title('Absorbers: X-ray Attenuation Lengths', fontsize = 20)
legend((r'Sn', r'Bi', r'Au'), shadow = True, loc = 0,numpoints = 2)
ltext = gca().get_legend().get_texts()
setp(ltext[0], fontsize = 12, color = 'k')
setp(ltext[1], fontsize = 12, color = 'r')
setp(ltext[2], fontsize = 12, color = 'y')

grid()
show()

plot(energy,Sn_absorption,'k-')
plot(energy,Bi_absorption,'r-')
plot(energy,Au_absorption,'y-')

xlim(1,100)
ylim(0.0,1.1)
xlabel('Energy (keV)', fontsize = 18)
ylabel('Absorption', fontsize = 18)
title('Absorbers: X-ray Absorption (%d microns)' % (thickness), fontsize = 20)
legend((r'Sn (%d microns)'%thickness, r'Bi (%d microns)'%thickness, r'Au  (%d microns)'%thickness), shadow = True, loc = 0,numpoints = 2)
ltext = gca().get_legend().get_texts()
setp(ltext[0], fontsize = 12, color = 'k')
setp(ltext[1], fontsize = 12, color = 'r')
setp(ltext[2], fontsize = 12, color = 'y')
grid()
show()


Ge_Z = 32
Ge_atomic_wt =  72.5899963
Ge_density =  5.32299995

energy = linspace(1,100,10000)

Ge_attenuation_len = []

Ge_absorption = []

thickness_Ge = 3000.

for e in energy:
	Ge_attenuation_len.append( 10000*(Ge_density*CS_Total(Ge_Z,e))**-1  )# microns

	Ge_absorption.append(1.0 - exp(-1*thickness_Ge/(10000*(Ge_density*CS_Total(Ge_Z,e))**-1)))


plot(energy,Sn_absorption,'k-')
plot(energy,Bi_absorption,'r-')
plot(energy,Ge_absorption,'g-')
plot(energy,Au_absorption,'y-')

xlim(1,100)
ylim(0.0,1.1)
xlabel('Energy (keV)', fontsize = 18)
ylabel('Absorption', fontsize = 18)
title('Absorbers: X-ray Absorption', fontsize = 20)
legend((r'Sn (%d microns)'%thickness, r'Bi (%d microns)'%thickness, r'Germanium (3 mm)', r'Au  (%d microns)'%thickness), shadow = True, loc = 0,numpoints = 2)
ltext = gca().get_legend().get_texts()
setp(ltext[0], fontsize = 12, color = 'k')
setp(ltext[1], fontsize = 12, color = 'r')
setp(ltext[2], fontsize = 12, color = 'g')
setp(ltext[3], fontsize = 12, color = 'y')

grid()
show()



