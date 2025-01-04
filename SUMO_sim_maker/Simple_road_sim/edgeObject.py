#---Written by Michael Popov and Yuval Marsh---

#Imports
import laneObject as lane
from xml.dom import minidom
#Edge Object
class edgeObject:
    def __init__(self, id,numOfLanes,laneLeght,e_from,e_to,lane_shapes,speed):
        self.id = id
        self.numOfLanes = numOfLanes
        self.laneLeght = laneLeght
        self.priority = "-1"
        self.e_from = e_from
        self.e_to = e_to
        self.lane_shapes = lane_shapes
        self.speed = speed
        self.lanes = self.generateLanes()

    def generateLanes(self):
        lanes = []
        for laneNum in range(self.numOfLanes):
            new_lane = lane.laneObject(self.id + f"_{laneNum}",f":{laneNum}",
                                          self.speed,self.laneLeght,self.lane_shapes)
            lanes.append(new_lane)
        #Default speed is 13.89 will be changed later to be modular
        return lanes

    def to_XML(self,net_xml):
        edge_xml = net_xml.createElement("edge")
        edge_xml.setAttribute("id",self.id)
        edge_xml.setAttribute("from",self.e_from)
        edge_xml.setAttribute("to",self.e_to)
        edge_xml.setAttribute("priority",self.priority)
        for lane in self.lanes:
            edge_xml.appendChild(lane.to_XML(net_xml))
        return edge_xml

