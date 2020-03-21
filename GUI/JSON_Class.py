import json
class Packet:
    ''' This class is meant to be used for the incoming packet.
        Its main purposes is to decode the JSON -> to its individual fields
    '''
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

class Point:
    '''This class is meant to store each field at a specific point in time'''
    def __init__(self, ax_t,ay_t,az_t,ax_b,ay_b,az_b,fq,fh,gx_t,gy_t,gz_t,gx_b,gy_b,gz_b):
        self.ax_t = ax_t 
        self.ay_t = ay_t 
        self.az_t = az_t 
        self.ax_b = ax_b 
        self.ay_b = ay_b 
        self.az_b = az_b 
        self.fq = fq 
        self.fh = fh 
        self.gx_t = gx_t 
        self.gy_t = gy_t 
        self.gz_t = gz_t 
        self.gx_b = gx_b 
        self.gy_b = gy_b 
        self.gz_b = gz_b 
        self.knee_angle = 0
        self.angle_x_t = 0
        self.angle_x_b = 0
        #self.velocity = 0

    def __repr__(self):
        return "%f, %f, %f, %f, %f, %f, %d, %d, %f, %f, %f, %f, %f, %f"%(self.ax_t,self.ay_t,self.az_t, self.ax_b,self.ay_b, self.az_b, self.fq, self.fh, self.gx_t, self.gy_t, self.gz_t, self.gx_b, self.gy_b, self.gz_b)
    
if __name__ == "__main__":    
    x =  '''{"packet_num":10,
            "size":1,
            "ax_t":[-0.520452],
            "ay_t":[0.74298],
            "az_t":[-0.067344],
            "ax_b":[1.029924],
            "ay_b":[-0.180804],
            "az_b":[-0.5673],
            "fq":[0],
            "fh":[17],
            "gx_t":[29.96875],
            "gy_t":[36.63625],
            "gz_t":[-101.325],
            "gx_b":[-51.19625],
            "gy_b":[-115.5525],
            "gz_b":[-144.4362]}'''
    y = Packet(x)
    for i in range(y.size):
        p = Point(y.ax_t[i],y.ay_t[i],y.az_t[i],y.ax_b[i],y.ay_b[i],y.az_b[i],y.fsr_quad[i],y.fsr_ham[i],y.gx_t[i],y.gy_t[i],y.gz_t[i],y.gx_b[i],y.gy_b[i],y.gz_b[i])
        print(repr(p))
