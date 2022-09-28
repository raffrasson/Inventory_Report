from inventory_report.reports.simple_report import SimpleReport
from collections import Counter


class CompleteReport(SimpleReport):
    def generate(list):
        simple_report = SimpleReport.generate(list)
        companies = Counter([item["nome_da_empresa"] for item in list]).items()

        formatted_report = ""
        for key, value in companies:
            formatted_report += f"- {key}: {value}\n"

        return (
            f"{simple_report}\n"
            f"Produtos estocados por empresa:\n"
            f"{formatted_report}"
        )
