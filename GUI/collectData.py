from queue import Queue
from JSON_Class import *
import paho.mqtt.client as mqtt
import csv
import numpy as np

class collectData(mqtt.Client):
    at_q = Queue(25)
    ab_q = Queue(25)
    fq_q = Queue(25)
    fh_q = Queue(25)
    yt_q = Queue(25)
    pt_q = Queue(25)
    rt_q = Queue(25)
    yb_q = Queue(25)
    pb_q = Queue(25)
    rb_q = Queue(25)
    
    def __init__(self):
        mqtt.Client.__init__(self)
        self.connect("localhost",1883, 60)
        self.subscribe([("loadmanager",2)])
        self.message_callback_add("loadmanager", self.on_message)

    def on_connect(self, mqttc, obj, flags, rc):
        print("rc:"+str(rc))
        return 0

    def on_message(self, mqttc, obj, msg):
        print(str(msg.payload))
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
            print("queue full")

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

        print(len(dataObj.roll_bot))
        i=0
        while i < max_size_of_array:        
            with open('logs/sensor_output.csv', 'a') as sensorData:
                data = [dataObj.accel_top[i],dataObj.accel_bot[i],dataObj.fsr_quad[i],dataObj.fsr_ham[i],dataObj.yaw_top[i],dataObj.pitch_top[i],dataObj.roll_top[i],dataObj.yaw_bot[i],dataObj.pitch_bot[i],dataObj.roll_bot[i]]
                writer = csv.writer(sensorData)
                writer.writerow(data)
                i = i+1
            
            
            
        #storeData = [self.at_q[i],self.ab_q[i],self.fq_q[i],self.fh_q[i],self.yt_q[i],self.pt_q[i],self.rt_q[i],self.yb_q[i],self.pb_q[i],self.rb_q[i]]
 
            

    ##def store_data(at_q,ab_q,fq_q,fh_q,yt_q,pt_q,rt_q,yb_q,pb_q,rb_q):
        #data = [at_q,ab_q,fq_q,fh_q,yt_q,pt_q,rt_q,yb_q,pb_q,rb_q]
        #i = 0
        #while on_connect==0:#while the sensor is on
          #  at_q[25]=[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
           # ab_q[25]=[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
           # fq_q[25]=[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
           # fh_q[25]=[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
           # yt_q[25]=[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
            #pt_q[25]=[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
            #rt_q[25]=[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
            #yb_q[25]=[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
            #pb_q[25]=[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
            #rb_q[25]=[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
            #if i < 25:
             #   storeData = [at_q[i],ab_q[i],fq_q[i],fh_q[i],yt_q[i],pt_q[i],rt_q[i],yb_q[i],pb_q[i],rb_q[i]]
             #   with open('sensor_output.csv', 'a') as sensorData:
             #       writer = csv.writer(sensorData)
             #       writer.writerow(storeData)
             #       i=i+1

                    


        #sensorData.close



            

            
                

    
if __name__ == "__main__":
    test = collectData()
    rc = 0
    while rc == 0:
        rc = test.loop()    
