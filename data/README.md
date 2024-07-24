# 内容

此文件夹下存放从[PDBLigend](http://ligand-expo.rcsb.org/ld-download.html)站点下载下来的数据,用于解析PDB文件

**cc-counts-extra.tdd**存放小分子以及非标准残基的缩写(id)，在多少pdb结构中出现(count)，全称(name),分子式(formula)  
在PDBLigand中为***Chemical component counting statistics***,[下载地址](http://ligand-expo.rcsb.org/dictionaries/cc-counts-extra.tdd)

**cc-to-pdb.tdd**存放小分子非标准残基的缩写(第一列)，存在于哪些晶体中(第二列,给的是PDBID)，在PDBLigand中为***PDB and chemical component identifier correspondences***,
[下载地址](http://ligand-expo.rcsb.org/dictionaries/cc-to-pdb.tdd)

可以手动下载更新,文件名不可更改

```
更新方式：
 ·手动下载上述文件进行替换
 ·直接运行/fileIO/文件夹下的ExtractCCInfo.py