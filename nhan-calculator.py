import matplotlib
import requests
from matplotlib import pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime, timedelta
from random import randint


def get_values(sensor_id, readings):
    out = {
        "original": [],
        "prediction": []
    }
    prev_value = 0
    for v in readings[0]:
        if v["sensor_id"] == sensor_id:
            prev_value = v["value"]
            break

    for v in readings[0]:
        if v["sensor_id"] == sensor_id:
            # get real value
            out["original"].append(v["value"])

            # get corresponding prediction
            deviation = abs(v["value"]-prev_value)
            x = randint(0, 7)
            if x < 3:
                out["prediction"].append(v["value"] + deviation)
            elif 2 < x <= 5:
                out["prediction"].append(v["value"] - deviation)
            else:
                out["prediction"].append(v["value"])
            prev_value = v["value"]


    return out

plt.style.use("ggplot")


server_ip = "192.168.4.137"

# Fetch data from the server
r = requests.get(f"http://{server_ip}/readings")
data = r.json()
readings = data.get("readings", [])

# Sensor IDs
temp_bme_id = 326
temp_dht_id = 327
hum_bme_id = 329
hum_dht_id = 328
pres_id = 330

# Retrieve values
temp_bme = get_values(temp_bme_id, readings)
temp_dht = get_values(temp_dht_id, readings)
hum_bme = get_values(hum_bme_id, readings)
hum_dht = get_values(hum_dht_id, readings)
pressure = get_values(pres_id, readings)

temp_values_bme = temp_bme["prediction"]
temp_values_dht = temp_dht["prediction"]
hum_values_bme = hum_bme["prediction"]
hum_values_dht = hum_dht["prediction"]
pres_values = pressure["prediction"]

temp_values_original_bme = temp_bme["original"]
temp_values_original_dht = temp_dht["original"]
hum_values_original_bme = hum_bme["original"]
hum_values_original_dht = hum_dht["original"]
pres_values_original = pressure["original"]

# Convert start time to datetime
start_time_str = "00:00"  # 24-hour format
start_time = datetime.strptime(start_time_str, "%H:%M")

# Generate timestamps as datetime objects
timestamps = [start_time + timedelta(minutes=i) for i in range(len(hum_values_bme))]

# Create a single figure for overlayingw
plt.figure(figsize=(10, 9))

# Overlay Temperature
plt.subplot(3, 1, 1)
plt.plot(timestamps, hum_values_bme, marker="o", linestyle="-", color="y",
         label="BME Temp (Current)", linewidth=0.8, markersize=4)

plt.show()
