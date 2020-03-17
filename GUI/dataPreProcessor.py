import numpy as np
from scipy import signal,fftpack,integrate
import matplotlib.pyplot as plt
from matplotlib import style
import csv 
import time
import math
import pprint

class dataPreProcessor():
        def __init__(self, time_series, sampling_frequency):
                self.time_series = np.array(time_series)
                self.fs = sampling_frequency
                self.N = len(time_series)
                self.ax =None;
                self.fig = None;
                self.segmetedData = []

        def plot(self):
                self.fig, self.ax = plt.subplots()
                self.ax.plot(self.time_series)

        def fftPlot(self):
                fig, ax = plt.subplots()
                yf = abs(fftpack.fft(self.time_series))
                xf = np.linspace(0.0,self.fs/2.0,self.N//2)
                ax.plot(xf,2.0/self.N * np.abs(yf[:self.N//2]))

        def subtract(self, array):
                return dataPreProcessor(list(np.subtract(self.time_series, array.time_series)),self.fs)

        def removeDCOffset(self):
                self.time_series = signal.detrend(self.time_series)

        def applyFilter(self, filtype, cutoff, order):
                sos = signal.butter(order, cutoff,btype = filtype,analog = False, output="sos", fs=self.fs)
                self.time_series = signal.sosfilt(sos,self.time_series)
        
        def integrate(self):
        	self.time_series = np.cumsum(self.time_series)
        def segmentDataTrain(self):
                # self.time_series = abs(np.gradient(self.time_series))
                # self.time_series = abs(self.time_series)
                integrated = np.cumsum(self.time_series)
                hsignal = signal.hilbert(integrated)
                envelope = np.abs(hsignal)
                segment_array = np.array(([0]*self.N))
                for i in range(self.N):
                        if envelope[i] > 2.1:
                                segment_array[i] = 1

                for i in range(5,self.N-5):
                        if sum(segment_array[i-5:i+5])>5:
                                segment_array[i] = 1

                plt.plot(segment_array);
                return segment_array

        def segmentArray(self, segmentDataTrain):
                multiplied_signal = np.multiply(segmentDataTrain,self.time_series)
                plt.plot(multiplied_signal)
                self.segmetedData = []
                start = False
                sub_array = []
                for i in range(len(segmentDataTrain)):
                        if (segmentDataTrain[i]) == 1:
                                start = True
                                sub_array.append(multiplied_signal[i])

                        elif (segmentDataTrain[i] == 0 and start):
                                start = False
                                self.segmetedData.append(sub_array)
                                sub_array = []
                self.segmetedData = [s for s in self.segmetedData if len(s) > 15]
                return self.segmetedData

        def showPeaks(self):
                peaks,_ = signal.find_peaks(self.time_series,distance=40)
                plt.plot(peaks, self.time_series[peaks], "x")
                average_peak = np.mean(self.time_series[peaks])

                print(len(peaks))
                sd = np.std(self.time_series[peaks], axis=0)
                final_list = [x for x in self.time_series[peaks] if (x > average_peak - 2 * sd)]
##                new_peaks,_ = signal.find_peaks(self.time_series,distance=40,height = average_peak)

                print(len(final_list))
                #plt.plot(final_list, self.time_series[final_list],"o")

                return final_list
        def segmented_and_peak(self,segment_train, peaks):
                sp_peaks = []
                print(len(peaks))
                for s in range(len(peaks)):
                        if (segment_train[s]):
                                sp_peaks.append(s)
                print(len(sp_peaks))
                sp_peaks = np.array(sp_peaks)
                plt.plot(sp_peaks, self.time_series[sp_peaks],"o")
                
        def waveletTransform(self):
                widths = np.arange(1, 31)
                cwtmatr = signal.cwt(self.time_series,signal.ricker, widths)
                plt.imshow(cwtmatr, extent=[-1, 1, 1, 31], cmap='PRGn', aspect='auto',
                        vmax=abs(cwtmatr).max(), vmin=-abs(cwtmatr).max())
                plt.show()


if __name__ == '__main__':
	for x in range(1,2):
		with open("/home/vasav/Documents/Capstone/LoadManager/GUI/logs/increasing_speed_2.csv","r") as dataFile:
			dataset = csv.reader(dataFile)
			ax_t = []
			ay_t = []
			az_t = []
			gx_t = []
			gy_t = []
			gz_t = []
			mx_t = []
			my_t = []
			mz_t = []

			ax_b = []
			ay_b = []
			az_b = []
			gx_b = []
			gy_b = []
			gz_b = []
			mx_b = []
			my_b = []
			mz_b = []

			fq = []
			fh = []
			angle_x_t = [0]
			angle_x_b = [0]
			angle_y_t = [0]
			angle_y_b = [0]
			angle_z_t = [0]
			angle_z_b = [0]
			angle= []
			dt = 0.005
			for row in dataset:
				ax_t.append(float(row[0]))
				ay_t.append(float(row[1]))
				az_t.append(float(row[2]))
				ax_b.append(float(row[3]))
				ay_b.append(float(row[4]))
				az_b.append(float(row[5]))

				fq.append(row[6])
				fh.append(row[7])

				gx_t.append(float(row[8]))
				gy_t.append(float(row[9]))
				gz_t.append(float(row[10]))
				gx_b.append(float(row[11]))
				gy_b.append(float(row[12]))
				gz_b.append(float(row[13]))

				angle_x_t.append(0.98*(angle_x_t[-1] + gx_t[-1]*dt)+(0.02)*ax_t[-1])
				angle_x_b.append(0.98*(angle_x_b[-1] + gx_b[-1]*dt)+(0.02)*ax_b[-1])
				
				angle_y_t.append(0.98*(angle_y_t[-1] + gy_t[-1]*dt)+(0.02)*ay_t[-1])
				angle_y_b.append(0.98*(angle_y_b[-1] + gy_b[-1]*dt)+(0.02)*ay_b[-1])

				angle_z_t.append(0.98*(angle_z_t[-1] + gz_t[-1]*dt)+(0.02)*az_t[-1])
				angle_z_b.append(0.98*(angle_z_b[-1] + gz_b[-1]*dt)+(0.02)*az_b[-1])

				# angle.append(angle_x_t[-1]-angle_x_b[-1])
				ab_dot = angle_x_t[-1]*angle_x_b[-1] + angle_y_t[-1]*angle_y_b[-1]
				a_mag = (angle_x_t[-1]**2 + angle_y_t[-1]**2)**0.5
				b_mag = (angle_x_b[-1]**2 + angle_y_b[-1]**2)**0.5
				

				angle.append(math.degrees (math.acos(ab_dot/(a_mag*b_mag))))

				# ab_dot = angle_x_t[-1]*angle_x_b[-1] + angle_y_t[-1]*angle_y_b[-1]
				# a_mag = (angle_x_t[-1]**2 + angle_y_t[-1]**2)**0.5
				# b_mag = (angle_x_b[-1]**2 + angle_y_b[-1]**2)**0.5
				# angle.append(math.degrees (math.acos(ab_dot/(a_mag*b_mag))))
	

	# gyro_x_bot = dataPreProcessor(gy_b,200)
	# gyro_x_bot.plot()
	# gyro_x_bot.integrate()
	# gyro_x_bot.applyFilter('lowpass',20,10)
	# gyro_x_bot.fftPlot()

	# gyro_x_top = dataPreProcessor(gy_t,200)
	# gyro_x_top.plot()
	# gyro_x_top.integrate()

	# angle_x_t = dataPreProcessor(angle_y_t, 200)
	# angle_x_t.plot()

	angle_x_b = dataPreProcessor(angle, 200)
	angle_x_b.applyFilter('lowpass',2,10)
	angle_x_b.plot()
	# angle_x_t.integrate()

	# diff = angle_x_t.subtract(angle_x_b)
	# diff.removeDCOffset()
	# diff.applyFilter('bandpass',[1,10],10)
	# diff.plot()
	# gyro_x_top.applyFilter('lowpass',20,10)
	# gyro_x_top.fftPlot()


	plt.show()

