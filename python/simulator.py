import time
import random
import math
import json
import paho.mqtt.client as mqtt

# ─── Configuration ───────────────────────────────────────────
BROKER = "mqtt"
TOPIC  = "sensors/group17/lighting/data"

# ─── Connect to MQTT ─────────────────────────────────────────
client = mqtt.Client()
client.connect(BROKER, 1883, 60)

print("✅ Simulator started — publishing light sensor data...")

t = 0
while True:
    # 1. Simulate day/night cycle (lux 0–1000)
    hour_of_day = (t % 720) / 720 * 24
    base_lux    = 500 + 450 * math.sin((hour_of_day - 6) * math.pi / 12)
    base_lux    = max(0, base_lux)
    
    # 2. Add realistic noise
    noise = random.uniform(-30, 30)
    lux   = base_lux + noise
    
    t += 1
    time.sleep(3)