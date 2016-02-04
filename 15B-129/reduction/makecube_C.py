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

scanranges = {3:([7, 49], [51,90]),
             }
sampler_feeds = {x: 1 for x in 'ABCDEFGH'}
fntemplate = '15B_129_{obsrun}_{0:d}to{1:d}_{2:s}_F{3:d}.fits'

for cubename,restfreq,samplers,cunit3,ctype3,naxis3,cdelt3 in (
        ('CMZ_East_5.2GHz_cube', 5.2e9, ['B1_0','B2_0'], 'Hz',
         'FREQ', 15000, 1e5),
        ('CMZ_East_6.0GHz_cube', 6.0e9, ['C1_0','C2_0'], 'Hz',
         'FREQ', 15000, 1e5),
        ('CMZ_East_6.8GHz_cube', 6.8e9, ['D1_0','D2_0'], 'Hz',
         'FREQ', 15000, 1e5),
        ('CMZ_East_H100a_cube',  6.478759895377347e9,  ['F1_0','F2_0'], 'km/s', 'VRAD',
         300, 2),
        ('CMZ_East_H99a_cube',  6.6760758542031216e9,  ['F1_2','F2_2'], 'km/s', 'VRAD',
         300, 2),
        ('CMZ_East_H110a_cube',  4.874157079778041e9,  ['E1_3','E2_3'], 'km/s', 'VRAD',
         300, 2),
        ('CMZ_East_H111a_cube',  4.744183027188663e9,  ['A1_7','A2_7'], 'km/s', 'VRAD',
         300, 2),
        ('CMZ_East_H109a_cube',  5.008922635977179e9,  ['E1_4','E2_4'], 'km/s', 'VRAD',
         300, 2),
        ('CMZ_East_H112a_cube',  4.618789407132678e9,  ['A1_6','A2_6'], 'km/s', 'VRAD',
         300, 2),
        ('CMZ_East_H113a_cube',  4.497776208521413e9,  ['A1_4','A2_4'], 'km/s', 'VRAD',
         300, 2),
        ('CMZ_East_H114a_cube',  4.380953809985994e9,  ['A1_2','A2_2'], 'km/s', 'VRAD',
         300, 2),
        ('CMZ_East_H115a_cube',  4.268142355634107e9,  ['A1_1','A2_1'], 'km/s', 'VRAD',
         300, 2),
        ('CMZ_East_H116a_cube',  4.159171173305872e9,  ['A1_0','A2_0'], 'km/s', 'VRAD',
         300, 2),
        ('CMZ_East_CH3OHmaser_cube',   6668.47e6,  ['F2_1','F1_1'], 'km/s', 'VRAD',
         800, 0.5),
        ('CMZ_East_H2CO11_cube',  4.82966e9,  ['E1_1', 'E2_1'], 'km/s', 'VRAD',
         800, 0.5),
        ('CMZ_East_H213CO11_cube',  4593.09e6,  ['A1_5','A2_5'], 'km/s', 'VRAD',
         800, 0.5),
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
                                  kernel_fwhm=30./3600.,
                                  default_unit=u.Unit(cunit3),
                                  progressbar=True,
                                  linefreq=restfreq,
                                  flatheader=cubename+"flatheader.txt",
                                  cubeheader=cubename+"cubeheader.txt",
                                 )

    if ctype3 == 'VRAD':
        makecube.make_flats(cubename,vrange=[-20,80],noisevrange=[150,200])
