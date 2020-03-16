import json
class Packet:
    def __init__(self, string):
        if (type(string) == bytes):
            string = string.decode("utf-8")
        packet = json.loads(string.strip('\n'))
        #print(packet)
        self.packet_num = packet['packet_num']
        self.size = packet['size']
        self.ax_t = packet['ax_t']
        self.ay_t = packet['ay_t']
        self.az_t = packet['az_t']
        self.ax_b = packet['ax_b']
        self.ay_b = packet['ay_b']
        self.az_b = packet['az_b']
        self.fsr_quad = packet['fq']
        self.fsr_ham = packet['fh']
        self.gx_t = packet['gx_t']
        self.gy_t = packet['gy_t']
        self.gz_t = packet['gz_t']
        self.gx_b = packet['gx_b']
        self.gy_b = packet['gy_b']
        self.gz_b = packet['gz_b']
    
    
if __name__ == "__main__":    
    x =  '{ "packet_num":50,"size":10, "accel_top":[1.0,2.2,3.3,4.4,5.5,6.5,7.4,8.2,9.8,10.1],\
    "accel_bot":[1.0,2.2,3.3,4.4,5.5,6.5,7.4,8.2,9.8,10.1],"fsr_quad":50, "fsr_ham":2, "yaw_top":1, "pitch_top":[11,13], "roll_top":13,\
    "yaw_bot":45, "pitch_bot":20, "roll_bot":33,"yaw_top":"New York" }'

    y = Packet(x)
