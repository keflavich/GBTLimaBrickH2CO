# Ku-band H2CO 2 cm (and friends)
# keywords defined at www.gb.nrao.edu/~fghigo/gbtdoc/config/configparams_rev1.doc
#
# CONFIGURATION:
# Bandwidth Polarization Level Number of Number of Lags - Approximate Resolution
#   (MHz) Cross-Products Sampling Spectral Beams Low Medium High
# BW Pol Lev  Windows Beams Channels / resolution
# 50 No  9    4       2     4096 - 12.2070 kHz 4096 - 12.2070 kHz 4096 - 12.2070 kHz

receiver  = 'Rcvr4_6'                 # select C-band receiver
beam      = 'B1'                      # use two beams
obstype   = 'Spectroscopy'
backend   = 'VEGAS'
dopplertrackfreq = 4.82966
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
{"nchan":"low", "restfreq": 4.05489 , 'bandwidth': 23.44, "res":0.0057, "deltafreq": 0},
{"nchan":"low", "restfreq": 4.745365, 'bandwidth': 23.44, "res":0.0057, "deltafreq": 0},
{"nchan":"low", "restfreq": 6.480375, 'bandwidth': 23.44, "res":0.0057, "deltafreq": 0},
{"nchan":"low", "restfreq": 4.16021 , 'bandwidth': 23.44, "res":0.0057, "deltafreq": 0},
{"nchan":"low", "restfreq": 4.82966 , 'bandwidth': 23.44, "res":0.0057, "deltafreq": 0},
{"nchan":"low", "restfreq": 6.66847 , 'bandwidth': 23.44, "res":0.0057, "deltafreq": 0},
{"nchan":"low", "restfreq": 4.269205, 'bandwidth': 23.44, "res":0.0057, "deltafreq": 0},
{"nchan":"low", "restfreq": 4.875375, 'bandwidth': 23.44, "res":0.0057, "deltafreq": 0},
{"nchan":"low", "restfreq": 6.67774 , 'bandwidth': 23.44, "res":0.0057, "deltafreq": 0},
{"nchan":"low", "restfreq": 4.382045, 'bandwidth': 23.44, "res":0.0057, "deltafreq": 0},
{"nchan":"low", "restfreq": 5.00532 , 'bandwidth': 23.44, "res":0.0057, "deltafreq": 0},
{"nchan":"low", "restfreq": 6.883205, 'bandwidth': 23.44, "res":0.0057, "deltafreq": 0},
{"nchan":"low", "restfreq": 4.3888  , 'bandwidth': 23.44, "res":0.0057, "deltafreq": 0},
{"nchan":"low", "restfreq": 5.34614 , 'bandwidth': 23.44, "res":0.0057, "deltafreq": 0},
{"nchan":"low", "restfreq": 7.09718 , 'bandwidth': 23.44, "res":0.0057, "deltafreq": 0},
{"nchan":"low", "restfreq": 4.4989  , 'bandwidth': 23.44, "res":0.0057, "deltafreq": 0},
{"nchan":"low", "restfreq": 6.09607 , 'bandwidth': 23.44, "res":0.0057, "deltafreq": 0},
{"nchan":"low", "restfreq": 7.32012 , 'bandwidth': 23.44, "res":0.0057, "deltafreq": 0},
{"nchan":"low", "restfreq": 4.59309 , 'bandwidth': 23.44, "res":0.0057, "deltafreq": 0},
{"nchan":"low", "restfreq": 4.80    , 'bandwidth': 23.44, "res":0.0057, "deltafreq": 0},
{"nchan":"low", "restfreq": 4.85    , 'bandwidth': 23.44, "res":0.0057, "deltafreq": 0},
{"nchan":"low", "restfreq": 7.552495, 'bandwidth': 23.44, "res":0.0057, "deltafreq": 0},
{"nchan":"low", "restfreq": 4.61994 , 'bandwidth': 23.44, "res":0.0057, "deltafreq": 0},
{"nchan":"low", "restfreq": 7.794815, 'bandwidth': 23.44, "res":0.0057, "deltafreq": 0},
{"nchan":"high", "restfreq": 4400.0 , 'bandwidth': 1080, "res":0.092, "deltafreq": 0},
{"nchan":"high", "restfreq": 5200.0 , 'bandwidth': 1080, "res":0.092, "deltafreq": 0},
{"nchan":"high", "restfreq": 6000.0 , 'bandwidth': 1080, "res":0.092, "deltafreq": 0},
{"nchan":"high", "restfreq": 6800.0 , 'bandwidth': 1080, "res":0.092, "deltafreq": 0},
{"nchan":"high", "restfreq": 7600.0 , 'bandwidth': 1080, "res":0.092, "deltafreq": 0},
]
