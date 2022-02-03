# By Kami Bigdely
# Remove assignment to method parameter.

class Distance:
    def __init__(self, dis_value, dis_unit):
        self.dis_unit = dis_unit
        self.dis_value = dis_value

class Mass:
    def __init__(self, mass_value, mass_unit):
        self.mass_value = mass_value
        self.mass_unit = mass_unit

def calculate_kinetic_energy(mass, distance, time):
    if distance.dis_unit != 'km':
        if distance.dis_unit == "ly":  # [ly] stands for light-year (measure of distance in astronomy)
            # convert from light-year to km unit
            in_km = distance.dis_value * 9.461e12
            in_km_distance = Distance(in_km, "km")
        else:
            print ("unit is Unknown")
            return

    km_per_sec = in_km_distance.dis_value/time # [km per sec]
    if mass.mass_unit != 'kg':
        if mass.mass_unit == "solar-mass":
            # convert from solar mass to kg
            kg = mass.mass_value * 1.98892e30 # [kg]
            kg_mass = Mass(kg, 'kg')
        else:
            print ("unit is Unknown")
            return

    kinetic_energy = 0.5 * kg_mass.mass_value * km_per_sec ** 2
    return kinetic_energy

mass = Mass(2, "solar-mass")
distance = Distance(2, 'ly')
print(calculate_kinetic_energy(mass, distance, 3600e20))
