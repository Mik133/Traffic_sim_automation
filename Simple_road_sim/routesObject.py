#---Written by Michael Popov and Yuval Marsh---

#Imports
from xml.dom import minidom

class routeHeader:
    def __init__(self):
        self.xmlns_xsi = "http://www.w3.org/2001/XMLSchema-instance"
        self.xsi_noNamespaceSchemaLocation = "http://sumo.dlr.de/xsd/routes_file.xsd"

    def to_XML(self,rou_xml):
        route_xml = rou_xml.createElement("routes")
        route_xml.setAttribute('xmlns:xsi',self.xmlns_xsi)
        route_xml.setAttribute('xsi:noNamespaceSchemaLocation',self.xsi_noNamespaceSchemaLocation)
        return route_xml