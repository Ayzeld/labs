a=input("Введите название месяца: ")
match a:
    case "Январь"|"Март"|"Май"|"Июль"|"Август"|"Октябрь"|"Декабрь":
        print(31)
    case"Апрель"|"Июнь"|"Сентябрь"|"Ноябрь":
        print(30)
    case "Февраль":
        print("28 дней (в високосном году 29 дней)")