import astropy.io.fits as pyfits
import itertools
import sys
sys.path.append('/Users/adam/repos/casaradio/branches/python/ginsburg/')
import makecube
import numpy as np
np.seterr(all='ignore')

scanrange=[9,54]
ref1 = 9
ref2 = 54
refscans = [9,54]#,22,32]
sourcename = "LimaBean"
obsmode = "DecLatMap"
mapname = 'LimaBean'
outpath = '/Users/adam/observations/gbt/%smap/' % mapname

filename = '/Users/adam/observations/gbt/AGBT14A_110_01/AGBT14A_110_01.raw.acs.fits'
filepyfits = pyfits.open(filename,memmap=True)
datapfits = filepyfits[1].data
dataarr = datapfits.DATA

samplers = {
        0: ["A9","A13","C25","C29"],
        1: ["A10","A14","C26","C30"],
        2: ["B17","B21","D33","D37"],
        3: ["B18","B22","D34","D38"],
        }

feeds = {
        0: [1,1,2,2],
        1: [1,1,2,2],
        2: [1,1,2,2],
        3: [1,1,2,2]
        }

for ifnum in samplers:
    for sampler,feednum in zip(samplers[ifnum],feeds[ifnum]):

        if sampler in ('A9','A13','C25','C29'):
            off_template,off_template_in = makecube.make_off(filename, scanrange=scanrange,
                    exclude_velo=[-120,103,158,193], interp_vrange=[-600,600],
                    interp_polyorder=10, sampler=sampler, return_uninterp=True, 
                    percentile=50)
        if sampler in ["B17","B21","D33","D37"]: # h2 13CO
            off_template = makecube.make_off(filename, scanrange=scanrange,
                    exclude_velo=[-10,70], interp_vrange=[-100,150],
                    interp_polyorder=10, sampler=sampler)
        if sampler in ["B18","B22","D34","D38"]: # h2c18o
            off_template = makecube.make_off(filename, scanrange=scanrange,
                    exclude_velo=[-10,70], interp_vrange=[-150,250],
                    interp_polyorder=10, sampler=sampler)
        else:
            off_template = None

        makecube.calibrate_cube_data(filename,
                outpath+'14A_110_%ito%i_%s_F1.fits' %
                (ref1,ref2,sampler),scanrange=scanrange,refscan1=ref1,refscan2=ref2,
                feednum=feednum, refscans=refscans, sampler=sampler, filepyfits=filepyfits,
                datapfits=datapfits, tau=0, dataarr=dataarr, obsmode=obsmode,
                sourcename=sourcename, off_template=off_template)

cubename='LimaBean_H2CO22_cube'
# 15' x 12 ' 
makecube.generate_header(0.256, 0.0220, naxis1=100, naxis2=100, pixsize=15,
        naxis3=1200, cd3=1.0, clobber=True, restfreq=14.48848e9)
makecube.make_blank_images(cubename,clobber=True)

files = ['/Users/adam/observations/gbt/LimaBeanmap/14A_110_9to54_A13_F1.fits',
         '/Users/adam/observations/gbt/LimaBeanmap/14A_110_9to54_A9_F1.fits',
         #'/Users/adam/observations/gbt/LimaBeanmap/14A_110_22to32_A13_F1.fits',
         #'/Users/adam/observations/gbt/LimaBeanmap/14A_110_22to32_A9_F1.fits',
         ]

for fn in files:
    makecube.add_file_to_cube(fn,
        cubename+'.fits',nhits=cubename+'_nhits.fits',wcstype='V',
        add_with_kernel=True,
        kernel_fwhm=20./3600.,
        velocityrange=[-600,600],excludefitrange=[-225,250],
        smoothto=2)

import os
os.system('./LimaBean_H2CO22_cube_starlink.sh')

makecube.make_flats(cubename,vrange=[-20,60],noisevrange=[250,300])

