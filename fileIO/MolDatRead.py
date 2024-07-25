def read_type_dat():
    with open('../data/moltype.dat', 'r', encoding='utf-8') as f:
        data = {}
        s = f.readline()
        while s != "":
            if not s.startswith('#') and not s.isspace() and s != '\n':
                key, value = s.split(":")
                # 删除两边可能存在的空格和制表符
                value.rstrip().rstrip('\t').lstrip().lstrip('\t')
                while value[-1] == ';' or value[-1] == '\n':
                    value = value[:-1]
                value = value.split(';')
                value = [x.rstrip().lstrip() for x in value]
                data[key] = value
                s = f.readline()
            else:
                s = f.readline()

        f.close()
        del f, key, value, s
    return data
