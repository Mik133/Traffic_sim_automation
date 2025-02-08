#---Written by Michael Popov and Yuval Marsh---

class conncectionObject:
    def __init__(self,c_from,c_to,c_from_lane,c_to_lane,c_via,c_dir,c_state,net_xml):
        self.c_from=c_from
        self.c_to=c_to
        self.c_from_lane=c_from_lane
        self.c_to_lane=c_to_lane
        self.c_via=c_via
        self.c_dir=c_dir
        self.c_state=c_state
        self.net_xml=net_xml

    def to_XML(self):
        connect_xml = self.net_xml.createElement('connection')
        connect_xml.setAttribute('from',self.c_from)
        connect_xml.setAttribute('to',self.c_to)
        connect_xml.setAttribute('fromLane',self.c_from_lane)
        connect_xml.setAttribute('toLane',self.c_to_lane)
        if self.c_via != '':
            connect_xml.setAttribute('via',self.c_via)
        connect_xml.setAttribute('dir',self.c_dir)
        connect_xml.setAttribute('state',self.c_state)
        return connect_xml

class ConncectionObjectLinkIndex:
    def __init__(self, c_from, c_to, c_from_lane, c_to_lane, c_via,c_tl, c_link_index, c_dir, c_state, net_xml):
        self.c_from = c_from
        self.c_to = c_to
        self.c_from_lane = c_from_lane
        self.c_to_lane = c_to_lane
        self.c_via = c_via
        self.c_tl = c_tl
        self.c_link_index = c_link_index
        self.c_dir = c_dir
        self.c_state = c_state
        self.net_xml = net_xml

    def to_XML(self):
        connect_xml = self.net_xml.createElement('connection')
        connect_xml.setAttribute('from', self.c_from)
        connect_xml.setAttribute('to', self.c_to)
        connect_xml.setAttribute('fromLane', self.c_from_lane)
        connect_xml.setAttribute('toLane', self.c_to_lane)
        if self.c_via != '':
            connect_xml.setAttribute('via', self.c_via)
        connect_xml.setAttribute('tl', self.c_tl)
        connect_xml.setAttribute('linkIndex', self.c_link_index)
        connect_xml.setAttribute('dir', self.c_dir)
        connect_xml.setAttribute('state', self.c_state)
        return connect_xml