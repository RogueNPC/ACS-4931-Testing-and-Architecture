# By Kami Bigdely
# Decompose conditional
# Reference: https://www.healthline.com/health/high-cholesterol/levels-by-age

# Blood test analysis program
total_cholostrol = 70
ldl = 30
triglyceride = 120

def start_tlc_diet():
    print("Start TLC diet")
    print("Under this meal plan, only 7 percent of your daily calories \nshould come from saturated fat.")
    print('Some foods help your digestive tract absorb less cholesterol. For example,\nyour doctor may encourage you to eat more:')
    print('oats, barley, and other whole grains.')
    print('fruits such as apples, pears, bananas, and oranges.')

def check_cholostrol(total_cholostrol, ldl, triglyceride):
    if total_cholostrol < 200 and ldl < 100 and triglyceride < 150:
        return 'good level'
    elif total_cholostrol > 240 or ldl > 160 or triglyceride >= 200:
        return 'high cholestrol'
    elif total_cholostrol >= 200 or ldl > 130 or triglyceride >= 150:
        return 'borderline to moderate'
    return

if check_cholostrol(total_cholostrol, ldl, triglyceride) == 'good level':
    # good level
    print('*** Good level of cholestrol ***')
elif check_cholostrol(total_cholostrol, ldl, triglyceride) == 'high cholestrol':
    # High cholestrol level
    print('*** High cholestrol level ***')
    start_tlc_diet()
elif check_cholostrol(total_cholostrol, ldl, triglyceride) == 'borderline to moderate':
    #TLC_diet
    print('*** Borderline to moderately elevated ***')
    start_tlc_diet()
else:
    print('Error: unhandled case.')
