import os
from astropy import log
log.setLevel('DEBUG')
import astropy.io.fits as pyfits
from sdpy import makecube,make_off_template,calibrate_map_scans
import numpy as np
from astropy import units as u
from paths import AGBT15B_129_1_path,outpath
import paths

mapname = 'CMZ_East'


samplers = {
        0: ["H2_5","H1_5","D1_5","D2_5"],
        1: ['A1_1','A2_1','E1_1','E2_1'],
        15: ['B1_0','B2_0','F2_0','F1_0'],
             
        }

feeds = {
        0: [2,2,1,1],
        1: [1,1,2,2],
        15: [1,1,2,2],
        }


for ifnum in samplers:
    for sampler,feednum in zip(samplers[ifnum],feeds[ifnum]):

        filename = paths.AGBT15B_129_1_fullpath.format(sampler[0])
        filepyfits = pyfits.open(filename,memmap=True)
        datapfits = filepyfits[1].data
        dataarr = datapfits.DATA

        #gain_dict = calibrate_map_scans.compute_gains_highfreq(datapfits,
        #                                                       feednum=feednum,
        #                                                       sampler=sampler)
        #gain_dict = {k:v for k,v in gain_dict.iteritems() if v[1] > 0}
        #gaintimes = np.array(gain_dict.keys())
        #gains = np.array([v[0] for v in gain_dict.values()])
        #tsys = np.array([v[1] for v in gain_dict.values()])
        #gainsOK = gains > 0
        #gaintimes = gaintimes[gainsOK]
        #gains = gains[gainsOK]
        #gain = np.median(gains)
        #datapfits['TSYS'] = np.median(tsys[gainsOK])


        #for obsmode,refscans,scanrange in zip(('DecLatMap','RALongMap','DecLatMap'),([9,54],[62,98],[108,140]),([9,54],[62,98],[108,140])):
        for obsmode,refscans,scanrange,sourcename in zip(
            ('DecLatMap', 'DecLatMap', 'RALongMap', 'RALongMap', 'DecLatMap', 'DecLatMap'),
            ([19,24,29,34,39,44,49,54,59,64,69,74],
             [77,82,87,92,97,102,107,112,117,122,127,132,],
             [149,154,159,164,169,174,179,184,189,194],
             [196,201,206,211,216,221,226,231,236,241],
             [248,253,258,263,268,273,278,283,288,293,298,303,],
             [306,311,316,321,326,331,336,341,346,351],
            ),
            ([19,76],
             [77,134],
             [149,194],
             [196,242],
             [248,305],
             [306,352]
            ),
            ('CMZ_East_left',
             'CMZ_East_right',
             'CMZ_East_left',
             'CMZ_East_right',
             'CMZ_East_left',
             'CMZ_East_right',
            )
           ):

            s1,s2 = scanrange

            savefile = os.path.join(paths.AGBT15B_129_1_path,
                                    "AGBT15B_129_01_{0}_fd{1}_if{2}_sr{3}-{4}"
                                    .format(sampler,feednum,ifnum,s1,s2))
            log.info(savefile)

            #if sampler in ('A1_0','A2_0'):
            #    off_template,off_template_in = make_off_template.make_off(filename, scanrange=scanrange,
            #            #exclude_velo=[-10,70], interp_vrange=[-150,250],
            #            interp_polyorder=10, sampler=sampler, return_uninterp=True,
            #            feednum=feednum,
            #            percentile=50,
            #            sourcename=sourcename,
            #            savefile=savefile,
            #            clobber=True,
            #            #debug=True,
            #            linefreq=constants.restfreq, # needed to get velo right...
            #            extension=1, exclude_spectral_ends=10)

            outfn = os.path.join(outpath,
                                 '15B_129_1_%ito%i_%s_F%i.fits' % (s1,s2,sampler,feednum))
            calibrate_map_scans.calibrate_cube_data(filename,
                                                    outfn,
                                                    scanrange=scanrange,
                                                    #min_scale_reference=10,
                                                    feednum=feednum,
                                                    refscans=refscans,
                                                    sampler=sampler,
                                                    filepyfits=filepyfits,
                                                    datapfits=datapfits,
                                                    # ignored b/c gain tau=0.50,
                                                    #tsys=np.median(tsys[gainsOK]),
                                                    #gain=gain_dict,
                                                    dataarr=dataarr,
                                                    obsmode=obsmode,
                                                    sourcename=sourcename,
                                                    highfreq=False,
                                                    verbose=True,
                                                   )
                                                    #off_template=off_template)


