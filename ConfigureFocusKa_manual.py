"""
Configure and focus for a Ka-band observation
"""

cat = Catalog("/users/aginsbur/GBT12B-221/limabean.astrid")

Configure("/users/aginsbur/GBT12B-221/H2CO_1cm_KaSetup_GC.py")

Slew("1713-2658")
AutoPeakFocus(source='1713-2658', frequency=28974.8, beamName="1")
Break("Check pointing/focus")
Configure("/users/aginsbur/GBT12B-221/H2CO_1cm_KaSetup_GC.py")
