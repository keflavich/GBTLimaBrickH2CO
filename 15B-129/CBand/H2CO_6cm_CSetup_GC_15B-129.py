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
dopplertrackfreq = 4829.66
swmode    = "tp"                      # set switching scheme
swtype    = "none"                    # for frequency switching
swper     = 1.0                       # one second cycle for switching
swfreq    = 0.0, 0.0                  # for freq switching
tint      = 1.0                       # integration time (5s -> 0.1 beams)
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
#{"nchan":"low", "restfreq": 4054.89 , 'bandwidth': 23.44, "res":0.0057, "deltafreq": 0}, # h117a
{"nchan":"low", "restfreq": 4745.365, 'bandwidth': 23.44, "res":0.0057, "deltafreq": 0},
{"nchan":"low", "restfreq": 6480.375, 'bandwidth': 23.44, "res":0.0057, "deltafreq": 0},
{"nchan":"low", "restfreq": 4160.21 , 'bandwidth': 23.44, "res":0.0057, "deltafreq": 0}, # h116a
{"nchan":"low", "restfreq": 4829.66 , 'bandwidth': 23.44, "res":0.0057, "deltafreq": 0}, # h2co: ifnum0
{"nchan":"low", "restfreq": 6668.47 , 'bandwidth': 23.44, "res":0.0057, "deltafreq": 0}, # ch3ohmaser: ifnum17
{"nchan":"low", "restfreq": 4269.205, 'bandwidth': 23.44, "res":0.0057, "deltafreq": 0},
{"nchan":"low", "restfreq": 4875.375, 'bandwidth': 23.44, "res":0.0057, "deltafreq": 0},
{"nchan":"low", "restfreq": 6677.74 , 'bandwidth': 23.44, "res":0.0057, "deltafreq": 0},
{"nchan":"low", "restfreq": 4382.045, 'bandwidth': 23.44, "res":0.0057, "deltafreq": 0},
{"nchan":"low", "restfreq": 5005.32 , 'bandwidth': 23.44, "res":0.0057, "deltafreq": 0}, # ch3oh ifnum12
#{"nchan":"low", "restfreq": 6883.205, 'bandwidth': 23.44, "res":0.0057, "deltafreq": 0},
{"nchan":"low", "restfreq": 4388.8  , 'bandwidth': 23.44, "res":0.0057, "deltafreq": 0}, # h2c18o ifnum3
{"nchan":"low", "restfreq": 5346.14 , 'bandwidth': 23.44, "res":0.0057, "deltafreq": 0}, # hdco ifnum14
#{"nchan":"low", "restfreq": 7097.18 , 'bandwidth': 23.44, "res":0.0057, "deltafreq": 0},
{"nchan":"low", "restfreq": 4498.9  , 'bandwidth': 23.44, "res":0.0057, "deltafreq": 0},
#{"nchan":"low", "restfreq": 6096.07 , 'bandwidth': 23.44, "res":0.0057, "deltafreq": 0},
#{"nchan":"low", "restfreq": 7320.12 , 'bandwidth': 23.44, "res":0.0057, "deltafreq": 0},
{"nchan":"low", "restfreq": 4593.09 , 'bandwidth': 23.44, "res":0.0057, "deltafreq": 0}, # h213co ifnum5
{"nchan":"low", "restfreq": 4800.0  , 'bandwidth': 23.44, "res":0.0057, "deltafreq": 0},
{"nchan":"low", "restfreq": 4850.0  , 'bandwidth': 23.44, "res":0.0057, "deltafreq": 0},
#{"nchan":"low", "restfreq": 7552.495, 'bandwidth': 23.44, "res":0.0057, "deltafreq": 0},
{"nchan":"low", "restfreq": 4619.94 , 'bandwidth': 23.44, "res":0.0057, "deltafreq": 0},
#{"nchan":"low", "restfreq": 7794.815, 'bandwidth': 23.44, "res":0.0057, "deltafreq": 0},
#{"nchan":"high", "restfreq": 4400.0 , 'bandwidth': 1080, "res":0.066, "deltafreq": 0},
{"nchan":"high", "restfreq": 5200.0 , 'bandwidth': 1500, "res":0.092, "deltafreq": 0},
{"nchan":"high", "restfreq": 6000.0 , 'bandwidth': 1500, "res":0.092, "deltafreq": 0},
{"nchan":"high", "restfreq": 6800.0 , 'bandwidth': 1500, "res":0.092, "deltafreq": 0},
#{"nchan":"high", "restfreq": 7600.0 , 'bandwidth': 1080, "res":0.066, "deltafreq": 0},
]
