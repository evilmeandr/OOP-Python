class Tree:
    """
            Документация на класс.
            Класс описывает сущность дерева.
            """
    def __init__(self, age:int, height:int):
        self.age = age
        self.height = height
        """ Инициализация экземпляра класса.
                :param age: возраст дерева (годы)
                :param height: высота дерева (метры)
                """

    def __str__(self):
        return f"Tree Age: {self.age}, Tree height: {self.height}"

    def __repr__(self):
        return f"{self.__class__.__name__}({self.age!r}, {self.height!r})"

    def cut_the_top(self, x:int)-> int:
        """
                 Метод отрезает от верхушки дерева отрезок ствола,длинной "x"
                 :param x: сколько нужно отрезать сверху дерева
                 Пример:
                 >>> tree1 = tree(15, 2)
                 >>> tree1.cut_the_top(0,5)
                 """
        self.height -= x
        return self.height

    def defence(self)-> str:
        """
                 Метод выдает строчку рекомендаций о том как защищать дерево от вредителей
                        """
        return f"Белить ствол"


class FruitTree(Tree):
    """
               Документация на класс.
               Класс описывает сущность плодового дерева.
               """
    def __int__(self, age:int, height:int, fruit:str):
        """ Инициализация экземпляра класса.
                        :param age: возраст дерева (годы)
                        :param height: высота дерева (метры)
                        :param fruit: тип плодов на дереве
                        """

        super().__init__(age, height)
        self.fruit = fruit

    def __str__(self):
        return f"Tree Age: {self.age}, Tree height: {self.height}, Fruit{self.fruit}"

    def __repr__(self):
        return f"{self.__class__.__name__}({self.age!r}, {self.height!r}, {self.fruit!r})"

    def defence(self) -> str:
        """
             Метод выдает строчку рекомендаций о том как защищать дерево от вредителей
             Данный метод переопределен,т.к. исходный метод базового класса не полностью удовлетворяет дочернему
                                """
        return f"Белить ствол и укрывать дерево от птиц"

if __name__ == "__main__":
    # Write your solution here
    pass
