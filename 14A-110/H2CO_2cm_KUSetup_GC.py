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
backend   = 'Spectrometer'
nwin      = 4                         # four spectral windows
restfreq  = 14488.479,12178.597,13778.804,13165.96 # H2CO, CH3OH, H213CO, H2C18O; max separation 2310 MHz
deltafreq = 0,0,0,0                   # DO NOT MENTION IF3FREQ IN SETUP!
bandwidth = 50.0                      # MHz Moderate-resolution mode (0.25 km/s)
swmode    = "tp"                      # set switching scheme (tp(total power with cal), tp_nocal, sp(switched power with cal), sp_nocal )
swtype    = "none"                    # for frequency switching; not used for tp mode
swper     = 1.0                       # one second cycle for switching
swfreq    = 0.0, 0.0                  # for freq switching
tint      = 2.0                       # integration time (for 4 quadrants, 1.2-40 sec.  Important to avoid smearing)
vlow      = 0
vhigh     = 0
vframe    = "lsrk"                    # LSR - kinematic is the "normal" definition (don't use dynamic)
vdef      = "Radio"                   # radio (optical is also acceptable, but not the norm for Galactic observations)
noisecal  = "lo"
pol       = "Circular"
nchan     = "high"                     # 4096 channels over 2 beams and 4 windows
        # spectrometer guide says 12.5 MHz = 237 km/s bandwidth = 8192 channels,
        # 50 MHz = 1035 km/s BW
        # 4096 channels, 12.2 KHz = 0.253 km/s
        # numsamplers=8, nwin=4, chanwidth = 1.526 KHz -> resolution = .06 km/s (2 channels)... nchan = high
spect.levels = 9                      # nine level sampling
#iftarget = 0.25                       # IF target is now always 1
