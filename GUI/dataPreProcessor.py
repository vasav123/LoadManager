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
                self.segmetedData = []

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
                with open(r"C:\Users\mklei\OneDrive\Documents\GitHub\LoadManager\GUI\logs\long_walking_102"+".csv","r") as dataFile:
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
                                at.append(float(row[1]))
                                ab.append(float(row[0]))
                                fq.append(float(row[3]))
                                fh.append(float(row[2]))
                                yt.append(float(row[7]))
                                pt.append(float(row[8]))
                                rt.append(float(row[9]))
                                yb.append(float(row[4]))
                                pb.append(float(row[5]))
                                rb.append(float(row[6]))

                accelDataTop = dataPreProcessor(at,200)
                accelDataTop.removeDCOffset()
                accelDataTop.fftPlot()
                accelDataTop.applyFilter("bandpass",[1,40],5)
                accelDataTop.plot()
                peaks = accelDataTop.showPeaks()
                segmentTrain = accelDataTop.segmentDataTrain()
                accelDataTop.segmented_and_peak(segmentTrain,peaks)
                
##              accelDataBot = dataPreProcessor(ab, 200)
##              accelDataBot.removeDCOffset()
##              accelDataBot.applyFilter("bandpass",[2,10],5)
##              accelDataBot.plot()
##
##              yawTop = dataPreProcessor(yt, 200)
##              yawTop.removeDCOffset()
##              yawTop.applyFilter("bandpass",[2,10],5)
##              # yawTop.plot()
##
##              pitchTop = dataPreProcessor(pt, 200)
##              pitchTop.removeDCOffset()
##              pitchTop.applyFilter("bandpass",[2,10],5)
##              # pitchTop.plot()
##
##              rollTop = dataPreProcessor(rt, 200)
##              rollTop.removeDCOffset()
##              rollTop.applyFilter("bandpass",[2,10],5)
##              # rollTop.plot()
##
##              yawBot = dataPreProcessor(yb, 200)
##              yawBot.removeDCOffset()
##              yawBot.applyFilter("bandpass",[2,10],5)
##              # yawBot.plot()
##
##              pitchBot = dataPreProcessor(pb, 200)
##              pitchBot.removeDCOffset()
##              pitchBot.applyFilter("bandpass",[2,10],5)
##              # pitchBot.plot()
##
##              rollBot = dataPreProcessor(rb, 200)
##              rollBot.removeDCOffset()
##              rollBot.applyFilter("bandpass",[2,10],5)
##              # rollBot.plot()
##
##              fsrQuad = dataPreProcessor(fq, 200)
##              fsrQuad.removeDCOffset()
##              fsrQuad.applyFilter("bandpass",[2,10],5)
##              # fsrQuad.plot()        
##
##              fsrHam = dataPreProcessor(fh, 200)
##              fsrHam.removeDCOffset()
##              fsrHam.applyFilter("bandpass",[2,10],5)
##              # fsrHam.plot() 
##
##              segment_at = accelDataTop.segmentArray(segmentTrain)
##              segment_ab = accelDataBot.segmentArray(segmentTrain)
##              segment_yt = yawTop.segmentArray(segmentTrain)
##              segment_pt = pitchTop.segmentArray(segmentTrain)
##              segment_rt = rollTop.segmentArray(segmentTrain)
##              segment_yb = yawBot.segmentArray(segmentTrain)
##              segment_pb = pitchBot.segmentArray(segmentTrain)
##              segment_rb = rollBot.segmentArray(segmentTrain)
##              segment_fq = fsrQuad.segmentArray(segmentTrain)
##              segment_fh = fsrHam.segmentArray(segmentTrain)
                
                plt.show()
##              for i in range(len(segment_at)):
##                      with open('segmented_2/LongWalk_'+str(x)+'_'+str(i)+'.csv', 'w', newline='') as sensorData:
##                              for j in range(len(segment_at[i])):
##                                      data = [segment_at[i][j], segment_ab[i][j], segment_yt[i][j], segment_pt[i][j], segment_rt[i][j], segment_yb[i][j], segment_pb[i][j], segment_rb[i][j], segment_fq[i][j], segment_fh[i][j]]
##                                      writer = csv.writer(sensorData)
##                                      writer.writerow(data)
