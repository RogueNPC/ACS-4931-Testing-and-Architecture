# Written by Kamran Bigdely
# Example for Compose Methods: Extract Method.
import math

def generate_grades():
    # Generates grades from user input
    grade_list = []
    students = 5
    for i in range(students):
        grade_list.append(int(input('Enter a number: ')))
    return grade_list

def calculate_mean():
    # Calls helper function above
    grade_list = generate_grades()

    # Calculates the mean of the grades
    grade_total = 0
    for grade in grade_list:
        grade_total += grade
    mean = grade_total / len(grade_list)

    # Calculates the standard deviation of the grades
    std_dev = 0
    sum_of_sqrs = 0
    for grade in grade_list:
        sum_of_sqrs += (grade - mean) ** 2
    std_dev = math.sqrt(sum_of_sqrs / len(grade_list))

    return mean, std_dev

def print_grade_stats():
    mean, std_dev = calculate_mean()
    # print out the mean and standard deviation in a nice format.
    print("The grades's mean is:", mean)
    print('The population standard deviation of grades is: ', round(std_dev, 3))

print_grade_stats()
