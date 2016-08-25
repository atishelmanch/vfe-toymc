import numpy as np 
import sys
import matplotlib.pyplot as plt

# The purpose of this function definition is to plot Method - True pulse, for either method 1, method 2, or both (not sure yet). This should be plotted separately for each waveform
# Average over waveforms?
def Plot(files, Last_nSmple, all_True_Pulse_x, all_True_Pulse_y, all_Met1_x, all_Met1_y, all_Met2_x, all_Met2_y): #need variables

  #Plotting
  #Choosing nSmple to plot. Eventually want to plot all three at once

    # Creating Met 1 List for each waveform
    CRRC10_met1 = [] #(x,y) = (met1_x, met1_y)
    CRRC20_met1 = []
    CRRC30_met1 = []
    CRRC43_met1 = []
    CRRC50_met1 = []
    CRRC60_met1 = []

    # Creating Met 2 List for each waveform
    CRRC10_met2 = [] #(x,y) = (met2_x, met2_y)
    CRRC20_met2 = []
    CRRC30_met2 = []
    CRRC43_met2 = []
    CRRC50_met2 = []
    CRRC60_met2 = []

    # Creating True List for each waveform
    CRRC10_True = [] #(x,y) = (met_x, met2_y)
    CRRC20_True = []
    CRRC30_True = []
    CRRC43_True = []
    CRRC50_True = []
    CRRC60_True = []

    i=0
    while (i<2):
      CRRC10_met1.append([]) #Might have to do one noise per set of files
      CRRC20_met1.append([])
      CRRC30_met1.append([])
      CRRC43_met1.append([])
      CRRC50_met1.append([])
      CRRC60_met1.append([])
      CRRC10_met2.append([])
      CRRC20_met2.append([])
      CRRC30_met2.append([])
      CRRC43_met2.append([])
      CRRC50_met2.append([])
      CRRC60_met2.append([])
      CRRC10_True.append([])
      CRRC20_True.append([])
      CRRC30_True.append([])
      CRRC43_True.append([])
      CRRC50_True.append([])
      CRRC60_True.append([])
      i += 1 

    i=0
    while (i<len(files)):
        CRRC10_met1[0].append(all_Met1_x[i+1])
        CRRC20_met1[0].append(all_Met1_x[i+2])
        CRRC30_met1[0].append(all_Met1_x[i+3])
        CRRC43_met1[0].append(all_Met1_x[i+4])
        CRRC50_met1[0].append(all_Met1_x[i+5])
        CRRC60_met1[0].append(all_Met1_x[i+6])
        CRRC10_met1[1].append(all_Met1_y[i+1])
        CRRC20_met1[1].append(all_Met1_y[i+2])
        CRRC30_met1[1].append(all_Met1_y[i+3])
        CRRC43_met1[1].append(all_Met1_y[i+4])
        CRRC50_met1[1].append(all_Met1_y[i+5])
        CRRC60_met1[1].append(all_Met1_y[i+6])
        i += 6
   
    i=0
    while (i<len(files)):
        CRRC10_met2[0].append(all_Met2_x[i+1])
        CRRC20_met2[0].append(all_Met2_x[i+2])
        CRRC30_met2[0].append(all_Met2_x[i+3])
        CRRC43_met2[0].append(all_Met2_x[i+4])
        CRRC50_met2[0].append(all_Met2_x[i+5])
        CRRC60_met2[0].append(all_Met2_x[i+6])
        CRRC10_met2[1].append(all_Met2_y[i+1])
        CRRC20_met2[1].append(all_Met2_y[i+2])
        CRRC30_met2[1].append(all_Met2_y[i+3])
        CRRC43_met2[1].append(all_Met2_y[i+4])
        CRRC50_met2[1].append(all_Met2_y[i+5])
        CRRC60_met2[1].append(all_Met2_y[i+6])
        i += 6

    i=0
    while (i<len(files)):
        CRRC10_True[0].append(all_True_Pulse_x[i+1])
        CRRC20_True[0].append(all_True_Pulse_x[i+2])
        CRRC30_True[0].append(all_True_Pulse_x[i+3])
        CRRC43_True[0].append(all_True_Pulse_x[i+4])
        CRRC50_True[0].append(all_True_Pulse_x[i+5])
        CRRC60_True[0].append(all_True_Pulse_x[i+6])
        CRRC10_True[1].append(all_True_Pulse_y[i+1])
        CRRC20_True[1].append(all_True_Pulse_y[i+2])
        CRRC30_True[1].append(all_True_Pulse_y[i+3])
        CRRC43_True[1].append(all_True_Pulse_y[i+4])
        CRRC50_True[1].append(all_True_Pulse_y[i+5])
        CRRC60_True[1].append(all_True_Pulse_y[i+6])
        i += 6
    

    if (Last_nSmple == 10):
      #Plotting
      plt.figure(1)
      plt.title("True Pulse - Met1", y=1.04)
      plt.xlabel("Time [ns]")
      plt.ylabel("")
      #plt.plot(CRRC10_True[0], CRRC10_True[1], 'ob-', label="CRRC10 True Pulse") #Average over each waveform?
      plt.plot(CRRC10_met1[0], CRRC10_met1[1], 'or-', label="CRRC10 Method 1") #Average over each waveform?
      #plt.plot(CRRC10_met2[0], CRRC10_met2[1], 'og-', label="CRRC10 Method 2") #Average over each waveform?
      plt.legend(loc='best', title="Waveform", prop={'size':12})
      plt.savefig("nSmple_10_pulses.png")
      plt.show()
      #plt.xlim(-0.001,0.001)
      #plt.ylim(9.9,10.1)
 
    elif (Last_nSmple == 20):
      #Plotting
      plt.figure(1)
      plt.title("Reconstructed in time Amp vs. Pulse_Shift, smpl/freq = 20/12.5", y=1.04)
      plt.xlabel("Pulse Shift [ns]")
      plt.ylabel("Reconstructed In Time Amplitude[GeV]")
      #plt.ylim(9.995,10.039)
      plt.plot(CRRC60_ps_sr[0], CRRC60_ps_sr[1], 'ok-', label="CRRC60")
      plt.legend(loc='best', title="Waveform", prop={'size':12})
      plt.savefig("title.png")
      plt.show()
      #plt.xlim(-0.001,0.001)

    elif (Last_nSmple == 40):
      #Plotting
      plt.figure(1)
      plt.title("Reconstructed in time Amp vs. Pulse_Shift, smpl/freq = 40/6.25", y=1.04)
      plt.xlabel("Pulse Shift [ns]")
      plt.ylabel("Reconstructed In Time Amplitude[GeV]")
      plt.ticklabel_format(useOffset=False) #Y axis absolute values without offset (like +9.99)
      #plt.ylim(9.995029,10.03)
      plt.plot(CRRC60_ps_sr[0], CRRC60_ps_sr[1], 'ok-', label="CRRC60")
      plt.legend(loc='upper left', title="Waveform", prop={'size':12})
      plt.savefig("eltit.png")
      plt.show()
      #plt.xlim(-0.001,0.001) 
