MENU = {
    "cappuccino": {
        "water": 100,
        "milk": 150,
        "coffee": 50,
    },
    "espresso": {
        "water": 100,
        "milk": 0,
        "coffee": 30,
    },
    "americano": {
        "water": 100,
        "milk": 0,
        "coffee": 10,
    },
    "latte": {
        "water": 100,
        "milk": 150,
        "coffee": 50,
    },
}

resources = {
    "water": 1000,
    "milk": 1000,
    "coffee": 1000,

}

condition = False


# Возвращает всегда True
def PowerON():
    global condition
    condition = True
    return condition


# Возвращает всегда False
def PowerOFF():
    global condition
    condition = False
    return condition

# Возвращает состояние!
def isPower():
    global condition
    return condition



# Проверяем пользовательский ввод и выключаем/выключаем машинку
def controlPowerAndPringMessage(input):
    if input == 'ON':
        print('Кофемашина запущена')
        PowerON()
    elif input == 'OFF':
        print('Кофемашина выключена')
        PowerOFF()
    else:
        print('Неизвестная команда')


#блок вычисления cappuccino/espresso/latte/americano
def printDrinkInformation(selectDrink):
    global MENU
    global resources


    lastWater = resources["water"] - MENU[selectDrink]["water"]
    coffeLast = resources["coffee"] - MENU[selectDrink]["coffee"]
    milkLast = resources["milk"] - MENU[selectDrink]["milk"]
    cancel(lastWater, coffeLast, milkLast)

    print('Напиток', selectDrink, 'готов!')
    print('1. Израсходовано воды:', MENU[selectDrink]["water"])
    print('2. Израсходовано зерен:', MENU[selectDrink]["coffee"])
    print('3. Израсходовано молока:', MENU[selectDrink]["milk"])

    updateConsumers(lastWater, coffeLast, milkLast)



#расход ресурсов
def cancel(lastWater, coffeLast, milkLast):


        if lastWater and coffeLast and milkLast > 0:
            print("Остаток воды:", lastWater, "зерен:", coffeLast, "молока:", milkLast)
            updateConsumers(lastWater, coffeLast, milkLast)
        else:
            if lastWater < 150:
                print("Для приготовления не хватает, воды:", -lastWater)
            elif coffeLast < 50:
                    print("Для приготовления не хватает, зерен:", -coffeLast)
            elif milkLast < 150:
                    print("Для приготовления не хватает, молока:", -milkLast)
            refill()
            #print("Для приготовления не хватает, воды:", -lastWater, "зерен:", -coffeLast, "молока:", -milkLast)



def refill():
    print('Ресурсов для приготовления не достаточно!')
    #print('Приготовление невозможно, один из расходников нужно пополнить')
    #print('Для пополнения расходников нажмите "ON"/"exit" для завершения работы!')
    print('Пополните запасы и перезапустите устройство кнопкой "exit"')
    text = input()
    if text == 'exit':
        exit(0)
        PowerOFF()
    elif text == 'ON':
        print('Запасы пополнены!')
        selectDrink()

    else:
        print('Ошибка, попробуйте еще раз!')
        refill()
    #lastWater = resources["water"] == 1000
    #coffeLast = resources["coffee"] == 1000
    #milkLast = resources["milk"] == 1000
    #print("Остаток воды:", lastWater, "зерен:", coffeLast, "молока:", milkLast)




def updateConsumers(water, coffee, milk):
    resources["water"] = water
    resources["coffee"] = coffee
    resources["milk"] = milk


#выбор напитков
def selectDrink():
    print('Выбери напиток:"cappuccino"/"espresso"/"latte"/"americano"')
    slectDrink = input()
    if slectDrink == 'cappuccino':
        printDrinkInformation(slectDrink)
    elif slectDrink == 'espresso':
        printDrinkInformation(slectDrink)
    elif slectDrink == 'latte':
        printDrinkInformation(slectDrink)
    elif slectDrink == 'americano':
        printDrinkInformation(slectDrink)
    else:
        print('Ошибка попробуй еще раз !')



def makeCoffe():
    print('Для включения машинки введите "ON"/"OFF" для выключения!')
    print('Введите "exit" для завершения работы!')
    while True:
        if (isPower()):
            selectDrink()
            continue

        userInput = input()
        if userInput == 'exit':
            exit(0)
            PowerOFF()

        elif (not isPower()):
            controlPowerAndPringMessage(userInput)
            if (isPower()):
                selectDrink()


makeCoffe()



