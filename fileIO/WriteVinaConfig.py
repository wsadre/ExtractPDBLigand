from classself.VinaConfigClass import VinaConfig


def write_vina_config(vinaconfig: VinaConfig, centerlist: list, sizelist: list, n_cpu: int, n_exhaustiveness: int,
                      n_num_modes: int, n_energy_range: int):
    vinaconfig.center_x = centerlist[0]
    vinaconfig.center_y = centerlist[1]
    vinaconfig.center_z = centerlist[2]
    vinaconfig.size_x = sizelist[0]
    vinaconfig.size_y = sizelist[1]
    vinaconfig.size_z = sizelist[2]
    vinaconfig.cpu = n_cpu
    vinaconfig.num_modes = n_num_modes
    vinaconfig.energy_range = n_energy_range
    vinaconfig.exhaustiveness = n_exhaustiveness


def export_vina_config(vinaconfig: VinaConfig, filepath: str):
    with open(filepath, 'w') as file:
        file.write(f"center_x = {vinaconfig.center_x} \n")
        file.write(f"center_y = {vinaconfig.center_y} \n")
        file.write(f"center_z = {vinaconfig.center_z} \n")
        file.write(f"size_x = {vinaconfig.size_x} \n")
        file.write(f"size_y = {vinaconfig.size_y} \n")
        file.write(f"size_z = {vinaconfig.size_z} \n")
        file.write(f"cpu = {vinaconfig.cpu} \n")
        file.write(f"num_modes = {vinaconfig.num_modes} \n")
        file.write(f"energy_range = {vinaconfig.energy_range} \n")
        file.write(f"exhaustiveness = {vinaconfig.exhaustiveness} \n")
