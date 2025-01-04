#---Written by Michael Popov and Yuval Marsh---

#Imports
from xml.dom import minidom

class junctionObject:
    def __init__(self,id,type,x_cord,y_cord,incLanes,intLanes,shape):
        self.id = id
        self.type = type
        self.x_cord = x_cord
        self.y_cord = y_cord
        self.incLanes = incLanes
        self.intLanes = intLanes
        self.shape = shape

    def to_XML(self,net_xml):
        junc_xml = net_xml.createElement("junction")
        junc_xml.setAttribute('id',self.id)
        junc_xml.setAttribute('type',self.type)
        junc_xml.setAttribute('x',self.x_cord)
        junc_xml.setAttribute('y',self.y_cord)
        junc_xml.setAttribute('incLanes',self.incLanes)
        junc_xml.setAttribute('intLanes',self.intLanes)
        junc_xml.setAttribute('shape', self.shape)
        return junc_xml