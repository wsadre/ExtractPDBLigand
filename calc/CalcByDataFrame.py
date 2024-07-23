import pandas as pd

'''
计算给定原子的几何中心，返回一个字典
'''


def get_center_coord_as_dict(DF: pd.DataFrame):
    try:
        if not isinstance(DF, pd.DataFrame):
            raise ValueError("Please enter the correct DataFrame format")
        center_coord = DF.mean()
        res = {'center_x': center_coord[0],
               'center_y': center_coord[1],
               'center_z': center_coord[2]}
        return res
    except ValueError as e:
        print('error:', repr(e))


'''
计算给定原子的最大外接长方体大小，默认不扩大最大正方形，在type中指定扩大类型
absolute为指定扩大等长的距离，距离由extend指定
percentage为指定扩大等比的距离，其中extend为指定的百分比
'''


def get_size_permanent_as_dict(DF: pd.DataFrame, extend: float = 0, extend_type: str = 'absolute'):
    try:
        if not isinstance(DF, pd.DataFrame):
            raise ValueError("Please enter the correct DataFrame format")
        if not isinstance(extend + 0.0, float):
            raise ValueError("Please enter the correct float format")
        if extend_type not in ['absolute', 'percentage']:
            raise ValueError("The wrong extension value type was entered")
        box_size = DF.max() - DF.min()
        if extend_type == 'absolute':
            res = {'size_x': box_size[0] + extend,
                   'size_y': box_size[1] + extend,
                   'size_z': box_size[2] + extend}
        if extend_type == 'percentage':
            res = {'size_x': box_size[0] + box_size[0] * extend / 100,
                   'size_y': box_size[1] + box_size[1] * extend / 100,
                   'size_z': box_size[2] + box_size[2] * extend / 100}
        return res
    except ValueError as e:
        print('error:', repr(e))


'''
计算给定原子的最大外接长方体大小，默认不扩大最大正方形，但指定扩展的长宽高可以不为相同值，以列表形式传入
list[0]为x的扩展值，list[1]为x的扩展值，list[2]为x的扩展值
absolute为指定扩大等长的距离，距离由extend指定
percentage为指定扩大等比的距离，其中extend为指定的百分比
'''


def get_size_customize_as_dict(DF: pd.DataFrame, extend: list = [0, 0, 0], extend_type: str = 'absolute'):
    try:
        if not isinstance(DF, pd.DataFrame):
            raise ValueError("Please enter the correct DataFrame format")
        if not isinstance(extend, list):
            raise ValueError("Please enter the correct list format")
        if extend_type not in ['absolute', 'percentage']:
            raise ValueError("The wrong extension value type was entered")
        box_size = DF.max() - DF.min()
        if extend_type == 'absolute':
            res = {'size_x': box_size[0] + extend[0],
                   'size_y': box_size[1] + extend[1],
                   'size_z': box_size[2] + extend[2]}
        if extend_type == 'percentage':
            res = {'size_x': box_size[0] + box_size[0] * extend[0] / 100,
                   'size_y': box_size[1] + box_size[1] * extend[1] / 100,
                   'size_z': box_size[2] + box_size[2] * extend[2] / 100}
        return res
    except ValueError as e:
        print('error:', repr(e))
