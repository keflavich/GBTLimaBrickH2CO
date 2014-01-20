"""
Observe an off position near the LimaBean

Useful as a quick reference during observations (for getsigref) and a sanity
check when performing the "artificial off" creation using on-source map data.
"""


cat = Catalog("/users/aginsbur/GBT12B-221/limabean.astrid")

Slew("LimaBeanOff")
# 90 seconds to match each scan
Track("LimaBeanOff",None,90)


