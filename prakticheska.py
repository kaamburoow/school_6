print("Здравей!")
points = 0
firstQuestion = input("Внимавахте ли в час? ")
secondQuestion = input("Написахте ли си домашното? ")
thirdQuestion = input("Упражнявахте ли се допълнително? ")
fourthQuestion = input("Решихте ли примерните задачи? ")
fifthQuestion = input("Бяхте ли на консултация? ")

if(firstQuestion.lower() == "да"):
    points+=3
if(secondQuestion.lower() == "да"):
    points+=2
if(thirdQuestion.lower() == "да"):
    points+=2
if(fourthQuestion.lower() == "да"):
    points+=3
if(fifthQuestion.lower() == "да"):
    points+=2
print("Оценката ти ще е " + str(points/2))