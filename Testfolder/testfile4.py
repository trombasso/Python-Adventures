class Account:
    def __init__(self, id=0, balance=0, annualInterestRate=0):
        self.__id = int(id)
        self.__balance = float(balance)
        self.__annualInterestRate = float(annualInterestRate)

    @property
    def id(self):
        pass

    @property
    def balance(self):
        pass

    @property
    def annualInterestRate(self):
        pass

    @id.setter
    def id(self):
        pass

    @balance.setter
    def balance(self):
        pass

    @annualInterestRate.setter
    def annualInterestRate(self):
        pass

    def getMonthlyInterestRate(self):
        pass

    def getMonthlyInterest(self):
        pass

    def withdraw(self):
        pass

    def deposit(self):
        pass


def main():
    ...


if __name__ == "__main__":
    main()
