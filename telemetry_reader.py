import csv

with open("telemetry.csv", "r") as file:
    reader = csv.reader(file)

    next(reader)

    for row in reader:
        time = int(row[0])
        fuel = int(row[3])
        altitude = int(row[4])
        temperature=int

        print(time)
        print(fuel)
        print(altitude)
        if fuel < 90:
            print("Low Fuel")
        print("------------")
         