def convert_temp(temp_val, temp_unit):
    if temp_unit == "F":
        temperatures = {
            "Farenheit": temp_val,
            "Celsius": int((temp_val - 32) / 1.8),
            "Kelvin": int((temp_val + 459.67) / 1.8)
        }
    elif temp_unit == "C":
        temperatures = {
            "Celsius": temp_val,
            "Fahrenheit": int(temp_val * 1.8 + 32),
            "Kelvin": int(temp_val  + 273.15)
        }
    else:
        temperatures = {
            "Kelvin": temp_val,
            "Celsius": int(temp_val - 273.15),
            "Fahrenheit": int(temp_val * 1.8 - 459.67)
        }
    for unit, temp in temperatures.items():
        print(f"{unit}: {temp}")

while True:
    temp_val = input("Enter a temperature or 'q' to quit: ")
    if temp_val.lower() == 'q':
        break
    try:
        temp_val = int(temp_val)
        temp_unit = input("What is the temperature unit? (K)elvin, (F)arenheit, or (C)elsius: ").capitalize()
        if temp_unit in ['F', 'C', 'K']:
            convert_temp(temp_val, temp_unit)
        else:
            print("Enter a Valid Temperature Unit!")
    except:
        print("Enter Valid Temperature!")
