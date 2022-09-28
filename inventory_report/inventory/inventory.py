from inventory_report.reports.simple_report import SimpleReport
import csv


class Inventory:
    def get_csv(path):
        with open(path, encoding="utf-8") as file:
            data = list(csv.DictReader(file))
            return data

    def import_data(path, type):

        if type == "simples":
            return SimpleReport.generate(Inventory.get_csv(path))
