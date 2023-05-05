score = 0
answer1 = str(input("Внимавахте ли в час? "))
answer2 = str(input("Написахте ли си домашните? "))
answer3 = str(input("Имате ли повече от мн. добър 5.00 на предишното контролно? "))
answer4 = str(input("Извадихте ли си в тетрадка най-важните неща от урока? "))
answer5 = str(input("Споделихте ли интересните неща от урока с приятел? "))
answer6 = str(input("Търсихте ли допълнителна информация по темата? "))

if(answer1.lower() == "да"):
    score+=1
if(answer2.lower() == "да"):
    score+=1
if(answer3.lower() == "да"):
    score+=1
if(answer4.lower() == "да"):
    score+=1
if(answer5.lower() == "да"):
    score+=1
if(answer6.lower() == "да"):
    score+=1

if(score <= 2):
    print("\nОценката ти от контролното ще бъде 2.00\nБъди по-взискателен към себе си!")
else:
    print("\nОценката ти от контролното ще бъде " + str(score) + ".00")