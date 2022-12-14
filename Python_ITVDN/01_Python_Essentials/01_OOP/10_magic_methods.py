# Атрибуты, имена которых начинаются и заканчиваются двумя знаками
# подчёркивания, являются внутренними для Python и задают особые
# свойства объектов. С одним из подобных атрибутов мы уже имели
# дело ранее (документационная строка __doc__). Другим примером
# может служить атрибут __class__, в котором хранится класс
# данного объекта.
#
# Среди таких атрибутов есть методы. В документации Python
# подобные методы называются методами со специальными именами,
# однако в сообществе Python-разработчиков очень распространено
# название «магические методы». Также встречается и название
# «специальные методы». Они задают особое поведение объектов
# и позволяют переопределять поведение встроенных функций и
# операторов для экземпляров данного класса.
#
# Наиболее часто используемым специальным методом является
# метод-конструктор __init__.


class Complex:
    """
    Комплексное число
    """

    def __init__(self, real=0.0, imaginary=0.0):
        """
        Конструктор

        :param real:      действительная часть
        :param imaginary: мнимая часть
        """
        self.real = real
        self.imaginary = imaginary

    def __repr__(self):
        """
        Метод __repr__ возвращает строковое представление объекта, которое,
        если это возможно, должно быть корректным выражением, создающим
        аналогичный объект, иначе содержать его описание;
        вызывается функцией repr.
        """
        return 'Complex(%g, %g)' % (self.real, self.imaginary)

    def __str__(self):
        """
        Метод __str__ возвращает предназначенное для человека строковое
        представление объекта; вызывается функциями str, print и format.
        """
        return '%g %c %gi' % (self.real,
                              '+' if self.imaginary >= 0 else '-',
                              abs(self.imaginary))

    # Арифметические операции

    def __add__(self, other):
        """
        Метод __add__ определяет операцию сложения.
        """
        return Complex(self.real + other.real,
                       self.imaginary + other.imaginary)

    def __neg__(self):
        """
        Операция отрицания
        """
        return Complex(-self.real, -self.imaginary)

    def __sub__(self, other):
        """
        Операция вычитания.
        Сложение и отрицание уже определены, поэтому вычитание
        можно определить через них
        """
        return self + (-other)

    def __abs__(self):
        """
        Модуль числа
        """
        return (self.real ** 2 + self.imaginary ** 2) ** 0.5

    # Операции сравнения

    def __eq__(self, other):
        return self.real == other.real and self.imaginary == other.imaginary

    def __ne__(self, other):
        return not (self == other)


def main():
    x = Complex(2, 3.5)
    print(repr(x))
    print('x =', x)

    y = Complex(5, 7)
    print('y =', y)

    print('x + y =', x + y)
    print('x - y =', x - y)

    print('|x| =', abs(x))

    print('(x == y) =', x == y)


if __name__ == '__main__':
    main()
