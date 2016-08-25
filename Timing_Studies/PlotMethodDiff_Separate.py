# The purpose of this function is to plot method 1 - method 2 vs. time for each waveform separately
# This should output a plot with method 1 - method 2 vs. time for single pulse_shift value, single
# smp/frq value, line for each waveform.

import matplotlib.pyplot as plt

def Plot_Per_Waveform():
  if (Last_nSmple == 10):   #(nSmpl,nFreq) = (10,25)
 	plt.figure(1)
        x = all_x_list[1] #b/c for first file of homogeneous batch of files, all have same x list
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
        #plt.plot(x, all_y_list[1], 'ob--', label="CRRC10", linewidth=3)
        #plt.plot(x, all_y_list[2], 'og--', label="CRRC20", linewidth=3)
        #plt.plot(x, all_y_list[3], 'or--', label="CRRC30", linewidth=3)
        #plt.plot(x, all_y_list[4], 'oc--', label="CRRC43", linewidth=3)
        #plt.plot(x, all_y_list[5], 'om--', label="CRRC50", linewidth=3)
        #plt.plot(x, all_y_list[6], 'oy--', label="CRRC60", linewidth=3)
        plt.legend(loc='upper right', title="Pulse_Shift[ns]") 
        plt.show()
        plt.savefig("RootScanPlot_10_25_first_5.png")

        plt.figure(2)
        #x = all_x_list[1]
        #y data, for each pulse_shift value  
        #for i in range(7): #Not sure why this loop isn't working
        #  y_i = Pulse_Shift_List[i]
        #plt.title("Pulse Representation Difference Nsmp/Nfrq=10/25", y=1.04)
        #plt.xlabel("Time (ns)")
        #plt.ylabel("Method 1 - Method 2")
        #plt.legend(loc='upper left', title="Pulse_Shift[ns]") 
        #plt.show() #Just need to use this once after all figures made
        #plt.savefig("RootScanPlot_10_25_last_2.png")
 	   
 	
  elif (Last_nSmple == 20): #(nSmpl,nFreq) = (20,12.5)
 	plt.figure(1)
        x = all_x_list[1]
        #y data, for each pulse_shift value  
        #for i in range(7): #Not sure why this loop isn't working
        #  y_i = Pulse_Shift_List[i]
        

        plt.title("Pulse Representation Difference Nsmp/Nfrq=20/12.5", y=1.04) #raises title y position to above axis information
        plt.xlabel("Time (ns)")
        plt.ylabel("Method 1 - Method 2") 
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
        plt.legend(loc='upper right', title="Pulse_Shift[ns]") 
        #plt.show() #Just need to use this once after all figures made
        plt.savefig("RootScanPlot_40_625_last_2.png")
