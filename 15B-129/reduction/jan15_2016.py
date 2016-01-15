import os
from astropy import log
log.setLevel('DEBUG')
import astropy.io.fits as pyfits
from sdpy import makecube,make_off_template,calibrate_map_scans
import numpy as np
from astropy import units as u
from paths import AGBT15B_129_2_path,outpath
import paths

mapname = 'CMZ_East'


samplers = {
        0: ["H2_5","H1_5","D1_5","D2_5"],
        1: ['A1_1','A2_1','E1_1','E2_1'],
        2: ['A1_2','A2_2','E1_2','E2_2'],
        3: ['A1_3','A2_3','E1_3','E2_3'],
        4: ['A1_4','A2_4','E1_4','E2_4'],
        15: ['C1_0','C2_0','G2_0','G1_0'],
        6: ['A1_5','A2_5','E1_5','E2_5'],
        7: ['A1_6','A2_6','E1_6','E2_6'],
        8: ['A1_7','A2_7','E1_7','E2_7'],
        9: ['D1_0','D2_0','H1_0','H2_0'],
        10: ['D1_1','D2_1','H1_1','H2_1'],
        11: ['D1_2','D2_2','H1_2','H2_2'],
        12: ['D1_3','D2_3','H1_3','H2_3'],
        13: ['D1_4','D2_4','H1_4','H2_4'],
        14: ['A1_0','A2_0','E1_0','E2_0'],
        15: ['B1_0','B2_0','F2_0','F1_0'],
        16: ['D1_6','D2_6','H1_6','H2_6'],
        17: ['D1_7','D2_7','H1_7','H2_7'],
             
        }

feeds = {
        0: [2,2,1,1],
        1: [1,1,2,2],
        2: [1,1,2,2],
        3: [1,1,2,2],
        4: [1,1,2,2],
        5: [1,1,2,2],
        6: [1,1,2,2],
        7: [1,1,2,2],
        8: [1,1,2,2],
        9: [1,1,2,2],
        10: [1,1,2,2],
        11: [1,1,2,2],
        12: [1,1,2,2],
        13: [1,1,2,2],
        14: [1,1,2,2],
        15: [1,1,2,2],
        16: [1,1,2,2],
        17: [1,1,2,2],
        }


for ifnum in samplers:
    for sampler,feednum in zip(samplers[ifnum],feeds[ifnum]):

        filename = paths.AGBT15B_129_2_fullpath.format(sampler[0])
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
            ('RALongMap', ),
            ([6,11,16,21,26,31,36,41,46,51],
             [53,58,63,68,73,78,83,88,93,98],
             [105,110,115,120,125,130,135,140,145,150,155,160],
            ),
            ([7,52],
             [54,99],
             [106,162],
            ),
            ('CMZ_East_left',
             'CMZ_East_right',
             'CMZ_East_right',
            )
           ):

            s1,s2 = scanrange

            savefile = os.path.join(paths.AGBT15B_129_2_path,
                                    "AGBT15B_129_02_{0}_fd{1}_if{2}_sr{3}-{4}"
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
                                 '15B_129_2_%ito%i_%s_F%i.fits' % (s1,s2,sampler,feednum))
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
