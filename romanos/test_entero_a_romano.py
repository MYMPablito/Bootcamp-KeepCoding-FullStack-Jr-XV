from main import entero_a_romano

valor_final1 = entero_a_romano(1994)
valor_final2 = entero_a_romano(333)
valor_final3 = entero_a_romano(33)
valor_final4 = entero_a_romano(3)

# def test_prueba_entero_a_romano():
#    assert valor_final == [1000,900,90,4] #True

def test_prueba_entero_a_romano_1994():
    assert valor_final1 == 'MCMXCIV'

def test_prueba_entero_a_romano_333():
    assert valor_final2 == 'CCCXXXIII'

def test_prueba_entero_a_romano_33():
    assert valor_final3 == 'XXXIII'

def test_prueba_entero_a_romano_3():
    assert valor_final4 == 'III'