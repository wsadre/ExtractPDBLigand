import os

from classself.CCClass import CC

from mainscript import mainscript

input_path = 'C:\\Users\\A\\Desktop\\AAAA\\AA'
input_file = os.listdir(input_path)
output_path = "C:\\Users\\A\\Desktop\\output"

for i in input_file:
    mainscript(os.path.join(input_path, i),output_path)
