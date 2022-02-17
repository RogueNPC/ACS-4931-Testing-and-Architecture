import math

T_HALF = 5730
DECAY_CONSTANT = -0.693

# TODO: Write a unit test which feed 0.35 to the function.
# The result should be '8680.34'.
    # - Does the function handle every possible input correctly?
    # - What if the input is zero or negative?
    # - Add the necessary logic to make sure the function handle every possible input properly. Then write a unit test against this special case.

def get_age_carbon_14_dating(carbon_14_ratio):
    """Returns the estimated age of the sample in year.
    carbon_14_ratio: the percent (0 < percent < 1) of carbon-14
    in the sample conpared to the amount in living
    tissue (unitless).
    """
    if not carbon_14_ratio > 0:
        return "Error, your carbon_14_ratio must be greater than 0."

    return math.log(carbon_14_ratio) / DECAY_CONSTANT * T_HALF
