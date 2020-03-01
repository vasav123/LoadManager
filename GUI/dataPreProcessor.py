import numpy as np
from scipy import signal,fftpack,integrate
import matplotlib.pyplot as plt
from matplotlib import style
import csv 
import time
import pprint

class dataPreProcessor():
	def __init__(self, time_series, sampling_frequency):
		self.time_series = np.array(time_series)
		self.fs = sampling_frequency
		self.N = len(time_series)
		self.ax =None;
		self.fig = None;

	def plot(self):
		self.fig, self.ax = plt.subplots()
		self.ax.plot(self.time_series)

	def fftPlot(self):
		fig, ax = plt.subplots()
		yf = fftpack.fft(self.time_series)
		xf = np.linspace(0.0,self.fs/2.0,self.N//2)
		ax.plot(xf,2.0/self.N * np.abs(yf[:self.N//2]))

	def subtract(self, array):
		return dataPreProcessor(list(np.subtract(self.time_series, array.time_series)),self.fs)

	def removeDCOffset(self):
		self.time_series = signal.detrend(self.time_series)

	def applyFilter(self, filtype, cutoff, order):
		sos = signal.butter(order, cutoff,btype = filtype,analog = False, output="sos", fs=self.fs)
		self.time_series = signal.sosfilt(sos,self.time_series)

	def segmentData(self):
		# self.time_series = abs(np.gradient(self.time_series))
		# self.time_series = abs(self.time_series)
		self.time_series = signal.hilbert(self.time_series)
		self.time_series = np.abs(self.time_series)
		segment_array = np.array(([0]*self.N))
		for i in range(self.N):
			if self.time_series[i] > 2:
				segment_array[i] = 1

		for i in range(5,self.N-5):
			if sum(segment_array[i-5:i+5])>5:
				segment_array[i] = 1

		self.ax.plot(segment_array)
		# self.applyFilter('lowpass', 5, 10)

	def waveletTransform(self):
		widths = np.arange(1, 31)
		cwtmatr = signal.cwt(self.time_series,signal.ricker, widths)
		plt.imshow(cwtmatr, extent=[-1, 1, 1, 31], cmap='PRGn', aspect='auto',
			vmax=abs(cwtmatr).max(), vmin=-abs(cwtmatr).max())
		plt.show()

	def integrate(self):
		self.time_series = np.cumsum(self.time_series)
		# print(min(self.time_series[1:self.N]))

if __name__ == '__main__':
	with open("/home/vasav/Documents/Capstone/LoadManager/TestingData/Fast_Sampling/Walking_2.csv","r") as dataFile:
		dataset = csv.reader(dataFile)
		at = []
		ab = []
		fq = []
		fh = []
		yt = []
		pt = []
		rt = []
		yb = []
		pb = []
		rb = []
		for row in dataset:
			at.append(float(row[0]))
			ab.append(float(row[1]))
			fq.append(float(row[2]))
			fh.append(float(row[3]))
			yt.append(float(row[4]))
			pt.append(float(row[5]))
			rt.append(float(row[6]))
			yb.append(float(row[7]))
			pb.append(float(row[8]))
			rb.append(float(row[9]))

	accelDataParser = dataPreProcessor(at,200)
	# pitchBotDataParser = dataPreProcessor(pb,200)
	# pitchBotDataParser.removeDCOffset()
	# pitchBotDataParser.applyFilter('lowpass',10,5)
	accelDataParser.plot()
	accelDataParser.removeDCOffset()
	# accelDataParser.fftPlot()
	accelDataParser.applyFilter("bandpass",[2,10],5)
	accelDataParser.plot()
	accelDataParser.integrate()
	# accelDataParser.removeDCOffset()
	accelDataParser.plot()
	accelDataParser.segmentData()
	# accelDataParser.waveletTransform()

	# subtractedValues = accelDataParser.subtract(pitchBotDataParser)
	# subtractedValues.plot()
	# accelDataParser.fftPlot()
	# accelDataParser.plot()

	plt.show()