#---Written by Michael Popov and Yuval Marsh---

#Imports
from xml.dom import minidom

class carObject:
    def __init__(self,id,deprat,e_from,e_to,depart_lane):
        self.id = id
        self.depart = deprat
        self.e_from = e_from
        self.e_to = e_to
        self.departLane = depart_lane

    def to_XML(self,rou_xml):
        trip_xml = rou_xml.createElement("trip")
        trip_xml.setAttribute('id',self.id)
        trip_xml.setAttribute('depart',self.depart)
        trip_xml.setAttribute('from',self.e_from)
        trip_xml.setAttribute('to',self.e_to)
        trip_xml.setAttribute('departLane',self.departLane)
        return trip_xml
