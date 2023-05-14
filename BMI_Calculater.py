#BMI CALCULATER
#BMI=WEIGHT(KG)/HEIGHT**2(M2)

height = float(input("enter your height in m: \n"))
height2 = height**2

weight = float(input("enter your weight in kg: \n"))
bmi = round(weight/height2,0)

print(int(bmi))
