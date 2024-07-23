from Bio import PDB

def read_pdb_file(id,file_path):
    # 设置文件读取流
    read_pdb = PDB.PDBParser(QUIET=1)
    return read_pdb.get_structure(id=id, file=file_path)

def write_pdb_file(structure,file_path):
    write_pdb = PDB.PDBIO()
    write_pdb.set_structure(structure)
    write_pdb.save(file_path)