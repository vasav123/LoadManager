from queue import Queue
from JSON_Class import *
import paho.mqtt.client as mqtt

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
        self.at_q.put(dataObj.accel_top)
        self.ab_q.put(dataObj.accel_bot)
        self.fq_q.put(dataObj.fsr_quad)
        self.fh_q.put(dataObj.fsr_ham)
        self.yt_q.put(dataObj.yaw_top)
        self.pt_q.put(dataObj.pitch_top)
        self.rt_q.put(dataObj.roll_top)
        self.yb_q.put(dataObj.yaw_bot)
        self.pb_q.put(dataObj.pitch_bot)
        self.rb_q.put(dataObj.roll_bot)

if __name__ == "__main__":
    test = collectData()
    rc = 0
    while rc == 0:
        rc = test.loop()    
