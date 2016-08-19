import numpy as np 
import sys
import matplotlib.pyplot as plt

#The purpose of this function definition is to plot (x,y)=(Pulse_Shift,SamplesReco(4)) lines graphs for each CRRC
def Plot(Last_nSmple, files, CRRC10_ps_sr, CRRC20_ps_sr, CRRC30_ps_sr, CRRC43_ps_sr, CRRC50_ps_sr, CRRC60_ps_sr, all_pulse_shift, all_samplesReco):

    #Only works because of order of file input
    #Adding x values
    i=0
    while (i<len(files)):
        CRRC10_ps_sr[0].append(all_pulse_shift[i+1])
        CRRC20_ps_sr[0].append(all_pulse_shift[i+2])
        CRRC30_ps_sr[0].append(all_pulse_shift[i+3])
        CRRC43_ps_sr[0].append(all_pulse_shift[i+4])
        CRRC50_ps_sr[0].append(all_pulse_shift[i+5])
        CRRC60_ps_sr[0].append(all_pulse_shift[i+6])
        i += 6
   
    #Adding y values
    i=0
    while (i<len(files)):
        CRRC10_ps_sr[1].append(all_samplesReco[i+1])
        CRRC20_ps_sr[1].append(all_samplesReco[i+2])
        CRRC30_ps_sr[1].append(all_samplesReco[i+3])
        CRRC43_ps_sr[1].append(all_samplesReco[i+4])
        CRRC50_ps_sr[1].append(all_samplesReco[i+5])
        CRRC60_ps_sr[1].append(all_samplesReco[i+6])
        i += 6

  #Plotting
  #Choosing nSmple to plot. Eventually want to plot all three at once
    if (Last_nSmple == 10):
      #Plotting
      plt.figure(1)
      plt.title("Reconstructed in time Amp vs. Pulse_Shift, smpl/freq = 10/25", y=1.04)
      plt.xlabel("Pulse Shift [ns]")
      plt.ylabel("Reconstructed In Time Amplitude")
      plt.plot(CRRC10_ps_sr[0], CRRC10_ps_sr[1], 'ob-', label="CRRC10")
      plt.plot(CRRC20_ps_sr[0], CRRC20_ps_sr[1], 'og-', label="CRRC20")
      plt.plot(CRRC30_ps_sr[0], CRRC30_ps_sr[1], 'or-', label="CRRC30")
      plt.plot(CRRC43_ps_sr[0], CRRC43_ps_sr[1], 'oc-', label="CRRC43")
      plt.plot(CRRC50_ps_sr[0], CRRC50_ps_sr[1], 'om-', label="CRRC50")
      plt.plot(CRRC60_ps_sr[0], CRRC60_ps_sr[1], 'ok-', label="CRRC60")
      plt.legend(loc='lower left', title="Waveform")
      plt.show()
      plt.savefig("CRRC_10_25_ps_sr")
      #plt.xlim(-0.001,0.001)
      #plt.ylim(9.9,10.1)
 
    elif (Last_nSmple == 20):
      #Plotting
      plt.figure(1)
      plt.title("Reconstructed in time Amp vs. Pulse_Shift, smpl/freq = 20/12.5", y=1.04)
      plt.xlabel("Pulse Shift [ns]")
      plt.ylabel("Reconstructed In Time Amplitude")
      #plt.ylim(9.995,10.039)
      plt.plot(CRRC60_ps_sr[0], CRRC60_ps_sr[1], 'ok-', label="CRRC60")
      plt.plot(CRRC50_ps_sr[0], CRRC50_ps_sr[1], 'om-', label="CRRC50")
      plt.plot(CRRC43_ps_sr[0], CRRC43_ps_sr[1], 'oc-', label="CRRC43")
      plt.plot(CRRC30_ps_sr[0], CRRC30_ps_sr[1], 'or-', label="CRRC30")
      plt.plot(CRRC20_ps_sr[0], CRRC20_ps_sr[1], 'og-', label="CRRC20")
      plt.plot(CRRC10_ps_sr[0], CRRC10_ps_sr[1], 'ob-', label="CRRC10")
      plt.legend(loc='lower left', title="Waveform")
      plt.show()
      plt.savefig("CRRC_20_125_ps_sr")
      #plt.xlim(-0.001,0.001)

    elif (Last_nSmple == 40):
      #Plotting
      plt.figure(1)
      plt.title("Reconstructed in time Amp vs. Pulse_Shift, smpl/freq = 40/6.25", y=1.04)
      plt.xlabel("Pulse Shift [ns]")
      plt.ylabel("Reconstructed In Time Amplitude")
      #plt.ylim(9.995029,10.03)
      plt.plot(CRRC60_ps_sr[0], CRRC60_ps_sr[1], 'ok-', label="CRRC60")
      plt.plot(CRRC50_ps_sr[0], CRRC50_ps_sr[1], 'om-', label="CRRC50")
      plt.plot(CRRC43_ps_sr[0], CRRC43_ps_sr[1], 'oc-', label="CRRC43")
      plt.plot(CRRC30_ps_sr[0], CRRC30_ps_sr[1], 'or-', label="CRRC30")
      plt.plot(CRRC20_ps_sr[0], CRRC20_ps_sr[1], 'og-', label="CRRC20")
      plt.plot(CRRC10_ps_sr[0], CRRC10_ps_sr[1], 'ob-', label="CRRC10")
      plt.legend(loc='upper left', title="Waveform")
      plt.show()
      plt.savefig("CRRC_40_625_ps_sr")
      #plt.xlim(-0.001,0.001) 
