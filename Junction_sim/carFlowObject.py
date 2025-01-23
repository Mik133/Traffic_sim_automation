

class carFlowObject:
    def __init__(self,f_id,f_begin,f_from,f_to,f_end,f_vhs_per_hour):
        self.f_id = f_id
        self.f_begin = f_begin
        self.f_from = f_from
        self.f_to = f_to
        self.f_end = f_end
        self.f_vhs_per_hour = f_vhs_per_hour

    def to_XML(self,net_xml):
        car_flow_xml = net_xml.createElement('flow')
        car_flow_xml.setAttribute('id',self.f_id)
        car_flow_xml.setAttribute('begin',self.f_begin)
        car_flow_xml.setAttribute('from',self.f_from)
        car_flow_xml.setAttribute('to',self.f_to)
        car_flow_xml.setAttribute('end',self.f_end)
        car_flow_xml.setAttribute('vehsPerHour',self.f_vhs_per_hour)
        return car_flow_xml

