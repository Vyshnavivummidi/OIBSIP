#BMI means BODY MASS INDEX, it is a body fat indicator
#Take inputs from the user
weight = float(input("Enter your weight in kilograms: "))
height = float(input("Enter your height in meters: "))
#Here we are calculating BMI using the BMI formula
bmi = weight/(height ** 2)
#Interpreting the given inputs and displaying the result
if bmi < 18.5:
    Result= "Underweight"
elif 18.5 <= bmi < 24.9:
    Result= "Normal weight"
elif 25 <= bmi < 29.9:
    Result= "Overweight"
else:
    Result= "Obese"
#printing the result
print(f"Your BMI is {bmi:.3f}, which is considered {Result}.")
