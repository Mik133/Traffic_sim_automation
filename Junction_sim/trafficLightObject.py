#---Written by Michael Popov and Yuval Marsh---

class TrafficLightObject:
    def __init__(self,tl_id,tl_type,tl_pid,tl_offset,tl_duration,tl_state,tl_num_of_phase,net_xml):
        self.tl_id = tl_id
        self.tl_type = tl_type
        self.tl_pid = tl_pid
        self.tl_offset = tl_offset
        self.tl_duration = tl_duration
        self.tl_state = tl_state
        self.net_xml = net_xml
        self.tl_num_of_phase = tl_num_of_phase

    def tl_pahse_create(self,tl_dur,tl_state):
        phase_xml = self.net_xml.createElement('phase')
        phase_xml.setAttribute('duration',tl_dur)
        phase_xml.setAttribute('state',tl_state)
        return phase_xml

    def to_xml(self):
        tl_xml = self.net_xml.createElement('tlLogic')
        tl_xml.setAttribute('id',self.tl_id)
        tl_xml.setAttribute('type',self.tl_type)
        tl_xml.setAttribute('programID',self.tl_pid)
        tl_xml.setAttribute('offset',self.tl_offset)
        for phase in range(self.tl_num_of_phase):
            new_phase = self.tl_pahse_create(self.tl_duration[phase],self.tl_state[phase])
            tl_xml.appendChild(new_phase)
        return tl_xml