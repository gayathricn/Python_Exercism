"""Functions to prevent a nuclear meltdown."""


def is_criticality_balanced(temperature, neutrons_emitted):
    return (temperature < 800 and neutrons_emitted > 500 and temperature * neutrons_emitted < 500000)


def reactor_efficiency(voltage, current, theoretical_max_power):
    generated_power = voltage * current
    efficiency = (generated_power/theoretical_max_power)*100
    if efficiency >= 80:
        return 'green'
    elif efficiency >= 60 and efficiency < 80:
        return 'orange'
    elif efficiency >= 30 and efficiency < 60:
        return 'red'
    else:
        return 'black'

def fail_safe(temperature, neutrons_produced_per_second, threshold):
    output = temperature * neutrons_produced_per_second
    lower_bound = 0.9 * threshold
    upper_bound = 1.1 * threshold
    if output < lower_bound:
        return 'LOW'
    elif lower_bound <= output <= upper_bound:
        return 'NORMAL'
    else:
        return 'DANGER'