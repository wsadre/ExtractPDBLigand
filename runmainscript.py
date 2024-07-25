import os
from multiprocessing import Pool
from functools import partial


from mainscript import mainscript

'''
输入的文件应该放在同一个文件夹内，每个文件不要单独建一个文件夹保存
输出的文件以每个输入文件的PDBID作为文件夹，保存了删除水和配体后的PDB文件 \
以及每个配体的config文件用于Vina的对接
对于没有找到配体的PDB文件则不会创建文件夹，打印‘{PDBID}没有配体’
文件采用多实例计算，具体运行速度取决于CPU核心数

'''

input_path = 'C:\\Users\\A\\Desktop\\AAAA\\AA'
input_file = os.listdir(input_path)
output_path = "C:\\Users\\A\\Desktop\\output"
input_file = [os.path.join(input_path,x) for x in input_file]

'''循环速度太慢
for i in input_file:
    mainscript(os.path.join(input_path, i),output_path)
'''

'''
    |   #SAA：Standard Amino Acid 标准氨基酸                          
    |   #UNK：Unknow 未知配体                                        
    |   #WAT：水分子                                                
    |   #SAG：Structural Elucidation Assistance Group 结构解析辅助基团   
    |   #ICG：Ion or Culster Group 离子或簇类集团                       
    |   #ATM：原子                                                 
    |   #MNP：MONOPHOSPHATE 单磷酸盐分子(核苷酸及核苷酸类似物)                     
    |   #GSG：Gas and Simple Group 气体或者单体分子                          
  
'''


if __name__ == '__main__':
    ##定义偏函数
    par_fun = partial(mainscript, output_path=output_path)
    with Pool(os.cpu_count()-2) as p:
        p.map(par_fun, input_file)
        p.close()
