from astropy.io import fits
from spectral_cube import SpectralCube
from astropy import units as u
import numpy as np

rrls = [109,110,111,112,113,114]
# 115 and 116 have rfi

fntemplate = '/Volumes/passport/gbt/AGBT15B_129/reduced/CMZ_East_H{rrln}a_cube.fits'

data = np.array([fits.getdata(fntemplate.format(rrln=rrln)) for rrln in rrls])

avg = np.mean(data, axis=0)

f = fits.open(fntemplate.format(rrln=111))
f[0].data = avg
f.writeto(fntemplate.format(rrln='109to114avg'), clobber=True)

cube = SpectralCube.read(fntemplate.format(rrln='109to114avg')).minimal_subcube()
scube = cube - cube.median(axis=0)
scube.with_spectral_unit(u.km/u.s).write(fntemplate.format(rrln='109to114avg').replace(".fits","_contsub.fits"))


cubes = [SpectralCube.read(fntemplate.format(rrln=rrln)).minimal_subcube() for rrln in rrls]
for ii,cube in enumerate(cubes):
    cubes[ii] = cube - cube.median(axis=0)

data = np.array([cube.filled_data[:].value for cube in cubes])
avg = np.mean(data, axis=0)

f = fits.open(fntemplate.format(rrln='109to114avg').replace(".fits","_contsub.fits"))
f[0].data = avg
f.writeto(fntemplate.format(rrln='109to114_contsub_b4_avg'), clobber=True)
