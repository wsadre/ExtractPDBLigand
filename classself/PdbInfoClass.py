"""
定义一个PDB信息的class，在里面存储需要得知的PDB文件的一些信息
包括固定结合水分子，金属配体离子,是否存在相应的配体
自定义一个PDBinfo类，是一个类的集合 \
里面的所有类都继承于residbaseclass中个一个基类的两个派生子类
"""
from classself.ResidBaseClass import BaseMolAttri, BaseChainAttri


class PDBInfo:
    def __init__(self, uuid):
        self.id = uuid
        self.Water = self.Water()
        self.Ligand = self.Ligand()
        self.Ion = self.Ion()
        self.Other = self.Other()
        self.Uniquechain = self.Uniquechain()
        self.Nuniquechain = self.Nuniquechain()

    class Water(BaseMolAttri):
        def __init__(self):
            super().__init__()
            self.__is_exist = False

        @property
        def is_exist(self):
            return self.__is_exist

        @is_exist.setter
        def is_exist(self, value):
            self.__is_exist = value

    class Ligand(BaseMolAttri):
        def __init__(self):
            super().__init__()
            self.__is_exist = False

        @property
        def is_exist(self):
            return self.__is_exist

        @is_exist.setter
        def is_exist(self, value):
            self.__is_exist = value

    class Ion(BaseMolAttri):
        def __init__(self):
            super().__init__()
            self.__is_exist = False

        @property
        def is_exist(self):
            return self.__is_exist

        @is_exist.setter
        def is_exist(self, value):
            self.__is_exist = value

    class Other(BaseMolAttri):
        def __init__(self):
            super().__init__()
            self.__is_exist = False

        @property
        def is_exist(self):
            return self.__is_exist

        @is_exist.setter
        def is_exist(self, value):
            self.__is_exist = value

    class Uniquechain(BaseChainAttri):
        def __init__(self):
            super().__init__()
            self.__is_exist = False

        @property
        def is_exist(self):
            return self.__is_exist

        @is_exist.setter
        def is_exist(self, value):
            self.__is_exist = value

    class Nuniquechain(BaseChainAttri):
        def __init__(self):
            super().__init__()
            self.__is_exist = False

        @property
        def is_exist(self):
            return self.__is_exist

        @is_exist.setter
        def is_exist(self, value):
            self.__is_exist = value

    def refresh(self):
        for i in ["Ion", "Ligand", "Water", "Uniquechain", "Nuniquechain", "Other"]:
            #理论上逻辑应该是if bool()，但是结果完全是反的，不知道为什么
            if bool(getattr(getattr(self, i), 'chain').get()):
                getattr(self, i).is_exist = True

    def which_type_exist(self):
        __res = []
        for i in ["Ion", "Ligand", "Water", "Uniquechain", "Nuniquechain", "Other"]:
            if getattr(self, i).is_exist:
                __res.append(i)
        return __res
