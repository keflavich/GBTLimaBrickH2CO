"""
Create a 3-degree-long vertical scan across the Galactic Center, focused on The
Brick.  The intent is to examine continuum calibration, while also acquiring an
unbiased sample of the H2CO absorption depth across the inner Plane.

The scan is programmed to go for 22.5 minutes, which means including setup it will
probably take ~30 minutes.
"""

Break("Make sure you run ConfigureFocusKu.py before beginning this observation")

cat = Catalog("/users/aginsbur/GBT12B-221/limabean.astrid")
Configure("/users/aginsbur/GBT12B-221/H2CO_2cm_KUSetup_GC.py")


Slew("LimaBean")
Balance()

amintodeg = 1/60.
scanrate = 8. # arcmin/min

# vertical scans
DecLatMap('LimaBean',     #center of map
    hLength = Offset("Galactic",0.5*amintodeg,0.0,cosv=True), 
    vLength = Offset("Galactic",0.0,180*amintodeg,cosv=True), 
    hDelta  = Offset("Galactic",(1.)*amintodeg,0.0,cosv=True), 
    scanDuration = 180/scanrate * 60,
    beamName="1")


