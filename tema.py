import random

print("ЗдравеЙ!")
theme=["Летни приключения", "Есенно благоденствие", "Празнични небивалици", "Котешки истории", "Зимни приключения"]
themeRange=random.randint(0, (len(theme)-1))
print(themeRange)
print("Твоята тема е: " + theme[themeRange] + ".")