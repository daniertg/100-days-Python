height = float(input("Input your height: "))
weight = int(input("Input your weight: "))

bmi = int(round(weight / (height * height), 2))
if bmi >= 18 and bmi < 22:
    print(f"Your BMI is {bmi}, you are underweight.")
elif bmi >= 22 and bmi < 28:
    print(f"Your BMI is {bmi}, you have a normal weight.")
elif bmi >= 28 and bmi < 33:
    print(f"Your BMI is {bmi}, you are slightly overweight.")
elif bmi >= 33 and bmi < 40:
    print(f"Your BMI is {bmi}, you are obese.")
elif bmi >= 40:
    print(f"Your BMI is {bmi}, you are clinically obese.")


