class CC:
    ligand_map_PDBID: list
    PDBID_map_ligand: list
    ligand_type: dict


if __name__ == '__main__':
    import pandas as pd
    import dill as pickle
    from fileIO.MolDatRead import read_type_dat

    def __read_cc_counts_extra_as_df(filepath='../data/cc-counts-extra.tdd'):
        return pd.read_table(filepath, sep='\t', na_values=['N/A'], keep_default_na=False)


    def __read_cc_to_pdb_as_long_list(filepath='../data/cc-to-pdb.tdd'):
        value = []
        with open(filepath, 'r') as f:
            s = f.readline()
            while s != '':
                # 删除字符最右边存在的空格
                s = s.rstrip()
                # Ligand_name和PDBID之间用'\t'分割，PDBID之间用‘space’分割
                s_split = s.split('\t')
                s_key = s_split[0]
                s_value = s_split[1].split(' ')
                while bool(s_value):
                    value.append([s_key, s_value.pop()])
                s = f.readline()
        f.close()
        del s, s_key, s_value, s_split, f
        return value


    def __molname_map_PDBID_as_dict(list: list):
        __dict = {l[0]: [] for l in list}
        for i in range(len(list)):
            __dict[list[i][0]].append(list[i][1])
        return __dict


    def __PDBID_map_molname_as_dict(list: list):
        __dict = {l[1]: [] for l in list}
        for i in range(len(list)):
            __dict[list[i][1]].append(list[i][0])
        return __dict


    def __molname_type_as_dict(df: pd.DataFrame):

        moltype = read_type_dat()

        df = df[~df['id'].isin(moltype['SAA'])]

        df = df[~df['id'].isin(moltype['UNK'])]
        __unknow_list = ["H_" + x.rjust(3) for x in moltype['UNK']]

        df = df[~df['id'].isin(moltype['WAT'])]
        # BioPDB会把水解析成W，但是文件中的W是钨，只能在删除后添加
        __water_list = ["H_" + x.rjust(3) for x in moltype['WAT']]
        __water_list.extend(['W'])

        df = df[~df['id'].isin(moltype['SAG'])]
        __SAG_list = ["H_" + x.rjust(3) for x in moltype['SAG']]

        df = df[~df['id'].isin(moltype['ICG'])]
        __ion_list = ["H_" + x.rjust(3) for x in moltype['ICG']]

        df = df[~df['id'].isin(moltype['ATM'])]
        __atom_list = ["H_" + x.rjust(3) for x in moltype['ATM']]

        df = df[~df['id'].isin(moltype['MNP'])]
        __monophosphate_list = ["H_" + x.rjust(3) for x in moltype['MNP']]

        df = df[~df['id'].isin(moltype['GSG'])]
        __gas_and_simple_list = ["H_" + x.rjust(3) for x in moltype['GSG']]

        __other_list = df['id'].to_list()
        __other_list = ["H_" + x.rjust(3) for x in __other_list]

        return {
            'UNK': __unknow_list,
            'SAG': __SAG_list,
            'WAT': __water_list,
            'ICG': __ion_list,
            'MNP': __monophosphate_list,
            'GSG': __gas_and_simple_list,
            'ATM': __atom_list,
            'Other': __other_list
        }


    _cc_counts_extra = __read_cc_counts_extra_as_df()
    _cc_to_pdb = __read_cc_to_pdb_as_long_list()
    _ligand_map_PDBID = __molname_map_PDBID_as_dict(_cc_to_pdb)
    _PDBID_map_ligand = __PDBID_map_molname_as_dict(_cc_to_pdb)
    _ligand_type = __molname_type_as_dict(_cc_counts_extra)

    del _cc_counts_extra, _cc_to_pdb

    CCInfo = CC()
    CCInfo.ligand_map_PDBID = _ligand_map_PDBID
    CCInfo.ligand_type = _ligand_type
    CCInfo.ligand_map = _ligand_map_PDBID

    del _ligand_type, _PDBID_map_ligand, _ligand_map_PDBID

    with open('../data/ligandict.pkl', 'wb') as f:
        pickle.dump(CCInfo, f)
        f.close()
