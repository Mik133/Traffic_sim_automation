#---Written by Michael Popov and Yuval Marsh---

class LaneObject:
    def __init__(self, lane_id, index, speed, lane_length, shape, net_xml):
        self.lane_id = lane_id
        self.index = index
        self.speed = speed
        self.length = lane_length
        self.shape = shape
        self.net_xml = net_xml

    def to_XML(self):
        lane_xml = self.net_xml.createElement('lane')
        lane_xml.setAttribute('id',self.lane_id)
        lane_xml.setAttribute('index',self.index)
        lane_xml.setAttribute('speed',self.speed)
        lane_xml.setAttribute('length',self.length)
        lane_xml.setAttribute('shape',self.shape)
        return lane_xml

