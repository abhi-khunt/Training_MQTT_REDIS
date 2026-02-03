# 📡 MQTT → Redis TimeSeries (Python)

## 📌 Project Overview
This project demonstrates a **real-time IoT data pipeline** where temperature data is generated, transmitted via **MQTT**, and stored efficiently in **Redis TimeSeries** using Python.

The project simulates a temperature sensor and shows how streaming data can be processed and stored for analytics and monitoring.

---

## 🧩 Project Components

### 1️⃣ `publisher.py`
- Generates random temperature values
- Attaches current timestamp
- Publishes data to an MQTT broker at fixed intervals

### 2️⃣ `subscriber.py`
- Subscribes to MQTT topic
- Receives temperature messages
- Converts timestamp to milliseconds
- Stores data in Redis TimeSeries



