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


Ge_Z = 32
Ge_atomic_wt =  72.5899963
Ge_density =  5.32299995
Ge_attenuation_len = []
Ge_absorption = []
thickness_Ge = 3000.

Cd_Z = 48
Cd_atomic_wt =  112.410004
Cd_density =  8.64999962
Te_Z = 52
Te_atomic_wt =  127.599998
Te_density =  6.23999977
CdTe_density = 5.85
Cd_fraction = (Cd_atomic_wt) / (Cd_atomic_wt + Te_atomic_wt)
Te_fraction = (Te_atomic_wt) / (Cd_atomic_wt + Te_atomic_wt)
print Cd_fraction, Te_fraction
CdTe_attenuation_len = []
CdTe_absorption = []
thickness_CdTe = 650.

Ga_Z = 31
Ga_atomic_wt =  69.7200012
Ga_density =  5.90299988
As_Z = 33
As_atomic_wt =  74.9199982
As_density =  5.73000002
GaAs_density = 5.32
Ga_fraction = (Ga_atomic_wt) / (Ga_atomic_wt + As_atomic_wt)
As_fraction = (As_atomic_wt) / (Ga_atomic_wt + As_atomic_wt)
GaAs_attenuation_len = []
GaAs_absorption = []
thickness_GaAs = 650.


energy = linspace(1,100,10000)
for e in energy:
	Ge_attenuation_len.append( 10000*(Ge_density*CS_Total(Ge_Z,e))**-1  )# microns
	Ge_absorption.append(1.0 - exp(-1*thickness_Ge/(10000*(Ge_density*CS_Total(Ge_Z,e))**-1)))
	cs_total_CdTe = Cd_fraction*CS_Total(Cd_Z,e) + Te_fraction*CS_Total(Te_Z,e)
	CdTe_attenuation_len.append( 10000*(CdTe_density*cs_total_CdTe)**-1  )# microns
	CdTe_absorption.append(1.0 - exp(-1*thickness_CdTe/(10000*(CdTe_density*cs_total_CdTe)**-1)))
	cs_total_GaAs = Ga_fraction*CS_Total(Ga_Z,e) + As_fraction*CS_Total(As_Z,e)
	GaAs_attenuation_len.append( 10000*(GaAs_density*cs_total_GaAs)**-1  )# microns
	GaAs_absorption.append(1.0 - exp(-1*thickness_GaAs/(10000*(GaAs_density*cs_total_GaAs)**-1)))




# semilogy(energy,Ge_attenuation_len,'k-')
# xlabel('Energy (keV)', fontsize = 18)
# ylabel('Attenuation length (microns)', fontsize = 18)
# title('Absorbers: X-ray Attenuation Lengths', fontsize = 20)
# legend((r'Ge'), shadow = True, loc = 0,numpoints = 2)
# ltext = gca().get_legend().get_texts()
# setp(ltext[0], fontsize = 12, color = 'k')
# grid()
# show()

plot(energy,Ge_absorption,'k-')
plot(energy,CdTe_absorption,'r-')
plot(energy,GaAs_absorption,'g-')

xlim(1,100)
ylim(0.0,1.1)
xlabel('Energy (keV)', fontsize = 18)
ylabel('Absorption', fontsize = 18)
title('Absorbers: X-ray Absorption', fontsize = 20)
legend((r'Germanium (%d microns)' % (thickness_Ge), r'CdTe (%d microns)' % (thickness_CdTe) , r'GaAs (%d microns)' % (thickness_GaAs)  ), shadow = True, loc = 0,numpoints = 2)
ltext = gca().get_legend().get_texts()
setp(ltext[0], fontsize = 12, color = 'k')
setp(ltext[1], fontsize = 12, color = 'r')
setp(ltext[2], fontsize = 12, color = 'g')
grid()
show()



