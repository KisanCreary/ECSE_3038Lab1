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


