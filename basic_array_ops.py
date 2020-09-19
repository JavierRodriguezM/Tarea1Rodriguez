# basic_ops
# el parámetro de operación debe ser escrito
# como un string para poder llamar la función.
def basic_ops(dato1, dato2, operacion):
    if (type(dato1) != int) or (type(dato2) != int):
        return "Error 1: operandos no enteros"
    if (dato1 > 127) or (dato1 < -127) or (dato2 > 127) or (dato2 < -127):
        return "Error 2: rango excedido"
    # Las operaciones deben ser escritas como "AND", "OR", "suma" y "resta",
    # tal cual se muestran las mayúsculas y minúsculas.
    if (operacion == "AND"):
        return dato1 & dato2
    if (operacion == "OR"):
        return dato1 | dato2
    if (operacion == "suma"):
        return dato1 + dato2
    if (operacion == "resta"):
        return dato1 - dato2
    if (operacion != "AND") or (operacion != "OR") or (operacion != "suma") or (operacion != "resta"):
        return "Error 3: operación inválida"
# Error 1: Tanto el operando 1 como el operando 2 deben ser números enteros.

# Error 2: Tanto el operando 1 como el operando 2 deben estar
# en el rango comprendido entre -127 y 127.

# Error 3: Solamente los strings "AND", "OR", "suma" y "resta"
# son admitidos en el parámetro correspondiente a la operación.


# array_ops

def array_ops(arreglo1, arreglo2, operacion):
    resultado = []
    if (len(arreglo1) != len(arreglo2)):
        return "Error 4: tamaño de arreglo incorrecto"
    for a in range(0, len(arreglo1)):
        resultado.append(basic_ops(arreglo1[a], arreglo2[a], operacion))
    return resultado

# Error 4: ambos arreglos deben tener la misma cantidad de elementos
