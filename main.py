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





