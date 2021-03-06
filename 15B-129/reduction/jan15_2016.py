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

        for obsmode,refscans,scanrange,sourcename in zip(
            ('RALongMap', 'RALongMap', 'DecLatMap', 'DecLatMap', 'RALongMap',
             'RALongMap',  ),
            ([6,11,16,21,26,31,36,41,46,51],
             [53,58,63,68,73,78,83,88,93,98],
             [105,110,115,120,125,130,135,140,145,150,155,160],
             [163,168,173,178,183,188,193,198,203,208,213,218],
             [226,231,236,241,246,251,256,261,266,271],
             [273,278,283,288,293],
            ),
            ([7,52],
             [54,99],
             [106,162],
             [164,217],
             [227,272],
             [274,295],
            ),
            ('CMZ_East_left',
             'CMZ_East_right',
             'CMZ_East_right',
             'CMZ_East_left',
             'CMZ_East_right',
             'CMZ_East_left',
            )
           ):

            s1,s2 = scanrange

            savefile = os.path.join(paths.AGBT15B_129_2_path,
                                    "AGBT15B_129_02_{0}_fd{1}_if{2}_sr{3}-{4}"
                                    .format(sampler,feednum,ifnum,s1,s2))
            log.info(savefile)

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
