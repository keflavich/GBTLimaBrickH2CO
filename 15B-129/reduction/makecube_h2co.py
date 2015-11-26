import os
import astropy.io.fits as pyfits
import itertools
import sys
from sdpy import makecube,make_off_template,calibrate_map_scans
import numpy as np
from paths import outpath
# to ignore div-by-zero errors?
np.seterr(all='ignore')

cubename = os.path.join(outpath,'CMZ_East_H2CO22_cube')
# 0.5x0.2 deg = 30x12'
makecube.generate_header(0.466, -0.025, naxis1=200, naxis2=150, pixsize=15,
                         naxis3=800, cd3=0.5, clobber=True,
                         cunit3='km/s', crval3=0.0, restfreq=14.48848e9)
makecube.make_blank_images(cubename,clobber=True)

files = [os.path.join(outpath,x) for x in
         (
          '15B_129_1_19to76_H1_5_F2.fits',
          '15B_129_1_77to134_H1_5_F2.fits',
          '15B_129_1_149to194_H1_5_F2.fits',
          '15B_129_1_196to242_H1_5_F2.fits',
          '15B_129_1_248to305_H1_5_F2.fits',
          '15B_129_1_306to352_H1_5_F2.fits',
          '15B_129_1_19to76_H2_5_F2.fits',
          '15B_129_1_77to134_H2_5_F2.fits',
          '15B_129_1_149to194_H2_5_F2.fits',
          '15B_129_1_196to242_H2_5_F2.fits',
          '15B_129_1_248to305_H2_5_F2.fits',
          '15B_129_1_306to352_H2_5_F2.fits',
          '15B_129_1_19to76_D1_5_F1.fits',
          '15B_129_1_77to134_D1_5_F1.fits',
          '15B_129_1_149to194_D1_5_F1.fits',
          '15B_129_1_196to242_D1_5_F1.fits',
          '15B_129_1_248to305_D1_5_F1.fits',
          '15B_129_1_306to352_D1_5_F1.fits',
          '15B_129_1_19to76_D2_5_F1.fits',
          '15B_129_1_77to134_D2_5_F1.fits',
          '15B_129_1_149to194_D2_5_F1.fits',
          '15B_129_1_196to242_D2_5_F1.fits',
          '15B_129_1_248to305_D2_5_F1.fits',
          '15B_129_1_306to352_D2_5_F1.fits',
         )
        ]

for fn in files:
    makecube.add_file_to_cube(fn,
                              cubename+'.fits',nhits=cubename+'_nhits.fits',
                              chmod=True,
                              add_with_kernel=True,
                              kernel_fwhm=20./3600.,
                              velocityrange=[-200,200],
                              excludefitrange=[-25,150],
                              diagnostic_plot_name=fn.replace('.fits','_data_scrubbed.png'),
                              progressbar=True
                             )

#os.system(os.path.join(outpath,'CMZ_East_H2CO22_cube_starlink.sh'))

makecube.make_flats(cubename,vrange=[-20,60],noisevrange=[250,300])

