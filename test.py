from basic_array_ops import basic_ops
from basic_array_ops import array_ops

# Tests para basic_ops

# Tests exitosos
def test_AND():
    assert basic_ops(15,8,"AND") == 8
def test_OR():
    assert basic_ops(15,8,"OR") == 15
def test_suma():
    assert basic_ops(25,5,"suma") == 30
def test_resta():
    assert basic_ops(13,30,"resta") == -17


# Tests con errores
def test_suma_error():
    assert basic_ops(128,8,"suma") == "Error 2: rango excedido"
def test_resta_error():
    assert basic_ops(15.5,8.5,"resta") == "Error 1: operandos no enteros"
def test_AND_error():
    assert basic_ops(15,8,"NAND") == "Error 3: operación inválida"


# Tests para array_ops

# Tests exitosos
def test_AND_array():
    assert array_ops([15, 5], [0, 7], "AND") == [0, 5]
def test_OR_array():
    assert array_ops([15, 1], [0, 2], "OR") == [15, 3]
def test_suma_array():
    assert array_ops([25, 5], [5, 10], "suma") == [30, 15]
def test_resta_array():
    assert array_ops([13, 30], [3, 15], "resta") == [10, 15]


# Tests con errores
def test_suma_error_array():
    assert array_ops([128, 8], [5, 8], "suma") == ["Error 2: rango excedido", 16]
def test_resta_error_array():
    assert array_ops([15.5, 8.5], [0.5, 2.5], "resta") == ["Error 1: operandos no enteros", "Error 1: operandos no enteros"]
def test_AND_error_array():
    assert array_ops([15, 8], [5, 7], "xor") == ["Error 3: operación inválida", "Error 3: operación inválida"]
