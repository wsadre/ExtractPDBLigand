import uuid
import os
import pandas as pd

from fileIO import PdbIO, WriteVinaConfig
from classself import PdbInfoClass
from classself.CCClass import CC
from parsingpdb.JudgeResidAndWritePdbinfo import judge_resid
from fileIO.WriteReadLigandDict import read_ligand_info_from_pkl
from parsingpdb import OperatePDB
from calc import CalcByDataFrame
from classself.VinaConfigClass import VinaConfig
from mainscript import mainscript

mainscript("C:\\Users\\A\\Desktop\\6m49.pdb", "C:\\Users\\A\\Desktop")
