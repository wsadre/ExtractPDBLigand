import os
from multiprocessing import Pool
from functools import partial


from mainscript import mainscript

input_path = 'C:\\Users\\A\\Desktop\\AAAA\\AA'
input_file = os.listdir(input_path)
output_path = "C:\\Users\\A\\Desktop\\output"
input_file = [os.path.join(input_path,x) for x in input_file]
'''
for i in input_file:
    mainscript(os.path.join(input_path, i),output_path)
'''




if __name__ == '__main__':
    ##定义偏函数
    par_fun = partial(mainscript, output_path=output_path)
    with Pool(os.cpu_count()-2) as p:
        p.map(par_fun, input_file)
        p.close()
