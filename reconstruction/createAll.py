# Convenience script to call CreateData.C with many different inputs.
# CreateData requires the existance of an input/ directory to run:
# % mkdir input
# To use this script, you must first compile CreateData.C into a bin/ directory:
# % mkdir bin
# % g++ -O3 -o bin/CreateData reconstruction/CreateData.C -Wl,--no-as-needed -lHist -lCore -lMathCore *not sure if core lowercase or uppercase C* -std=c++11 `root-config --cflags --glibs`
# % python createAll.py

import os  #imports os module, used here for os.system(toExec)
import sys #imports sys module, used here for sys.argv

if __name__ == '__main__':  #I believe this executes program only when directly run, not when called in another file.
    # number of events to simulate for each configuration
    NTOYS = 100

    # Currently we use 10 GeV events and no scale factor for pileup.
    AMPLITUDE = 10.0
    PU_FACTOR = 1.0

    # For the parameters pileup_shift, pulse_shift, nPU, and sigmaNoise, we
    # specify a list of values to use while holding other parameters constant
    # as well as a single value to use while varying other parameters.
    # Supplying an empty list will skip the loop where that parameter is varied.
    # If all lists are empty, CreateData will not be called at all.
    # More combinations of parameters can be used by altering the loop
    # structure below.
    PILEUP_SHIFT = 0 #Single value while varying other parameters
    PILEUP_SHIFTS = [0, 0.5, 1, 5]  
    PULSE_SHIFT = 0
    PULSE_SHIFTS = []
    NOISE = 0.0
    NOISES = [0,0.01,0.02,0.05,0.1]
    NPU = 0
    NPUS = [0, 20, 40, 100, 200]

    # We only use combinations of NSAMPLE and NFREQ that give a total sampling
    # period of 250 ns.
    NSAMPLE_NFREQ = [ (10, 25), (20, 12.5), (40, 6.25)] #nanoseconds

    # "CRRCXX" refers to a CR-RC pulse with time constant tau = XX.
    # CRRC pulse shaping is compatible with all sampling rates.
    CRRC_WF_NAMES = ["CRRC10", "CRRC20", "CRRC30", "CRRC60", "CRRC43", "CRRC90"]
    WF_NFREQ_DICT = {wf : NSAMPLE_NFREQ for wf in CRRC_WF_NAMES}

    QIE_WF_NAMES = ["QIE25", "QIE12", "QIE6"]
    WF_NFREQ_DICT.update(
        {wf : [NSAMPLE_NFREQ[i]] for i, wf in enumerate(QIE_WF_NAMES)})

    dryrun = 0
    if len(sys.argv) > 1 :
      print " dry run option:",
      dryrun = sys.argv[1]
      print dryrun
 
    for wf_name in QIE_WF_NAMES + CRRC_WF_NAMES:
      for (n_sample, n_freq) in WF_NFREQ_DICT[wf_name]:

        # loop through the desired combinations of pulse_shift and pileup_shift
        # while holding the other parameters constant at specific values
        for pulse_shift in PULSE_SHIFTS:
          for pileup_shift in PILEUP_SHIFTS:
            toExec = "bin/CreateData %f %d %d %f %f %f %f %f %s %f" % (
                 pulse_shift, NTOYS, n_sample, n_freq, NPU, AMPLITUDE, NOISE,
                 PU_FACTOR, wf_name, pileup_shift)
            print toExec
            if (dryrun == 0) :
              os.system(toExec) #Calls bin/CreateData

        # loop through the desired numbers of pileup events
        # while holding the other parameters constant at specific values
        for n_pu in NPUS:
          toExec = "bin/CreateData %f %d %d %f %f %f %f %f %s %f" % (
               PULSE_SHIFT, NTOYS, n_sample, n_freq, n_pu, AMPLITUDE, NOISE,
               PU_FACTOR, wf_name, PILEUP_SHIFT)
          print toExec
          if (dryrun == 0) :
            os.system(toExec)

        # loop through the desired values of sigmaNoise
        # while holding the other parameters constant at specific values
        for noise in NOISES:
          toExec = "bin/CreateData %f %d %d %f %f %f %f %f %s %f" % (
               PULSE_SHIFT, NTOYS, n_sample, n_freq, NPU, AMPLITUDE, noise,
               PU_FACTOR, wf_name, PILEUP_SHIFT)
          print toExec
          if (dryrun == 0) :
            os.system(toExec)

