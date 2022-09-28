from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
import csv
import json
import pathlib
import xmltodict


class Inventory:
    def get_data(path):
        if pathlib.Path(path).suffix == ".csv":
            with open(path, encoding="utf-8") as file:
                data = list(csv.DictReader(file))
                return data

        elif pathlib.Path(path).suffix == ".json":
            with open(path, encoding="utf-8") as file:
                data = list(json.load(file))
                return data

        else:
            # ref:
            # https://trybecourse.slack.com/archives/C01PLFW7347/p1643819956428249
            with open(path) as file:
                data = xmltodict.parse(file.read())["dataset"]["record"]
                print(data)
                return data

    def import_data(path, type):

        # ref (pesquisei como diferenciar por extensão):
        # https://www.geeksforgeeks.org/how-to-get-file-extension-in-python/

        if type == "simples":
            return SimpleReport.generate(Inventory.get_data(path))
        if type == "completo":
            return CompleteReport.generate(Inventory.get_data(path))