"""
obsmode = 'RALongMap'
scanrange=[22,32]
ref1 = 22
ref2 = 32
refscans = [22,32]#,22,32]
for sampler in ['A10', 'A13', 'A14', 'A9', 'B17', 'B18', 'B21', 'B22', 'C25', 'C26',
        'C29', 'C30', 'D33', 'D34', 'D37', 'D38']:

    if sampler in ('A9','A13'):
        off_template = makecube.make_off(filename, scanrange=scanrange,
                exclude_velo=[-125,103,158,193], interp_vrange=[-600,600],
                interp_polyorder=10, sampler=sampler)
    if sampler in ('C25','C29'): # h2 13CO
        off_template = makecube.make_off(filename, scanrange=scanrange,
                exclude_velo=[-10,70], interp_vrange=[-100,150],
                interp_polyorder=10, sampler=sampler)
    if sampler in ('D33','D37'): # 
        off_template = makecube.make_off(filename, scanrange=scanrange,
                exclude_velo=[-20,80], interp_vrange=[-100,150],
                interp_polyorder=10, sampler=sampler)
    else:
        off_template = None

    makecube.calibrate_cube_data(filename,
            outpath+'14A_110_%ito%i_%s_F1.fits' %
            (ref1,ref2,sampler),scanrange=scanrange,refscan1=ref1,refscan2=ref2,
            feednum=1, refscans=refscans, sampler=sampler, filepyfits=filepyfits,
            datapfits=datapfits, tau=0, dataarr=dataarr, obsmode=obsmode,
            sourcename=sourcename, off_template=off_template)




# SAMPLERS:
# [('A10', 5500000000.0),
#  ('A13', 4829659400.0),
#  ('A14', 5500000000.0),
#  ('A9', 4829659400.0),
#  ('B17', 5200000000.0),
#  ('B18', 5008992000.0),
#  ('B21', 5200000000.0),
#  ('B22', 5008992000.0),
#  ('C25', 4593089000.0),
#  ('C26', 4630000000.0),
#  ('C29', 4593089000.0),
#  ('C30', 4630000000.0),
#  ('D33', 4874157000.0),
#  ('D34', 4497776000.0),
#  ('D37', 4874157000.0),
#  ('D38', 4497776000.0)]
#  OH F0-1 4.66024 
#  OH F4-4 5.52344 
#  OH F4-3 5.54704 


for cubename,restfreq,samplers in (
        ('LimaBean_H113a_cube', 4.497776e9, ('D34','D38')),
        #('LimaBean_H110a_cube', 4.874157e9, ('D33','D37')),
        ('LimaBean_H213CO_cube', 4.593089e9, ('C25','C29')),
        #('LimaBean_H109a_cube', 5.008922e9, ('B18','B22')),
        #('LimaBean_H112a_cube', 4.61879e9, ('C26','C30')),
        #('LimaBean_OHF44_cube', 5.52344e9, ('A10','A14')),
        #('LimaBean_CH3NH2_cube', 5.19543e9, ('B21','B17'))
            ):


    makecube.generate_header(0.256, 0.0220, naxis1=24, naxis2=24, pixsize=60,
            naxis3=2400, cd3=1.0, clobber=True, restfreq=restfreq)
    makecube.make_blank_images(cubename,clobber=True)

    files = [
             '/Users/adam/observations/gbt/LimaBeanmap/14A_110_6to21_%s_F1.fits' % samplers[0],
             '/Users/adam/observations/gbt/LimaBeanmap/14A_110_6to21_%s_F1.fits' % samplers[1],]
             #'/Users/adam/observations/gbt/LimaBeanmap/14A_110_22to32_%s_F1.fits' % samplers[0],
             #'/Users/adam/observations/gbt/LimaBeanmap/14A_110_22to32_%s_F1.fits' % samplers[1],
    for fn in files:
        makecube.add_file_to_cube(fn,
            cubename+'.fits',nhits=cubename+'_nhits.fits',wcstype='V',
            velocityrange=[-1200,1200],excludefitrange=[-150,225])

    os.system('chmod +x %s_starlink.sh' % cubename)
    os.system('./%s_starlink.sh' % cubename)
    makecube.make_flats(cubename,vrange=[-20,60],noisevrange=[250,300])



import pyspeckit
#pyspeckit.wrappers.cube_fit('LimaBean_H2CO22_cube_smooth.fits','LimaBean_H2CO22_parfits.fits','LimaBean_H2CO22_noise.fits',fittype='formaldehyde',absorption=True,signal_cut=2)


from pylab import *
def some_plots(xx,yy,dolegend=False,dohalpha=False):
    c13 = h213cocube.get_spectrum(xx,yy)
    c12 = cube.get_spectrum(xx,yy)
    c12.baseline(exclude=[-225,200],order=5)
    c13.baseline(exclude=[-225,200],order=5)
    c13.plotter(label='H$_{2}$$^{13}$CO',axis=gca())
    c12.plotter(axis=c13.plotter.axis,clear=False,color='b',label="H$_{2}$CO")
    (c13*6).plotter(label='6$\\times$H$_{2}$$^{13}$CO',axis=gca(),color='r',clear=False)
    if dolegend:
        legend(loc='best')
    if dohalpha:
        halpha = h110acube.get_spectrum(xx,yy)
        halpha.baseline(exclude=[-225,200],order=5)
        (halpha*5).plotter(axis=c13.plotter.axis,clear=False,color='darkgreen')
    gca().set_xlim(-100,100)
    draw()
        

# some plots
if not 'do_some_plots' in locals():
    do_some_plots=False
    dohalpha=True
if do_some_plots:
    subplots_adjust(wspace=0,hspace=0,left=0.05,right=0.95,bottom=0.05,top=0.95)
    cube = pyspeckit.Cube('LimaBean_H2CO22_cube_sub.fits')
    h213cocube = pyspeckit.Cube('LimaBean_H213CO22_cube_sub.fits')
    #h110acube = pyspeckit.Cube('LimaBean_H110a_cube_sub.fits')

    figure(1); clf()
    nx,ny = 5,5
    for ii,(spy,spx) in enumerate(itertools.product(range(nx),range(ny))):
        sp = subplot(nx,ny,ii+1)
        sp.zorder = nx-spx+ny*spy
        some_plots(spx+9,spy+9,dolegend=(ii==24),dohalpha=True)
        if dohalpha:
            sp.set_ylim(-2.5,1)
        else:
            sp.set_ylim(-2.5,0.5)
        if spx > 0: 
            sp.set_yticks([])
        if spy < ny-1: 
            sp.set_xticks([])
        
"""
