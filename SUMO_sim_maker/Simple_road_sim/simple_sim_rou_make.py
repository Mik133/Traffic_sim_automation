#---Written by Michael Popov and Yuval Marsh---

#Imports
from xml.dom import minidom

import carObject
import routesObject

def simple_sim_rou_make():
    num_of_cars = 2 # TO BE ENTERED FROM EXTERNAL(DEBUG)
    interval = 5 # TO BE ENTERED FROM EXTERNAL(DEBUG)
    # Make XML Object
    simple_rou = minidom.Document()
    # Add routes header
    routes_header = routesObject.routeHeader()
    routes_xml = routes_header.to_XML(simple_rou)
    simple_rou.appendChild(routes_xml)
    # Make Cars Objects
    initial_time = 0.00
    for car in range(num_of_cars):
        new_car = carObject.carObject(f"t_{car}",f"{initial_time + car*interval}","E0","E0") # TO BE ENTERED FROM EXTERNAL(DEBUG)
        new_car_xml = new_car.to_XML(simple_rou)
        routes_xml.appendChild(new_car_xml)
    simple_rou_xml = simple_rou.toprettyxml(indent="\t")
    with open("simple_rou.xml", 'w') as xml_file:
        xml_file.write(simple_rou_xml)
