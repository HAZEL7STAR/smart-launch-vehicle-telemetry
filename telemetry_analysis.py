# 1. Imports

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns


# 2. Load telemetry data

data = pd.read_csv("telemetry.csv")


# 3. Basic analysis

print("Average Temperature:", data["Temperature"].mean())
print("Average Fuel:", data["Fuel"].mean())
print("Maximum Altitude:", data["Altitude"].max())
print("Maximum Velocity:", data["Velocity"].max())
correlation = data.corr(numeric_only=True)

print(correlation)
plt.figure(figsize=(10,6))

sns.heatmap(
    correlation,
    annot=True
)

plt.title("Telemetry Correlation Matrix")
plt.show()

# 4. Diagnostic function

def check_status(temp, fuel):

    if temp > 45:
        return "CRITICAL"

    elif temp >= 40 or fuel < 80:
        return "WARNING"

    else:
        return "NORMAL"


# 5. Generate diagnostic

data["Diagnostic"] = data.apply(
    lambda row: check_status(row["Temperature"], row["Fuel"]),
    axis=1
)
temperature_by_status = data.groupby("Diagnostic")["Temperature"].mean()

print(temperature_by_status)
temperature_sorted = data.sort_values(
    by="Temperature",
    ascending=False
)

print(temperature_sorted[["Time", "Temperature", "Diagnostic"]])

# 6. Diagnostic summary

print(data["Diagnostic"].value_counts())


# 7. Diagnostic distribution graph

counts = data["Diagnostic"].value_counts()

plt.figure(figsize=(10,5))

plt.bar(counts.index, counts.values)

plt.xlabel("Diagnostic Status")
plt.ylabel("Number of Readings")
plt.title("Telemetry Diagnostic Distribution")
plt.grid()
plt.show()


# 8. Temperature graph

plt.figure(figsize=(10,5))

plt.plot(
    data["Time"],
    data["Temperature"],
    marker="o",
    label="Temperature"
)

plt.axhline(40, label="Warning Threshold")
plt.axhline(45, label="Critical Threshold")

plt.xlabel("Time")
plt.ylabel("Temperature")
plt.title("Temperature vs Time")
plt.grid()
plt.legend()
plt.show()


# 9. Fuel graph

plt.figure(figsize=(10,5))

plt.plot(
    data["Time"],
    data["Fuel"],
    marker="o",
    label="Fuel"
)

plt.axhline(80, label="Fuel Warning Threshold")

plt.xlabel("Time")
plt.ylabel("Fuel")
plt.title("Fuel vs Time")
plt.grid()
plt.legend()
plt.show()


# 10. Altitude graph

plt.figure(figsize=(10,5))

plt.plot(
    data["Time"],
    data["Altitude"],
    marker="o",
    label="Altitude"
)

plt.xlabel("Time")
plt.ylabel("Altitude")
plt.title("Altitude vs Time")
plt.grid()
plt.legend()
plt.show()


# 11. Velocity graph

plt.figure(figsize=(10,5))

plt.plot(
    data["Time"],
    data["Velocity"],
    marker="o",
    label="Velocity"
)

plt.xlabel("Time")
plt.ylabel("Velocity")
plt.title("Velocity vs Time")
plt.grid()
plt.legend()
plt.show()