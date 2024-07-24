import os
from multiprocessing import Pool
from functools import partial


from mainscript import mainscript

input_path = 'C:\\Users\\A\\Desktop\\AAAA\\AA'
input_file = os.listdir(input_path)
output_path = "C:\\Users\\A\\Desktop\\output"

'''
for i in input_file:
    mainscript(os.path.join(input_path, i),output_path)
'''
##定义偏函数

par_fun = partial(mainscript,output_path = output_path)

with Pool(18) as p:
    p.map(par_fun,input_file)

