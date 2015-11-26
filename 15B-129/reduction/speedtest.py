import os
from astropy import log
log.setLevel('DEBUG')
import astropy.io.fits as pyfits
from sdpy import makecube,make_off_template,calibrate_map_scans
import numpy as np
from astropy import units as u
from paths import AGBT15B_129_1_path,outpath
import paths
import time
t0 = time.time()

mapname = 'CMZ_East'

ifnum = 0
sampler = 'H2_5'
feednum = 2

filename = paths.AGBT15B_129_1_fullpath.format(sampler[0])
filepyfits = pyfits.open(filename,memmap=True)
datapfits = filepyfits[1].data
dataarr = datapfits.DATA

obsmode = 'DecLatMap'
refscans = [19,24,29,34,39,44,49,54,59,64,69,74]
scanrange = [19,76]
sourcename = 'CMZ_East_left'

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

from sdpy.calibrate_map_scans import *
highfreq=False
tau=None
tauz=tau=0
refscan1=refscan2=None
extension=1
verbose=True
exclude_spectral_ends=10
tsys=None
tsysmethod='perscan'
min_scale_reference=False
airmass_method='maddalena'
tatm=273.0
off_template=None


if tau != 0:
    if tauz != 0:
        raise ValueError("Only use tauz, not both tau and tauz")
    else:
        tauz = tau
        warnings.warn("Use tauz instead of tau",
                      DeprecationWarning)

if refscan1 is not None or refscan2 is not None:
    warnings.warn("Use refscans (a list of scans) rather than ref1,ref2",
                  DeprecationWarning)
    if (type(refscans) == list and not
        (len(refscans) ==2 and
         refscans[0] == refscan1 and refscans[1] == refscan2)):
        raise ValueError('refscans does not match refscan1,2')
    elif refscans is None:
        refscans = refscan1,refscan2

if highfreq:
    assert gain is not None

data, dataarr, namelist, filepyfits = load_data_file(filename,
                                                     extension=extension,
                                                     dataarr=dataarr,
                                                     datapfits=datapfits,
                                                     filepyfits=filepyfits)
log.info("Data reading done at {0:0.1f}".format(time.time()-t0))

newdatadict = dict([(n,[]) for n in namelist])
formatdict = dict([(t.name,t.format) for t in filepyfits[extension].columns])

samplers = np.unique(data['SAMPLER'])
if isinstance(sampler,int):
    sampler = samplers[sampler]

OK = data['SAMPLER'] == sampler
log.info("Checking samplers done at {0:0.1f}".format(time.time()-t0))
if np.count_nonzero(OK) == 0:
    raise ValueError("No matches to sampler {0}".format(sampler))
OK &= data['FEED'] == feednum
log.info("Checking feeds done at {0:0.1f}".format(time.time()-t0))
if np.count_nonzero(OK) == 0:
    raise ValueError("No matches to sampler {0} and feed {1}"
                     .format(sampler, feednum))
# This can result in an asymmetric # of on/off scans, which sucks.
#OK &= np.isfinite(data['DATA'].sum(axis=1))
isfinite = np.isfinite(data['DATA']).max(axis=1)
if np.count_nonzero(isfinite) == 0:
    raise ValueError("There is no finite data.")

log.info("Checking finitude done at {0:0.1f}".format(time.time()-t0))

OKsource = OK.copy()
if sourcename is not None:
    OKsource &= (data['OBJECT'] == sourcename)
    if np.count_nonzero(OKsource) == 0:
        raise ValueError("Object {0} not in data".format(sourcename))
log.info("Checking sourcename done at {0:0.1f}".format(time.time()-t0))
if scanrange is not []:
    OKsource &= (scanrange[0] < data['SCAN'])&(data['SCAN'] < scanrange[1])
    if np.count_nonzero(OKsource) == 0:
        raise ValueError("No scans in range {0}-{1}".format(scanrange[0],
                                                            scanrange[1]))
log.info("Checking scanrange done at {0:0.1f}".format(time.time()-t0))
if obsmode is not None:
    OBSMODE = np.core.defchararray.rstrip(data.OBSMODE)
    OKsource &= ((obsmode == OBSMODE) |
                 ((obsmode+":NONE:TPWCAL") == OBSMODE) |
                 ((obsmode+":NONE:TPNOCAL") == OBSMODE)
                )
    if np.count_nonzero(OKsource) == 0:
        raise ValueError("No matches to OBSMODE={0}."
                         "  Valid modes include {1}".format(obsmode,
                                                            set(OBSMODE)))
