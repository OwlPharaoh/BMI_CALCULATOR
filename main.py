name = (input("Enter Patient's Name: "))
height_m = float(input("Enter Height(in metres): "))
weight_kg = float(input("Enter Weight(in kilograms): "))
ab = weight_kg/(height_m ** 2)
BMI_val = round (ab, 2)
print("The BMI of",name, "is", BMI_val)

if BMI_val <= 18.5:
    print (name.upper() + " is Underweight".upper())
    print("A BMI of less than 18.5 indicates that you are underweight, so you may need to put on some weight. You are recommended to ask your doctor or a dietitian for advice.")
elif BMI_val >= 18.5 and BMI_val <= 24.9:
    print (name.upper() + " is Healthy".upper())
    print("A BMI of 18.5-24.9 indicates that you are at a healthy weight for your height. By maintaining a healthy weight, you lower your risk of developing serious health problems.")
elif BMI_val >= 25 and BMI_val <= 29.9:
    print(name.upper() + " is Overweight".upper())
    print("A BMI of 25-29.9 indicates that you are slightly overweight. You may be advised to lose some weight for health reasons. You are recommended to talk to your doctor or a dietitian for advice.")
else:
    print(name.upper() + " is Obese".upper())
    print("A BMI of over 30 indicates that you are heavily overweight. Your health may be at risk if you do not lose weight. You are recommended to talk to your doctor or a dietitian for advice.")
