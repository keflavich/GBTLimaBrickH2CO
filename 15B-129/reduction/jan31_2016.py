import os
from astropy import log
import astropy.io.fits as pyfits
from sdpy import calibrate_map_scans
import paths

log.setLevel('DEBUG')

mapname = 'CMZ_East'

"""
In [9]: for fn in glob.glob('AGBT15B_129_03.raw.vegas/*fits'):
   ...:     f = fits.open(fn)
   ...:     print(set(zip(f[1].data['IFNUM'], f[1].data['SAMPLER'])))
set([(6, 'A1_6'), (3, 'A1_3'), (2, 'A2_2'), (9, 'A1_0'), (1, 'A1_1'), (9, 'A2_0'), (1, 'A2_1'), (2, 'A1_2'), (3, 'A2_3'), (6, 'A2_6'), (5, 'A1_5'), (4, 'A2_4'), (7, 'A1_7'), (7, 'A2_7'), (4, 'A1_4'), (5, 'A2_5')])
set([(13, 'B1_0'), (13, 'B2_0')])
set([(17, 'F2_1'), (16, 'F2_0'), (16, 'F1_0'), (17, 'F1_1'), (18, 'F2_2'), (18, 'F1_2')])
set([(15, 'C2_0'), (15, 'C1_0')])
set([(19, 'D1_0'), (19, 'D2_0')])
set([(0, 'E1_1'), (8, 'E2_0'), (14, 'E1_5'), (0, 'E2_1'), (10, 'E1_2'), (12, 'E1_4'), (10, 'E2_2'), (11, 'E1_3'), (11, 'E2_3'), (8, 'E1_0'), (14, 'E2_5'), (12, 'E2_4')])
"""

samplers = {
     0: ['E1_1', 'E2_1'], # h2co
     1: ['A1_1', 'A2_1'],
     2: ['A2_2', 'A1_2'],
     3: ['A1_3', 'A2_3'],
     4: ['A2_4', 'A1_4'],
     5: ['A1_5', 'A2_5'], # h213co
     6: ['A1_6', 'A2_6'],
     7: ['A1_7', 'A2_7'],
     8: ['E2_0', 'E1_0'],
     9: ['A1_0', 'A2_0'],
     10: ['E1_2', 'E2_2'],
     11: ['E1_3', 'E2_3'],
     12: ['E1_4', 'E2_4'],
     13: ['B1_0', 'B2_0'],
     14: ['E1_5', 'E2_5'],
     15: ['C2_0', 'C1_0'],
     16: ['F2_0', 'F1_0'],
     17: ['F2_1', 'F1_1'], # ch3oh maser
     18: ['F2_2', 'F1_2'],
     19: ['D1_0', 'D2_0']}

feeds = {
        0: [1,1,],
        1: [1,1,],
        2: [1,1,],
        3: [1,1,],
        4: [1,1,],
        5: [1,1,],
        6: [1,1,],
        7: [1,1,],
        8: [1,1,],
        9: [1,1,],
        10: [1,1,],
        11: [1,1,],
        12: [1,1,],
        13: [1,1,],
        14: [1,1,],
        15: [1,1,],
        16: [1,1,],
        17: [1,1,],
        18: [1,1,],
        19: [1,1,],
        }


for ifnum in samplers:
    for sampler,feednum in zip(samplers[ifnum],feeds[ifnum]):

        filename = paths.AGBT15B_129_3_fullpath.format(sampler[0])
        filepyfits = pyfits.open(filename,memmap=True)
        datapfits = filepyfits[1].data
        dataarr = datapfits.DATA

        for obsmode,refscans,scanrange,sourcename in zip(
            ('RALongMap',
             'DecLatMap',
            ),
            ([6,13,20,27,34,41,48,],
             [50,57,64,71,78,85],
            ),
            ([7,49],
             [51,90],
            ),
            ('CMZ_East',
             'CMZ_East',
            )
           ):

            s1,s2 = scanrange

            savefile = os.path.join(paths.AGBT15B_129_3_path,
                                    "AGBT15B_129_03_{0}_fd{1}_if{2}_sr{3}-{4}"
                                    .format(sampler,feednum,ifnum,s1,s2))
            log.info(savefile)

            outfn = os.path.join(paths.outpath,
                                 '15B_129_3_%ito%i_%s_F%i.fits' % (s1,s2,sampler,feednum))
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
