# Case-study #3
# Developers:   Kostylev M. (%),
#               Turchinovich M. (%),
#               Zubareva T. (%).
# This program allows to calculate the amount of capital on the bank deposit after a certain number of years

year = int(input("Введите срок размещения капитала (лет) "))
capital_rate = float(input("Введите начальный капитал ($) "))
interest_rate = int(input("Введите процентную ставку (%/мес.) "))
investment_inj = int(input("Введите инвестиционные вливания ($/мес.) "))
i = 0
month = 0
capital = 0
while i < year:
    i += 1
    month += 1
    print(i, "год")
    print("----------------------------------------------")
    print("|         |   основа   |  сумма %  |          |")
    print("|  месяц  | инвестиций | за месяц  | капитал  |")
    print("-----------------------------------------------")
    for month in range (1,13):
        if month == 1 and i == 1:
            invest_base = capital_rate
        else:
            invest_base = capital + investment_inj
        int_month = invest_base * interest_rate * 0.01
        capital =  invest_base + int_month
        print("|   ", month,  "|   ",  invest_base, "|   ", int_month, "|   ",capital,   "|")

    print("-----------------------------------------------")






