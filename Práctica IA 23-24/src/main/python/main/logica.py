import json
import os
from pathlib import Path

from main.variables.Age import Age
from main.read_classes.MFIS_Read_Functions import readApplicationsFile, readFuzzySetsFile
from main.read_classes.MFIS_Read_Functions import readApplicationsFile
from main.variables.Amount import Amount
from main.variables.Assets import Assets
from main.variables.History import History
from main.variables.IncomeLevel import IncomeLevel
from main.variables.Job import Job
from main.metodos_clases.InputVars import InputVars

json_files_path = (str(Path.home()) +
                           "/PycharmProjects/Practica-IA-2024-G-11/Práctica IA 23-24/src/main/python/main/variables/json")
file = json_files_path + '/json_app.json'

input = InputVars()
input.borrado_y_creado_json()
input_dict = input.calcular_variables()
input.guardado_vars(input_dict)


