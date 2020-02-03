import json
class Packet:
    def __init__(self, string):
        if (type(string) == bytes):
            string = string.decode("utf-8")
        packet = json.loads(string.strip('\n'))
        self.packet_num = packet['packet_num']
        self.size = packet['size']
        self.accel_top = packet['accel_top']
        self.accel_bot = packet['accel_bot']
        self.fsr_quad = packet['fsr_quad']
        self.fsr_ham = packet['fsr_ham']
        self.yaw_top = packet['yaw_top']
        self.pitch_top = packet['pitch_top']
        self.roll_top = packet['roll_top']
        self.yaw_bot = packet['yaw_bot']
        self.pitch_bot = packet['pitch_bot']
        self.roll_bot = packet['roll_bot']
    
    
if __name__ == "__main__":    
    x =  '{ "packet_num":50,"size":10, "accel_top":[1.0,2.2,3.3,4.4,5.5,6.5,7.4,8.2,9.8,10.1],\
    "accel_bot":[1.0,2.2,3.3,4.4,5.5,6.5,7.4,8.2,9.8,10.1],"fsr_quad":50, "fsr_ham":2, "yaw_top":1, "pitch_top":[11,13], "roll_top":13,\
    "yaw_bot":45, "pitch_bot":20, "roll_bot":33,"yaw_top":"New York" }'

    y = Packet(x)
