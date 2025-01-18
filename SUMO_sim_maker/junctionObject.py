#---Written by Michael Popov and Yuval Marsh---

# Imports


class junctDeadEndObject:
    def __init__(self,j_id,x_j,y_j,inc_lanes,int_lanes,shape,net_xml):
        self.id = j_id
        self.type = 'dead_end'
        self.x_j = x_j
        self.y_j = y_j
        self.inc_lanes = inc_lanes
        self.int_lanes = int_lanes
        self.shape = shape
        self.net_xml = net_xml

    def to_XML(self):
        junction_xml = self.net_xml.createElement('junction')
        junction_xml.setAttribute('id',self.id)
        junction_xml.setAttribute('type',self.type)
        junction_xml.setAttribute('x',self.x_j)
        junction_xml.setAttribute('y',self.y_j)
        junction_xml.setAttribute('incLanes',self.inc_lanes)
        junction_xml.setAttribute('intLanes',self.int_lanes)
        junction_xml.setAttribute('shape',self.shape)
        return junction_xml

class junctionPriorityObject:
    def __init__(self):
        