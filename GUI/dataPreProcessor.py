import numpy as np
from scipy	import signal,fftpack
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

	def plot(self):
		fig, ax = plt.subplots()
		ax.plot(self.time_series)

	def fftPlot(self):
		fig, ax = plt.subplots()
		yf = fftpack.fft(self.time_series)
		xf = np.linspace(0.0,self.fs/2.0,self.N//2)
		ax.plot(xf,2.0/self.N * np.abs(yf[:self.N//2]))

	def removeDCOffset(self):
		self.time_series = signal.detrend(self.time_series)

	def applyFilter(self, filtype, cutoff, order):
		sos = signal.butter(order, cutoff,btype = filtype,analog = False, output="sos", fs=self.fs)
		self.time_series = signal.sosfilt(sos,self.time_series)

if __name__ == '__main__':
	with open("/home/vasav/Documents/Capstone/LoadManager/TestingData/Fast_Sampling/Walking_10.csv","r") as dataFile:
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

	accelDataParser = dataPreProcessor(fh,200)
	accelDataParser.plot()
	accelDataParser.removeDCOffset()
	accelDataParser.fftPlot()
	accelDataParser.applyFilter("lowpass",10,5)
	accelDataParser.fftPlot()
	accelDataParser.plot()

	plt.show()

