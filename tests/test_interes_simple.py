import pytest
from interes_simple import interes_simple


# Caso correcto
def test_interes_correcto():
    resultado = interes_simple(1000, 0.05, 2)
    assert resultado == 100.0


#Caso límite
def test_tasa_cero():
    resultado = interes_simple(1000, 0, 2)
    assert resultado == 0


#Caso error
def test_capital_negativo():
    with pytest.raises(ValueError):
        interes_simple(-1000, 0.05, 2)