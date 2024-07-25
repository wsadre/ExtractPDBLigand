from Bio import PDB
from classself.PdbInfoClass import PDBInfo
from classself.CCClass import CC
from . import GetCoord


def judge_resid(resid: PDB.Residue.Residue, pdbstruct_info: PDBInfo, _CC: CC):
    try:
        if not isinstance(resid, PDB.Residue.Residue):
            raise ValueError("please input a correct PDB Residue")

        match resid.get_id()[0]:

            case _ if resid.get_id()[0] in _CC.ligand_type["UNK"]:
                __full_id = resid.get_full_id()
                pdbstruct_info.Other.struct.add(__full_id[1])
                pdbstruct_info.Other.chain.add(__full_id[2])
                pdbstruct_info.Other.name.add(__full_id[3][0])
                pdbstruct_info.Other.resseq.add(__full_id[3][1])
                pdbstruct_info.Other.icode.add(__full_id[3][2])
                pdbstruct_info.Other.type.add('UNK')
                pdbstruct_info.Other.coord.add(GetCoord.all_atom_coord_as_list(resid))

            case _ if resid.get_id()[0] in _CC.ligand_type["SAG"]:
                __full_id = resid.get_full_id()
                pdbstruct_info.Other.struct.add(__full_id[1])
                pdbstruct_info.Other.chain.add(__full_id[2])
                pdbstruct_info.Other.name.add(__full_id[3][0])
                pdbstruct_info.Other.resseq.add(__full_id[3][1])
                pdbstruct_info.Other.icode.add(__full_id[3][2])
                pdbstruct_info.Other.type.add('SAG')
                pdbstruct_info.Other.coord.add(GetCoord.all_atom_coord_as_list(resid))

            case _ if resid.get_id()[0] in _CC.ligand_type["WAT"]:
                __full_id = resid.get_full_id()
                pdbstruct_info.Water.struct.add(__full_id[1])
                pdbstruct_info.Water.chain.add(__full_id[2])
                pdbstruct_info.Water.name.add(__full_id[3][0])
                pdbstruct_info.Water.resseq.add(__full_id[3][1])
                pdbstruct_info.Water.icode.add(__full_id[3][2])
                pdbstruct_info.Water.type.add('WAT')
                pdbstruct_info.Water.coord.add(GetCoord.all_atom_coord_as_list(resid))

            case _ if resid.get_id()[0] in _CC.ligand_type["ICG"]:
                __full_id = resid.get_full_id()
                pdbstruct_info.Ion.struct.add(__full_id[1])
                pdbstruct_info.Ion.chain.add(__full_id[2])
                pdbstruct_info.Ion.name.add(__full_id[3][0])
                pdbstruct_info.Ion.resseq.add(__full_id[3][1])
                pdbstruct_info.Ion.icode.add(__full_id[3][2])
                pdbstruct_info.Ion.type.add('ICG')
                pdbstruct_info.Ion.coord.add(GetCoord.all_atom_coord_as_list(resid))

            case _ if resid.get_id()[0] in _CC.ligand_type["MNP"]:
                __full_id = resid.get_full_id()
                pdbstruct_info.Other.struct.add(__full_id[1])
                pdbstruct_info.Other.chain.add(__full_id[2])
                pdbstruct_info.Other.name.add(__full_id[3][0])
                pdbstruct_info.Other.resseq.add(__full_id[3][1])
                pdbstruct_info.Other.icode.add(__full_id[3][2])
                pdbstruct_info.Other.type.add('MNP')
                pdbstruct_info.Other.coord.add(GetCoord.all_atom_coord_as_list(resid))

            case _ if resid.get_id()[0] in _CC.ligand_type["GSG"]:
                __full_id = resid.get_full_id()
                pdbstruct_info.Other.struct.add(__full_id[1])
                pdbstruct_info.Other.chain.add(__full_id[2])
                pdbstruct_info.Other.name.add(__full_id[3][0])
                pdbstruct_info.Other.resseq.add(__full_id[3][1])
                pdbstruct_info.Other.icode.add(__full_id[3][2])
                pdbstruct_info.Other.type.add('GSG')
                pdbstruct_info.Other.coord.add(GetCoord.all_atom_coord_as_list(resid))

            case _ if resid.get_id()[0] in _CC.ligand_type["ATM"]:
                __full_id = resid.get_full_id()
                pdbstruct_info.Other.struct.add(__full_id[1])
                pdbstruct_info.Other.chain.add(__full_id[2])
                pdbstruct_info.Other.name.add(__full_id[3][0])
                pdbstruct_info.Other.resseq.add(__full_id[3][1])
                pdbstruct_info.Other.icode.add(__full_id[3][2])
                pdbstruct_info.Other.type.add('ATM')
                pdbstruct_info.Other.coord.add(GetCoord.all_atom_coord_as_list(resid))

            case _ if resid.get_id()[0] in _CC.ligand_type["Other"]:
                __full_id = resid.get_full_id()
                pdbstruct_info.Ligand.struct.add(__full_id[1])
                pdbstruct_info.Ligand.chain.add(__full_id[2])
                pdbstruct_info.Ligand.name.add(__full_id[3][0])
                pdbstruct_info.Ligand.resseq.add(__full_id[3][1])
                pdbstruct_info.Ligand.icode.add(__full_id[3][2])
                pdbstruct_info.Ligand.type.add('Ligand')
                pdbstruct_info.Ligand.coord.add(GetCoord.all_atom_coord_as_list(resid))

    except ValueError as e:
        print("error:", repr(e))
