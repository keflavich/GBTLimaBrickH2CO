"""
Configure and focus for a Ku-band observation
"""

cat = Catalog("/users/aginsbur/GBT12B-221/limabean.astrid")

Configure("/users/aginsbur/GBT12B-221/H2CO_2cm_KUSetup_GC.py")

Slew("LimaBean")
AutoPeakFocus( frequency=14488., beamName="1" )
Break("Check pointing/focus")
Configure("/users/aginsbur/GBT12B-221/H2CO_2cm_KUSetup_GC.py")
