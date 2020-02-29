from queue import Queue
from JSON_Class import *
import paho.mqtt.client as mqtt
import csv
import numpy as np

class collectData(mqtt.Client):
    at_q = Queue(500)
    ab_q = Queue(500)
    fq_q = Queue(500)
    fh_q = Queue(500)
    yt_q = Queue(500)
    pt_q = Queue(500)
    rt_q = Queue(500)
    yb_q = Queue(500)
    pb_q = Queue(500)
    rb_q = Queue(500)
    
    writeToFile = False
    fileName = ""


    def __init__(self):
        mqtt.Client.__init__(self)
        self.connect("localhost",1883, 60)
        self.subscribe([("loadmanager",2)])
        self.message_callback_add("loadmanager", self.on_message)


    def on_connect(self, mqttc, obj, flags, rc):
        print("rc:"+str(rc))
        return 0

    def on_message(self, mqttc, obj, msg):
        #print(str(msg.payload))
        dataObj = Packet(msg.payload)
        max_size_of_array = dataObj.size
        try:
            self.at_q.put_nowait(dataObj.accel_top)
            self.ab_q.put_nowait(dataObj.accel_bot)
            self.fq_q.put_nowait(dataObj.fsr_quad)
            self.fh_q.put_nowait(dataObj.fsr_ham)
            self.yt_q.put_nowait(dataObj.yaw_top)
            self.pt_q.put_nowait(dataObj.pitch_top)
            self.rt_q.put_nowait(dataObj.roll_top)
            self.yb_q.put_nowait(dataObj.yaw_bot)
            self.pb_q.put_nowait(dataObj.pitch_bot)
            self.rb_q.put_nowait(dataObj.roll_bot)
        except Exception as e:
            print("queue full not going to add to queue")

        if len(dataObj.accel_top)<max_size_of_array:
            N= max_size_of_array - len(dataObj.accel_top)
            dataObj.accel_top += [0]*N

        if len(dataObj.accel_bot)<max_size_of_array:
            N= max_size_of_array - len(dataObj.accel_bot)
            dataObj.accel_bot += [0]*N

        if len(dataObj.fsr_quad)<max_size_of_array:
            N= max_size_of_array - len(dataObj.fsr_quad)
            dataObj.fsr_quad += [0]*N

        if len(dataObj.fsr_ham)<max_size_of_array:
            N= max_size_of_array - len(dataObj.fsr_ham)
            dataObj.fsr_ham += [0]*N

        if len(dataObj.yaw_top)<max_size_of_array:
            N= max_size_of_array - len(dataObj.yaw_top)
            dataObj.yaw_top += [0]*N

        if len(dataObj.pitch_top)<max_size_of_array:
            N= max_size_of_array - len(dataObj.pitch_top)
            dataObj.pitch_top += [0]*N

        if len(dataObj.roll_top)<max_size_of_array:
            N= max_size_of_array - len(dataObj.roll_top)
            dataObj.roll_top += [0]*N

        if len(dataObj.yaw_bot)<max_size_of_array:
            N= max_size_of_array - len(dataObj.yaw_bot)
            dataObj.yaw_bot += [0]*N

        if len(dataObj.pitch_bot)<max_size_of_array:
            N= max_size_of_array - len(dataObj.pitch_bot)
            dataObj.pitch_bot += [0]*N

        if len(dataObj.roll_bot)<max_size_of_array:
            N= max_size_of_array - len(dataObj.roll_bot)
            dataObj.roll_bot += [0]*N         

        if self.writeToFile and self.fileName != "":
            with open('logs/sensor_output.csv', 'a+', newline='') as sensorData:
                for i in range(max_size_of_array):    
                    data = [dataObj.accel_top[i],dataObj.accel_bot[i],dataObj.fsr_quad[i],dataObj.fsr_ham[i],dataObj.yaw_top[i],dataObj.pitch_top[i],dataObj.roll_top[i],dataObj.yaw_bot[i],dataObj.pitch_bot[i],dataObj.roll_bot[i]]
                    writer = csv.writer(sensorData)
                    writer.writerow(data)
            

    def setWriteToFile(self, writeToFile, fileName):
        '''
        Args:
            writeToFile: used to control the pipe values to files
            fileName: what to call the fileName
        '''
        self.writeToFile = writeToFile
        if not fileName.endswith(".csv") and fileName != "":
            fileName+= ".csv"
        if fileName != "":
            self.fileName = fileName
        print(self.fileName, self.writeToFile)

if __name__ == "__main__":
    test = collectData()
    rc = 0
    while rc == 0:
        rc = test.loop()    
