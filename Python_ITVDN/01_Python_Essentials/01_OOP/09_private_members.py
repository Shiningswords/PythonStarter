# Атрибуты, имена которых начинаются, но не заканчиваются, двумя символами
# подчёркивания, считаются приватными. К ним применяется механизм
# «name mangling», суть которого заключается в том, что изнутри класса
# и его экземпляров к этим атрибутам можно обращаться по тому имени,
# которое было задано при объявлении, однако на самом деле к именам слева добавляется
# подчёркивание и имя класса. Этот механизм не предполагает защиты данных от
# изменения извне, так как к ним всё равно можно обратиться, зная имя класса
# и то, как Python изменяет имена приватных атрибутов, однако позволяет
# защитить их от случайного переопределения в классах-потомках.


class MyClass:
    def __init__(self):
        self.__private_attribute = 42

    def get_private(self):
        return self.__private_attribute


obj = MyClass()
print(obj.get_private())  # 42
print(obj.__private_attribute)  # ошибка
# print(obj._MyClass__private_attribute)  # 42
