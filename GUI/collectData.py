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
if __name__ == "__main__":
    test = collectData()
    rc = 0
    while rc == 0:
        rc = test.loop()    
