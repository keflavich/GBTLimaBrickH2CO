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
dopplertrackfreq = 14488.479
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
nchan     = "low" # 'low' uses mode 20, with 0.11 km/s channels
#iftarget = 0.25                       # IF target is now always 1
vegas.vpol='self'
restfreq  = [ 
{"nchan":"low", "restfreq": 14488.479, 'bandwidth': 23.44, "res":0.0057, "deltafreq": 0}, #1 H2CO
{"nchan":"low", "restfreq": 14511.0  , 'bandwidth': 23.44, "res":0.0057, "deltafreq": 0}, #2 H2CO
{"nchan":"low", "restfreq": 14465.0  , 'bandwidth': 23.44, "res":0.0057, "deltafreq": 0}, #3 H2CO
{"nchan":"low", "restfreq": 13788.0 ,  'bandwidth': 23.44, "res":0.0057, "deltafreq": 0}, #4 H213CO
{"nchan":"low", "restfreq": 13767.0 ,  'bandwidth': 23.44, "res":0.0057, "deltafreq": 0}, #5 H213CO
{"nchan":"low", "restfreq": 14130.00 , 'bandwidth': 23.44, "res":0.0057, "deltafreq": 0}, #6 H77a
{"nchan":"low", "restfreq": 13595.49 , 'bandwidth': 23.44, "res":0.0057, "deltafreq": 0}, #7 H78a
{"nchan":"low", "restfreq": 14689.99 , 'bandwidth': 23.44, "res":0.0057, "deltafreq": 0}, #8 H76a
# spw 2
{"nchan":"low", "restfreq": 13165.96 , 'bandwidth': 23.44, "res":0.0057, "deltafreq": 0}, #1 H2C18O
{"nchan":"low", "restfreq": 12511.0  , 'bandwidth': 23.44, "res":0.0057, "deltafreq": 0}, #2 CH3OH
{"nchan":"low", "restfreq": 12148.66 , 'bandwidth': 23.44, "res":0.0057, "deltafreq": 0}, #3 H81a
{"nchan":"low", "restfreq": 12168.56 , 'bandwidth': 23.44, "res":0.0057, "deltafreq": 0}, #4 CH3OH lo
#{"nchan":"low", "restfreq": 12.17856 , 'bandwidth': 23.44, "res":5.7, "deltafreq": 0}, # center of CH3OH
{"nchan":"low", "restfreq": 12188.56 , 'bandwidth': 23.44, "res":0.0057, "deltafreq": 0}, #5 CH3OH hi
{"nchan":"low", "restfreq": 12607.08 , 'bandwidth': 23.44, "res":0.0057, "deltafreq": 0}, #6 H80a
{"nchan":"low", "restfreq": 13088.85 , 'bandwidth': 23.44, "res":0.0057, "deltafreq": 0}, #7 H79a
{"nchan":"low", "restfreq": 13043.81 , 'bandwidth': 23.44, "res":0.0057, "deltafreq": 0}, #8 SO
# spw 3
{"nchan":"high", "restfreq": 14500.0 , 'bandwidth': 1500, "res":0.092, "deltafreq": 0},
# spw 4
{"nchan":"high", "restfreq": 13000.0 , 'bandwidth': 1500, "res":0.092, "deltafreq": 0},
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
