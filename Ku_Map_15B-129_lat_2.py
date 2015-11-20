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

cat = Catalog("/users/aginsbur/GBT15B-129/gc_15B-129.astrid")
Configure("/users/aginsbur/GBT15B-129/H2CO_2cm_KUSetup_GC_15B-129.py")

Slew("CMZ_East_right")
Balance()

amintodeg = 1/60.
scanrate = 20. # arcmin/min
mintosec = 60.

# vertical scans
height = 12.
width = 15.
DecLatMapWithReference(location='CMZ_East_right',     #center of map
                       hLength = Offset("Galactic",width*amintodeg,0.0,cosv=True), 
                       vLength = Offset("Galactic",0.0,height*amintodeg,cosv=True), 
                       hDelta  = Offset("Galactic",(1./3.)*amintodeg,0.0,cosv=True), 
                       scanDuration = (height/scanrate) * mintosec,
                       beamName="1",
                       # 1 degree vertical offset
                       referenceOffset=Offset("Galactic", 0.0, 1.0, cosv=True),
                       referenceInterval=4,
                      )


