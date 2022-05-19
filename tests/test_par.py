# EJERCICIO
# Crear un Test Case que evalúe el método es_par
# y determine si el resultado es par o impar
# En el caso de ser impar, se deberá marcar un error.

def es_par(a,b):
    if a % 2 == 0 and b % 2 == 0:
        return True
    else:
        return False

# CASO DE PRUEBA 1 > primer caso
def test_positive():
    result = es_par(2, 4)
    assert result, 'Los números no son pares'

# CASO DE PRUEBA 2 > caso de prueba negativo : esperando que el resultado sea falso
def test_negative():
    result = es_par(3, 9)
    #assert not result
    #assert result == False  # Los números son pares
    assert not result, 'El número debería ser par'

# CASO DE PRUEBA 3 > agregar un nuevo caso de prueba donde el primer número es par y el segundo es impar
def test_parYNopar():
    result = es_par(12, 1)
    print(result)
    assert not result, 'El primer número es par pero el segundo número no.'
    # assert result == False