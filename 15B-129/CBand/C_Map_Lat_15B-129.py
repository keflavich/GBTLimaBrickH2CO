"""

Following pipeline recommendations:
https://safe.nrao.edu/wiki/bin/view/Kbandfpa/ObserverGuide?sortcol=table;up=#Reduction_Execute_Pipeline_with
"""

#Break("Make sure you run ConfigureFocusKu.py before beginning this observation")

cat = Catalog("/users/aginsbur/GBT15B-129/gc_15B-129.astrid")
Configure("/users/aginsbur/GBT15B-129/H2CO_6cm_CSetup_GC_15B-129.py")

Slew("CMZ_East")
Balance()

amintodeg = 1/60.
# Target scan rate is 5 samples/beam
# 1 sample = 0.5s
# 1 beam = 2.5'
# 5 samples/beam = 5'/s = 300'/m
scanrate = 300. # arcmin/min
# we want our scan duration to actually be 1m though...
mintosec = 60.

# vertical scans
height = 12.
width = 30.
# 60 scans of 60s each + 10x reference positions = 70m, probably 90m w/overhead
DecLatMapWithReference(location='CMZ_East',     #center of map
                       hLength = Offset("Galactic",width*amintodeg,0.0,cosv=True), 
                       vLength = Offset("Galactic",0.0,height*amintodeg,cosv=True), 
                       hDelta  = Offset("Galactic",(0.5)*amintodeg,0.0,cosv=True), 
                       scanDuration = 60,
                       beamName="1",
                       # 1 degree vertical offset
                       referenceOffset=Offset("Galactic", 0.0, 1.0, cosv=True),
                       referenceInterval=6,
                      )



