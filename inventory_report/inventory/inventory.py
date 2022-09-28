from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
import csv
import json
import pathlib
import xmltodict


class Inventory:
    def get_csv(path):
        with open(path, encoding="utf-8") as file:
            data = list(csv.DictReader(file))
            return data

    def get_json(path):
        with open(path, encoding="utf-8") as file:
            data = list(json.load(file))
            return data

    def get_xml(path):
        # ref:
        # https://trybecourse.slack.com/archives/C01PLFW7347/p1643819956428249
        with open(path, encoding="utf-8") as file:
            data = xmltodict.parse(file.read())["dataset"]["record"]
            print(data)
            return data

    def import_data(path, type):

        # ref (pesquisei como diferenciar por extensão):
        # https://www.geeksforgeeks.org/how-to-get-file-extension-in-python/

        if type == "simples" and pathlib.Path(path).suffix == ".csv":
            return SimpleReport.generate(Inventory.get_csv(path))
        if type == "completo" and pathlib.Path(path).suffix == ".csv":
            return CompleteReport.generate(Inventory.get_csv(path))

        if type == "simples" and pathlib.Path(path).suffix == ".json":
            return SimpleReport.generate(Inventory.get_json(path))
        if type == "completo" and pathlib.Path(path).suffix == ".json":
            return CompleteReport.generate(Inventory.get_json(path))

        if type == "simples" and pathlib.Path(path).suffix == ".xml":
            return SimpleReport.generate(Inventory.get_xml(path))
        if type == "completo" and pathlib.Path(path).suffix == ".xml":
            return CompleteReport.generate(Inventory.get_xml(path))
