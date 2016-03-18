import os
import sys

if __name__ == '__main__':
    SHIFT = 0
    SHIFTS = range(1, 26)
    NTOYS = 1000
    AMPLITUDE = 10.0
    NOISES = [0.0, 0.01, 0.02, 0.03, 0.04, 0.05, 0.06, 0.07, 0.08, 0.09, 0.1]
    #NOISES = []
    NOISE = 0.0
    NPUS = range(0, 201, 10)
    #NPUS = range(1, 10) + [15]
    #NPUS = [0, 20, 40, 100, 200]
    #NPUS = [0, 5, 10, 20, 40, 100, 150, 200]
    #NPUS = [30, 50, 60, 70, 80, 90, 110, 120, 130, 140, 160, 170, 180, 190]
    NPU = 0
    PU_FACTOR = 1.0

    NSAMPLE_NFREQ = [ (10, 25), (20, 12.5), (40, 6.25) ]
    CRRC_WF_NAMES = ["CRRC10", "CRRC20", "CRRC30", "CRRC43", "CRRC60", "CRRC90"]
    QIE_WF_NAMES = ["QIE25", "QIE12", "QIE6"]

    WF_NFREQ_DICT = {wf : NSAMPLE_NFREQ for wf in CRRC_WF_NAMES}
    WF_NFREQ_DICT.update(
        {wf : [NSAMPLE_NFREQ[i]] for i, wf in enumerate(QIE_WF_NAMES)})

    dryrun = 0
    if len(sys.argv) > 1 :
      print " dry run option:",
      dryrun = sys.argv[1]
      print dryrun
 
    for wf_name in QIE_WF_NAMES:# + CRRC_WF_NAMES:
      for (n_sample, n_freq) in WF_NFREQ_DICT[wf_name]:

        for n_pu in NPUS:
          toExec = "bin/CreateData %d %d %d %f %f %f %f %f %s" % (
               SHIFT, NTOYS, n_sample, n_freq, n_pu, AMPLITUDE, NOISE,
               PU_FACTOR, wf_name)
          print toExec
          if (dryrun == 0) :
            os.system(toExec)

        for noise in NOISES:
          toExec = "bin/CreateData %d %d %d %f %f %f %f %f %s" % (
               SHIFT, NTOYS, n_sample, n_freq, NPU, AMPLITUDE, noise,
               PU_FACTOR, wf_name)
          print toExec
          if (dryrun == 0) :
            os.system(toExec)
