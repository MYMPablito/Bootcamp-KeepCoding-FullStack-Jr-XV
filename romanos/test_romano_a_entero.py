from old_main import romano_a_entero,RomanNumberError,restas
import pytest

def test_romano_a_entero_I():
    assert romano_a_entero("I") == 1

def test_romano_a_entero_MDCCXIII():
    assert romano_a_entero("MDCCXIII") == 1713

def test_romano_a_entero_IV():
    assert romano_a_entero("IV") == 4

def test_romano_a_entero_no_repetir_mas_de_tres():
    with pytest.raises ( RomanNumberError ) as exceptionInfo:
        romano_a_entero("LIII")
    assert str( exceptionInfo.value ) == "No se puede repetir el valor más de tres veces seguidas."

def test_romano_a_entero_no_repetir_caracteres_especiales():
    with pytest.raises ( RomanNumberError ) as exceptionInfoE:
        romano_a_entero("DD")
    assert str( exceptionInfoE.value ) == "Los caracteres 'D', 'L' y 'V' no se pueden repetir."

def test_romano_a_entero_no_repetir_caracteres_especiales():
    with pytest.raises ( RomanNumberError ) as exceptionInfoE:
        romano_a_entero("VM")
    assert str( exceptionInfoE.value ) == "Los caracteres 'D', 'L' y 'V' no se pueden restar."

def test_romano_a_entero_restasI():
    with pytest.raises ( RomanNumberError ) as exceptionInfoR:
        romano_a_entero("IL")
    assert str( exceptionInfoR.value) == f"I solo se puede restar de V y X"

def test_romano_a_entero_restasX():
    with pytest.raises ( RomanNumberError ) as exceptionInfoR:
        romano_a_entero("XM")
    assert str( exceptionInfoR.value) == f"X solo se puede restar de L y C"

def test_romano_a_entero_si_se_repite_no_se_pueden_restar_IXC():
    with pytest.raises( RomanNumberError ) as exceptionInfoRep:
        romano_a_entero("IIX")
    assert str(exceptionInfoRep) == "El valor no puede restarse"


