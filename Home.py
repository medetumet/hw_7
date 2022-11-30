class Bank:
    def __init__(self, money, name):
        self.__money = money
        self.__name = name

    def setMoney(self, money):
        self.__money=money

    def getMoney(self):
        return self.__money

    def setName(self, name):
        self.__name=name
    def getName(self):
        return self.__name

    def MoneyX(self):
        self.__money += int(input('Введите сумму которую хотите добавить'))

    def _kill(self):
        self. _money = 0

    def __jackpot(self):
        self.__money *= 10


kicb = Bank(0, 'Unknown')
kicb.setName('Unknown')
kicb.setMoney(2000)
print(f'Ваше имя:{kicb.getMoney()} \nНа вашем счету:{kicb.getMoney()}')
print(kicb.MoneyX())
print(kicb._kill())
print(kicb._Bank__jackpot())


print(kicb._Bank__jackpot())









