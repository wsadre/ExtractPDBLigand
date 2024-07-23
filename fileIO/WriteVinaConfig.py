import pathlib
from typing import Any

from classself.VinaConfigClass import VinaConfig


def write_vina_config(vinaconfig: VinaConfig, centerdict: dict, sizedict: dict, n_cpu: int = 12,
                      n_exhaustiveness: int = 25, n_num_modes: int = 50, n_energy_range: int = 4):
    vinaconfig.center_x = centerdict["center_x"]
    vinaconfig.center_y = centerdict['center_y']
    vinaconfig.center_z = centerdict['center_z']
    vinaconfig.size_x = sizedict['size_x']
    vinaconfig.size_y = sizedict['size_y']
    vinaconfig.size_z = sizedict['size_z']
    vinaconfig.cpu = n_cpu
    vinaconfig.num_modes = n_num_modes
    vinaconfig.energy_range = n_energy_range
    vinaconfig.exhaustiveness = n_exhaustiveness


def export_vina_config(vinaconfig: VinaConfig, filepath: Any):
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
