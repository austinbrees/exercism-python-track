"""Functions to prevent a nuclear meltdown."""


def is_criticality_balanced(temperature, neutrons_emitted):
   if temperature < 800 and neutrons_emitted > 500 and temperature * neutrons_emitted < 500000:
       return True
   else:
       return False
  


def reactor_efficiency(voltage, current, theoretical_max_power):
    green = "green"
    orange = "orange"
    red = "red"
    black = "black"
    generated_power = voltage * current
    efficiancy_percentage = float((generated_power/theoretical_max_power) * 100)
    
    if efficiancy_percentage >= 80:
        return green
    elif efficiancy_percentage <= 80 and efficiancy_percentage >= 60:
        return orange
    elif efficiancy_percentage <=60 and efficiancy_percentage >= 30:
        return red
    else:
        return black
   


def fail_safe(temperature, neutrons_produced_per_second, threshold):
    value = temperature * neutrons_produced_per_second
    if value < (threshold * .9):
        return "LOW"
    elif value >= (threshold * .9) and value <= (threshold * 1.1):
        return "NORMAL"
    else:
        return "DANGER"
 
