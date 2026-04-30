# AI Features (Summary)

This system uses 5 AI-based features for smart lighting control:

## 1. Scene Detection
Determines time-based context (Night, Morning, Day, Evening) using the hour to adjust lighting behavior.

## 2. Adaptive Learning
Learns average lux values per scene and updates thresholds dynamically for better accuracy over time.

## 3. Smart Brightness Control
Adjusts brightness based on ambient light:
- More daylight → lower brightness
- Less light → higher brightness

## 4. Anomaly Detection
Uses Z-score to detect abnormal lighting:
- Sudden drop → BLACKOUT
- Sudden spike → FLASH

## 5. Occupancy Prediction
Uses a Random Forest model to predict whether a space is occupied based on lux, changes, and time.

## 6. Energy Saving
Calculates power usage and tracks total energy saved compared to a 60W baseline.

---

**Result:** Intelligent, adaptive, and energy-efficient lighting system.