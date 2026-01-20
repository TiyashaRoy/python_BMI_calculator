print("=== BMI CALCULATOR ===")

weight = float(input("Enter your weight in kg: ")) 
height = float(input("Enter your height in meters: "))

bmi = weight / (height ** 2)

print("\nYour BMI is:", bmi)

if bmi < 18.5:
    print("You are Underweight.")
elif bmi >= 18.5 and bmi < 24.9:
    print("You are Normal weight.")
elif bmi >= 25 and bmi < 29.9:
    print("You are Overweight.")
else:
    print("You are Obese.")
