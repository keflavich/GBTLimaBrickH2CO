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

scanranges = {1:([19,76], [77,134], [149,194], [196,242], [248,305], [306,352]),
              2:([7,52], [54,99], [106,162], [164,217], [227,272], [274,295])
             }
sampler_feeds = {x: 1 if x in 'ABCD' else 2 for x in 'ABCDEFGH'}
fntemplate = '15B_129_{obsrun}_{0:d}to{1:d}_{2:s}_F{3:d}.fits'

for cubename,restfreq,samplers,cunit3,ctype3,naxis3,cdelt3 in (
        ('CMZ_East_CH3OH202313_cube',  12.17859e9,  ['A1_1', 'A2_1', 'E1_1',
                                                     'E2_1', 'A1_2', 'A2_2',
                                                     'E1_2', 'E2_2'], 'km/s',
         'VRAD', 800, 0.5),
        ('CMZ_East_CH3OH514515_cube',  12.511e9,  ['E1_3', 'E2_3', 'A1_3',
                                                   'A2_3'], 'km/s', 'VRAD',
         800, 0.5),
        ('CMZ_East_SO1211_cube',   13.04381e9,  ['E1_5', 'E2_5', 'A1_5',
                                                 'A2_5'], 'km/s', 'VRAD', 800, 0.5),
        ('CMZ_East_H213CO_cube',  13.7788e9,  ['D2_1', 'D2_2', 'H2_1', 'H2_2',
                                               'D1_1', 'H1_1', 'D1_2', 'H1_2'],
         'km/s', 'VRAD', 800, 0.5),
        ('CMZ_East_H2C18O_cube',  13.16596e9,  ['A1_7', 'A2_7', 'E1_7',
                                                'E2_7'], 'km/s', 'VRAD', 800, 0.5),
        ('CMZ_East_13.0_cube', 13.0e9, ['C1_0','C2_0','G2_0','G1_0'], 'Hz',
         'FREQ', 15000, 1e5),
        ('CMZ_East_14.5_cube', 14.5e9, ['C1_0','C2_0','G2_0','G1_0'], 'Hz',
         'FREQ', 15000, 1e5),
            ):

    cubename = os.path.join(outpath,cubename)

    makecube.generate_header(0.466, -0.025, naxis1=200, naxis2=150, pixsize=15,
                             naxis3=naxis3, cd3=cdelt3, cunit3=cunit3, clobber=True,
                             ctype3=ctype3,
                             crval3=restfreq if ctype3=='FREQ' else 0.0,
                             output_flatheader=cubename+"flatheader.txt",
                             output_cubeheader=cubename+"cubeheader.txt",
                             restfreq=restfreq)
    makecube.make_blank_images(cubename,
                               flatheader=cubename+"flatheader.txt",
                               cubeheader=cubename+"cubeheader.txt",
                               clobber=True)

    files = [x for obsrun in scanranges for scan1,scan2 in scanranges[obsrun] for x in
             [os.path.join(outpath,
                           fntemplate.format(scan1, scan2, samplers[ii],
                                             sampler_feeds[samplers[ii][0]],
                                             obsrun=obsrun))
              for ii in range(len(samplers))
             ]]

    iterator = makecube.freq_iterator if ctype3 == 'FREQ' else makecube.velo_iterator

    for fn in files:
        makecube.add_file_to_cube(fn,
                                  cubename+'.fits',
                                  nhits=cubename+'_nhits.fits',
                                  add_with_kernel=True, 
                                  chmod=True,
                                  velo_iterator=iterator,
                                  kernel_fwhm=20./3600.,
                                  default_unit=u.Unit(cunit3),
                                  progressbar=True,
                                  flatheader=cubename+"flatheader.txt",
                                  cubeheader=cubename+"cubeheader.txt",
                                 )

    if ctype3 == 'VRAD':
        makecube.make_flats(cubename,vrange=[-20,80],noisevrange=[150,200])
