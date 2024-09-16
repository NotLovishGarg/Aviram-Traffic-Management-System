import traci
import traci.constants as tc
from prettytable import PrettyTable


sumoCmd = ["sumo-gui", "-c", "demo.sumocfg"]  
traci.start(sumoCmd)


routes = {
    'clockwise_loop': ['E0', 'E2', 'E3', '-E8', 'E10'],
    
    'clockwise_loop2': ['E0', 'E2', 'E4'],
    'clockwise_loop4': ['E0', 'E1'],
    'clockwise_loop3': ['E0', 'E2', 'E3', 'E11'],
    'counterclockwise_loop': ['E8', '-E3', '-E2', '-E0', 'E7'],
    'counterclockwise_loop2': ['E8', '-E3', '-E2', 'E1'],
    'counterclockwise_loop3': ['E8', '-E3','E5' ],
    'emergency_route': ['E0', 'E2', 'E3', '-E8']
}


for route_id, edges in routes.items():
    traci.route.add(routeID=route_id, edges=edges)

traci.vehicle.add("emergency_1", routeID="emergency_route", typeID="DEFAULT_VEHTYPE", depart=100)
traci.vehicle.setColor("emergency_1", (255, 0, 0, 255))  

traci.vehicle.add("emergency_2", routeID="emergency_route", typeID="DEFAULT_VEHTYPE", depart=500)
traci.vehicle.setColor("emergency_2", (0, 0, 255, 255)) 

traci.vehicle.add("emergency_3", routeID="emergency_route", typeID="DEFAULT_VEHTYPE", depart=900)
traci.vehicle.setColor("emergency_3", (255, 255, 0, 255))  


for i in range(0, 3600, 10):
    traci.vehicle.add(f"car_{i}", routeID="clockwise_loop", typeID="DEFAULT_VEHTYPE", depart=i)
    traci.vehicle.add(f"car_{i+1}", routeID="counterclockwise_loop", typeID="DEFAULT_VEHTYPE", depart=i)
    traci.vehicle.add(f"car_{i+2}", routeID="counterclockwise_loop2", typeID="DEFAULT_VEHTYPE", depart=i)
    traci.vehicle.add(f"car_{i+3}", routeID="clockwise_loop4", typeID="DEFAULT_VEHTYPE", depart=i)
    traci.vehicle.add(f"car_{i+4}", routeID="counterclockwise_loop3", typeID="DEFAULT_VEHTYPE", depart=i)


detectors = {
    'detector_0': 'E0_0',
    'detector_1': '-E0_0',
    'detector_2': '-E2_0',
    'detector_3': 'E2_0',
    'detector_4': 'E3_0',
    'detector_5': '-E3_0',
    'detector_6': '-E8_0',
    'detector_7': 'E8_0',
    'detector_8': 'E7_0',
    'detector_9': 'E11_0',
    'detector_10': 'E6_0',
    'detector_11': 'E10_0',
    'detector_12': 'E1_0',
    'detector_13': 'E5_0',
    'detector_14': 'E4_0',
    'detector_15': 'E9_0',
}


junctions = {
    'Junction 1': ['detector_0', 'detector_1'],
    'Junction 2': ['detector_2', 'detector_3'],
    'Junction 3': ['detector_4', 'detector_5'],
    'Junction 4': ['detector_6', 'detector_7'],
    'Junction 5': ['detector_8', 'detector_9'],
    'Junction 6': ['detector_10', 'detector_11'],
    'Junction 7': ['detector_12', 'detector_13'],
    'Junction 8': ['detector_14', 'detector_15'],
}


step = 0
while step < 3600:
    traci.simulationStep()

   
    table = PrettyTable()
    table.field_names = ["Junction", "Road 1 Vehicles", "Road 2 Vehicles"]  # Assuming 2 roads per junction

   
    for junction, detector_ids in junctions.items():
        vehicle_counts = []
        for detector_id in detector_ids:
            vehicle_count = traci.inductionloop.getLastStepVehicleNumber(detector_id)
            vehicle_counts.append(vehicle_count)
        table.add_row([junction, vehicle_counts[0], vehicle_counts[1]])

    print(f"Simulation Step: {step}")
    print(table)  

    step += 1


traci.close()