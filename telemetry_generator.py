import random
import csv

time = 0
temperature = 25
pressure = 101
fuel = 100
altitude = 0
velocity = 0

print(time)
print(temperature)
print(pressure)
print(fuel)
print(altitude)
print(velocity)

print("\nTelemetry Simulation Starts\n")
with open("telemetry.csv","w",newline="") as file:
    writer = csv.writer(file)

    writer.writerow(["Time","Fuel","Altitude"])

    for i in range(20):
        print(f"Time:{time} Fuel:{fuel}% Altitude:{altitude}m")

        writer.writerow([time, fuel, altitude])

        time += 1
        fuel -= 1
        altitude += random.randint(90,130)