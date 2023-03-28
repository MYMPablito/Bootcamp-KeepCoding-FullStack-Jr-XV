from main import entero_a_romano

valor_final = entero_a_romano(1994)

def test_prueba_entero_a_romano(valor):
    assert valor == [1000,900,90,4] #True

# def test_entero_a_romano(valor):
#    assert valor == 'MCMXCIV'

test_prueba_entero_a_romano(valor_final)
    