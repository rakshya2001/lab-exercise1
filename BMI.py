#
height= float(input('Enter height'))
weight=int(input('Enter weight'))
bmi=weight/(height ** 2)
print("The BMI is","bmi", "so ", '=')

# Conditions to find out BMI category
if (bmi < 18.5):
    print("underweight")

elif (bmi >= 18.5 and bmi < 24.9):
    print("Healthy")

elif (bmi >= 24.9 and bmi < 30):
    print("overweight")

elif (bmi >= 30):
    print("Suffering from Obesity")