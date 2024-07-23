from Bio import PDB
from classself.PdbInfoClass import PDBInfo
from classself.CCClass import CC
from . import GetCoord


def judge_resid(resid: PDB.Residue.Residue, pdbstruct_info: PDBInfo, _CC: CC):
    try:
        if not isinstance(resid, PDB.Residue.Residue):
            raise ValueError("please input a correct PDB Residue")

        match resid.get_id()[0]:

            case _ if resid.get_id()[0] in _CC.ligand_type["Unknow"]:
                __full_id = resid.get_full_id()
                pdbstruct_info.Other.struct.add(__full_id[1])
                pdbstruct_info.Other.chain.add(__full_id[2])
                pdbstruct_info.Other.name.add(__full_id[3][0])
                pdbstruct_info.Other.resseq.add(__full_id[3][1])
                pdbstruct_info.Other.icode.add(__full_id[3][2])
                pdbstruct_info.Other.type.add('Unknow')
                pdbstruct_info.Other.coord.add(GetCoord.all_atom_coord_as_list(resid))

            case _ if resid.get_id()[0] in _CC.ligand_type["Nag"]:
                __full_id = resid.get_full_id()
                pdbstruct_info.Other.struct.add(__full_id[1])
                pdbstruct_info.Other.chain.add(__full_id[2])
                pdbstruct_info.Other.name.add(__full_id[3][0])
                pdbstruct_info.Other.resseq.add(__full_id[3][1])
                pdbstruct_info.Other.icode.add(__full_id[3][2])
                pdbstruct_info.Other.type.add('NAG')
                pdbstruct_info.Other.coord.add(GetCoord.all_atom_coord_as_list(resid))

            case _ if resid.get_id()[0] in _CC.ligand_type["Water"]:
                __full_id = resid.get_full_id()
                pdbstruct_info.Water.struct.add(__full_id[1])
                pdbstruct_info.Water.chain.add(__full_id[2])
                pdbstruct_info.Water.name.add(__full_id[3][0])
                pdbstruct_info.Water.resseq.add(__full_id[3][1])
                pdbstruct_info.Water.icode.add(__full_id[3][2])
                pdbstruct_info.Water.type.add('Water')
                pdbstruct_info.Water.coord.add(GetCoord.all_atom_coord_as_list(resid))

            case _ if resid.get_id()[0] in _CC.ligand_type["Ion"]:
                __full_id = resid.get_full_id()
                pdbstruct_info.Ion.struct.add(__full_id[1])
                pdbstruct_info.Ion.chain.add(__full_id[2])
                pdbstruct_info.Ion.name.add(__full_id[3][0])
                pdbstruct_info.Ion.resseq.add(__full_id[3][1])
                pdbstruct_info.Ion.icode.add(__full_id[3][2])
                pdbstruct_info.Ion.type.add('Ion')
                pdbstruct_info.Ion.coord.add(GetCoord.all_atom_coord_as_list(resid))

            case _ if resid.get_id()[0] in _CC.ligand_type["Monophosphate"]:
                __full_id = resid.get_full_id()
                pdbstruct_info.Other.struct.add(__full_id[1])
                pdbstruct_info.Other.chain.add(__full_id[2])
                pdbstruct_info.Other.name.add(__full_id[3][0])
                pdbstruct_info.Other.resseq.add(__full_id[3][1])
                pdbstruct_info.Other.icode.add(__full_id[3][2])
                pdbstruct_info.Other.type.add('Monophosphate')
                pdbstruct_info.Other.coord.add(GetCoord.all_atom_coord_as_list(resid))

            case _ if resid.get_id()[0] in _CC.ligand_type["Gas_and_Simple"]:
                __full_id = resid.get_full_id()
                pdbstruct_info.Other.struct.add(__full_id[1])
                pdbstruct_info.Other.chain.add(__full_id[2])
                pdbstruct_info.Other.name.add(__full_id[3][0])
                pdbstruct_info.Other.resseq.add(__full_id[3][1])
                pdbstruct_info.Other.icode.add(__full_id[3][2])
                pdbstruct_info.Other.type.add('Gas_and_Simple')
                pdbstruct_info.Other.coord.add(GetCoord.all_atom_coord_as_list(resid))

            case _ if resid.get_id()[0] in _CC.ligand_type["Atom"]:
                __full_id = resid.get_full_id()
                pdbstruct_info.Other.struct.add(__full_id[1])
                pdbstruct_info.Other.chain.add(__full_id[2])
                pdbstruct_info.Other.name.add(__full_id[3][0])
                pdbstruct_info.Other.resseq.add(__full_id[3][1])
                pdbstruct_info.Other.icode.add(__full_id[3][2])
                pdbstruct_info.Other.type.add('Atom')
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
