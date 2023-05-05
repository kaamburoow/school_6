import time

print("Здравей!")
time.sleep(1)
number = int(input("Добави 2 към намисленото число. След това умножи резултата по 5 и добави 15 към него. Най-накрая го умножи по 2 и го напиши тук: "))
guessedNumber = int(number / 10 - 5)
time.sleep(2)
print("Ти си мислиш за числото " + str(guessedNumber) + ".\n\nЧао!\n\nMade by Kamburow")
time.sleep(2.5)