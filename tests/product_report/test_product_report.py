from inventory_report.inventory.product import Product


def test_relatorio_produto():
    product_mock = Product(
        id=21,
        nome_da_empresa="empresa",
        nome_do_produto="produto",
        data_de_fabricacao="21-12-2012",
        data_de_validade="12-12-2121",
        numero_de_serie="18462946593",
        instrucoes_de_armazenamento="camara fria",
    )

    assert product_mock.__repr__() == (
        "O produto produto fabricado em 21-12-2012 por empresa "
        "com validade até 12-12-2121 precisa ser armazenado camara fria."
    )
