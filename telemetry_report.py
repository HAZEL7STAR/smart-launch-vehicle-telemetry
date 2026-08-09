import pandas as pd

data = pd.read_csv("telemetry.csv")

print("===== TELEMETRY REPORT =====")

print()

print("Highest Altitude :", data["Altitude"].max())

print("Lowest Fuel :", data["Fuel"].min())

print("Average Temperature :", data["Temperature"].mean())

print("Maximum Velocity :", data["Velocity"].max())

print()

print("Critical Fuel Readings")

print(data[data["Fuel"] < 50]) 