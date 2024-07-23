import uuid
from fileIO import PdbIO
from classself import PdbInfoClass,CCClass
from parsingpdb.JudgeResidAndWritePdbinfo import judge_resid
from fileIO.WriteReadLigandDict import read_ligand_info_from_pkl
from parsingpdb import OperatePDB

CCd = read_ligand_info_from_pkl()
UNIQID = uuid.uuid4().hex
pdbstruc = PdbIO.read_pdb_file(UNIQID, file_path='C:\\Users\\A\\Desktop\\5t5i.pdb')
pdbstruc_info = PdbInfoClass.PDBInfo(UNIQID)


for Model in pdbstruc.get_list():
    for Chain in Model.get_list():
        for Resid in Chain.get_list():
            if Resid.get_id()[0] != ' ':
                judge_resid(Resid, pdbstruc_info, CCd)

del Resid,Chain,Model
pdbstruc_info.refresh()
pdbstruc_info.which_type_exist()



OperatePDB.delete_water(pdbstruc,pdbstruc_info)
OperatePDB.delete_ligand(pdbstruc,pdbstruc_info)




