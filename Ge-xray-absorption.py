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

semilogy(energy,Ge_attenuation_len,'k-')

xlabel('Energy (keV)', fontsize = 18)
ylabel('Attenuation length (microns)', fontsize = 18)
title('Absorbers: X-ray Attenuation Lengths', fontsize = 20)
legend((r'Ge'), shadow = True, loc = 0,numpoints = 2)
ltext = gca().get_legend().get_texts()
setp(ltext[0], fontsize = 12, color = 'k')
grid()
show()

plot(energy,Ge_absorption,'k-')
xlim(1,100)
ylim(0.0,1.1)
xlabel('Energy (keV)', fontsize = 18)
ylabel('Absorption', fontsize = 18)
title('Absorbers: X-ray Absorption (%d microns)' % (thickness_Ge), fontsize = 20)
legend((r'Germanium'), shadow = True, loc = 0,numpoints = 2)
ltext = gca().get_legend().get_texts()
setp(ltext[0], fontsize = 12, color = 'k')
grid()
show()



