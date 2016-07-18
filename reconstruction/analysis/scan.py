import csv
from ROOT import TFile
from glob import glob
from math import sqrt
from sys import argv


def main(files, outfile_name="results.csv", in_time_bx=4):

    # Output csv file
    outputfile = open(outfile_name, 'w')
    outputwriter = csv.writer(outputfile)

    # Logging information headers used for writing to output file
    param_names = ["nEvents", "pulse_shift", "pileup_shift", "nSmpl", "nFreq",
                   "amplitudeTruth", "nPU", "sigmaNoise", "puFactor",
                   "pulse_tau", "WFNAME", "in_time_bx"]
    reco_stat_names  = ["avg_reco_amplitude", "sigma_eff", "sigma_eff_err"]
    outputwriter.writerow(param_names + reco_stat_names)

    # Accessing each file and making the histograms
    print "\nProcessing %d file(s)\n" % len(files)
    for i, f in enumerate(files):

        # Accessing the file
        print "File", i+1, ":", f
        in_file = TFile(f, "Read")
        tree = in_file.Get("RecoAndSim")
        nEvents = tree.GetEntries()

        # Getting the params for the file
        tree.GetEntry(0)
        params = [nEvents, tree.pulse_shift, tree.pileup_shift,
                  tree.nSmpl, tree.nFreq, tree.amplitudeTruth,
                  tree.nPU, tree.sigmaNoise, tree.puFactor,
                  tree.pulse_tau, tree.WFNAME, in_time_bx]

        for name, value in zip(param_names, params):
          print '{0:>17}: {1:>5}'.format(name, value)

        # Getting the reconstructed amplitudes
        reco_list = []
        for event in range(nEvents):
            tree.GetEntry(event)
            reco_list.append(tree.samplesReco.at(in_time_bx))

        # calculate uncertainty
        reco_stats = mean_sigma_eff(reco_list)

        for name, value in zip(reco_stat_names, reco_stats):
            print '{0:>17}: {1:>11}'.format(name, value)

        outputwriter.writerow(params + reco_stats)

        in_file.Close()

    outputfile.close()

# Takes in a list and calculates the effective sigma, the windowed
# range which contains 68% of the data (one sigma). Returns a tuple 
# containing (sigma, sigma_error).
def mean_sigma_eff(amp_list):      
    amp_list = sorted(amp_list) #orders values from least to greatest
    n_entries = len(amp_list)

    mean = sum(amp_list) / n_entries #calculates average amplitude value

    one_sigma = 0.68 * n_entries    #68% of entries value. Maybe use .682? or .682689492?

    last_start_value, last_end_value = amp_list[-1], amp_list[0]  #element -1 is last element
    window_size = last_start_value - last_end_value               #element 0 is first element
   
    #window_size is the range of values
    #Loops test 
    for start_index in range(0, n_entries - 1): 
        found_window = False
        start_value = amp_list[start_index]
        sum_in_range = 0
        for end_index in range(start_index, n_entries):
            end_value = amp_list[end_index]
            sum_in_range += 1
            if (sum_in_range >= one_sigma) and \
               (end_value - start_value < window_size):  
                found_window = True
                last_start_value, last_end_value = start_value, end_value
                window_size = last_end_value - last_start_value
                break    
        if not found_window:
            # No window was found so we can drop out of the outer loop
            break

    print "Window size of %f, between (%f, %f)." % (
         window_size, last_start_value, last_end_value)


    sigma = window_size / 2.0
    if n_entries > 1:
      sigma_err = sigma / sqrt(2.0*(n_entries - 1.0))
    else:
      sigma_err = 0

    return [mean, sigma, sigma_err]

if __name__ == "__main__":
    
    args = []
    # for loop that converts arguments with a '*' to the corresponding files
    for arg in argv[1:]:
        args += glob(arg)
    main(args)
