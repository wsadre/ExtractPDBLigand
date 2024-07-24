import dill as pickle

def read_ligand_info_from_pkl():
    with open('data/ligandict.pkl', 'rb') as file:
        s = pickle.load(file)
    file.close()
    return s

