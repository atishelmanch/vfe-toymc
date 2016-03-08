import os
import sys

if __name__ == '__main__':
    SHIFT = 0
    SHIFTS = range(1, 26)
    NTOYS = 1000
    NSAMPLE_NFREQ = [ (10, 25), (20, 12.5), (40, 6.25) ]
    #NSAMPLE_NFREQ = [ (20, 12.5) ]
    #NSAMPLE_NFREQ = [ (10, 25), (40, 6.25) ]
    AMPLITUDE = 10.0
    #AMPLITUDE = 100.0
    NOISE = 0.0
    NOISES = [0.0, 0.01, 0.02, 0.03, 0.04, 0.05, 0.06, 0.07, 0.08, 0.09, 0.1]
    #NPUS = range(0, 201, 10)
    #NPUS = range(1, 10) + [15]
    NPUS = [0, 5, 10, 20, 40, 100, 150, 200]
    NPU = 0
    #NPUS = [0, 20, 40, 100, 200]
    PU_FACTOR = 1.0

    WF_NAMES = ["CRRC10", "CRRC20", "CRRC30", "CRRC43", "CRRC60", "CRRC90"]

    dryrun = 0
    if len(sys.argv) > 1 :
      print " dry run option:",
      dryrun = sys.argv[1]
      print dryrun
 
    for n_pu in NPUS:
      for (n_sample, n_freq) in NSAMPLE_NFREQ:
        for wf_name in WF_NAMES:
          toExec = "bin/CreateData %d %d %d %f %f %f %f %f %s" % (
               SHIFT, NTOYS, n_sample, n_freq, n_pu, AMPLITUDE, NOISE,
               PU_FACTOR, wf_name)
          print toExec
          if (dryrun == 0) :
            os.system(toExec)

    for noise in NOISES:
      for (n_sample, n_freq) in NSAMPLE_NFREQ:
        for wf_name in WF_NAMES:
          toExec = "bin/CreateData %d %d %d %f %f %f %f %f %s" % (
               SHIFT, NTOYS, n_sample, n_freq, NPU, AMPLITUDE, noise,
               PU_FACTOR, wf_name)
          print toExec
          if (dryrun == 0) :
            os.system(toExec)
