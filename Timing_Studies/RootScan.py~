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
    all_x_list=[] # = [file number][list of y values] Contains a list of x values for each file
    all_y_list=[] # = [file number][list of y values] Contains a list of y values for each file

    #Creating empty data list for each loop (file)
    for i in range(50):
      all_x_list.append([])
      all_y_list.append([])  
        

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

	Pulse_shift = str(tree.pulse_shift)
        Nsample = str(tree.nSmpl)
	
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
    Pulse_Shift_List=[]
    
    for i in range(7):
      Pulse_Shift_List.append([])

    entries=len(all_x_list[1]) #For now, running loop for only one Nsamp/Nfreq, so all files have same x list. Eventually make better.  

    #create average for each pulse_shift set
    p=7 #average every number of files per pulse_shift value
    q=0 #Begin with Pulse_Shift_List[0]
    while (p<=49):
      for i in range(entries): 
        total=0.0
        for j in range(0,p):
          total += all_y_list[j+1][i]
        average_y=total/(len(files))
        Pulse_Shift_List[q].append(average_y) 
      p=p+7
      q=q+1

    print "all_x_list for file 1 = ", all_x_list[1]
    print "Pulse_Shift_List[0] = ", Pulse_Shift_List[0]
    print "Pulse_Shift_List[1] = ", Pulse_Shift_List[1]
    print "Pulse_Shift_List[2] = ", Pulse_Shift_List[2]
    print "Pulse_Shift_List[3] = ", Pulse_Shift_List[3]
    print "Pulse_Shift_List[4] = ", Pulse_Shift_List[4]
    print "Pulse_Shift_List[5] = ", Pulse_Shift_List[5]
    print "Pulse_Shift_List[6] = ", Pulse_Shift_List[6] 
    print "Last_nSmple = ", Last_nSmple

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

    #Plotting
    #Deciding which plots to make based on Last_nSmple

    if (Last_nSmple == 10):   #(nSmpl,nFreq) = (10,25)
 	plt.figure(1)
        x = all_x_list[1]
        #y data, for each pulse_shift value  
        #for i in range(7): #Not sure why this loop isn't working
        #  y_i = Pulse_Shift_List[i]
        y_0 = Pulse_Shift_List[0]
        y_1 = Pulse_Shift_List[1]
        y_2 = Pulse_Shift_List[2]
        y_3 = Pulse_Shift_List[3]
        y_4 = Pulse_Shift_List[4]
        y_5 = Pulse_Shift_List[5]
        y_6 = Pulse_Shift_List[6]

        plt.title("Pulse Representation Difference Nsmp/Nfrq=10/25", y=1.04) #raises title y position to above axis information
        plt.xlabel("Time (ns)")
        plt.ylabel("Method 1 - Method 2") 
        plt.plot(x, y_4, 'om--', label="0.1", linewidth=3)
        plt.plot(x, y_3, 'oc--', label="0.05", linewidth=3)
        plt.plot(x, y_2, 'or--', label="0.02", linewidth=3)
        plt.plot(x, y_1, 'og--', label="0.01", linewidth=3)
        plt.plot(x, y_0, 'ob--', label="0", linewidth=3)  
        #plt.plot(x, y_5, 'y--', label="0.2", linewidth=3) 
        #plt.plot(x, y_6, 'k--', label="0.5", linewidth=3) 
        #plt.ylim(-2E-16,7E-16)
        plt.legend(loc='upper right', title="Pulse_Shift[ns]") 
        plt.savefig("RootScanPlot_10_25_first_5.png")

        plt.figure(2)
        x = all_x_list[1]
        #y data, for each pulse_shift value  
        #for i in range(7): #Not sure why this loop isn't working
        #  y_i = Pulse_Shift_List[i]
        plt.title("Pulse Representation Difference Nsmp/Nfrq=10/25", y=1.04)
        plt.xlabel("Time (ns)")
        plt.ylabel("Method 1 - Method 2")
        plt.plot(x, y_6, 'ok--', label="0.5", linewidth=3) 
        plt.plot(x, y_5, 'oy--', label="0.2", linewidth=3) 
        plt.legend(loc='upper left', title="Pulse_Shift[ns]") 
        #plt.show() #Just need to use this once after all figures made
        plt.savefig("RootScanPlot_10_25_last_2.png")
 	   
 	
    elif (Last_nSmple == 20): #(nSmpl,nFreq) = (20,12.5)
 	plt.figure(1)
        x = all_x_list[1]
        #y data, for each pulse_shift value  
        #for i in range(7): #Not sure why this loop isn't working
        #  y_i = Pulse_Shift_List[i]
        y_0 = Pulse_Shift_List[0]
        y_1 = Pulse_Shift_List[1]
        y_2 = Pulse_Shift_List[2]
        y_3 = Pulse_Shift_List[3]
        y_4 = Pulse_Shift_List[4]
        y_5 = Pulse_Shift_List[5]
        y_6 = Pulse_Shift_List[6]

        plt.title("Pulse Representation Difference Nsmp/Nfrq=20/12.5", y=1.04) #raises title y position to above axis information
        plt.xlabel("Time (ns)")
        plt.ylabel("Method 1 - Method 2") 
        plt.plot(x, y_0, 'ob--', label="0", linewidth=3)
        plt.plot(x, y_1, 'og--', label="0.01", linewidth=3) 
        plt.plot(x, y_2, 'or--', label="0.02", linewidth=3)
        plt.plot(x, y_3, 'oc--', label="0.05", linewidth=3)
        plt.plot(x, y_4, 'om--', label="0.1", linewidth=3)
        #plt.plot(x, y_5, 'y--', label="0.2", linewidth=3) 
        #plt.plot(x, y_6, 'k--', label="0.5", linewidth=3) 
        #plt.ylim(-2E-16,7E-16)
        plt.legend(loc='lower right', title="Pulse_Shift[ns]") 
        plt.savefig("RootScanPlot_20_125_first_5.png")

        plt.figure(2)
        x = all_x_list[1]
        #y data, for each pulse_shift value  
        #for i in range(7): #Not sure why this loop isn't working
        #  y_i = Pulse_Shift_List[i]
        plt.title("Pulse Representation Difference Nsamp=20/12.5", y=1.04)
        plt.xlabel("Time (ns)")
        plt.ylabel("Method 1 - Method 2")
        plt.plot(x, y_6, 'ok--', label="0.5", linewidth=3) 
        plt.plot(x, y_5, 'oy--', label="0.2", linewidth=3) 
        plt.legend(loc='upper right', title="Pulse_Shift[ns]") 
        #plt.show() #Just need to use this once after all figures made
        plt.savefig("RootScanPlot_20_125_last_2.png")	       
 	 
 	
    elif (Last_nSmple == 40): #(nSmpl,nFreq) = (40,6.25)
 	plt.figure(1)
        x = all_x_list[1]
        #y data, for each pulse_shift value  
        #for i in range(7): #Not sure why this loop isn't working
        #  y_i = Pulse_Shift_List[i]
        y_0 = Pulse_Shift_List[0]
        y_1 = Pulse_Shift_List[1]
        y_2 = Pulse_Shift_List[2]
        y_3 = Pulse_Shift_List[3]
        y_4 = Pulse_Shift_List[4]
        y_5 = Pulse_Shift_List[5]
        y_6 = Pulse_Shift_List[6]

        plt.title("Pulse Representation Difference Nsmp/Nfrq=40/6.25", y=1.04) #raises title y position to above axis information
        plt.xlabel("Time (ns)")
        plt.ylabel("Method 1 - Method 2") 
        plt.plot(x, y_4, 'om--', label="0.1", linewidth=3)
        plt.plot(x, y_3, 'oc--', label="0.05", linewidth=3)
        plt.plot(x, y_2, 'or--', label="0.02", linewidth=3)
        plt.plot(x, y_1, 'og--', label="0.01", linewidth=3)
        plt.plot(x, y_0, 'ob--', label="0", linewidth=3)  
        #plt.plot(x, y_5, 'y--', label="0.2", linewidth=3) 
        #plt.plot(x, y_6, 'k--', label="0.5", linewidth=3) 
        plt.ylim(-2E-16,7E-16)
        plt.legend(loc='upper left', title="Pulse_Shift[ns]") 
        plt.savefig("RootScanPlot_40_625_first_5.png")

        plt.figure(2)
        x = all_x_list[1]
        #y data, for each pulse_shift value  
        #for i in range(7): #Not sure why this loop isn't working
        #  y_i = Pulse_Shift_List[i]
        plt.title("Pulse Representation Difference Nsmp/Nfrq=40/6.25", y=1.04)
        plt.xlabel("Time (ns)")
        plt.ylabel("Method 1 - Method 2")
        plt.plot(x, y_6, 'ok--', label="0.5", linewidth=3) 
        plt.plot(x, y_5, 'oy--', label="0.2", linewidth=3) 
        plt.legend(loc='upper right', title="Pulse_Shift[ns]") 
        #plt.show() #Just need to use this once after all figures made
        plt.savefig("RootScanPlot_40_625_last_2.png")



	      
    #Plotting nsmpl/nfrq = 20/12.5
    #plt.figure(2) #3?
    #x = all_x_list[1]
    #y = Average_difference_y
    #plt.title("fdsa")
    #plt.xlabel("Time (ns)")
    #plt.ylabel("Pulse Representation Difference Nsmp/Nfrq=")
    #plt.plot(x, y, 'b--', linewidth=5) #First plot on graph
    #plt.plot(y, x, 'r--', linewidth=5) #Second plot on graph 
    #plt.savefig("RootScanPlot_20_125.png") #can I do 12.5? scared of using decimal point in file name

    #Plotting nsmpl/nfrq = 40/6.25
    #plt.figure(2)
    #x = all_x_list[1]
    #y = Average_difference_y
    #plt.title("fdsa")
    #plt.xlabel("Time (ns)")
    #plt.ylabel("Pulse Representation Difference Nsmp/Nfrq=")
    #plt.plot(x, y, 'b--', linewidth=5) #First plot on graph
    #plt.plot(y, x, 'r--', linewidth=5) #Second plot on graph 
    #plt.show()
    #plt.savefig("RootScanPlot_40_625.png")

    #outputfile.close()

if __name__ == "__main__":
    
    args = [] #Creating a list
    # for loop that converts arguments with a '*' to the corresponding files
    for arg in argv[1:]:  #For arguments argv[1] and following
        args += glob(arg) #Search for and add all * files to args
    scan(args)            #Runs 'scan' definition with files=args 
