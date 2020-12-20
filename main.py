# Case-study #3
# Developers:   Kostylev M. (35%),
#               Turchinovich M. (40%),
#               Zubareva T. (35%).
# This program allows to calculate the amount of capital on the bank deposit after a certain number of years

year = int(input("Введите срок размещения капитала (лет) "))
capital_rate = float(input("Введите начальный капитал ($) "))
interest_rate = int(input("Введите процентную ставку (%/мес.) "))
investment_inj = int(input("Введите инвестиционные вливания ($/мес.) "))
i = 0
month = 0
capital = 0
# create a table
while i < year:
    i += 1
    month += 1
    print(i, "год")
    print("-----------------------------------------------")
    print("|         |   основа   |  сумма %  |           |")
    print("|  месяц  | инвестиций | за месяц  | капитал   |")
    print("-----------------------------------------------")
    for month in range (1,13):
        if month == 1 and i == 1:
            invest_base = capital_rate
        else:
            invest_base = capital + investment_inj
        int_month = invest_base * interest_rate * 0.01  # calculate the amount of interest for the month
        capital = invest_base + int_month  # count the capital

        # make out the first column
        print ('|', end = '')
        for j in range (1, 6 - len (str (month))):
            print (' ', end ='')
        print (month, end = '')
        for j in range (1,5):
            print (' ', end = '')
        print ('|', end = '')

        # make out the second column
        for j in range (1, 9 -  len(str('%.2f' % (invest_base)))):
            print (' ', end = '')
        print ('%.2f' % (invest_base), end = '')
        if len (str ('%.2f' % (invest_base))) <= 8:
            print ('    |', end = '')
        elif len (str ('%.2f' % (invest_base))) == 9:
            print ('   |', end = '')
        elif len(str('%.2f' % (invest_base))) == 10:
            print ('  |', end = '')
        elif len(str('%.2f' % (invest_base))) == 11:
            print (' |', end = '')
        else:
            print ('|', end = '')

        # make out the third column
        for j in range (1, 9 -  len(str('%.2f' % (int_month)))):
            print (' ', end = '')
        print ('%.2f' % (int_month), end = '')
        if len (str ('%.2f' % (int_month))) <= 8:
            print ('   |', end = '')
        elif len (str ('%.2f' % (int_month))) == 9:
            print ('  |', end = '')
        elif len(str('%.2f' % (int_month))) == 10:
            print (' |', end = '')
        else:
            print ('|', end = '')

        # make out the fourth column
        for j in range (1, 9 -  len(str('%.2f' % (capital)))):
            print (' ', end = '')
        print ('%.2f' % (capital), end = '')
        if len (str ('%.2f' % (capital))) <= 8:
            print ('   |', end = '')
        elif len(str('%.2f' % (capital))) == 9:
            print('  |', end='')
        elif len(str('%.2f' % (capital))) == 10:
            print (' |', end = '')
        else:
            print ('|', end = '')
        print ()

    print("-----------------------------------------------")






