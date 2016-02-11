from ROOT import *
from glob import glob
from math import sqrt
from sys import argv
import re

""" Accepts a series of root files to be read.
    Input Files are generated by Example07.multifit.cc.
    Returns energy distribution histograms for each input file and a histogram
    ploting RMS of these histograms vs. the various tunable parameters:
    [NSAMPLE, NFREQ, Amplitude, Pileup]


    Examples:
    - With one root file
        $ python plot_energy.py output_file1.root

    - With many root files (you can pass it as many as you want)
        $ python plot_energy.py output_file1.root output_file2.root output_file2.root

    - With many root files, using an asterisk to select them
        $ python plot_energy.py "output_file*.root"
        $ python plot_energy.py "output_file*.root" new_data1.root
        $ python plot_energy.py "output_file*.root" "new_data*.root"
    

    IMPORTANT: When selecting files using the wildcard '*', the filename must
                be surrounded with quotes "" as a string, to protect the
                wildcard from being interpreted by the shell. When passing
                files one at a time with their full names, using quotes or
                not doesn't matter.


    SOURCE: https://github.com/cms-eb-upgrade/vfe-toymc/
"""
def main(files):
    # Output file
    out_file = TFile("energy_error_plots.root", "Recreate")
    # The percent error (out of 1) around the histogram that will be checked
    # Done to weed out the many low energy pileup events (usually < 0.2 GeV)
    ERROR = 0.10
    # The number of bins to use in the histogram
    BINS = 199
    # Starts at 0.5 so thatentries are centered about integers
    MIN_BIN = 0.5

    # Histograms for standard deviations vs. vairous values
    sample_hist = TH1F("StdDev_Sample",
                    "Standard Deviation vs. NSAMPLES for NFREQ=25;\
                    NSAMPLES; Standard Deviation",
                    BINS, MIN_BIN, BINS + MIN_BIN)
    frequency_hist = TH1F("StdDev_Frequency",
                    "Standard Deviation vs. NSAMPLES for NFREQ=25;\
                    NSAMPLES; Standard Deviation",
                    BINS, MIN_BIN, BINS + MIN_BIN)
    amplitude_hist = TH1F("StdDev_Amplitude",
                    "Standard Deviation vs. NSAMPLES for NFREQ=25;\
                    NSAMPLES; Standard Deviation",
                    BINS, MIN_BIN, BINS + MIN_BIN)
    pileup_hist = TH1F("StdDev_PileUp",
                    "Standard Deviation vs. NSAMPLES for NFREQ=25;\
                    NSAMPLES; Standard Deviation",
                    BINS, MIN_BIN, BINS + MIN_BIN)
    hists = [sample_hist, frequency_hist, amplitude_hist, pileup_hist]
    # Boundaries for how to draw the histograms
    # Each pair represents the [lower, upper] bounds, initialized in reverse
    # so they will be overwritten gauranteed  
    hist_bounds = [[1000, 0], [1000, 0], [1000, 0], [1000, 0]]
    # Stat names only for printing out information as the code runs
    stat_names = ["NSAMPLE", "NFREQ", "Amplitude", "Pileup"]

    # Accessing each file and making the histograms
    for i, f in enumerate(files):
        # Accessing the file
        print "File", i+1, ":", f
        in_file = TFile(f, "Read")
        tree = in_file.Get("RecoAndSim")
        events = tree.GetEntries()

        # Getting and checking the stats for the file
        # stats = [NSAMPLE, NFREQ, AMP, PU]
        tree.GetEntry(0)
        # **** Currently energy PU is gotten from the file format. This is to be changed
        # **** once Andrea updates his analysis to include it in the root tree
        # replace the map(int(...)) with: round(tree.energyPU, 2) or tree.whatevertheaddress is
        stats = [round(tree.nSmpl, 2), round(tree.nFreq, 2), 
                round(tree.amplitudeTruth, 2), map(int, re.findall(r'\d+', f))[5]]

        # Energy Distribution from all events
        energy_hist = TH1F("NSAMPLE:"+str(stats[0])+"_NFREQ:"+str(stats[1])+"_AMP:"+str(stats[2])+"_PU:"+str(stats[3]),
                         "Error of Signal Amplitude about True Amplitude; Error (GeV); Frequency",
                          BINS, -ERROR*stats[2], ERROR*stats[2])

        # Filling the energy distribution histograms
        for event in range(0, events):
            tree.GetEntry(event)
            for sample in tree.samplesReco:
                if (sample > (1 - ERROR)*stats[2]):
                    energy_hist.Fill(sample - stats[2])

        # This is where the magic happens, everything else is just bookkeeping
        standard_dev = energy_hist.GetStdDev()
        standard_dev_err = 1.0 / sqrt(2.0*(events - 1.0))*standard_dev
        for hist, bounds, stat, name in zip(hists, hist_bounds, stats, stat_names):
            print " ", name, ":", stat
            # Checking/updating the bound for the histograms
            if (stat < bounds[0]): bounds[0] = stat
            if (stat > bounds[1]): bounds[1] = stat
            # Filling the standard deviation histograms
            hist.SetBinContent(int(stat), standard_dev)
            hist.SetBinError(int(stat), standard_dev_err)
        print "  Standard Deviation:", standard_dev
        print "  Error:", standard_dev_err

        # Writing the energy distribution histogram
        out_file.cd()
        energy_hist.Write()

    # Final formatting and writing of the histograms
    for hist, bounds in zip(hists, hist_bounds):
        hist.GetXaxis().SetRangeUser(bounds[0] - 1, bounds[1] + 1)
        hist.Write()
    out_file.Close()
    in_file.Close()

if __name__ == "__main__":
    
    args = []
    # for loop that converts arguments with a '*' to the corresponding files
    for arg in argv[1:]:
        args += glob(arg)
    print args
    main(args)
    
    