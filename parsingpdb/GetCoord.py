from Bio import PDB

# 输出给定结构中的所有原子坐标
def all_atom_coord_as_list(PDBstruct: PDB):
    try:
        if not isinstance(PDBstruct, (
        PDB.Structure.Structure, PDB.Model.Model, PDB.Chain.Chain, PDB.Residue.Residue, PDB.Atom.Atom)):
            raise ValueError("Please enter the correct PDB file format")
        coord = []
        match PDBstruct.level:
            case 'S':
                for model in PDBstruct.get_list():
                    for chain in model.get_list():
                        for residues in chain.get_list():
                            for atom in residues.get_list():
                                coord.append(atom.get_coord().tolist())
            case 'M':
                for chain in PDBstruct.get_list():
                    for residues in chain.get_list():
                        for atom in residues.get_list():
                            coord.append(atom.get_coord().tolist())
            case 'C':
                for residues in PDBstruct.get_list():
                    for atom in residues.get_list():
                        coord.append(atom.get_coord().tolist())
            case 'R':
                for atom in PDBstruct.get_list():
                    coord.append(atom.get_coord().tolist())
            case 'A':
                coord.append(PDBstruct.get_coord().tolist())
        return coord
    except ValueError as e:
        print("error:", repr(e))
