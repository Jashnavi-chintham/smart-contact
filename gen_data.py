import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

def generate_iot_dataset(rows=100):
    data = []
    start_time = datetime.now() - timedelta(days=1)
    
    devices = ['Sensor_A1', 'Gateway_02', 'Camera_X', 'Actuator_Z']
    statuses = ['Active', 'Warning', 'Compromised', 'Maintenance']
    
    for i in range(rows):
        timestamp = start_time + timedelta(minutes=15 * i)
        device = random.choice(devices)
        # Trust level usually correlates with status
        status = random.choices(statuses, weights=[70, 15, 5, 10])[0]
        
        if status == 'Active':
            trust_level = random.randint(80, 100)
        elif status == 'Warning':
            trust_level = random.randint(40, 79)
        else:
            trust_level = random.randint(0, 39)
            
        # Access is granted if trust > 50 (Simulating Smart Contract logic)
        access_status = 1 if trust_level >= 50 else 0
        
        data.append([timestamp, device, trust_level, status, access_status])
    
    df = pd.DataFrame(data, columns=['Timestamp', 'Device_ID', 'Trust_Level', 'Device_Status', 'Access_Status'])
    df.to_csv('uploaded_iot_data.csv', index=False)
    print("Success: 'uploaded_iot_data.csv' created with 100 records.")

if __name__ == "__main__":
    generate_iot_dataset()