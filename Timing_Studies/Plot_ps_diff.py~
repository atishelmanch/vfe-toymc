import numpy as np 
import sys
import matplotlib.pyplot as plt

#The purpose of this function definition is to plot (x,y)=(Pulse_Shift,SamplesReco(4)) lines graphs for each CRRC
def Plot(Last_nSmple, Last_trueamp, files, CRRC10_ps_diff, CRRC20_ps_diff, CRRC30_ps_diff, CRRC43_ps_diff, CRRC60_ps_diff, CRRC90_ps_diff):

  #Plotting
  # Right now can only plot one samp/freq combination based on nSmple of final file. Therefore can only input one samp/freq per file batch. Want to eventually input all three and plot all three.

    CRRC10_ps_diff.sort()                 # Sort by x values
    CRRC10 = filter(None, CRRC10_ps_diff) # Remove empty elements
    CRRC20_ps_diff.sort()
    CRRC20 = filter(None, CRRC20_ps_diff)
    CRRC30_ps_diff.sort()
    CRRC30 = filter(None, CRRC30_ps_diff)
    CRRC43_ps_diff.sort()
    CRRC43 = filter(None, CRRC43_ps_diff)
    CRRC60_ps_diff.sort()
    CRRC60 = filter(None, CRRC60_ps_diff)
    CRRC90_ps_diff.sort()
    CRRC90 = filter(None, CRRC90_ps_diff)

    print "CRRC10 = ",CRRC10
    print "CRRC20 = ",CRRC20
    print "CRRC30 = ",CRRC30
    print "CRRC43 = ",CRRC43
    print "CRRC60 = ",CRRC60
    print "CRRC90 = ",CRRC90

    x_10 = [x[0] for x in CRRC10]
    y_10 = [y[1] for y in CRRC10]
    x_20 = [x[0] for x in CRRC20]
    y_20 = [y[1] for y in CRRC20]
    x_30 = [x[0] for x in CRRC30]
    y_30 = [y[1] for y in CRRC30]
    x_43 = [x[0] for x in CRRC43]
    y_43 = [y[1] for y in CRRC43]
    x_60 = [x[0] for x in CRRC60]
    y_60 = [y[1] for y in CRRC60]
    x_90 = [x[0] for x in CRRC90]
    y_90 = [y[1] for y in CRRC90]
    print "CRRC10 x = ",x_10
    print "CRRC10 y = ",y_10
   
    # Why aren't my error bars working.

    if (Last_nSmple == 10):
      #Plotting
      plt.figure(1)
      plt.title("Amplitude Difference vs. Pulse Shift, smpl/freq = 10/25, True Amp = "+str(Last_trueamp)+"GeV", y=1.04)
      plt.xlabel("Pulse Shift [ns]")
      plt.ylabel("Amplitude Difference [GeV]")
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
      plt.savefig("CRRC_10_25_ps_diff_"+str(Last_trueamp)+".png")
      plt.show()
      #plt.xlim(-0.001,0.001)
      #plt.ylim(9.9,10.1)
 
    elif (Last_nSmple == 20):
      #Plotting
      plt.figure(1)
      plt.title("Amplitude Difference vs. Pulse Shift, smpl/freq = 20/12.5, True Amp = "+str(Last_trueamp)+"GeV", y=1.04)
      plt.xlabel("Pulse Shift [ns]")
      plt.ylabel("Amplitude Difference [GeV]")
      #plt.ylim(9.995,10.039)
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
      plt.savefig("CRRC_20_125_ps_diff_"+str(Last_trueamp)+".png")
      plt.show()
      #plt.xlim(-0.001,0.001)

    elif (Last_nSmple == 40):
      #Plotting
      plt.figure(1)
      plt.title("Amp Difference vs. Pulse Shift, smpl/freq = 40/6.25, True Amp = "+str(Last_trueamp)+"GeV", y=1.04)
      plt.xlabel("Pulse Shift [ns]")
      plt.ylabel("Amplitude Difference [GeV]")
      plt.ticklabel_format(useOffset=False) #Y axis absolute values without offset (like +9.99)
      #plt.ylim(9.995029,10.03)
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
      plt.legend(loc='upper left', title="Waveform", prop={'size':12})
      plt.savefig("CRRC_40_625_ps_diff_"+str(Last_trueamp)+".png")
      plt.show()
      #plt.xlim(-0.001,0.001)
