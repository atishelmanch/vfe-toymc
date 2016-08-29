#
# Abraham Tishelman-Charny
# Northeastern University High Energy Physics
# August 2016
#
# The purpose of this file is to scan root files for parameters, and create lists of values of interest.
# Plotting is done with imported python files.

# Import other python files by treating like modules
import PlotMethodDiff 
import Plot_ps_sr
import Plot_ps_diff 
import Plot_True_Pulse 
import Plot_oot   

# Import necessary modules
import sys  # To use sys.exit(0)
from sys import argv
from ROOT import TFile
from glob import glob
from math import sqrt
import numpy as np 
import matplotlib.pyplot as plt

def scan(files): 
    
    # Logging information headers 
    param_names = ["nEvents", "pulse_shift", "pileup_shift", "nSmpl", "nFreq",
                   "amplitudeTruth", "nPU", "sigmaNoise", "puFactor",
                   "pulse_tau", "WFNAME"]
     
    # Creating data lists
    all_x_list = [] # = [file number][list of x values] Contains a list of x values for each file
    all_y_list = [] # = [file number][list of y values] Contains a list of y values for each file
    all_Met1_x = []
    all_Met1_y = [] # Method 1 y values for each file number
    all_Met2_x = []
    all_Met2_y = [] # Method 2 y values for each file number
    all_True_Pulse_x = [] # = [file number][list of x values]
    all_True_Pulse_y = [] # = [file number][list of y values]
    all_Met1_min_TrueP = [] # = [file number][list of y values]
    all_Met2_min_TrueP = [] # = [file number][list of y values]
    #all_WFNAME = []
    #all_pulse_tau = []
    
    # Creating Met 1 List for each waveform
    #CRRC10_met1 = [] #(x,y) = (met1_x, met1_y)
    #CRRC20_met1 = []
    #CRRC30_met1 = []
    #CRRC43_met1 = []
    #CRRC60_met1 = []
    #CRRC90_met1 = []

    # Creating Met 2 List for each waveform
    #CRRC10_met2 = [] #(x,y) = (met2_x, met2_y)
    #CRRC20_met2 = []
    #CRRC30_met2 = []
    #CRRC43_met2 = []
    #CRRC60_met2 = []
    #CRRC90_met2 = []

    # Creating True List for each waveform
    #CRRC10_True = [] #(x,y) = (met_x, met2_y)
    #CRRC20_True = []
    #CRRC30_True = []
    #CRRC43_True = []
    #CRRC60_True = []
    #CRRC90_True = []

    # Creating List for each waveform
    CRRC10_ps_sr = [] #(ps,sr) = (Pulse_Shift, SamplesReco)
    CRRC20_ps_sr = []
    CRRC30_ps_sr = []
    CRRC43_ps_sr = []
    CRRC60_ps_sr = []
    CRRC90_ps_sr = []

    # (x,y) = (pulse shift, samplesReco-amplitudetruth)
    CRRC10_ps_diff = []
    CRRC20_ps_diff = []
    CRRC30_ps_diff = []
    CRRC43_ps_diff = []
    CRRC60_ps_diff = []
    CRRC90_ps_diff = []

    Out_of_Time_amp_10 = []
    Out_of_Time_amp_20 = []
    Out_of_Time_amp_30 = []
    Out_of_Time_amp_43 = []
    Out_of_Time_amp_60 = []
    Out_of_Time_amp_90 = []

    # Creating (x,y) in each waveform list, for each file
    i=0
    while (i<len(files)+1):
      CRRC10_ps_sr.append([])
      CRRC20_ps_sr.append([])
      CRRC30_ps_sr.append([])
      CRRC43_ps_sr.append([])
      CRRC60_ps_sr.append([])
      CRRC90_ps_sr.append([])
      # (x,y) = (pulse shift, samplesReco-amplitudetruth)
      CRRC10_ps_diff.append([])
      CRRC20_ps_diff.append([])
      CRRC30_ps_diff.append([])
      CRRC43_ps_diff.append([])
      CRRC60_ps_diff.append([])
      CRRC90_ps_diff.append([])
      
      Out_of_Time_amp_10.append([])
      Out_of_Time_amp_20.append([])
      Out_of_Time_amp_30.append([])
      Out_of_Time_amp_43.append([])
      Out_of_Time_amp_60.append([])
      Out_of_Time_amp_90.append([])
      #CRRC10_met1.append([]) #Might have to do one noise per set of files
      #CRRC20_met1.append([])
      #CRRC30_met1.append([])
      #CRRC43_met1.append([])
      #CRRC60_met1.append([])
      #CRRC90_met1.append([])
      #CRRC10_met2.append([])
      #CRRC20_met2.append([])
      #CRRC30_met2.append([])
      #CRRC43_met2.append([])
      #CRRC60_met2.append([])
      #CRRC90_met2.append([])
      #CRRC10_True.append([])
      #CRRC20_True.append([])
      #CRRC30_True.append([])
      #CRRC43_True.append([])
      #CRRC60_True.append([])
      #CRRC90_True.append([])
      i += 1    

    # Creating empty data list for each loop (file)
    for i in range(len(files)+1): #Right now have empty slot in each of these lists for file 0 b/c fi+1 is file index, starts at 1.
      all_x_list.append([]) # = [file number][list of y values] Contains a list of x values for each file
      all_y_list.append([])  
      #all_Met1_x.append([]) # Method 1 x values for each file number
      #all_Met1_y.append([]) # Method 1 y values for each file number
      #all_Met2_x.append([]) # Method 2 x values for each file number 
      #all_Met2_y.append([]) # Method 2 y values for each file number
      #all_True_Pulse_x.append([])
      #all_True_Pulse_y.append([])
      #all_Met1_min_TrueP.append([]) # = [file number][list of y values]
      #all_Met2_min_TrueP.append([]) # = [file number][list of y values] 

      #all_WFNAME.append([])
      #all_pulse_tau.append([])

    #Out_of_Time_amp = []
    #for i in range(len(files)+1):
    #  Out_of_Time_amp.append([])

    # Let the user know that files are about to be accessed 
    print "\nProcessing %d file(s)\n" % len(files)
    
    # Accessing each file f, index fi+1
    for fi, f in enumerate(files):
	# Accessing the file.  
        print "File", fi+1, ":", f  #fi+1 because first i is 0. fi+1=file number, f=file path
        in_file = TFile(f, "Read")
        tree = in_file.Get("RecoAndSim") # Tree is RecoAndSim tree in root file
        nEvents = tree.GetEntries() # Defining nEvents as number of entries in RecoAndSim

        # Getting the params from the file
        print "nEvents = ", nEvents
        tree.GetEntry(0) #tree.GetEntry(n) chooses nth event
        params = [nEvents, tree.pulse_shift, tree.pileup_shift,
                  tree.nSmpl, tree.nFreq, tree.amplitudeTruth,
                  tree.nPU, tree.sigmaNoise, tree.puFactor,
                  tree.pulse_tau, tree.WFNAME]

        for name, value in zip(param_names, params): #name,value=x,y
          print '{0:>17}: {1:>5}'.format(name, value)

        # Extracting pulse shift and in-time samples Reco for each file.
        # Before plotting, empty elements are removed.

        if (tree.pulse_tau == 10):
          CRRC10_ps_sr[fi+1].append(tree.pulse_shift)
          CRRC10_ps_sr[fi+1].append(tree.samplesReco.at(4))

        elif (tree.pulse_tau == 20):
          CRRC20_ps_sr[fi+1].append(tree.pulse_shift)
          CRRC20_ps_sr[fi+1].append(tree.samplesReco.at(4))

        elif (tree.pulse_tau == 30):
          CRRC30_ps_sr[fi+1].append(tree.pulse_shift)
          CRRC30_ps_sr[fi+1].append(tree.samplesReco.at(4))

        elif (tree.pulse_tau == 43):
          CRRC43_ps_sr[fi+1].append(tree.pulse_shift)
          CRRC43_ps_sr[fi+1].append(tree.samplesReco.at(4))

        elif (tree.pulse_tau == 60):
          CRRC60_ps_sr[fi+1].append(tree.pulse_shift)
          CRRC60_ps_sr[fi+1].append(tree.samplesReco.at(4))

        elif (tree.pulse_tau == 90):
          CRRC90_ps_sr[fi+1].append(tree.pulse_shift)
          CRRC90_ps_sr[fi+1].append(tree.samplesReco.at(4))

        # Below is for y = diff = samplesreco-amplitudetruth

        if (tree.pulse_tau == 10):
          CRRC10_ps_diff[fi+1].append(tree.pulse_shift)
          CRRC10_ps_diff[fi+1].append(tree.samplesReco.at(4)-tree.amplitudeTruth)
          Out_of_Time_amp_10[fi+1].append(tree.pulse_shift) 
          Out_of_Time_amp_10[fi+1].append(tree.samplesReco.at(3))  #reco range(0,9)

        elif (tree.pulse_tau == 20):
          CRRC20_ps_diff[fi+1].append(tree.pulse_shift)
          CRRC20_ps_diff[fi+1].append(tree.samplesReco.at(4)-tree.amplitudeTruth)
          Out_of_Time_amp_20[fi+1].append(tree.pulse_shift) 
          Out_of_Time_amp_20[fi+1].append(tree.samplesReco.at(3))

        elif (tree.pulse_tau == 30):
          CRRC30_ps_diff[fi+1].append(tree.pulse_shift)
          CRRC30_ps_diff[fi+1].append(tree.samplesReco.at(4)-tree.amplitudeTruth)
          Out_of_Time_amp_30[fi+1].append(tree.pulse_shift) 
          Out_of_Time_amp_30[fi+1].append(tree.samplesReco.at(3))

        elif (tree.pulse_tau == 43):
          CRRC43_ps_diff[fi+1].append(tree.pulse_shift)
          CRRC43_ps_diff[fi+1].append(tree.samplesReco.at(4)-tree.amplitudeTruth)
          Out_of_Time_amp_43[fi+1].append(tree.pulse_shift) 
          Out_of_Time_amp_43[fi+1].append(tree.samplesReco.at(3))

        elif (tree.pulse_tau == 60):
          CRRC60_ps_diff[fi+1].append(tree.pulse_shift)
          CRRC60_ps_diff[fi+1].append(tree.samplesReco.at(4)-tree.amplitudeTruth)
          Out_of_Time_amp_60[fi+1].append(tree.pulse_shift) 
          Out_of_Time_amp_60[fi+1].append(tree.samplesReco.at(3))

        elif (tree.pulse_tau == 90):
          CRRC90_ps_diff[fi+1].append(tree.pulse_shift)
          CRRC90_ps_diff[fi+1].append(tree.samplesReco.at(4)-tree.amplitudeTruth)
          Out_of_Time_amp_90[fi+1].append(tree.pulse_shift) 
          Out_of_Time_amp_90[fi+1].append(tree.samplesReco.at(3))

	#Defining OOT RecoSpectrum for each file. Need to change 'NewtotalRecoSpectrum' in PlotPulses.C
	Out_of_Time_RecoSpectrum = [0]*50
	
	for iBx in range(0,len(tree.samplesReco)):
	  #print "iBx = ", iBx	
	  if iBx==4: 
	    continue #skips in time bunch crossing
	  for i in range(0,len(tree.samples)): 
	    #print "i = ", i 
	    iReco_f=((i * tree.nFreq + tree.activeBXs.at(iBx) * tree.nFreq + 2.0 * 25.0) / (tree.nFreq) ) #why?
	    iReco=int(iReco_f)	
	    #print "iReco = ", iReco
	    if (iReco>=0 and iReco < len(tree.samples)):
	      #print "Conditions met."
	      #print "tree.pulseShapeTemplate.at("+str(i)+") = ",tree.pulseShapeTemplate.at(i)
	      #print "tree.samplesReco.at("+str(iBx)+") = ",tree.samplesReco.at(iBx)
	      for x, y in enumerate(Out_of_Time_RecoSpectrum):
                if x == iReco:
                  Out_of_Time_RecoSpectrum[x]+=(tree.pulseShapeTemplate.at(i) * tree.samplesReco.at(iBx))
          
	#print "Out_of_Time_RecoSpectrum = %s" % ", ".join(map(str, Out_of_Time_RecoSpectrum))
  	

	
        #initializing data sets for Pulse Representation Difference data.
	#all_x_list[fi+1] = [] #are these necessary? 
	#all_y_list[fi+1] = [] 

	#Setting parameters skip, points based on nsamp/nfreq
	#Depending on samp/freq, different number of points on pulse representation graph
	#Each all_y_list=[fi+1] will have accurate x data based on file traits nSmpl,nFreq

	if (tree.nSmpl == 10):   #(nSmpl,nFreq) = (10,25)
 	   skip = 2
 	   points = 8
 	
 	elif (tree.nSmpl == 20): #(nSmpl,nFreq) = (20,12.5)
 	   skip = 4
 	   points = 16
 	
 	elif (tree.nSmpl == 40): #(nSmpl,nFreq) = (40,6.25)
 	   skip = 8
 	   points = 32 	

	#Extract x,y based on file parameters
	i = 0
	tree.GetEntry(0)
	while (i<points): 
	  all_x_list[fi+1].append( i * (tree.nFreq) + 25 * 2)
	  all_y_list[fi+1].append(tree.pulseShapeTemplate.at(i) * tree.samplesReco.at(4) - (tree.samples.at(i+skip) - Out_of_Time_RecoSpectrum[i+skip])) #fi+1 = file number. all_y_list[fi+1] contains y values for file fi+1
	  i += 1   
	
	print "x_List for file " + str(fi+1) + ": " + str(all_x_list[fi+1])
	print "Difference_y " + str(fi+1) + ": " + str(all_y_list[fi+1])
	print "nSmple for file " + str(fi+1) + ":", tree.nSmpl
        Last_nSmple = tree.nSmpl
        Last_trueamp = tree.amplitudeTruth

        # Extracting the Met1, Met2 data
        #i = 0
        #while (i<points):
          #all_Met1_x[fi+1].append(i * (tree.nFreq) + tree.activeBXs.at(4) * (tree.nFreq) + 2 * 25) 
          #all_Met1_y[fi+1].append(tree.pulseShapeTemplate.at(i) * tree.samplesReco.at(4)) 
          #all_Met2_x[fi+1].append(i * (tree.nFreq)) 
          #all_Met2_y[fi+1].append(tree.samples.at(i) - Out_of_Time_RecoSpectrum[i]) 
          #all_True_Pulse_x[fi+1].append(i * tree.nFreq)
          #print "i - tree.pulse_Shift = ", i - tree.pulse_shift
          #all_True_Pulse_y[fi+1].append(tree.amplitudeTruth * tree.pulseShapeTemplate.at(i-int(tree.pulse_shift)))
          #i += 1
        #print "al met1x[1]:", all_Met1_x[1]
        #print "al met1y[1]:", all_Met1_y[1]
        #print "al met2x[1]:", all_Met2_x[1]
        #print "al met2y[1]:", all_Met2_y[1]
        #print "al true x[1]:", all_True_Pulse_x[1]
        #print "al true y[1]:", all_True_Pulse_y[1]
        #outputwriter.writerow(params) #Fill row with extracted parameters

        in_file.Close() #Close file being read
    
    # After calculating Difference_y for each file, now want to average y values and create list of (x,average y)
    
    #Average_difference_y = [] #For one averaged set
             #For seven averaged sets

    #Pulse_Shift_List=[]
    #for i in range(21): # Range(number of pulse_shift values) 
    #  Pulse_Shift_List.append([])

    #entries=len(all_x_list[1]) #For now, running loop for only one Nsamp/Nfreq, so all files have same x list. Eventually make better.  

    # Create average for each pulse_shift set
    #p=6 #average every 'p' files per pulse_shift value. p = number of waveforms
    #q=0 #Begin with Pulse_Shift_List[0]
    #while (p<=126):  # While p <= 
    #  for i in range(entries): #'i' loops for 'i' x values
    #    total=0.0
    #    for j in range(0,p):
    #      total += all_y_list[j+1][i]
    #    average_y=total/(len(files))
    #    Pulse_Shift_List[q].append(average_y) 
    #  p=p+6
    #  q=q+1

    #print "all_x_list for file 1 = ", all_x_list[1]
    #print "Pulse_Shift_List[20] = ", Pulse_Shift_List[20]
    #print "Pulse_Shift_List[1] = ", Pulse_Shift_List[1]
    #print "Pulse_Shift_List[2] = ", Pulse_Shift_List[2]
    #print "Pulse_Shift_List[3] = ", Pulse_Shift_List[3]
    #print "Pulse_Shift_List[4] = ", Pulse_Shift_List[4]
    #print "Pulse_Shift_List[5] = ", Pulse_Shift_List[5]
    #print "Pulse_Shift_List[6] = ", Pulse_Shift_List[6] 
    #print "Last_nSmple = ", Last_nSmple

    #for fi in range(0,6):
    #    print "Y list for file " + str(fi+1) + ": ", all_y_list[fi+1]
    
    # Ask user what they want to plot
    print "Which would you like to Plot? (select one)"
    print "SamplesReco (sr)"
    print "SamplesReco - AmplitudeTruth (diff)"
    print "Out of Time (oot)"
    name = raw_input()

    # Call plotting functions from other files
    if (name == "sr"):
      Plot_ps_sr.Plot(Last_nSmple, Last_trueamp, files, CRRC10_ps_sr, CRRC20_ps_sr, CRRC30_ps_sr, CRRC43_ps_sr, CRRC60_ps_sr, CRRC90_ps_sr)
    elif (name == "diff"):
      Plot_ps_diff.Plot(Last_nSmple, Last_trueamp, files, CRRC10_ps_diff, CRRC20_ps_diff, CRRC30_ps_diff, CRRC43_ps_diff, CRRC60_ps_diff, CRRC90_ps_diff)
    elif (name == "oot"):
      Plot_oot.Plot(Last_nSmple, Last_trueamp, Out_of_Time_amp_10, Out_of_Time_amp_20, Out_of_Time_amp_30, Out_of_Time_amp_43, Out_of_Time_amp_60, Out_of_Time_amp_90)

    #PlotMethodDiff.plot(Last_nSmple, all_x_list, all_y_list, Pulse_Shift_List)
    #Plot_True_Pulse.Plot(files, Last_nSmple, all_True_Pulse_x, all_True_Pulse_y, all_Met1_x, all_Met1_y, all_Met2_x, all_Met2_y)
if __name__ == "__main__":
    
    args = []             # List of input aguments
    for arg in argv[1:]:  # For arguments argv[1] and following,
        args += glob(arg) # Search for and add all * files to args
    scan(args)            # Runs 'scan' function with files=args 
