
cat = Catalog("/users/aginsbur/GBT15B-129/gc_15B-129.astrid")

Configure("/users/aginsbur/GBT15B-129/H2CO_2cm_KUSetup_GC_15B-129.py")

Slew("CMZ_East")
AutoPeakFocus( frequency=14488., beamName="1" )
Break("Check pointing/focus")

Configure("/users/aginsbur/GBT15B-129/H2CO_2cm_KUSetup_GC_15B-129.py")
