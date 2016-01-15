import os
import astropy.io.fits as pyfits
from astropy import units as u
import itertools
import sys
from sdpy import makecube,make_off_template,calibrate_map_scans
import numpy as np
from paths import outpath
# to ignore div-by-zero errors?
np.seterr(all='ignore')

scanranges = ([19,76], [77,134], [149,194], [196,242], [248,305], [306,352])
sampler_feeds = {x: 1 if x in 'ABCD' else 2 for x in 'ABCDEFGH'}
fntemplate = '15B_129_1_{0:d}to{1:d}_{2:s}_F{3:d}.fits'

for cubename,restfreq,samplers,cunit3,ctype3 in (
        ('CMZ_East_13.0_cube', 13.0e9, ['C1_0','C2_0','G2_0','G1_0'], 'Hz', 'FREQ'),
        ('CMZ_East_14.5_cube', 14.5e9, ['C1_0','C2_0','G2_0','G1_0'], 'Hz', 'FREQ'),
            ):

    cubename = os.path.join(outpath,cubename)

    makecube.generate_header(0.466, -0.025, naxis1=200, naxis2=150, pixsize=15,
                             naxis3=15000, cd3=1e5, cunit3=cunit3, clobber=True,
                             ctype3=ctype3,
                             crval3=restfreq,
                             output_flatheader=cubename+"flatheader.txt",
                             output_cubeheader=cubename+"cubeheader.txt",
                             restfreq=restfreq)
    makecube.make_blank_images(cubename,
                               flatheader=cubename+"flatheader.txt",
                               cubeheader=cubename+"cubeheader.txt",
                               clobber=True)

    files = [x for scan1,scan2 in scanranges for x in
             [os.path.join(outpath,
                           fntemplate.format(scan1, scan2, samplers[ii],
                                             sampler_feeds[samplers[ii][0]]))
              for ii in xrange(len(samplers))]]
    for fn in files:
        makecube.add_file_to_cube(fn,
                                  cubename+'.fits',
                                  nhits=cubename+'_nhits.fits',
                                  add_with_kernel=True, 
                                  chmod=True,
                                  velo_iterator=makecube.freq_iterator,
                                  kernel_fwhm=20./3600.,
                                  default_unit=u.Hz,
                                  progressbar=True,
                                  flatheader=cubename+"flatheader.txt",
                                  cubeheader=cubename+"cubeheader.txt",
                                 )

    makecube.make_flats(cubename,vrange=[-20,60],noisevrange=[250,300])
