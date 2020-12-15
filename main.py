# Case-study #3
# Developers:   Kostylev M. (%),
#               Turchinovich M. (%),
#               Zubareva T. (%).
# This program allows to calculate the amount of capital on the bank deposit after a certain number of years

year = int (input ("Введите срок размещения капитала (лет) "))
capital_rate = float (input ("Введите начальный капитал ($) "))
interest_rate = int (input ("Введите процентную ставку (%/мес.) "))
investment_injection = int (input ("Введите инвестиционные вливания ($/мес.) "))
i = 0
month = 0
while i < year:
    i += 1
    print(i, "год")
    print("----------------------------------------------")
    print("|         |   основа   |  сумма %  |          |")
    print("|  месяц  | инвестиций | за месяц  | капитал  |")
    print("-----------------------------------------------")
    print("|    1    |            |           |          |")
    print("|    2    |            |           |          |")
    print("|    3    |            |           |          |")
    print("|    4    |            |           |          |")
    print("|    5    |            |           |          |")
    print("|    6    |            |           |          |")
    print("|    7    |            |           |          |")
    print("|    8    |            |           |          |")
    print("|    9    |            |           |          |")
    print("|    10   |            |           |          |")
    print("|    11   |            |           |          |")
    print("|    12   |            |           |          |")
    print("-----------------------------------------------")






