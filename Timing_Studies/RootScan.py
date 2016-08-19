import PlotMethodDiff #import other python files by treating like modules
import Plot_ps_sr      
import numpy as np 
import sys
import matplotlib.pyplot as plt
from ROOT import TFile
from glob import glob
from math import sqrt
from sys import argv


def scan(files): 
    
    # Logging information headers 
    
     
    param_names = ["nEvents", "pulse_shift", "pileup_shift", "nSmpl", "nFreq",
                   "amplitudeTruth", "nPU", "sigmaNoise", "puFactor",
                   "pulse_tau", "WFNAME"]
    
    #outputwriter.writerow(param_names + )
    
    #Initializing data lists
    all_x_list = [] # = [file number][list of y values] Contains a list of x values for each file
    all_y_list = [] # = [file number][list of y values] Contains a list of y values for each file
    all_pulse_shift = []  
    all_samplesReco = [] # = [Single samplesReco value,]
    #all_WFNAME = []
    #all_pulse_tau = []

        #Creating List for each waveform
    CRRC10_ps_sr = [] #(ps,sr) = (Pulse_Shift, SamplesReco)
    CRRC20_ps_sr = []
    CRRC30_ps_sr = []
    CRRC43_ps_sr = []
    CRRC50_ps_sr = []
    CRRC60_ps_sr = []
    
    #Creating (x,y) lists in each waveform list
    i=0
    while (i<2):
      CRRC10_ps_sr.append([])
      CRRC20_ps_sr.append([])
      CRRC30_ps_sr.append([])
      CRRC43_ps_sr.append([])
      CRRC50_ps_sr.append([])
      CRRC60_ps_sr.append([])
      i += 1    

    #Creating empty data list for each loop (file)
    print "len(files) = ", len(files)
    for i in range(len(files)+1): #Right now have empty slot in each of these lists for file 0 b/c fi+1 is file index, starts at 1.
      all_x_list.append([])
      all_y_list.append([])  
      all_samplesReco.append([])
      all_pulse_shift.append([])  
      #all_WFNAME.append([])
      #all_pulse_tau.append([])

    print "\nProcessing %d file(s)\n" % len(files)
    
    # Accessing each file f, index fi+1
    for fi, f in enumerate(files):
	# Accessing the file.  
        print "File", fi+1, ":", f  #fi+1 because first i is 0. fi+1=file number, f=file path
        in_file = TFile(f, "Read")
        tree = in_file.Get("RecoAndSim") #tree is RecoAndSim tree in root file
        nEvents = tree.GetEntries() #Defining nEvents as number of entries in RecoAndSim

        # Getting the params from the file
        print "nEvents = ", nEvents
        tree.GetEntry(0) #tree.GetEntry(n) chooses nth event
        params = [nEvents, tree.pulse_shift, tree.pileup_shift,
                  tree.nSmpl, tree.nFreq, tree.amplitudeTruth,
                  tree.nPU, tree.sigmaNoise, tree.puFactor,
                  tree.pulse_tau, tree.WFNAME]

        for name, value in zip(param_names, params): #name,value=x,y
          print '{0:>17}: {1:>5}'.format(name, value)

          #Might be more efficient than out of file append method (right before plotting)
	  #Adding current file's (pulse shape, sample reco) point to correct CRRC list
          #if (tree.pulse_tau == 10):
          #  CRRC10_ps_sr[0].append(tree.pulse_shift)
          #  CRRC10_ps_sr[1].append(tree.samplesReco.at(4))

          #elif (tree.pulse_tau == 20):
          #  CRRC20_ps_sr[0].append(tree.pulse_shift)
          #  CRRC20_ps_sr[1].append(tree.samplesReco.at(4))

          #elif (tree.pulse_tau == 30):
          #  CRRC30_ps_sr[0].append(tree.pulse_shift)
          #  CRRC30_ps_sr[1].append(tree.samplesReco.at(4))

          #elif (tree.pulse_tau == 43):
          #  CRRC43_ps_sr[0].append(tree.pulse_shift)
          #  CRRC43_ps_sr[1].append(tree.samplesReco.at(4))

          #elif (tree.pulse_tau == 50):
          #  CRRC50_ps_sr[0].append(tree.pulse_shift)
          #  CRRC50_ps_sr[1].append(tree.samplesReco.at(4))

         # elif (tree.pulse_tau == 60):
         #   CRRC60_ps_sr[0].append(tree.pulse_shift)
         #   CRRC60_ps_sr[1].append(tree.samplesReco.at(4))

          #print "CRRC i 0 ps sr = ",CRRC10_ps_sr
          #print "CRRC i 0 ps sr = ",CRRC30_ps_sr
          #print "CRRC i 0 ps sr = ",CRRC43_ps_sr
          #print "CRRC i 0 ps sr = ",CRRC60_ps_sr
          #print "system exit"
          #sys.exit(0)

	#Pulse_shift = str(tree.pulse_shift)
        #Nsample = str(tree.nSmpl)
        all_pulse_shift[fi+1].append(tree.pulse_shift)
        all_samplesReco[fi+1].append(tree.samplesReco.at(4))
        #all_WFNAME[fi+1].append(str(tree.WFNAME))
        #all_pulse_tau[fi+1].append(tree.pulse_tau)
	
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
	all_x_list[fi+1] = [] 
	all_y_list[fi+1] = []

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
	i=0
	tree.GetEntry(0)
	while (i<points): 
	  all_x_list[fi+1].append( i * (tree.nFreq) + 25 * 2)
	  all_y_list[fi+1].append(tree.pulseShapeTemplate.at(i) * tree.samplesReco.at(4) - (tree.samples.at(i+skip) - Out_of_Time_RecoSpectrum[i+skip])) #fi+1 = file number. all_y_list[fi+1] contains y values for file fi+1
	  i = i + 1    
	
	print "x_List for file " + str(fi+1) + ": " + str(all_x_list[fi+1])
	print "Difference_y " + str(fi+1) + ": " + str(all_y_list[fi+1])
	print "nSmple for file " + str(fi+1) + ":", tree.nSmpl
        Last_nSmple = tree.nSmpl

        #outputwriter.writerow(params) #Fill row with extracted parameters

        in_file.Close()
    
    #After calculating Difference_y for each file, now want to average y values and create list of (x,average y)
    
    #Average_difference_y = [] #For one averaged set
             #For seven averaged sets
    #Pulse_Shift_List=[]
    
    #for i in range(7):
    #  Pulse_Shift_List.append([])

    #entries=len(all_x_list[1]) #For now, running loop for only one Nsamp/Nfreq, so all files have same x list. Eventually make better.  

    #create average for each pulse_shift set
    #p=6 #average every 'p' files per pulse_shift value
    #q=0 #Begin with Pulse_Shift_List[0]
    #while (p<=42):
    #  for i in range(entries): #'i' loops for 'i' x values
    #    total=0.0
    #    for j in range(0,p):
    #      total += all_y_list[j+1][i]
    #    average_y=total/(len(files))
    #    Pulse_Shift_List[q].append(average_y) 
    #  p=p+6
    #  q=q+1

    #print "all_x_list for file 1 = ", all_x_list[1]
    #print "Pulse_Shift_List[0] = ", Pulse_Shift_List[0]
    #print "Pulse_Shift_List[1] = ", Pulse_Shift_List[1]
    #print "Pulse_Shift_List[2] = ", Pulse_Shift_List[2]
    #print "Pulse_Shift_List[3] = ", Pulse_Shift_List[3]
    #print "Pulse_Shift_List[4] = ", Pulse_Shift_List[4]
    #print "Pulse_Shift_List[5] = ", Pulse_Shift_List[5]
    #print "Pulse_Shift_List[6] = ", Pulse_Shift_List[6] 
    #print "Last_nSmple = ", Last_nSmple

    for fi in range(0,6):
        print "Y list for file " + str(fi+1) + ": ", all_y_list[fi+1]
    #print "samplesreco list = ",all_samplesReco 
    #print "pulse shift list = ",all_pulse_shift
    #print "WFNAME list = ",all_WFNAME 
    #print "Pulse tau list = ",all_pulse_tau
    #print "Pulse shift list = ",all_pulse_shift
    #sys.exit(0)
#----------------------------------------------------------------
    #To get One average
    #for i in range(entries): #Loop to append values for each x value. 'range()' includes 0 
      #total=0.0
      #for j in range(len(files)):      #Average the y's for given x over files
        #total += all_y_list[j+1][i]
      #average_y=total/(len(files))
      #Average_difference_y.append(average_y) 

    #print "all_x_list[1] = ", all_x_list[1]
    #print "Average_difference_y = ", Average_difference_y
#----------------------------------------------------------------  

    #Call plotting functions from other files
    Plot_ps_sr.Plot(Last_nSmple, files, CRRC10_ps_sr, CRRC20_ps_sr, CRRC30_ps_sr, CRRC43_ps_sr, CRRC50_ps_sr, CRRC60_ps_sr, all_pulse_shift, all_samplesReco)
    #PlotMethodDiff.plot(Last_nSmple, all_x_list, all_y_list, Pulse_Shift_List)

if __name__ == "__main__":
    
    args = [] #Creating a list
    # for loop that converts arguments with a '*' to the corresponding files
    for arg in argv[1:]:  #For arguments argv[1] and following
        args += glob(arg) #Search for and add all * files to args
    scan(args)            #Runs 'scan' definition with files=args 
