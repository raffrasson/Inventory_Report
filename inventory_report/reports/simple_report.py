from datetime import datetime
import statistics


class SimpleReport:
    def generate(list):
        oldest_date = min(product["data_de_fabricacao"] for product in list)

        actual_date = datetime.now().strftime("%Y-%m-%d")

        closest_expiration = min(
            [
                product["data_de_validade"]
                for product in list
                if product["data_de_validade"] > actual_date
            ]
        )

        # ref:
        # https://www.geeksforgeeks.org/python-find-most-frequent-element-in-a-list/
        companies = [name["nome_da_empresa"] for name in list]
        # cada produto tem uma empresa.
        # Logo, após listar as empresas
        # basta achar o nome que se repete mais(moda)

        most_products = statistics.mode(companies)

        return (
            f"Data de fabricação mais antiga: {oldest_date}\n"
            f"Data de validade mais próxima: {closest_expiration}\n"
            f"Empresa com mais produtos: {most_products}"
        )
