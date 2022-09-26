from inventory_report.inventory.product import Product

# referencia para tuplas no assert:
# https://stackoverflow.com/questions/43119776/can-i-handle-multiple-asserts-within-a-single-python-pytest-method


def test_cria_produto():
    product_mock = Product(
        id=21,
        nome_da_empresa="empresa",
        nome_do_produto="produto",
        data_de_fabricacao="21-12-2012",
        data_de_validade="12-12-2121",
        numero_de_serie="18462946593",
        instrucoes_de_armazenamento="camara fria",
    )

    assert (
        product_mock.id,
        product_mock.nome_da_empresa,
        product_mock.nome_do_produto,
        product_mock.data_de_fabricacao,
        product_mock.data_de_validade,
        product_mock.numero_de_serie,
        product_mock.instrucoes_de_armazenamento,
    ) == (
        21,
        "empresa",
        "produto",
        "21-12-2012",
        "12-12-2121",
        "18462946593",
        "camara fria",
    )
