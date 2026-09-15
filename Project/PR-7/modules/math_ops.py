import math

def fact(fact_num):
    result =  math.factorial(fact_num)

    print("\nFactorial Num is:",result)

def calculate_compound_interest(principal, rate, time):
    total_amount = principal * ((1 + (rate / 100)) ** time)
    interest = total_amount - principal

    return round(total_amount, 2), round(interest, 2)

def calculate_trig(angle_deg, function_type):
    rad = math.radians(angle_deg)
    
    if function_type == 1:
        return math.sin(rad)
    elif function_type == 2:
        return math.cos(rad)
    elif function_type == 3:
        if angle_deg % 180 == 90:
            return "Undefined"
        return math.tan(rad)
    return None

def area_circle(radius):
    return math.pi * (radius ** 2)

def area_rectangle(length, width):
    return length * width

def area_triangle(base, height):
    return 0.5 * base * height