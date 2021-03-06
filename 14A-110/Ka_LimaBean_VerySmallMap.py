"""
Create a 8x8' map of the Lima Bean at Ka band

*This observation will take 42 minutes on-source, *PLUS* overheads, so about 1 hour*

Per Glen Langston's recommendations, I should:
    1. not use refs for each scan (because the pipeline doesn't use them)
    2. use "Track" to observe offs
    3. do pointing scans as normal; break up map into 2 sub-maps

Following pipeline recommendations:
https://safe.nrao.edu/wiki/bin/view/Kbandfpa/ObserverGuide?sortcol=table;up=#Reduction_Execute_Pipeline_with
"""

#Break("Make sure you run ConfigureFocusKa.py before beginning this observation")

cat = Catalog("/users/aginsbur/GBT12B-221/limabean.astrid")
Configure("/users/aginsbur/GBT12B-221/H2CO_1cm_KaSetup_GC.py")


Slew("LimaBean3")
Balance()
Slew("LimaBeanOff")
Track("LimaBeanOff",None,60)


amintodeg = 1/60.
arcsectodeg = 1/3600.
# samplerate = 30/minute = 0.5/s
# beam ~ 27"
# 3 samples/beam
# 8 seconds / arcminute
scanheight = 6.4 # arcmin
scanwidth = 4.0 # arcmin
hdelta = 10.0 * arcsectodeg
vdelta = 10.0 * arcsectodeg

# 22 vertical scans -> 30 minutes
scanrate = 5.0 # arcmin/min
DecLatMap('LimaBean3',     #center of map
    hLength = Offset("J2000",scanwidth*amintodeg,0.0,cosv=True),
    vLength = Offset("J2000",0.0,scanheight*amintodeg,cosv=True),
    hDelta  = Offset("J2000",hdelta,0.0,cosv=True),
    scanDuration = scanheight/scanrate * 60,
    beamName="1")

Slew("LimaBeanOff")
Track("LimaBeanOff",None,60)

# 39 horizontal scans -> ~50 minutes
scanrate = 3.0 # arcmin/min
RALongMap('LimaBean3',     #center of map
    hLength = Offset("J2000",scanwidth*amintodeg,0.0,cosv=True),
    vLength = Offset("J2000",0.0,scanheight*amintodeg,cosv=True),
    vDelta  = Offset("J2000",0.0,vdelta,cosv=True),
    scanDuration = scanwidth/scanrate * 60,
    beamName="1")

Slew("LimaBeanOff")
Track("LimaBeanOff",None,60)
