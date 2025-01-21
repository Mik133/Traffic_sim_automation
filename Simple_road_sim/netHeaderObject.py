#---Written by Michael Popov and Yuval Marsh---

#Imports
from xml.dom import minidom
#Net Object
class netHeader:
    def __init__(self,version,junctionCornerDetail,limitTurnSpeed):
        self.version = version
        self.junctionCornerDetail = junctionCornerDetail
        self.limitTurnSpeed = limitTurnSpeed
        self.xmlns_xsi = 'http://www.w3.org/2001/XMLSchema-instance'
        self.xsi_noNamespaceSchemaLocation = 'http://sumo.dlr.de/xsd/net_file.xsd'

    def getVersion(self):
        return self.version

    def getJunctionCornerDetail(self):
        return self.junctionCornerDetail

    def getLimitTurnSpeed(self):
        return self.limitTurnSpeed

    def getXMLNS(self):
        return self.xmlns_xsi

    def getXSI(self):
        return self.xsi_noNamespaceSchemaLocation

    def to_XML(self,net_xml):
        net_header_xml = net_xml.createElement('net')
        net_header_xml.setAttribute('version', self.version)
        net_header_xml.setAttribute('junctionCornerDetail', self.junctionCornerDetail)
        net_header_xml.setAttribute('limitTurnSpeed', self.limitTurnSpeed)
        net_header_xml.setAttribute('xmlns', self.xmlns_xsi)
        net_header_xml.setAttribute('xsi', self.xsi_noNamespaceSchemaLocation)
        return net_header_xml