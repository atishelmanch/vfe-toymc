import numpy as np 
import sys
import matplotlib.pyplot as plt

#The purpose of this function definition is to plot (x,y)=(Pulse_Shift,SamplesReco(4)) lines graphs for each CRRC
def Plot(Last_nSmple, Last_trueamp, Out_of_Time_amp_10, Out_of_Time_amp_20, Out_of_Time_amp_30, Out_of_Time_amp_43, Out_of_Time_amp_60, Out_of_Time_amp_90):

  #Plotting
  # Right now can only plot one samp/freq combination based on nSmple of final file. Therefore can only input one samp/freq per file batch. Want to eventually input all three and plot all three.

    Out_of_Time_amp_10.sort()                 # Sort by x values
    Out_of_Time_amp_10 = filter(None, Out_of_Time_amp_10) # Remove empty elements
    Out_of_Time_amp_20.sort()                 # Sort by x values
    Out_of_Time_amp_20 = filter(None, Out_of_Time_amp_20)
    Out_of_Time_amp_30.sort()                 # Sort by x values
    Out_of_Time_amp_30 = filter(None, Out_of_Time_amp_30)
    Out_of_Time_amp_43.sort()                 # Sort by x values
    Out_of_Time_amp_43 = filter(None, Out_of_Time_amp_43)
    Out_of_Time_amp_60.sort()                 # Sort by x values
    Out_of_Time_amp_60 = filter(None, Out_of_Time_amp_60)
    Out_of_Time_amp_90.sort()                 # Sort by x values
    Out_of_Time_amp_90 = filter(None, Out_of_Time_amp_90)

    x_10 = [x[0] for x in Out_of_Time_amp_10]
    y_10 = [y[1] for y in Out_of_Time_amp_10]
    x_20 = [x[0] for x in Out_of_Time_amp_20]
    y_20 = [y[1] for y in Out_of_Time_amp_20]
    x_30 = [x[0] for x in Out_of_Time_amp_30]
    y_30 = [y[1] for y in Out_of_Time_amp_30]
    x_43 = [x[0] for x in Out_of_Time_amp_43]
    y_43 = [y[1] for y in Out_of_Time_amp_43]
    x_60 = [x[0] for x in Out_of_Time_amp_60]
    y_60 = [y[1] for y in Out_of_Time_amp_60]
    x_90 = [x[0] for x in Out_of_Time_amp_90]
    y_90 = [y[1] for y in Out_of_Time_amp_90]
   
    if (Last_nSmple == 10):
      #Plotting
      plt.figure(1)
      plt.title("Out of Time Amp vs. Pulse Shift, smpl/freq = 10/25, True Amp = "+str(Last_trueamp)+"GeV", y=1.04)
      plt.xlabel("Pulse Shift [ns]")
      plt.ylabel("Out of Time Reco Amp [GeV]")
      plt.errorbar(x_10, y_10, xerr=0, yerr=0.04)
      plt.errorbar(x_20, y_20, xerr=0, yerr=0.04)
      plt.errorbar(x_30, y_30, xerr=0, yerr=0.04)
      plt.errorbar(x_43, y_43, xerr=0, yerr=0.04)
      plt.errorbar(x_60, y_60, xerr=0, yerr=0.04)
      plt.errorbar(x_90, y_90, xerr=0, yerr=0.04)
      plt.plot(x_10, y_10, 'ob-', label="CRRC10")
      plt.plot(x_20, y_20, 'og-', label="CRRC20")
      plt.plot(x_30, y_30, 'or-', label="CRRC30")
      plt.plot(x_43, y_43, 'oc-', label="CRRC43")
      plt.plot(x_60, y_60, 'om-', label="CRRC60")
      plt.plot(x_90, y_90, 'ok-', label="CRRC90")
      plt.legend(loc='best', title="Waveform", prop={'size':12})
      plt.savefig("10_25_Out_of_Time_amp_"+str(Last_trueamp)+".png")
      plt.show()
      #plt.xlim(-0.001,0.001)
      #plt.ylim(9.9,10.1)
 
    elif (Last_nSmple == 20):
      #Plotting
      plt.figure(1)
      plt.title("Out of Time Amp vs. Pulse Shift, smpl/freq = 20/12.5, True Amp = "+str(Last_trueamp)+"GeV", y=1.04)
      plt.xlabel("Pulse Shift [ns]")
      plt.ylabel("Out of Time Reco Amp [GeV]")
      plt.errorbar(x_10, y_10, xerr=0, yerr=0.04)
      plt.errorbar(x_20, y_20, xerr=0, yerr=0.04)
      plt.errorbar(x_30, y_30, xerr=0, yerr=0.04)
      plt.errorbar(x_43, y_43, xerr=0, yerr=0.04)
      plt.errorbar(x_60, y_60, xerr=0, yerr=0.04)
      plt.errorbar(x_90, y_90, xerr=0, yerr=0.04)
      plt.plot(x_10, y_10, 'ob-', label="CRRC10")
      plt.plot(x_20, y_20, 'og-', label="CRRC20")
      plt.plot(x_30, y_30, 'or-', label="CRRC30")
      plt.plot(x_43, y_43, 'oc-', label="CRRC43")
      plt.plot(x_60, y_60, 'om-', label="CRRC60")
      plt.plot(x_90, y_90, 'ok-', label="CRRC90")
      plt.legend(loc='best', title="Waveform", prop={'size':12})
      plt.savefig("20_125_Out_of_Time_amp_"+str(Last_trueamp)+".png")
      plt.show()
      #plt.xlim(-0.001,0.001)
      #plt.ylim(9.9,10.1)
    elif (Last_nSmple == 40):
      #Plotting
      plt.figure(1)
      plt.title("Out of Time Amp vs. Pulse Shift, smpl/freq = 40/6.25, True Amp = "+str(Last_trueamp)+"GeV", y=1.04)
      plt.xlabel("Pulse Shift [ns]")
      plt.ylabel("Out of Time Reco Amp [GeV]")
      plt.errorbar(x_10, y_10, xerr=0, yerr=0.04)
      plt.errorbar(x_20, y_20, xerr=0, yerr=0.04)
      plt.errorbar(x_30, y_30, xerr=0, yerr=0.04)
      plt.errorbar(x_43, y_43, xerr=0, yerr=0.04)
      plt.errorbar(x_60, y_60, xerr=0, yerr=0.04)
      plt.errorbar(x_90, y_90, xerr=0, yerr=0.04)
      plt.plot(x_10, y_10, 'ob-', label="CRRC10")
      plt.plot(x_20, y_20, 'og-', label="CRRC20")
      plt.plot(x_30, y_30, 'or-', label="CRRC30")
      plt.plot(x_43, y_43, 'oc-', label="CRRC43")
      plt.plot(x_60, y_60, 'om-', label="CRRC60")
      plt.plot(x_90, y_90, 'ok-', label="CRRC90")
      plt.legend(loc='best', title="Waveform", prop={'size':12})
      plt.savefig("40_625_Out_of_Time_amp_"+str(Last_trueamp)+".png")
      plt.show()
      #plt.xlim(-0.001,0.001)
      #plt.ylim(9.9,10.1)
