from classself.CCClass import CC

def read_ligand_info_from_pkl():
    import pickle
    with open('data/ligandict.pkl', 'rb') as file:
        s = pickle.load(file)
    file.close()
    return s

