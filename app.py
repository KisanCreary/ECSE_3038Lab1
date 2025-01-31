def parallel(resistances):
    total_reciprocal = 0

    for resistance in resistances:

        total_reciprocal += 1 / resistance

    total_resistance = 1 / total_reciprocal

    print(f"{total_resistance:.3f} ohms")

parallel([330, 1000, 2200])

def potential_divider(voltage, resistances):

    total_resistance = sum(resistances) 

    for resistance in resistances:

        voltage_drop = voltage * (resistance / total_resistance)
        
        print(f"{voltage_drop:.2f}v")

potential_divider(9, [3000, 1000])


def temperature_check(temperature, unit):
    if unit == "C":
        if temperature < 35:
            print("The patient is hypothermic.")
        elif 36.5 <= temperature <= 37.5:
            print("The patient's temperature is normal.")
        else:
            print("The patient is hyperthermic.")
    elif unit == "F":
        if temperature < 95:
            print("The patient is hypothermic.")
        elif 97.7 <= temperature <= 99.5:
            print("The patient's temperature is normal.")
        else:
            print("The patient is hyperthermic.")
    else:
        print("Invalid temperature unit. Please use 'C' for Celsius or 'F' for Fahrenheit.")

# Testing with the function with the examples
temperature_check(14, "C")  # "The patient is hypothermic"
temperature_check(37, "C")  # "The patient's temperature is normal"
temperature_check(37, "F")  # "The patient is hypothermic"



