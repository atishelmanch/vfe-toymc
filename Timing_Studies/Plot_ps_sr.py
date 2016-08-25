import numpy as np 
import sys
import matplotlib.pyplot as plt

#The purpose of this function definition is to plot (x,y)=(Pulse_Shift,SamplesReco(4)) lines graphs for each CRRC
def Plot(Last_nSmple, files, CRRC10_ps_sr, CRRC20_ps_sr, CRRC30_ps_sr, CRRC43_ps_sr, CRRC60_ps_sr, CRRC90_ps_sr, all_pulse_shift, all_samplesReco):

    #Only works because of order of file input, 6 waveforms
    #Adding x values
    #i=0
    #while (i<len(files)):
    #    CRRC10_ps_sr[0].append(all_pulse_shift[i+1])
    #    CRRC20_ps_sr[0].append(all_pulse_shift[i+2])
    #    CRRC30_ps_sr[0].append(all_pulse_shift[i+3])
    #    CRRC43_ps_sr[0].append(all_pulse_shift[i+4])
    #    CRRC60_ps_sr[0].append(all_pulse_shift[i+5])
    #    CRRC90_ps_sr[0].append(all_pulse_shift[i+6])
    #    i += 6
   
    #Adding y values
    #i=0
    #while (i<len(files)):
    #    CRRC10_ps_sr[1].append(all_samplesReco[i+1])
    #    CRRC20_ps_sr[1].append(all_samplesReco[i+2])
    #    CRRC30_ps_sr[1].append(all_samplesReco[i+3])
    #    CRRC43_ps_sr[1].append(all_samplesReco[i+4])
    #    CRRC60_ps_sr[1].append(all_samplesReco[i+5])
    #    CRRC90_ps_sr[1].append(all_samplesReco[i+6])
    #    i += 6

  #Plotting
  #Choosing nSmple to plot. Eventually want to plot all three at once

    CRRC10_ps_sr.sort()
    CRRC10 = filter(None, CRRC10_ps_sr) #Remove empty elements
    CRRC20_ps_sr.sort()
    CRRC20 = filter(None, CRRC20_ps_sr)
    CRRC30_ps_sr.sort()
    CRRC30 = filter(None, CRRC30_ps_sr)
    CRRC43_ps_sr.sort()
    CRRC43 = filter(None, CRRC43_ps_sr)
    CRRC60_ps_sr.sort()
    CRRC60 = filter(None, CRRC60_ps_sr)
    CRRC90_ps_sr.sort()
    CRRC90 = filter(None, CRRC90_ps_sr)

    print "CRRC10 = ",CRRC10
    print "CRRC20 = ",CRRC20
    print "CRRC30 = ",CRRC30
    print "CRRC43 = ",CRRC43
    print "CRRC60 = ",CRRC60
    print "CRRC90 = ",CRRC90
    print "Manual Exit."
    sys.exit(0)


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
    print "x = ",x_10
    print "y = ",y_10

    if (Last_nSmple == 10):
      #Plotting
      plt.figure(1)
      plt.title("Reconstructed in time Amp vs. Pulse_Shift, smpl/freq = 10/25", y=1.04)
      plt.xlabel("Pulse Shift [ns]")
      plt.ylabel("Reconstructed In Time Amplitude [GeV]")
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
      plt.savefig("CRRC_10_25_ps_sr_neg")
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
      plt.legend(loc='upper center', title="Waveform", prop={'size':10})
      plt.savefig("CRRC_20_125_ps_sr_neg")
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
      plt.legend(loc='upper left', title="Waveform", prop={'size':11})
      plt.savefig("CRRC_40_625_ps_sr_neg")
      plt.show()
      #plt.xlim(-0.001,0.001) 
