from Bio import PDB
from classself import PdbInfoClass


def get_member_name(PDBInfo: PdbInfoClass):
    return list(vars(PDBInfo).keys())


# 添加成员后需要在这里添加内容
def info_get_non_chain_member_attri(PDBInfo: PdbInfoClass, member_name: str):
    # 首字母大写
    member_name = member_name.capitalize()
    __member_name = ["Water", "Ion", "Ligand", "Other"]
    if member_name not in __member_name:
        raise KeyError
    __submember_name = ["struct", "chain", "name", "type", "resseq", "icode", "coord"]
    __loop = len(getattr(getattr(PDBInfo, member_name), __submember_name[1]).get())
    __res = []
    for i in range(__loop):
        __cache = []
        for j in __submember_name:
            __cache.append(getattr(getattr(PDBInfo, member_name), j).get()[i])
        __res.append(__cache)

    return __res


def info_get_non_chain_member_tuple_for_pdb(PDBInfo: PdbInfoClass, member_name: str):
    member_name = member_name.capitalize()
    __member_name = ["Water", "Ion", "Ligand", "Other"]
    if member_name not in __member_name:
        raise KeyError
    __submember_name = ["struct", "chain", "name", "resseq", "icode"]
    __loop = len(getattr(getattr(PDBInfo, member_name), __submember_name[1]).get())
    __res = []
    for i in range(__loop):
        __cache = (
            getattr(getattr(PDBInfo, member_name), __submember_name[0]).get()[i],
            getattr(getattr(PDBInfo, member_name), __submember_name[1]).get()[i],
            (
                getattr(getattr(PDBInfo, member_name), __submember_name[2]).get()[i],
                getattr(getattr(PDBInfo, member_name), __submember_name[3]).get()[i],
                getattr(getattr(PDBInfo, member_name), __submember_name[4]).get()[i],
            )
        )
        __res.append(__cache)
    return __res

def delete_ligand(pdbstruct: PDB.Structure.Structure, pdbinfo: PdbInfoClass):
    if pdbstruct.id != pdbinfo.id:
        print("PDB structure ids do not match")
        return 0
    else:
        __ligand_list = info_get_non_chain_member_tuple_for_pdb(pdbinfo,"Ligand")
        for i in __ligand_list:
            del pdbstruct[i[0]][i[1]][i[2]]

def delete_water(pdbstruct: PDB.Structure.Structure, pdbinfo: PdbInfoClass):
    if pdbstruct.id != pdbinfo.id:
        print("PDB structure ids do not match")
        return 0
    else:
        __water_list = info_get_non_chain_member_tuple_for_pdb(pdbinfo,"Water")
        for i in __water_list:
            del pdbstruct[i[0]][i[1]][i[2]]