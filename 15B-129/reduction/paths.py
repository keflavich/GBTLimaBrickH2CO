import os
import socket

if socket.gethostname() == 'eso-macbook':
    projpath = '/Volumes/passport/gbt/AGBT15B_129/'
else:
    projpath = '/lustre/pipeline/scratch/aginsbur/15B_129'

AGBT15B_129_1_path = os.path.join(projpath, 'AGBT15B_129_01.raw.vegas/')
AGBT15B_129_1_file = 'AGBT15B_129_01.raw.vegas.{0}.fits'
AGBT15B_129_1_fullpath = os.path.join(AGBT15B_129_1_path, AGBT15B_129_1_file)

outpath = os.path.join(projpath, 'reduced')

#root = '/Users/adam/work/w51/2014_wband_h2co'
#spectra = os.path.join(root,'spectra')
