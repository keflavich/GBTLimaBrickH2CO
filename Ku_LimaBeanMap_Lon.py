"""
Create a 12x15' map of the Lima Bean 

*This observation will take 1.13 hours on-source, *PLUS* overheads, so about 1.5 hours*

Per Glen Langston's recommendations, I should:
    1. not use refs for each scan (because the pipeline doesn't use them)
    2. use "Track" to observe offs
    3. do pointing scans as normal; break up map into 2 sub-maps

Following pipeline recommendations:
https://safe.nrao.edu/wiki/bin/view/Kbandfpa/ObserverGuide?sortcol=table;up=#Reduction_Execute_Pipeline_with
"""

Break("Make sure you run ConfigureFocusKu.py before beginning this observation")

cat = Catalog("/users/aginsbur/GBT12B-221/limabean.astrid")
Configure("/users/aginsbur/GBT12B-221/H2CO_2cm_KuSetup_GC.py")


Slew("LimaBean")
Balance()

amintodeg = 1/60.
scanrate = 8. # arcmin/min = arcsec/sec

# horizontal scans
RALongMap('LimaBean',     #center of map
    hLength = Offset("Galactic",15*amintodeg,0.0,cosv=True), 
    vLength = Offset("Galactic",0.0,12*amintodeg,cosv=True), 
    vDelta  = Offset("Galactic",0.0,(1./3.)*amintodeg,cosv=True),  # 20" = 1/3 of an arcminute
    scanDuration = 15/scanrate * 60,
    beamName="1")


