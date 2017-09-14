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

# print DCSP_Rayl(35, 13.3,90.0*DEGREES2RADIANS,45.0*DEGREES2RADIANS)


Se_Z = 34
Se_atomic_wt =  78.9599991
Se_density =  4.78999996

energy = linspace(1,100,20000)

Se_attenuation_len_50um = []
Se_absorption_50um = []


Se_attenuation_len_100um = []
Se_absorption_100um = []



## 3 mm thick Germanium
thickness_Se_100um = 100. # In microns

for e in energy:
	
	Se_attenuation_len_100um.append( 10000*(Se_density*CS_Total(Se_Z,e))**-1  )# microns
	Se_absorption_100um.append(1.0 - exp(-1*thickness_Se_100um/(10000*(Se_density*CS_Total(Se_Z,e))**-1)))
	
	
print thickness_Se_100um


figure()
plot(energy,Se_absorption_100um,'r-',linewidth=3)
xlim(0,100)
ylim(0.0,1.1)
xlabel('Energy (keV)', fontsize = 18)
ylabel('Absorption', fontsize = 18)
title('Selenium X-ray Absorption 100 microns', fontsize = 20)
#legend((r'%d um' % (thickness_Se_100um)), shadow = True, loc = 0,numpoints = 2)
#ltext = gca().get_legend().get_texts()
#setp(ltext[0], fontsize = 16, color = 'k')
grid()
show()

