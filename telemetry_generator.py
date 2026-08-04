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
status = "Normal"
with open("telemetry.csv","w",newline="") as file:
    writer = csv.writer(file)
    
    writer.writerow([
        "Time",
        "Temperature",
        "Pressure",
        "Fuel",
        "Altitude",
        "Velocity",
        "Status"
    ])

    for i in range(20):
        if fuel <= 20:
            status = "CRITICAL"
        
        elif fuel <= 50:
            status = "LOW FUEL"
            
        else:
            status = "NORMAL"
        
        print(
            f"Time:{time} | "
            f"Temp:{temperature}°C | "
            f"Pressure:{pressure}kPa | "
            f"Fuel:{fuel}% | "
            f"Altitude:{altitude}m | "
            f"Velocity:{velocity}m/s | "
            f"Status:{status}"
        )

        writer.writerow([
            time,
            temperature,
            pressure,
            fuel,
            altitude,
            velocity,
            status
        ])
        if fuel <= 50:
            print("⚠ LOW FUEL WARNING")

        time += 1

        fuel -= 1

        altitude += random.randint(90,130)

        velocity += random.randint(18,25)

        temperature += random.randint(0,2)

        pressure += random.randint(-1,1)