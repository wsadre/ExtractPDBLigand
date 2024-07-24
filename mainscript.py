import uuid
import os
import pandas as pd

from fileIO import PdbIO, WriteVinaConfig
from classself import PdbInfoClass
from classself.CCClass import CC
from parsingpdb.JudgeResidAndWritePdbinfo import judge_resid
from fileIO.WriteReadLigandDict import read_ligand_info_from_pkl
from parsingpdb import OperatePDB
from calc import CalcByDataFrame
from classself.VinaConfigClass import VinaConfig


def mainscript(input_file, output_path):
    CCd = read_ligand_info_from_pkl()
    UNIQID = uuid.uuid4().hex
    pdbstruc = PdbIO.read_pdb_file(UNIQID, file_path=input_file)
    pdbstruc_info = PdbInfoClass.PDBInfo(UNIQID)

    for Model in pdbstruc.get_list():
        for Chain in Model.get_list():
            for Resid in Chain.get_list():
                if Resid.get_id()[0] != ' ':
                    judge_resid(Resid, pdbstruc_info, CCd)

    del Resid, Chain, Model
    pdbstruc_info.refresh()

    pdb_name = pdbstruc.header['idcode']

    # 删除水和配体
    if pdbstruc_info.Water.is_exist:
        OperatePDB.delete_water(pdbstruc, pdbstruc_info)
    if pdbstruc_info.Ligand.is_exist:
        OperatePDB.delete_ligand(pdbstruc, pdbstruc_info)
    else:
        print(f"{pdb_name} PDB file does not have any Ligand")
        return 0

    output_path = os.path.join(output_path, pdb_name)
    # 创建输出文件夹
    if not os.path.exists(output_path):
        os.makedirs(output_path)

    # 数据是等长度的可以用任意一个字段去获取长度
    n_ligand = len(pdbstruc_info.Ligand.name.get())

    # 保存对接config
    for i in range(n_ligand):
        __center = CalcByDataFrame.get_center_coord_as_dict(pd.DataFrame(pdbstruc_info.Ligand.coord.get()[i]))
        __size = CalcByDataFrame.get_size_permanent_as_dict(pd.DataFrame(pdbstruc_info.Ligand.coord.get()[i]),
                                                            400,
                                                            "percentage")
        __n_cpu = 18
        __vinaconfig = VinaConfig()
        WriteVinaConfig.write_vina_config(__vinaconfig, centerdict=__center, sizedict=__size, n_cpu=__n_cpu)

        __ligand_name = 'chain' + '_' + pdbstruc_info.Ligand.chain.get()[i] + '_' + str(
            pdbstruc_info.Ligand.resseq.get()[i]) + '_' + pdbstruc_info.Ligand.name.get()[i]

        WriteVinaConfig.export_vina_config(__vinaconfig, os.path.join(output_path, __ligand_name + '.config'))

    # 保存删除水和配体的PDB
    PdbIO.write_pdb_file(structure=pdbstruc, file_path=os.path.join(output_path, pdb_name + '.pdb'))

    return 0
