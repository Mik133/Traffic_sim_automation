#---Written by Michael Popov and Yuval Marsh---

#Imports
from xml.dom import minidom
#Lane Object
class laneObject:
    def __init__(self,id,index,speed,length,shape):
        self.id = id
        self.index = index
        self.speed = speed
        self.length = length
        self.shape = shape

    def getId(self):
        return self.id

    def getIndex(self):
        return self.index

    def getSpeed(self):
        return self.speed

    def getLength(self):
        return self.length

    def getShape(self):
        return self.shape

    def to_XML(self,net_xml):
        lane_xml = net_xml.createElement('lane')
        lane_xml.setAttribute('id',self.id)
        lane_xml.setAttribute('index',self.index)
        lane_xml.setAttribute('speed',self.speed)
        lane_xml.setAttribute('length',self.length)
        lane_xml.setAttribute('shape',self.shape)
        return lane_xml



