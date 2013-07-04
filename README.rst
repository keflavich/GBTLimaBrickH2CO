Lima Bean / Brick / G0.253 GBT Mapping Observations Setup
=========================================================

For proposals GBT12B-221 and GBT13A-532 (DD).

The C-band observations were completed in August 2012 using LimaBeanMap_lon.py


Observing Setup & Instructions
------------------------------

Log in at least 30 minutes prior to observations

 1. `ssh username@prospero.gb.nrao.edu`
 2. Start `cleo &`
 3. Start `astrid &`

Important Links
~~~~~~~~~~~~~~~
List of links:

 * `Guidelines for Balancing <http://www.gb.nrao.edu/gbt/support/pdf/balancing-presentation.pdf>`_
 * `GBT Observers Guide <https://science.nrao.edu/facilities/gbt/observing/GBTog.pdf>`_
 * `Remote Observing site <https://science.nrao.edu/facilities/gbt/observing/remote-observing-with-the-gbt>`_
 * `GBT Schedule <https://dss.gb.nrao.edu/schedule/public>`_
 * `GBT High-Frequency Weather <http://www.gb.nrao.edu/~rmaddale/Weather/AllOverviews.html>`_
 * `GBT Remote Login (from CU's CASA:radio group) <http://code.google.com/p/casaradio/wiki/GBTRemoteLogin>`_

Observing Scripts
-----------------
 * `LimaBeanOff.py` - Use for a simple single off position observation

Ku-band scripts
~~~~~~~~~~~~~~~
 * `ConfigureFocusKu.py` - Run this first.  Sets up the observations and calibrates using `AutoPeakFocus`
 * `Ku_LimaBeanMap_Lat.py` - Latitude map.  Should take ~1.5 hours
 * `Ku_LimaBeanMap_Lon.py` - Longitude map.  Should take ~1.5 hours


C-band scripts
~~~~~~~~~~~~~~
(these are complete, so can be ignored, but are included for completeness)
 * `LimaBeanMap_Lat.py`
 * `LimaBeanMap_Lat_nocal.py`
 * `LimaBeanMap_Lon.py`
 * `LimaBeanMap_Lon_nocal.py`


Some information from the proposal
----------------------------------

::

    The Ku band observations will require 36 strips separated by 20′′ in
    latitude and 45 strips separated by 20 ′′in longitude. These will be
    performed at a scan rate of 4 ′′/sec and a sampling rate of once per second
    to minimize smearing. This will result in an integration time of 20s per
    20′′ pixel.

I've modified this to speed up the observations somewhat for the DD time in
case we're assigned a shorter block.

The data backends can't handle integration times below 1.2s.
To sample the beam, we want to Nyquist sample a 1-sigma beam width, i.e. 2
samples per "sigma"
FWHM = 50
sigma = FWHM / 50 = 21.3
sample = 10.6", round to 10

The best rate we can do is 10" in 1.2s, or 8.33 "/s, round to 8"/s

One other subtle change from the proposal is that we are now including H2C18O
and the 12.1 GHz CH3OH maser line instead of some of the RRLs.
