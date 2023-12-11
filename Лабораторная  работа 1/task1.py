# TODO Написать 3 класса с документацией и аннотацией типов
import doctest

class Car:
    def init(self, name: str, color: str):
        """
        :param name: название марки
        :param color: цвет машины
        """
        self.name = name
        self.color = color

    def move(self):
        """
        Метод, описывающий движение машины
        >>> car = Car("Машина", "Красный")
        >>> car.move()
        """
        ...

    def stop(self):
        """
        Метод, описывающий остановку машины
        """
        ...


class Pet:
    def init(self, name: str, age: int, breed: str):
        """
        :param name: имя питомца
        :param age: возраст питомца
        :param breed: порода питомца
        """
        self.name = name
        self.age = age
        self.breed = breed

    def feed(self, food: str):
        """
        Метод, описывающий кормление питомца
        :param food: еда для кормления
        >>> cat = Pet("Кот", 2, "Британец")
        >>> cat.feed("Рыба")
        """
        ...

    def play(self, toy: str):
        """
        Метод, описывающий игру с питомцем
        :param toy: игрушка для игры
        """
        ...


class BankAccount:
    def init(self, account_number: str, balance: float):
        """
        :param account_number: номер банковского счета
        :param balance: текущий баланс на счете
        """
        self.account_number = account_number
        self.balance = balance
        self.minsum = 60 # минимальная сумма списания

    def deposit(self, amount: float):
        """
        Метод, описывающий пополнение банковского счета
        :param amount: сумма пополнения
        """
        if amount <= 0:
            raise ValueError("Пополняемая сумма должна быть больше нуля")

    def withdraw(self, amount: float) -> str:
        """
        Метод, описывающий снятие денег с банковского счета
        :param amount: сумма снятия
        Примеры:
        >>> account = BankAccount("1234567890", 1000.0)
        >>> account.withdraw(500.0)
        "Со счета 1234567890 списано 500.0 руб."
        """
        if amount < self.minsum:
            raise ValueError("Сумма снятия должна быть больше или равна минимальной")
        if self.balance >= amount:
            self.balance -= amount
            return f"Со счета {self.account_number} списано {amount} руб."
        else:
            raise ValueError("Недостаточно средств на счете")

if __name__ == "__main__":
    doctest.testmod()
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    pass
