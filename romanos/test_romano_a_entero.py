from main import romano_a_entero, RomanNumberError
import pytest

def test_romano_a_entero_I():
    assert romano_a_entero("I") == 1

def test_romano_a_entero_MDCCXIII():
    assert romano_a_entero("MDCCXIII") == 1713

def test_romano_a_entero_IV():
    assert romano_a_entero("IV") == 4

def test_romano_a_entero_no_repetir_mas_de_tres():
    with pytest.raises ( RomanNumberError ) as exceptionInfo:
        romano_a_entero("III")
    assert str( exceptionInfo.value ) == "No se puede repetir el valor más de tres veces seguidas."

def test_romano_a_entero_no_repetir_caracteres_especiales():
    with pytest.raises ( RomanNumberError ) as exceptionInfoE:
        romano_a_entero("DD")
    assert str( exceptionInfoE.value ) == "Los caracteres 'D', 'L' y 'V' no se pueden repetir."
