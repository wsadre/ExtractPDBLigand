# 用于提取PDB文件中的Ligand及其他残基或者分子的脚本
- 此脚本还未完善，目前只能用于windows系统，mac和Linux还未测试
- 此脚本的运行依赖于biopython和pandas两个包
- 识别配体类型取决于 **/data** 里的文件，具体内容以 **/data** 里的README.md为准
- 配体类型识别只依靠名称，所以准确度可能很低
- 提取出的坐标可以直接计算并输出 ***AutoDockVina*** 需要的 ***Config*** 文件