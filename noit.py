import subprocess, platform

print("Здравей!")
name = input("Как се казваш? ")
project = input("Как се казва проекта ти? ")
category = ["Мултимедийни проекти", "Интерактивни проекти"]
choice = int(input("Каква е категорията на проекта ти?\nВ момента олимпиадата има " + str(len(category)) + " категории.\nНапиши 1, ако категорията ти е " + category[0] + ", а ако категорията ти е " + category[1] + " - напиши 2.\nКатегория: "))
print("""
================================
   Национална олимпиада по ИТ
--------------------------------
""", end="")
print("Име:       " + name.capitalize())
print("Проект:    " + project.capitalize())
print("Категория: ", end="")
if choice == 1:
    print(category[0])
    print("================================")
elif choice == 2:
        print(category[1])
        print("================================")
else:
    if platform.system()=="Windows":
        if platform.release() in {"10", "11"}:
            subprocess.run("", shell=True)
            print("\033c", end="")
        else:
            subprocess.run(["cls"])
    else:
        print("\033c", end="")
        print("Моля, въведи правилна категория!")
    raise SystemExit