import json
import time
import numpy as np
import paho.mqtt.client as mqtt
from collections import deque
from sklearn.ensemble import RandomForestClassifier

# Configuration 
BROKER      = "mqtt"
SUB_TOPIC   = "sensors/group17/lighting/data"
CMD_TOPIC   = "sensors/group17/lighting/command"
ALERT_TOPIC = "alerts/group17/lighting/status"
ENERGY_TOPIC= "sensors/group17/lighting/energy"

#  State 
history = deque(maxlen=30)

# Adaptive learning — stores average lux per scene
learned_thresholds = {
    "Night":   50,
    "Morning": 200,
    "Day":     600,
    "Evening": 300
}
scene_samples = {
    "Night":   [],
    "Morning": [],
    "Day":     [],
    "Evening": []
}

# Energy tracking
BASELINE_WATTS  = 60.0   # watts if lights were always 100%
total_saved_wh  = 0.0
last_time       = time.time()

# Train occupancy model with synthetic data 
def train_occupancy_model():
    # Features: [lux, lux_change, hour]
    # Label: 1 = occupied, 0 = empty
    X = [
        # Occupied patterns (lights on, active changes)
        [300, 20, 9],  [400, 15, 10], [350, 25, 11],
        [500, 30, 12], [450, 20, 14], [400, 18, 15],
        [300, 22, 16], [250, 15, 17], [200, 10, 18],
        [150, 12, 19], [100, 8,  20], [120, 10, 21],
        # Empty patterns (stable low or high lux, no changes)
        [10,  1,  2],  [5,   0,  3],  [8,   1,  4],
        [900, 2,  12], [950, 1,  13], [880, 3,  14],
        [20,  0,  1],  [15,  1,  6],  [800, 2,  7],
        [750, 1,  8],  [30,  2,  23], [10,  0,  0],
    ]
    y = [
        1,1,1,1,1,1,1,1,1,1,1,1,
        0,0,0,0,0,0,0,0,0,0,0,0
    ]
    model = RandomForestClassifier(n_estimators=10, random_state=42)
    model.fit(X, y)
    print("Occupancy model trained")
    return model

occupancy_model = train_occupancy_model()

