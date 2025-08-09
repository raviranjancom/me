temperature = float(input("Enter the temperature : "))
unit=input("Enter C/F : ")

if(unit=="C"):
    temperature=(9/5*temperature)+32
    temperature=round(temperature,2)
    print(f"The temperature = {temperature} F")
else:
    temperature=5/9*(temperature-32)
    temperature=round(temperature,2)
    print(f"The temperature = {temperature} C")
