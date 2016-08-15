import csv
from ROOT import TFile
from glob import glob
from math import sqrt
from sys import argv


def main(files, outfile_name="RootScan.csv"): #args becomes files

    # Output csv file
    outputfile = open(outfile_name, 'w')  #open outfile_name in write mode (erases existing content)
    outputwriter = csv.writer(outputfile)

    # Logging information headers used for writing to output file
    param_names = ["nEvents", "pulse_shift", "pileup_shift", "nSmpl", "nFreq",
                   "amplitudeTruth", "nPU", "sigmaNoise", "puFactor",
                   "pulse_tau", "WFNAME"]
    DigiDifference_parameters  = ["DigiDifference_x", "DigiDifference_y"]
    outputwriter.writerow(param_names + DigiDifference_parameters)
    
    #Creating empty list for each loop
    all_difference_y_list=[]

    for i in range(50):
      all_difference_y_list.append([])    

    # Accessing each file f, index fi+1
    print "\nProcessing %d file(s)\n" % len(files)
    for fi, f in enumerate(files):
        
	# Accessing the file.  
        print "File", fi+1, ":", f  #fi+1 because first i is 0. fi+1=file number, f=file path
        in_file = TFile(f, "Read")
        tree = in_file.Get("RecoAndSim") #tree is RecoAndSim tree
        nEvents = tree.GetEntries() #Defining nEvents as number of entries in RecoAndSim

        # Getting the params from the file
        print nEvents
        tree.GetEntry(0)
        params = [nEvents, tree.pulse_shift, tree.pileup_shift,
                  tree.nSmpl, tree.nFreq, tree.amplitudeTruth,
                  tree.nPU, tree.sigmaNoise, tree.puFactor,
                  tree.pulse_tau, tree.WFNAME]

        for name, value in zip(param_names, params): #name,value=x,y
          print '{0:>17}: {1:>5}'.format(name, value)

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
	      #print "ok"
	      #print tree.pulseShapeTemplate.at(i)
	      #print tree.samplesReco.at(iBx)
	      for x, y in enumerate(NewtotalRecoSpectrum):
                if x == iReco:
                  NewtotalRecoSpectrum[x]+=(tree.pulseShapeTemplate.at(i) * tree.samplesReco.at(iBx))
          
	print "NewtotalRecoSpectrum = %s" % ", ".join(map(str, NewtotalRecoSpectrum))
  	

	
        #initializing data sets for DigiDifference data. DIFFERENT FOR EACH FILE!
	Difference_x = [] #x values same for all
	all_difference_y_list[fi+1] = []

	#for each entry extract x,y
	i=0
	tree.GetEntry(0)
	while (i<6): #I think range will need to be changed for nsamp != 10
	  Difference_x.append( i * (tree.nFreq) + 25 * 2)
	  all_difference_y_list[fi+1].append(tree.pulseShapeTemplate.at(i) * tree.samplesReco.at(4) - (tree.samples.at(i+2) - NewtotalRecoSpectrum[i+2]))
	  i = i + 1    
	
	print "Difference_x = ", Difference_x
	print "Difference_y" + str(fi+1) + " = " + str(all_difference_y_list[fi+1])
	

        outputwriter.writerow(params) #Fill row with extracted parameters

        in_file.Close()
    
    #After calculating Difference_y for each file, now want to average y values and create list of (x,average y)
    
    Average_difference_y = []
    entries=len(Difference_x)
    print "len(Difference_x) = ", len(Difference_x)
    print "range(len(Difference_x)) = ", range(len(Difference_x))
    print "range(len(files)) = ", range(len(files))
    print "all_difference_y_list = ", all_difference_y_list[0+1][0]
   
    for i in range(len(Difference_x)):
      total=0.0
      for j in range(len(files)):
        total += all_difference_y_list[j+1][i]
      average_y=total/(len(files))
      Average_difference_y.append(average_y) 

    print "Difference_x = ", Difference_x
    print "Average_difference_y = ", Average_difference_y

    outputfile.close()

if __name__ == "__main__":
    
    args = [] #Creating a list
    # for loop that converts arguments with a '*' to the corresponding files
    for arg in argv[1:]:  #For arguments argv[1] and following
        args += glob(arg) #Search for and add all * files to args
    main(args)
