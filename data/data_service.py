def get_balance():
    from_file = [
        "Грошові кошти;290;4,0;21,0;18,0;330,0;269,0",
        "Грошові кошти;300;7,0;40,0;48,0;104,0;271,0",
        "Дебіторська заборгованість;200;7,0;10,0;21,0;122,0;51,0",
        "Дебіторська заборгованість;270;5,0;17,0;40,0;63,0;526,0",
        "Матеріальні обігові кошти;160;396,0;832,0;1818,0;6631,0;19426,0",
        "Матеріальні обігові кошти;120;2,0;3,0;3,0;3,0;6,0",
        "Грошові кошти;310;6,0;58,0;165,0;483,0;850,0",
        "Дебіторська заборгованість;210;1,0;2,0;12,0;25,0;119,0",
        "Дебіторська заборгованість;230;2,0;1,0;1,0;0,3;2,0",
        "Дебіторська заборгованість;240;54,0;3,0;3,0;3,7;2,0",
        "Матеріальні обігові кошти; 170;0,1;4,0;6,0;19,0;61,0",
        "Грошові кошти;320;15,0; 29,0;30,0;117,0;821,0"
    ]

    balance_list = []

    for line in from_file:
        line_list = line.split(';')
        balance_list.append(line_list)

    return balance_list


def show_balance(balance_dump):
    balance_code_from = input("З якого коду рядка балансу?\n")
    balance_code_to   = input("По який?\n")

    for balance in balance_dump:
        if balance_code_from < balance[1] < balance_code_to:
            print("Підрозділ балансу: {:18} Код рядка балансу: {:5} На початок 1кв: {:12} 2кв: {:12} 3кв: {:12} 4кв: {:12} На кінець року: {:15}".format( balance[0], balance[1], balance[2], balance[3], balance[4], balance[5], balance[5]))



balance_dump = get_balance()

show_balance(balance_dump)
