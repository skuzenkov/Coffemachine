#cappuccino = [50, 30, 70]
#resources = [1000, 1000, 1000] #[water, milk, coffee]
condition = False
MENU = {
    "espresso": {
        "water": 50,
        "coffee": 18,
    },

    "latte": {
        "water": 200,
        "milk": 150,
        "coffee": 24,
    },
    "cappuccino": {
        "water": 250,
        "milk": 100,
        "coffee": 50,
    },
}

resources = {
    "water": 1000,
    "milk": 1000,
    "coffee": 1000,

}


def PowerON():
    global condition
    condition = True


def PowerOFF():
    global condition
    condition = False


def controlMessage():
    print('Для выбора напитка введите "ON"!')
    while True:
        if input() == 'ON':
            print('Машина запущена')
            return PowerON()
        else:
            PowerOFF()
            print('Ошибка ввода, повторите попытку!')


def drink(resources):
    drinks = ['cappuccino', 'latte']
    print('Выберите напиток из предложенных', drinks)
    button = input()
    if button == 'cappuccino':
        if resources["water"] - MENU["cappuccino"]["water"] and resources["coffee"] - MENU["cappuccino"]["coffee"] \
                and resources["milk"] - MENU["cappuccino"]["milk"]:
            print('Напиток готов, израсходовано воды:', MENU["cappuccino"]["water"], ', зерен:', MENU["cappuccino"]["coffee"],
                  ', молока:', MENU["cappuccino"]["milk"])
            print('Остаток воды:', resources["water"]-MENU["cappuccino"]["water"], ', зерен:',
                  resources["coffee"] - MENU["cappuccino"]["coffee"],
                  ', молока:', resources["milk"] - MENU["cappuccino"]["milk"])
            #drink(resources)
            return resources
        #print('Остаток'resources[0]-cappuccino[0], resources[1]-cappuccino[1], resources[2] - cappuccino[2])
        #controlMessage()
        #drink()
        #return resources




    elif button == 'latte':
        print('Латте закончилось')


controlMessage()
drink(resources)