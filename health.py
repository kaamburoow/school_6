print("Здравей!")
points = 0
question1 = input("Добре ли спа? ")
question2 = input("Имаше ли кошмари? ")
question3 = input("Направи ли утринна гимнастика? ")
question4 = input("Закуси ли? ")
question5 = input("Обядва ли топла храна? ")

if(question1.lower() == "да"):
    points+=2
if(question2.lower() == "не"):
    points+=2
if(question3.lower() == "да"):
    points+=2
if(question4.lower() == "да"):
    points+=3
if(question5.lower() == "да"):
    points+=3

if(points <= 8):
    print("Днес не си в добра кондиция.")
else:
    print("Днес си супер!")
