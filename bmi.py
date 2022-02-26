Height=float(input("m: "))
Weight=float(input("kg: "))
BMI=Weight/(Height*Height)
if BMI<18.5:
    print("UnderWeight")
elif 18.5<=BMI<=24.9:
    print("Normal")
elif 25<=BMI<=29.9:
    print("OverWeight")
elif 30<=BMI<=34.9:
    print("Obese")
else:
    print("Extremely Obese")