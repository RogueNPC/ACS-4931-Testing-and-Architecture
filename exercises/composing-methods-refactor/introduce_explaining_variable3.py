# by Kami Bigdely
# Extract Variable (alias introduce explaining variable)
WELL_DONE = 900000
MEDIUM = 600000
COOKED_CONSTANT = 0.05

def is_cooking_correctly(time, temperature, pressure, desired_state):
    cook_state = time * temperature * pressure * COOKED_CONSTANT

    if desired_state == 'well-done' and cook_state >= WELL_DONE: 
        return True
    elif desired_state == 'medium' and cook_state >= MEDIUM:
        return True
    else:
        return False