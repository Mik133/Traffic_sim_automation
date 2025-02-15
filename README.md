# Traffic sim automated user guide
## Intro
This is a basic automated network generator for the SUMO traffic simulator, it can be used to generate networks with varying configurations.
Using this tool you can control over parameters as: road length, number of lanes, car flow etc.
## Installation
Open the terminal and enter:
```
git clone https://github.com/Mik133/Traffic_sim_automation.git
```
After running this command the tool will be installed on your PC.
##### dependencies:
* Pyhton `math` lib
* Python `minidom` lib
###### Clarification
The tool was developed and tested on **Ubuntu 24.04**.
## Choosing the network 
In the `sumo_main_runner.py` choose the network by changing the `sim_type` variable,the options are:
* `Simple net`
* `Split road`
* `Half junction(T type junction)`
## Simple road net
This network is a simple 2 way road with multiple lanes, in order to generate this network open the `sumo_main_runner.py` file and 
adjust the network parameters in the `SimpleSimParams` object.
The network files will be created in the folder `Sumo sim files\Simple road`.
###### The simulation
![image](https://github.com/user-attachments/assets/f6ee6a1a-753c-4a9f-8650-4891cc5cb05b)

## Split road net
This is similar to the `Simple road net` with additional options, in this simulation it's possible to choose number
of lanes for each direction and the flow of cars.
To adjust the simulation parameters open the `junction_sim_main.py` and adjust the parameters in the `split_road_params` object.
The network files will be created in the folder `Sumo sim files\Intersection road`.
###### The simulation
![image](https://github.com/user-attachments/assets/c54705ca-4525-44c7-9bd3-cb5f6d6e2e4f)

## Half junction(T type junction)
This network is a T type junction with traffic lights, in this simulation the parameters are:
The flow of cars and the traffic light timing.
To adjust the simulation parameters open the `junction_sim_main.py` and adjust the parameters in the `HalfJunctionParams` object.
The network files will be created in the folder `Sumo sim files\Intersection road`.

###### The simulation
![image](https://github.com/user-attachments/assets/306d19c9-0061-451a-8e1e-db255786778a)

## Conclusion 
This is the base code for automated `Traffic sim` as for the moment.
New simulation can be added in the future and wrappers to enable external parametes adjustment.
