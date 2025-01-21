#---Written by Michael Popov and Yuval Marsh---

# Imports
import laneObject

class RegularEdgeObject:
    def __init__(self,id,e_from,e_to,num_of_lanes,lane_length,lane_shapes,speed,net_xml):
        self.id = id
        self.e_from = e_from
        self.e_to = e_to
        self.e_priority = '-1'
        self.num_of_lanes = num_of_lanes
        self.lane_shapes = lane_shapes
        self.lane_length = lane_length
        self.speed = speed
        self.net_xml = net_xml
        self.lanes = []

    def make_lanes(self):
        for lane in range(self.num_of_lanes):
            new_lane = laneObject.LaneObject(self.id + f"_{lane}",f"{lane}",self.speed,f"{self.lane_length}",
                                             self.lane_shapes,self.net_xml)
            self.lanes.append(new_lane)

    def to_XML(self):
        self.make_lanes()
        edge_xml = self.net_xml.createElement('edge')
        edge_xml.setAttribute('id',self.id)
        edge_xml.setAttribute('from',self.e_from)
        edge_xml.setAttribute('to',self.e_to)
        edge_xml.setAttribute('priority',self.e_priority)
        for lane in range(self.num_of_lanes):
            new_lane_xml = self.lanes[lane].to_XML()
            edge_xml.appendChild(new_lane_xml)
        return edge_xml

class InternalEdgeObject:
    def __init__(self,e_id,num_of_lanes,lane_length,lane_shapes,speed,net_xml):
        self.id = e_id
        self.function = 'internal'
        self.num_of_lanes = num_of_lanes
        self.lane_shapes = lane_shapes
        self.lane_length = lane_length
        self.speed = speed
        self.net_xml = net_xml
        self.lanes = []

    def make_lanes(self):
        for lane in range(self.num_of_lanes):
            new_lane = laneObject.LaneObject(self.id + f"_{lane}", f"{lane}", self.speed, f"{self.lane_length}",
                                             self.lane_shapes, self.net_xml)
            self.lanes.append(new_lane)

    def to_XML(self):
        edge_xml = self.net_xml.createElement('edge')
        edge_xml.setAttribute('id',self.id)
        edge_xml.setAttribute('function',self.function)
        self.make_lanes()
        for lane in range(self.num_of_lanes):
            new_lane_xml = self.lanes[lane].to_XML()
            edge_xml.appendChild(new_lane_xml)
        return edge_xml
