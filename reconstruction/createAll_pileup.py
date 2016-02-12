import os
import sys

if __name__ == '__main__':
    SHIFT = 0
    NTOYS = 100
    #NSAMPLE_NFREQ = [ (10, 25), (20, 12.5), (40, 6.25) ]
    NSAMPLE_NFREQ = [ (20, 12.5) ]
    AMPLITUDE = 10.0
    NPUS = range(0, 201, 10)

    dryrun = 0
    if len(sys.argv) > 1 :
      print " dry run option:",
      dryrun = sys.argv[1]
      print dryrun
 
    for n_pu in NPUS:
      for (n_sample, n_freq) in NSAMPLE_NFREQ:
	toExec = "bin/CreateData %d %d %d %f %f %f" % (SHIFT, NTOYS, n_sample, n_freq, n_pu, AMPLITUDE)
	print toExec
	if (dryrun == 0) :
	  os.system(toExec)
