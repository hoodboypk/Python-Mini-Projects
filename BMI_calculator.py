height = float(input("Enter your height in meters: "))
weight = float(input("Enter your weight in kgs: "))

cal_bmi = weight/(height**2)
bmi = round(cal_bmi,2)

print("Your BMI is: " + str(bmi))

if (bmi <= 18.5):
    print("You are underweight.")
elif(bmi > 18.5 and bmi <= 25):
    print("You are normal weight.")
elif(bmi > 25 and bmi <=30):
    print("You are overweight.")
elif(bmi > 30):
    print("You are obese.")
