from queue import Queue
from JSON_Class import *
import paho.mqtt.client as mqtt
import numpy as np
import time
from recordControl import *
from mainWidgetWrapper import *

class collectData(mqtt.Client):
    ax_t = Queue(500)
    ay_t = Queue(500)
    az_t = Queue(500)
    ax_b = Queue(500)
    ay_b = Queue(500)
    az_b = Queue(500)
    fq_q = Queue(500)
    fh_q = Queue(500)
    gx_t = Queue(500)
    gy_t = Queue(500)
    gz_t = Queue(500)
    gx_b = Queue(500)
    gy_b = Queue(500)
    gz_b = Queue(500)

    dataQ = Queue(500)
    writeToFile = False
    fileName = ""
    StartTime = time.time()
    Timer = False

    def __init__(self):
        mqtt.Client.__init__(self)
        self.connect("localhost",1883, 60)
        self.subscribe([("loadmanager",2)])
        self.message_callback_add("loadmanager", self.on_message)
        self.record_widget = recordControl.Ui_recordControl()

    def on_connect(self, mqttc, obj, flags, rc):
        print("rc:"+str(rc))
        return 0

    def on_message(self, mqttc, obj, msg):
        #print(str(msg.payload))
        dataObj = Packet(msg.payload)
        max_size_of_array = dataObj.size
        # incase we have have missing values we just zeropadd them just so the timing stays correct
        # we really should never have missing values though
        if len(dataObj.ax_t)<max_size_of_array:
            N= max_size_of_array - len(dataObj.ax_t)
            dataObj.ax_t += [0]*N
            
        if len(dataObj.ay_t)<max_size_of_array:
            N= max_size_of_array - len(dataObj.ay_t)
            dataObj.ay_t += [0]*N

        if len(dataObj.az_t)<max_size_of_array:
            N= max_size_of_array - len(dataObj.az_t)
            dataObj.az_t += [0]*N

        if len(dataObj.ax_b)<max_size_of_array:
            N= max_size_of_array - len(dataObj.ax_b)
            dataObj.ax_b += [0]*N
            
        if len(dataObj.ay_b)<max_size_of_array:
            N= max_size_of_array - len(dataObj.ay_b)
            dataObj.ay_b += [0]*N

        if len(dataObj.az_b)<max_size_of_array:
            N= max_size_of_array - len(dataObj.az_b)
            dataObj.az_b += [0]*N

        if len(dataObj.fsr_quad)<max_size_of_array:
            N= max_size_of_array - len(dataObj.fsr_quad)
            dataObj.fsr_quad += [0]*N

        if len(dataObj.fsr_ham)<max_size_of_array:
            N= max_size_of_array - len(dataObj.fsr_ham)
            dataObj.fsr_ham += [0]*N

        if len(dataObj.gx_t)<max_size_of_array:
            N= max_size_of_array - len(dataObj.gx_t)
            dataObj.gx_t += [0]*N

        if len(dataObj.gy_t)<max_size_of_array:
            N= max_size_of_array - len(dataObj.gy_t)
            dataObj.gy_t += [0]*N

        if len(dataObj.gz_t)<max_size_of_array:
            N= max_size_of_array - len(dataObj.gz_t)
            dataObj.gz_t += [0]*N

        if len(dataObj.gx_b)<max_size_of_array:
            N= max_size_of_array - len(dataObj.gx_b)
            dataObj.gx_b += [0]*N

        if len(dataObj.gy_b)<max_size_of_array:
            N= max_size_of_array - len(dataObj.gy_b)
            dataObj.gy_b += [0]*N

        if len(dataObj.gz_b)<max_size_of_array:
            N= max_size_of_array - len(dataObj.gz_b)
            dataObj.gz_b += [0]*N         

        for i in range(max_size_of_array):
            data_point = Point(dataObj.ax_t[i],dataObj.ay_t[i],dataObj.az_t[i],dataObj.ax_b[i],dataObj.ay_b[i],dataObj.az_b[i],dataObj.fsr_quad[i],dataObj.fsr_ham[i],dataObj.gx_t[i],dataObj.gy_t[i],dataObj.gz_t[i],dataObj.gx_b[i],dataObj.gy_b[i],dataObj.gz_b[i])
            try:
                self.dataQ.put_nowait(data_point)
            except Exception as e:
                print("queue full not going to add to queue", e)

        
        if self.writeToFile and self.fileName != "":
            with open('logs/' + self.fileName, 'a+', newline='') as file:
                for i in range(max_size_of_array):    
                    p = Point(dataObj.ax_t[i],dataObj.ay_t[i],dataObj.az_t[i],dataObj.ax_b[i],dataObj.ay_b[i],dataObj.az_b[i],dataObj.fsr_quad[i],dataObj.fsr_ham[i],dataObj.gx_t[i],dataObj.gy_t[i],dataObj.gz_t[i],dataObj.gx_b[i],dataObj.gy_b[i],dataObj.gz_b[i])
                    file.write(repr(p)+"\n")

        if self.writeToFile == True:
            if self.Timer == False:
                self.Timer = True
                StartTime = time.time()
            ElapsedTime = int(time.time()-StartTime)
            self.record_widget.TotalSeconds.display(ElapsedTime)

        if self.Timer == True and self.writeToFile == False:
            self.Timer = False

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
    test.setWriteToFile(True, "Test_vasav")
    rc = 0
    while rc == 0:
        rc = test.loop()    