log.info("Checking obsmode done at {0:0.1f}".format(time.time()-t0))
if sourcename is None and scanrange is None:
    raise IndexError("Must specify a source name and/or a scan range")


if verbose:
    log.info("Beginning scan selection and calibration for "
             "sampler {0} and feed {1}.  Found {2} matching "
             "scans and {3} with the source {4} in it."
             .format(sampler,feednum, OK.sum(), OKsource.sum(),
                     sourcename))

CalOff = (data['CAL']=='F') & OK
CalOn  = (data['CAL']=='T') & OK

log.info("Checking calon/caloff done at {0:0.1f}".format(time.time()-t0))

speclen = dataarr.shape[1]

# Fraction of ends to exclude.  exslice = "Exclusion Slice"
exfrac = exclude_spectral_ends/100.
exslice = slice(speclen*exfrac,-speclen*exfrac)

# reference scans define the "background continuum"
if type(refscans) == list:
    if not highfreq:
        # split into two steps for readability
        temp_ref = get_reference(data, refscans, CalOn=CalOn, CalOff=CalOff,
                                 exslice=exslice, OK=OK, isfinite=isfinite)
        LSTrefs, refarray, ref_cntstoK, tsysref = temp_ref
    else:
        LSTrefs, refarray = get_reference_highfreq(data, refscans, OK=OK)
else:
    raise TypeError("Must specify reference scans as a list of scan numbers.")

if highfreq:
    nscansok = np.count_nonzero(OKsource)
else:
    nscansok = np.count_nonzero(OKsource*CalOn)

if verbose:
    log.info("Beginning calibration of %i scans." % nscansok)

if nscansok == 0:
    import pdb; pdb.set_trace()
    raise ValueError("There are no locations where the source was observed"
                     " with the calibration diode on.  That can't be right.")

if tsys is None:
    compute_tsys(data, tsysmethod=tsysmethod, OKsource=OKsource, OK=OK,
                 CalOn=CalOn, CalOff=CalOff, exslice=exslice,
                 verbose=verbose, isfinite=isfinite)
else:
    data['TSYS'] = tsys
if np.any(np.isnan(data['TSYS'])):
    raise ValueError("NaNs in TSYS")

# experimental: try to rescale the "reference" scan to be the minimum
if min_scale_reference:
    ref_scale,ref_airmass = get_min_scale_reference(data,
                                                    min_scale_reference,
                                                    OKsource=OKsource,
                                                    CalOn=CalOn,
                                                    CalOff=CalOff,
                                                    exslice=exslice,
                                                    airmass_method=airmass_method,
                                                    isfinite=isfinite,
                                                   )
    if verbose:
        log.info("EXPERIMENTAL: min_scale_reference = {0}".format(ref_scale))

log.debug("data.shape = {0}, dataarr.shape = {1}, tsys=[{2}-{3}]".format(data.shape, dataarr.shape, data['TSYS'].min(), data['TSYS'].max()))

# thin out
#OKsource[np.nonzero(OKsource)[0][100:]] = False

#if highfreq:
#    newdatadict = cal_loop_highfreq(data, dataarr, newdatadict, OKsource,  speclen,
#                                    airmass_method, LSTrefs, exslice,
#                                    refscans, namelist, refarray, off_template, gain)
#else:
#    newdatadict = cal_loop_lowfreq(data, dataarr, newdatadict, OKsource, CalOn,
#                                   CalOff, speclen, airmass_method,
#                                   LSTrefs, min_scale_reference, exslice,
#                                   tatm, tauz, refscans, namelist,
#                                   refarray, off_template, isfinite)
#log.debug("newdatadict has length {0}, and its data entry has length {1}".format(len(newdatadict), len(newdatadict['DATA'])))

get_ipython().magic(u'lprun -f cal_loop_lowfreq newdatadict = cal_loop_lowfreq(data, dataarr, newdatadict, OKsource, CalOn, CalOff, speclen, airmass_method, LSTrefs, min_scale_reference, exslice, tatm, tauz, refscans, namelist, refarray, off_template, isfinite)')
#%lprun -f cal_loop_lowfreq newdatadict = cal_loop_lowfreq(data, dataarr, newdatadict, OKsource, CalOn, CalOff, speclen, airmass_method, LSTrefs, min_scale_reference, exslice, tatm, tauz, refscans, namelist, refarray, off_template, isfinite)
