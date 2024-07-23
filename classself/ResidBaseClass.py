"""
所有的基类的函数都需要加上@classmethod关键字
正常继承时都不会实例化类对象
用classmethod修饰后就可以在非实例化的使用调用
"""


class BaseListAndOption:
    def __init__(self):
        self.__value = []

    def get(self):
        return self.__value

    def add(self, value):
        self.__value.append(value)

    def delete(self, value):
        del self.__value[value]


class BaseMolAttri:
    def __init__(self):
        self.struct = self.__Struct()
        self.chain = self.__Chain()
        self.name = self.__Name()
        self.resseq = self.__Resseq()
        self.icode = self.__Icode()
        self.type = self.__Type()
        self.coord = self.__Coord()


    class __Struct(BaseListAndOption):
        pass

    class __Chain(BaseListAndOption):
        pass

    class __Name(BaseListAndOption):
        pass

    class __Resseq(BaseListAndOption):
        pass

    class __Icode(BaseListAndOption):
        pass

    class __Type(BaseListAndOption):
        pass

    class __Coord(BaseListAndOption):
        pass


class BaseChainAttri:
    def __init__(self):
        self.chain = self.__Chain()

    class __Chain(BaseListAndOption):
        pass
