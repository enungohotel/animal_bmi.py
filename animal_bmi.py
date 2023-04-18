# animal_bmi.py

def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return bmi

weight = float(input("Введите вес животного (в кг): "))
height = float(input("Введите рост животного (в метрах): "))

bmi = calculate_bmi(weight, height)

print("Индекс массы тела животного: ", bmi)
