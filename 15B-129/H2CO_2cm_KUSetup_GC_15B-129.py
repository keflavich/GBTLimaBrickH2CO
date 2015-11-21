# Ku-band H2CO 2 cm (and friends)
# keywords defined at www.gb.nrao.edu/~fghigo/gbtdoc/config/configparams_rev1.doc
#
# CONFIGURATION:
# Bandwidth Polarization Level Number of Number of Lags - Approximate Resolution
#   (MHz) Cross-Products Sampling Spectral Beams Low Medium High
# BW Pol Lev  Windows Beams Channels / resolution
# 50 No  9    4       2     4096 - 12.2070 kHz 4096 - 12.2070 kHz 4096 - 12.2070 kHz

receiver  = 'Rcvr12_18'               # select Ku-band receiver
beam      = 'B12'                     # use two beams
obstype   = 'Spectroscopy'
backend   = 'VEGAS'
dopplertrackfreq = 14.488479
swmode    = "tp"                      # set switching scheme
swtype    = "none"                    # for frequency switching
swper     = 1.0                       # one second cycle for switching
swfreq    = 0.0, 0.0                  # for freq switching
tint      = 0.5                       # integration time (5s -> 0.1 beams)
vlow      = 0
vhigh     = 0
vframe    = "lsrk"                    # LSR - kinematic is the "normal" definition (don't use dynamic)
vdef      = "Radio"                   # radio (optical is also acceptable, but not the norm for Galactic observations)
noisecal  = "lo"
pol       = "Circular"
nchan     = "high"
#iftarget = 0.25                       # IF target is now always 1
vegas.vpol='self'
restfreq  = [ 
{"restfreq": 14.488479, 'bandwidth': 23.44, "res":5.7, "deltafreq": 0},
{"restfreq": 14.511   , 'bandwidth': 23.44, "res":5.7, "deltafreq": 0},
{"restfreq": 14.465   , 'bandwidth': 23.44, "res":5.7, "deltafreq": 0},
{"restfreq": 13.7880 ,  'bandwidth': 23.44, "res":5.7, "deltafreq": 0},
{"restfreq": 13.7670 ,  'bandwidth': 23.44, "res":5.7, "deltafreq": 0},
{"restfreq": 14.13000 , 'bandwidth': 23.44, "res":5.7, "deltafreq": 0},
{"restfreq": 12.17856 , 'bandwidth': 23.44, "res":5.7, "deltafreq": 0},
{"restfreq": 13.16596 , 'bandwidth': 23.44, "res":5.7, "deltafreq": 0},
]

#Configure(myconfig)
#Balance()
#
#"""
#{"restfreq": 14.488479, 'bandwidth': 23.44, "res":5.7, "deltafreq": 0}, #H2CO, very wide
#{"restfreq": 14.511   , 'bandwidth': 23.44, "res":5.7, "deltafreq": 0}, #H2CO, very wide
#{"restfreq": 14.465   , 'bandwidth': 23.44, "res":5.7, "deltafreq": 0}, #H2CO, very wide
#{"restfreq": 13.7880 ,  'bandwidth': 23.44, "res":5.7, "deltafreq": 0}, # overlap with 13.7788 H213CO
#{"restfreq": 13.7670 ,  'bandwidth': 23.44, "res":5.7, "deltafreq": 0}, # overlap with 13.7788
#{"restfreq": 14.13000 , 'bandwidth': 23.44, "res":5.7, "deltafreq": 0}, # H77a 14.12861 He77a 14.13437
#{"restfreq": 12.17856 , 'bandwidth': 23.44, "res":5.7, "deltafreq": 0}, # CH3OH 12.17856
#{"restfreq": 13.16596 , 'bandwidth': 23.44, "res":5.7, "delatfreq": 0}, # 13.16596 = H2C18O
#"""
#
## these are not permitted with the current 1/2 functional VEGAS
##{"restfreq": 14.10561 , 'bandwidth': 23.44, "res":5.7, "deltafreq": 0},
##{"restfreq": 12.16856 , 'bandwidth': 23.44, "res":5.7, "deltafreq": 0},
##{"restfreq": 12.18856 , 'bandwidth': 23.44, "res":5.7, "deltafreq": 0},
##{"restfreq": 12.511   , 'bandwidth': 23.44, "res":5.7, "deltafreq": 0},
##{"restfreq": 12.625   , 'bandwidth': 23.44, "res":5.7, "deltafreq": 0}, # wideband?
##{"restfreq": 13.875   , 'bandwidth': 23.44, "res":5.7, "deltafreq": 0}, # wideband?
##{"restfreq": 14.775   , 'bandwidth': 23.44, "res":5.7, "deltafreq": 0}, # wideband?
