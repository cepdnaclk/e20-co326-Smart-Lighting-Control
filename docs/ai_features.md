# AI Features Documentation

This system implements **five AI-driven features** to enable intelligent lighting control using real-time sensor data. These features combine rule-based logic, machine learning, and statistical methods to optimize brightness, detect anomalies, and improve energy efficiency.

---

## 1. Scene Detection (Context Awareness)

### Description
Scene detection determines the current environmental context based on the **time of day**. This allows the system to adapt lighting behavior to natural human activity patterns.

### Logic
The system divides the day into four scenes:
- **Night**: 22:00 – 05:59
- **Morning**: 06:00 – 09:59
- **Day**: 10:00 – 16:59
- **Evening**: 17:00 – 21:59

### Purpose
- Provides context-aware lighting control
- Enables scene-specific learning and optimization

---

## 2. Adaptive Learning (Self-Learning Thresholds)

### Description
The system continuously learns the **average light intensity (lux)** for each scene and updates its internal thresholds dynamically.

### How it Works
- Stores recent lux values for each scene (up to 20 samples)
- Computes the **mean lux value**
- Updates the scene threshold using:
  threshold = average(lux_samples)

### Purpose
- Adapts to different environments automatically
- Improves accuracy over time
- Eliminates need for manual calibration

---

## 3. Smart Brightness Control

### Description
Brightness is automatically adjusted based on:
- Current lux level
- Learned scene threshold

### Formula
brightness = (1 - lux / threshold) * 100


### Behavior
- High ambient light → Lower brightness
- Low ambient light → Higher brightness
- Output is clamped between 0% and 100%

### Purpose
- Maintains comfortable lighting levels
- Reduces unnecessary energy usage

---

## 4. Anomaly Detection (Z-Score Based)

### Description
Detects abnormal lighting conditions using statistical analysis.

### Method
- Maintains a rolling history of lux values
- Computes:
  - Mean (μ)
  - Standard deviation (σ)
- Calculates Z-score:
Z = |lux - μ| / σ


### Detection Rules
- **Z > 3** → Anomaly detected
- If lux < mean → **BLACKOUT**
- If lux > mean → **FLASH**

### Purpose
- Detects sudden failures or unusual events
- Triggers alerts via MQTT
- Improves system reliability

---

## 5. Occupancy Prediction (Machine Learning)

### Description
Predicts whether a space is **occupied or empty** using a trained model.

### Model
- Algorithm: **Random Forest Classifier**
- Features:
- Current lux
- Change in lux
- Hour of day

### Output
- `"occupied"`
- `"empty"`
- `"unknown"` (if insufficient data)

### Purpose
- Enables intelligent automation
- Avoids lighting empty spaces
- Improves energy efficiency

---

## 6. Energy Saving Calculator

### Description
Tracks real-time and cumulative energy savings compared to a baseline.

### Assumptions
- Baseline power = **60W (100% brightness)**

### Calculations
- Actual power: actual = baseline * (brightness / 100)
- Saved power: saved = baseline - actual
- Total energy saved (Wh): total += saved * elapsed_time

### Output Metrics
- Current power usage (W)
- Saved power (W)
- Total energy saved (Wh)
- Saving percentage (%)

### Purpose
- Quantifies system efficiency
- Provides measurable impact of AI decisions

---