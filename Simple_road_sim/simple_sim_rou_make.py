#---Written by Michael Popov and Yuval Marsh---

#Imports
from xml.dom import minidom

from Simple_road_sim import routesObject, carObject


def simple_sim_rou_make(simple_sim_args_object):
    num_of_cars_lane_lf = 7 # TO BE ENTERED FROM EXTERNAL(DEBUG)
    num_of_cars_lane_rl = 5 # TO BE ENTERED FROM EXTERNAL(DEBUG)
    interval_lf = 0.50 # TO BE ENTERED FROM EXTERNAL(DEBUG)
    # Make XML Object
    simple_rou = minidom.Document()
    # Add routes header
    routes_header = routesObject.routeHeader()
    routes_xml = routes_header.to_XML(simple_rou)
    simple_rou.appendChild(routes_xml)
    # Make Cars Objects
    initial_time = 0.00
    for car in range(num_of_cars_lane_lf):
        new_car = carObject.carObject(f"t_{car}",f"{initial_time + car*interval_lf}","E0","E0",
                                      "random") # TO BE ENTERED FROM EXTERNAL(DEBUG)
        new_car_xml = new_car.to_XML(simple_rou)
        routes_xml.appendChild(new_car_xml)
    for car in range(num_of_cars_lane_rl):
        new_car = carObject.carObject(f"r_{car}", f"{initial_time + car * interval_lf}", "E1", "E1",
                                      "random")  # TO BE ENTERED FROM EXTERNAL(DEBUG)
        new_car_xml = new_car.to_XML(simple_rou)
        routes_xml.appendChild(new_car_xml)
    simple_rou_xml = simple_rou.toprettyxml(indent="\t")
    with open("simple_rou.xml", 'w') as xml_file:
        xml_file.write(simple_rou_xml)
