# Ku-band H2CO 2 cm (and friends)
# keywords defined at www.gb.nrao.edu/~fghigo/gbtdoc/config/configparams_rev1.doc
#
# CONFIGURATION:
# Bandwidth Polarization Level Number of Number of Lags - Approximate Resolution
#   (MHz) Cross-Products Sampling Spectral Beams Low Medium High
# BW Pol Lev  Windows Beams Channels / resolution
# 50 No  9    4       2     4096 - 12.2070 kHz 4096 - 12.2070 kHz 4096 - 12.2070 kHz

receiver  = 'Rcvr4_6'               # select C-band receiver
beam      = 'B1'                     # use one beam
obstype   = 'Spectroscopy'
backend   = 'Spectrometer'
nwin      = 8                         # four spectral windows
# Maximum instantaneous IF bandwidth is 3500 MHz
# these frequencies were used for the pilot restfreq  = 14488.479,14131.5,14693.0,15284.6  # the line freqs (add more lines!)
# frequencies used in "obs_session1_innergalaxy": restfreq  = 14488.479,13778.804,13165.96,14693.0  # the line freqs H2CO, H2_13CO, H2_C18O, and H76a
# used for SESSION 2, outergal, August 15 2010: restfreq  = 14488.479,13026.06,13595.49,14825.79  # the line freqs H2CO, NaCl, H78a, and H2CN
# used for 2 scans in SESSION 3 restfreq  = 14488.479,13026.06,14128.61,14825.79  # the line freqs H2CO, NaCl, H77a, and H2CN
# used for most of session 3, 4 restfreq  = 14488.479,13036.06,14128.61,14825.79  # the line freqs H2CO, NaCl + SO, H77a, and H2CN
# We will also use the GBT C-band receiver with the GBT spectrometer. We will
# use 8 spectral windows with 50 MHz (3000 km s􀀀1) bandwidth, 12.2070 kHz
# channel width (0.75 km s􀀀1), no polarization cross- products, and 9-level
# sampling. Our windows will target the following lines (frequencies are
# specied in GHz): 4.8296594 (H2CO 110􀀀111), 4.593089 (H2 13CO 110􀀀111), 5.50
# (H106 and OH), 5.20 (H107 and { 3 { CH2NH), 5.008922 (H109), 4.63
# (H112 and OH), 4.874157 (H110), and 4.497776 (H113 and HCN)
# # 
restfreq  = 4829.6594, 4593.089, 5500.0, 5200.0, 5008.992, 4630.0, 4874.157, 4497.776
deltafreq = 0,0,0,0,0,0,0,0           # DO NOT MENTION IF3FREQ IN SETUP!
bandwidth = 50.0                      # MHz Moderate-resolution mode (0.75 km/s) -> 12 kHz channels
swmode    = "tp"                      # set switching scheme
swtype    = "none"                    # for frequency switching
swper     = 1.0                       # one second cycle for switching
swfreq    = 0.0, 0.0                  # for freq switching
tint      = 5                         # integration time (5s -> 0.1 beams)
vlow      = 0
vhigh     = 0
vframe    = "lsrk"                    # LSR - kinematic is the "normal" definition (don't use dynamic)
vdef      = "Radio"                   # radio (optical is also acceptable, but not the norm for Galactic observations)
noisecal  = "lo"
pol       = "Circular"
nchan     = "high"
spect.levels = 9                      # nine level sampling
#iftarget = 0.25                       # IF target is now always 1

