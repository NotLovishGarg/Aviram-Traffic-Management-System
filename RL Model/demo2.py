import traci
import numpy as np
import random
import time


alpha = 0.1  
gamma = 0.9 
epsilon = 0.1  


q_table = np.zeros((5, 3)) 


def get_state(vehicle_count):
    if vehicle_count == 0:
        return 0
    elif vehicle_count <= 5:
        return 1
    elif vehicle_count <= 10:
        return 2
    elif vehicle_count <= 20:
        return 3
    else:
        return 4


def choose_action(state):
    if random.uniform(0, 1) < epsilon:
        return random.choice([0, 1, 2])  
    else:
        return np.argmax(q_table[state]) 


def update_q_table(state, action, reward, next_state):
    predict = q_table[state, action]
    target = reward + gamma * np.max(q_table[next_state])
    q_table[state, action] = q_table[state, action] + alpha * (target - predict)


def get_reward(vehicle_count):
    return -vehicle_count 

def run_rl_sumo(sumo_cfg, num_episodes=1, steps_per_episode=3000):  
    sumoCmd = ["sumo-gui", "-c", sumo_cfg]
    
    for episode in range(num_episodes):
        traci.start(sumoCmd)
        step = 0
        
        while step < steps_per_episode:
            try:
                traci.simulationStep()
                
               
                vehicle_count_0 = traci.inductionloop.getLastStepVehicleNumber('detector_0')
                vehicle_count_1 = traci.inductionloop.getLastStepVehicleNumber('detector_1')
                vehicle_count_2 = traci.inductionloop.getLastStepVehicleNumber('detector_2')
                vehicle_count_3 = traci.inductionloop.getLastStepVehicleNumber('detector_3')
                vehicle_count_4 = traci.inductionloop.getLastStepVehicleNumber('detector_4')
                vehicle_count_5 = traci.inductionloop.getLastStepVehicleNumber('detector_5')
                vehicle_count_6 = traci.inductionloop.getLastStepVehicleNumber('detector_6')
                vehicle_count_7 = traci.inductionloop.getLastStepVehicleNumber('detector_7')
                vehicle_count_8 = traci.inductionloop.getLastStepVehicleNumber('detector_8')
                vehicle_count_9 = traci.inductionloop.getLastStepVehicleNumber('detector_9')
                vehicle_count_10 = traci.inductionloop.getLastStepVehicleNumber('detector_10')
                vehicle_count_11= traci.inductionloop.getLastStepVehicleNumber('detector_11')
                vehicle_count_12= traci.inductionloop.getLastStepVehicleNumber('detector_12')
                vehicle_count_13= traci.inductionloop.getLastStepVehicleNumber('detector_13')
                vehicle_count_14= traci.inductionloop.getLastStepVehicleNumber('detector_14')
                vehicle_count_15= traci.inductionloop.getLastStepVehicleNumber('detector_15')
                vehicle_count_16= traci.inductionloop.getLastStepVehicleNumber('detector_16')
                vehicle_count_17= traci.inductionloop.getLastStepVehicleNumber('detector_17')
                vehicle_count_18= traci.inductionloop.getLastStepVehicleNumber('detector_18')
                vehicle_count_19= traci.inductionloop.getLastStepVehicleNumber('detector_19')
                vehicle_count_20= traci.inductionloop.getLastStepVehicleNumber('detector_20')
                vehicle_count_21= traci.inductionloop.getLastStepVehicleNumber('detector_21')
                vehicle_count_22= traci.inductionloop.getLastStepVehicleNumber('detector_22')
                vehicle_count_23= traci.inductionloop.getLastStepVehicleNumber('detector_23')
                vehicle_count_24= traci.inductionloop.getLastStepVehicleNumber('detector_24')
                vehicle_count_25= traci.inductionloop.getLastStepVehicleNumber('detector_25')
                vehicle_count_26= traci.inductionloop.getLastStepVehicleNumber('detector_26')




                
               
                total_vehicle_count = vehicle_count_0 + vehicle_count_1 + vehicle_count_2 + vehicle_count_3+vehicle_count_4+vehicle_count_5+vehicle_count_6+vehicle_count_7+vehicle_count_8+vehicle_count_9+vehicle_count_10+vehicle_count_11+vehicle_count_12+vehicle_count_13+vehicle_count_14+vehicle_count_15+vehicle_count_16+vehicle_count_17+vehicle_count_18+vehicle_count_19+vehicle_count_20+vehicle_count_21+vehicle_count_22+vehicle_count_23+vehicle_count_24+vehicle_count_25+vehicle_count_26
                
               
                state = get_state(total_vehicle_count)
                

                action = choose_action(state)
                traci.trafficlight.setPhase("J0", action)  
                
               
                reward = get_reward(total_vehicle_count)
                
                
                update_q_table(state, action, reward, state)
                
                step += 1
            
            except traci.exceptions.FatalTraCIError as e:
                print(f"Error during simulation step: {e}")
                break
        
        traci.close()
        print(f"Episode {episode+1} complete.")


sumo_cfg_path = "demo.sumocfg"
run_rl_sumo(sumo_cfg_path, num_episodes=1, steps_per_episode=5000)

print(f"Simulation complete. Traffic data saved in detector_output.xml")