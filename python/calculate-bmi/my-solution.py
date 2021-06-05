def bmi(weight, height):
    bmi_value = weight/pow(height, 2)
    if bmi_value <= 18.5:
        return "Underweight"
    elif bmi_value <= 25.0:
        return "Normal"
    elif bmi_value <= 30.0:
        return "Overweight"
    elif bmi_value > 30:
        return "Obese"


print(bmi(30, 15))
