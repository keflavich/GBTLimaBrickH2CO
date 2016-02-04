We experienced some major startup problems that lead to the loss of 1.25h of
telescope time.  These errors were triggered by an incorrect VEGAS
configuration file that was not caught as part of the ASTRID syntax-checking:

1. The configuration had both dopplertrackfreq and the rest frequencies of many
   lines in GHz instead of MHz.  This lead to some minor warnings but no error
   when run by ASTRID.  However, because the configuration failed to complete
   (silently), future observing commands (e.g., "slew") also failed.
2. The 1080 MHz bandwidth mode with nchan=high is incompatible with either the
   23.44 MHz bandwidth mode or tint = 0.5s, it is not clear which.  It is also
   possible that 1080 + nchan=high is not allowed.
3. When the configuration fails, "slew" and other commands that are related to
   observing sources prompt for an immediate abort.   There was no error
   message related to VEGAS having failed to configure
