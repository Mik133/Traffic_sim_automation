#---Written by Michael Popov and Yuval Marsh---

# Imports


class JunctDeadEndObject:
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

class JRequestObject:
    def __init__(self,r_index,r_response,r_foes,r_cont,net_xml):
        self.index = r_index
        self.response = r_response
        self.foes = r_foes
        self.cont = r_cont
        self.net_xml = net_xml

    def to_XML(self):
        req_xml = self.net_xml.createElement('request')
        req_xml.setAttribute('index',self.index)
        req_xml.setAttribute('response',self.response)
        req_xml.setAttribute('foes',self.foes)
        req_xml.setAttribute('cont',self.cont)
        return req_xml

class JunctionPriorityObject:
    def __init__(self,j_id,x_j,y_j,inc_lanes,int_lanes,shape,net_xml,num_of_req,req_responses,req_foes,req_cont):
        self.id = j_id
        self.type = 'priority'
        self.x_j = x_j
        self.y_j = y_j
        self.inc_lanes = inc_lanes
        self.int_lanes = int_lanes
        self.shape = shape
        self.net_xml = net_xml
        self.num_of_req = num_of_req
        self.reqs = []
        self.req_responses = req_responses
        self.req_foes = req_foes
        self.req_cont = req_cont

    def make_jreqs(self):
        for req in range(self.num_of_req):
            new_req = JRequestObject(f"{req}",self.req_responses[req],self.req_foes[req],self.req_cont[req],self.net_xml)
            self.reqs.append(new_req)

    def to_XML(self):
        junction_xml = self.net_xml.createElement('junction')
        junction_xml.setAttribute('id',self.id)
        junction_xml.setAttribute('type',self.type)
        junction_xml.setAttribute('x',self.x_j)
        junction_xml.setAttribute('y',self.y_j)
        junction_xml.setAttribute('incLanes',self.inc_lanes)
        junction_xml.setAttribute('intLanes',self.int_lanes)
        junction_xml.setAttribute('shape',self.shape)
        for req in range(self.num_of_req):
            junction_xml.appendChild(self.reqs[req].to_XML())
        return junction_xml
























