import psutil

def batterystatus():
    battery = psutil.sensors_battery()

    battery_perct = battery.percent
    batter_power_plugged = battery.power_plugged

    return battery_perct, batter_power_plugged

# print(f"Battery percentage = {batterystatus()[0]}")
# if batterystatus()[1]:
#     print("System plugged in to power")
# else:
#     print("System not plugged in to power")