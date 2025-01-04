#---Written by Michael Popov and Yuval Marsh---

#Imports
from xml.dom import minidom
#Location Object
class locationHeader:
    def __init__(self,convBoundary):
        self.netOffset = "0.00,0.00"
        self.convBoundary = f"{convBoundary[0]},{convBoundary[1]},{convBoundary[2]},{convBoundary[3]}"
        self.origBoundary = '-10000000000.00,-10000000000.00,10000000000.00,10000000000.00'
        self.projParameter = '!'

    def getNetOffset(self):
        return self.netOffset

    def getConvBoundary(self):
        return self.convBoundary

    def getOrigBoundary(self):
        return self.origBoundary

    def getProjParameter(self):
        return self.projParameter

    def setConvBoundary(self,convBoundary):
        self.convBoundary = convBoundary

    def to_XML(self,net_xml):
        location_xml = net_xml.createElement('location')
        location_xml.setAttribute('netOffset',self.netOffset)
        location_xml.setAttribute('convBoundary',self.convBoundary)
        location_xml.setAttribute('origBoundary',self.origBoundary)
        location_xml.setAttribute('projParameter',self.projParameter)
        return location_xml