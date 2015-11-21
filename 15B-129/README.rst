CMZ-East GBT Mapping Observations Setup
=======================================

For proposals GBT15B-129



Observing Setup & Instructions for November 2015
------------------------------------------------

Log in at least 30 minutes prior to observations

 1. `ssh username@stargate.gb.nrao.edu`
 2. From stargate, `ssh titania`
 3. Start a VNC server: `vncserver -geometry 1440x860` (for example)
 4. SSH tunnel: `ssh -N -C -L 590n:HOSTNAME1.gbt.nrao.edu:590n USERNAME@HOSTNAME2.gb.nrao.edu`
 5. Start up the VNC client locally 
 6. Start `cleo &`
 7. Start `astrid &`
 8. Load session `AGBT15B_129`
 9. Enter your name and the obs-spec's name in the queue tab
 10. Once the obs-spec has given you permission, activate your astrid session
 11. Run the `autopeakfocus_Ku_15B-129.py <autopeakfocus_Ku_15B-129.py>`_ script
 12. Run one of the mapping scripts:

   * `Ku_Map_15B-129_lat_1.py <Ku_Map_15B-129_lat_1.py>`_
   * `Ku_Map_15B-129_lat_2.py <Ku_Map_15B-129_lat_2.py>`_
   * `Ku_Map_15B-129_lon_1.py <Ku_Map_15B-129_lon_1.py>`_
   * `Ku_Map_15B-129_lon_2.py <Ku_Map_15B-129_lon_2.py>`_

     These have expected execution times ~60 minutes, with either 45 or 36
     scans of length 36 or 45 seconds, respectively.  Every 4th scan will be
     followed by a nod to an off position.  Integration times are 0.5 seconds,
     so there should be 72 or 90 integrations per successful scan.


Important Links
~~~~~~~~~~~~~~~
List of links:

 * `Guidelines for Balancing <http://www.gb.nrao.edu/gbt/support/pdf/balancing-presentation.pdf>`_
 * `GBT Observers Guide <https://science.nrao.edu/facilities/gbt/observing/GBTog.pdf>`_
 * `Remote Observing site <https://science.nrao.edu/facilities/gbt/observing/remote-observing-with-the-gbt>`_
 * `GBT Schedule <https://dss.gb.nrao.edu/schedule/public>`_
 * `GBT High-Frequency Weather <http://www.gb.nrao.edu/~rmaddale/Weather/AllOverviews.html>`_
 * `GBT Remote Login (from CU's CASA:radio group) <http://code.google.com/p/casaradio/wiki/GBTRemoteLogin>`_

