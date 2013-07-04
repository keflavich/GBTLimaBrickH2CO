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
restfreq  = 14488.479,12178.597,13778.804,13165.96 # H2CO, CH3OH, H213CO, H2C18O
                                                    # max separation 2310 MHz
deltafreq = 0,0,0,0                   # DO NOT MENTION IF3FREQ IN SETUP!
#bandwidth = 12.5                      # MHz High-resolution mode (0.063 km/s)
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


#############################
# LINE LISTS AND OTHER INFO #
#############################
#** Maximum instantaneous IF bandwidth is 3500 MHz
# Lines from Splatalogue:
# H2CO   2-2    : 14.488479 GHz
# HDCO   2-2    : 16.0378737 GHz  # +/-25 MHz contains H, He 116 delta
# H213CO 2-2    : 13.778804 GHz   # +/-25 MHz contains C6H 5-4, H139 gamma
# H2C18O 2-2    : 13.16596 GHz    # +/-25 MHz contains H,He,C 113 delta, H,He,C 99 beta
# NaCl   1-0    : 13.02606 GHz    # SO 3sig v=0  1(2)-1(1) is nearby ( 13.04370 )
# KCl    2-1    : 15.37807 GHz    # H134 gamma,
# OCS    1-0    : 12.16298 GHz    # H81alpha=12.14866, H116delta=12.16516   --- in order to get H81alpha in-band with the C RRL, choose 12.1425 GHz
# H2CN   2(11)-2(12) F=7/2-7/2 (n=1-1) : 14.82579 GHz  # Acetic Acid (CH3COOH) 1(01)-0(00) at  	14.80400, another H2CN at 14.80914
# OH and SO2    : 13.450 GHz.  OH v=0 J=7/2 om=3/2 F=[34+-]-[34+-] 13.43393, 13.44142, SO2 v2=1 1(1,1)-2(0,2) 13.45735
# Hα,Heα,Cα 79  : 13.08885 
# Hα,Heα,Cα 78  : 13.59549 13.60103 13.60227
# Hα,Heα,Cα 77  : 14.12861 14.13437 14.13567 & 14.14304 H121d, 14.14491 H130e, 14.14881 He121d, Cyclopropenone 101-000 14.10572 , Acetic Acid 211-110 14.13643 
# Hα,Heα,Cα 76  : 14.68999 14.69597 14.69731
# Hα,Heα,Cα 75  : 15.28149 & KCl 2-1 15.28375
# Hα,Heα,Cα 74  : 15.90519 & Methyl Formate 110-101 15.91121 
# Hα,Heα,Cα 73  : 16.56329 16.57004 16.57156 -> 16.567425
# CH3OH maser 2_0-3_{-1} E   12.178597
# Resonances are at:
# Ku 12875.0 8.1
# Ku 12885.0 7.1
# BAD FREQUENCIES below 12.35 GHz - DO NOT observer
#
# these frequencies were used for the pilot restfreq  = 14488.479,14131.5,14693.0,15284.6  # the line freqs (add more lines!)
# frequencies used in "obs_session1_innergalaxy": restfreq  = 14488.479,13778.804,13165.96,14693.0  # the line freqs H2CO, H2_13CO, H2_C18O, and H76a
# used for SESSION 2, outergal, August 15 2010: restfreq  = 14488.479,13026.06,13595.49,14825.79  # the line freqs H2CO, NaCl, H78a, and H2CN
# used for 2 scans in SESSION 3 restfreq  = 14488.479,13026.06,14128.61,14825.79  # the line freqs H2CO, NaCl, H77a, and H2CN
# used for most of session 3, 4 restfreq  = 14488.479,13036.06,14128.61,14825.79  # the line freqs H2CO, NaCl + SO, H77a, and H2CN
