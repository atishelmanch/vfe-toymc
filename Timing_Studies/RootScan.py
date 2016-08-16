import csv
import numpy as np
import matplotlib 
import sys
#matplotlib.use('Agg') #Need this to save plot image
import matplotlib.pyplot as plt
from ROOT import TFile
from glob import glob
from math import sqrt
from sys import argv


def scan(files): #, outfile_name="RootScan.csv"): #args becomes files

    # Output csv file
    #outputfile = open(outfile_name, 'w')  #open outfile_name in write mode (erases existing content)
    #outputwriter = csv.writer(outputfile)

    # Logging information headers used for writing to output file
    param_names = ["nEvents", "pulse_shift", "pileup_shift", "nSmpl", "nFreq",
                   "amplitudeTruth", "nPU", "sigmaNoise", "puFactor",
                   "pulse_tau", "WFNAME"]
    DigiDifference_parameters  = ["DigiDifference_x", "DigiDifference_y"]
    #outputwriter.writerow(param_names + DigiDifference_parameters)
    
    #Initializing data lists
    all_difference_y_list=[]

    #Creating empty data list for each loop
    for i in range(50):
      all_difference_y_list.append([])    

    # Accessing each file f, index fi+1
    print "\nProcessing %d file(s)\n" % len(files)
    #sys.exit(0) #exit program
    for fi, f in enumerate(files):
	# Accessing the file.  
        print "File", fi+1, ":", f  #fi+1 because first i is 0. fi+1=file number, f=file path
        in_file = TFile(f, "Read")
        tree = in_file.Get("RecoAndSim") #tree is RecoAndSim tree in root file
        nEvents = tree.GetEntries() #Defining nEvents as number of entries in RecoAndSim

        # Getting the params from the file
        print "nEvents = ", nEvents
        tree.GetEntry(0)
        params = [nEvents, tree.pulse_shift, tree.pileup_shift,
                  tree.nSmpl, tree.nFreq, tree.amplitudeTruth,
                  tree.nPU, tree.sigmaNoise, tree.puFactor,
                  tree.pulse_tau, tree.WFNAME]

        for name, value in zip(param_names, params): #name,value=x,y
          print '{0:>17}: {1:>5}'.format(name, value)

	Pulse_shift = str(tree.pulse_shift)
        Nsample = str(tree.nSmpl)
	
	#Defining NewtotalRecoSpectrum: DIFFERENT FOR EACH FILE!
	NewtotalRecoSpectrum = [0]*50
	
	for iBx in range(0,len(tree.samplesReco)):
	  #print "iBx = ", iBx	
	  if iBx==4: 
	    continue #skips in time bunch crossing
	  for i in range(0,len(tree.samples)): 
	    #print "i = ", i 
	    iReco_f=((i * tree.nFreq + tree.activeBXs.at(iBx) * tree.nFreq + 2.0 * 25.0) / (tree.nFreq) )
	    iReco=int(iReco_f)	
	    #print "iReco = ", iReco
	    if (iReco>=0 and iReco < len(tree.samples)):
	      #print "Conditions met."
	      #print "tree.pulseShapeTemplate.at("+str(i)+") = ",tree.pulseShapeTemplate.at(i)
	      #print "tree.samplesReco.at("+str(iBx)+") = ",tree.samplesReco.at(iBx)
	      for x, y in enumerate(NewtotalRecoSpectrum):
                if x == iReco:
                  NewtotalRecoSpectrum[x]+=(tree.pulseShapeTemplate.at(i) * tree.samplesReco.at(iBx))
          
	print "NewtotalRecoSpectrum = %s" % ", ".join(map(str, NewtotalRecoSpectrum))
  	

	
        #initializing data sets for DigiDifference data. DIFFERENT FOR EACH FILE!
	Difference_x = [] #x values same for all
	all_difference_y_list[fi+1] = []

	#Setting parameters based on nsamp/nfreq
	#Depending on samp/freq, different number of points on digitization graph

	if (tree.nSmpl == 10): 
 	   skip = 2
 	   points = 8
 	
 	elif (tree.nSmpl == 20):
 	   skip = 4
 	   points = 16
 	
 	elif (tree.nSmpl == 40):
 	   skip = 8
 	   points = 32
 	
	print ("tree.nSmple = ", tree.nSmpl) 	

	#for each entry extract x,y
	i=0
	tree.GetEntry(0)
	while (i<points): #I think range will need to be changed for nsamp != 10
	  Difference_x.append( i * (tree.nFreq) + 25 * 2)
	  all_difference_y_list[fi+1].append(tree.pulseShapeTemplate.at(i) * tree.samplesReco.at(4) - (tree.samples.at(i+skip) - NewtotalRecoSpectrum[i+skip]))
	  i = i + 1    
	
	print "Difference_x = ", Difference_x
	print "Difference_y" + str(fi+1) + " = " + str(all_difference_y_list[fi+1])
	

        #outputwriter.writerow(params) #Fill row with extracted parameters

        in_file.Close()
    
    #After calculating Difference_y for each file, now want to average y values and create list of (x,average y)
    
    Average_difference_y = []
    entries=len(Difference_x)
   
    for i in range(entries): #Loop to append values for each x value. 'range()' includes 0 
      total=0.0
      for j in range(len(files)):      #Average the y's for given x over files
        total += all_difference_y_list[j+1][i]
      average_y=total/(len(files))
      Average_difference_y.append(average_y) 

    print "Difference_x = ", Difference_x
    print "Average_difference_y = ", Average_difference_y
    
    #Plotting nsmpl/nfrq = 10/25
    plt.figure(1)
    x = Difference_x
    y = Average_difference_y
    plt.title("Old Digitization - New Digitization")
    plt.xlabel("Time (ns)")
    plt.ylabel("Digitization Difference")
    plt.plot(x, y, 'b--', linewidth=5) #First plot on graph
    #plt.plot(y, x, 'r--', linewidth=5) #Second plot on graph 
    plt.show()
    plt.savefig("RootScanPlot.png")

    #Plotting nsmpl/nfrq = 20/12.5
    #plt.figure(2)
    #x = Difference_x
    #y = Average_difference_y
    #plt.title("fdsa")
    #plt.xlabel("Time (ns)")
    #plt.ylabel("Digitization Difference")
    #plt.plot(x, y, 'b--', linewidth=5) #First plot on graph
    #plt.plot(y, x, 'r--', linewidth=5) #Second plot on graph 
    #plt.show()
    #plt.savefig("SecondRootScanPlot.png")

    #Plotting nsmpl/nfrq = 40/6.25
    #plt.figure(2)
    #x = Difference_x
    #y = Average_difference_y
    #plt.title("fdsa")
    #plt.xlabel("Time (ns)")
    #plt.ylabel("Digitization Difference")
    #plt.plot(x, y, 'b--', linewidth=5) #First plot on graph
    #plt.plot(y, x, 'r--', linewidth=5) #Second plot on graph 
    #plt.show()
    #plt.savefig("ThirdRootScanPlot.png")

    #outputfile.close()

if __name__ == "__main__":
    
    args = [] #Creating a list
    # for loop that converts arguments with a '*' to the corresponding files
    for arg in argv[1:]:  #For arguments argv[1] and following
        args += glob(arg) #Search for and add all * files to args
    scan(args)            #Runs 'scan' definition with files=args 
