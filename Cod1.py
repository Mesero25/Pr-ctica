
def calcular_imc(peso, altura):
    # Fórmula para el cálculo del IMC en el que estpoo es un cambio 
    imc = peso / (altura ** 2)
    return imc

def interpretar_imc(imc):
    # Interpretación del IMC según las categorías establecidas
    if imc < 18.5:
        return "Bajo peso"
    elif imc < 24.9:
        return "Normal"
    elif imc < 29.9:
        return "Sobrepeso"
    else:
        return "Obesidad"

# Entrada de datos
peso = float(input("Ingresa tu peso en kilogramos: "))
altura = float(input("Ingresa tu altura en metros: "))

# Cálculo del IMC
imc = calcular_imc(peso, altura)

# Interpretación del IMC
categoria = interpretar_imc(imc)

# Resultado
print("Tu IMC es:", imc)
print("Categoría:", categoria)

