import os
import astropy.io.fits as pyfits
import itertools
import sys
from sdpy import makecube,make_off_template,calibrate_map_scans
import numpy as np
from paths import outpath
# to ignore div-by-zero errors?
np.seterr(all='ignore')

scanranges = ([19,76], [77,134], [149,194], [196,242], [248,305], [306,352])
sampler_feeds = {x: 1 if x in 'ABCD' else 2 for x in 'ABCDEFGH'}

for cubename,restfreq,samplers,cunit3,ctype3 in (
        #('CMZ_East_H113a_cube', 4.497776e9, ('D34','D38')),
        #('CMZ_East_H110a_cube', 4.874157e9, ('D33','D37')),
        ('CMZ_East_14.5_cube', 14.5e9, ['B1_0','B2_0','F2_0','F1_0'], 'Hz', 'FREQ'),
        #('CMZ_East_H2C18O22_cube', 13.16596, ["B18","B22","D34","D38"]),
        #('CMZ_East_H109a_cube', 5.008922e9, ('B18','B22')),
        #('CMZ_East_H112a_cube', 4.61879e9, ('C26','C30')),
        #('CMZ_East_OHF44_cube', 5.52344e9, ('A10','A14')),
        #('CMZ_East_CH3NH2_cube', 5.19543e9, ('B21','B17'))
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
                           '15B_129_1_%ito%i_%s_F%i.fits' %
                           (scan1, scan2, samplers[ii],
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

    #os.system('chmod +x %s_starlink.sh' % cubename)
    #os.system('%s_starlink.sh' % cubename)
    makecube.make_flats(cubename,vrange=[-20,60],noisevrange=[250,300])


##import FITS_tools
#import FITS_tools.cube_regrid
#from astropy.io import fits
### TODO: REPLACE WITH FITS_TOOLS!!
##from agpy.cubes import smooth_cube
#from FITS_tools.cube_regrid import spatial_smooth_cube
#
#for cubename in ('CMZ_East_H2CO22_cube', 'CMZ_East_H213CO22_cube', 'CMZ_East_H2C18O22_cube'):
#
#    cubename = os.path.join(outpath,cubename)
#    cube = fits.open(cubename+"_sub.fits")
#    # kernel = ((2.5*60)**2 -  50.**2)**0.5 / sqrt(8*log(2)) = 60 arcsec
#    # 60 arcsec / 15 "/pixel = 4
#    cubesm2 = FITS_tools.cube_regrid.gsmooth_cube(cube[0].data, [5,4,4], use_fft=True, psf_pad=False, fft_pad=False)
#    cubesm = spatial_smooth_cube(cube[0].data, kernelwidth=4, interpolate_nan=True)
#    cube[0].data = cubesm
#    cube.writeto(cubename+"_sub_smoothtoCband.fits",clobber=True)
#    cube[0].data = cubesm2
#    cube.writeto(cubename+"_sub_smoothtoCband_vsmooth.fits",clobber=True)
#
#    #makecube.make_taucube(cubename,cubename+"_continuum.fits",etamb=0.886)
#    #makecube.make_taucube(cubename,cubename+"_continuum.fits",etamb=0.886, suffix="_sub_smoothtoCband.fits")
#    # -0.4 is the most negative point in the continuum map...
#    makecube.make_taucube(cubename,
#                          cubename+"_continuum.fits",
#                          etamb=0.886,
#                          tex=2.0,
#                          suffix="_sub_smoothtoCband_vsmooth.fits",
#                          outsuffix="_smoothtoCband_vsmooth.fits",
#                          TCMB=2.7315+0.4)
#
#    makecube.make_taucube(cubename,
#                          cubename+"_continuum.fits",
#                          etamb=0.886,
#                          tex=2.0,
#                          suffix="_sub_smoothtoCband.fits",
#                          outsuffix="_smoothtoCband.fits",
#                          TCMB=2.7315+0.4)
#
#    makecube.make_taucube(cubename,
#                          cubename+"_continuum.fits",
#                          etamb=0.886,
#                          tex=2.0,
#                          suffix="_sub.fits",
#                          outsuffix=".fits",
#                          TCMB=2.7315+0.4)
