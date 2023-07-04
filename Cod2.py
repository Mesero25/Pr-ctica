def evaluar_diabetes():
    preguntas = [
        "¿Cuál es tu edad?",
        "¿Cuál es tu índice de masa corporal (IMC)?",
        "¿Tienes antecedentes familiares de diabetes?",
        "¿Realizas actividad física regularmente? (sí/no)",
        "¿Tienes hipertensión arterial? (sí/no)",
        "¿Has experimentado sed excesiva y frecuente?",
        "¿Has experimentado fatiga o debilidad inusual?",
        "¿Tienes antecedentes de niveles altos de glucosa en sangre?"
    ]

    respuestas = []

    for pregunta in preguntas:
        respuesta = input(pregunta + " ")
        respuestas.append(respuesta)

    puntos = 0

    # Asignar puntos basados en las respuestas
    if int(respuestas[0]) > 40:
        puntos += 2

    if float(respuestas[1]) > 30:
        puntos += 3

    if respuestas[2].lower() == "si":
        puntos += 2

    if respuestas[3].lower() == "no":
        puntos += 1

    if respuestas[4].lower() == "si":
        puntos += 2

    if respuestas[5].lower() == "si":
        puntos += 2

    if respuestas[6].lower() == "si":
        puntos += 2

    if respuestas[7].lower() == "si":
        puntos += 3

    # Determinar si es propenso a la diabetes
    if puntos >= 7:
        resultado = "Eres propenso/a a la diabetes. Te recomendamos consultar a un médico para una evaluación más detallada."
    else:
        resultado = "No pareces ser propenso/a a la diabetes, pero es importante mantener un estilo de vida saludable."

    # Mostrar el resultado
    print("\nResultado:")
    print(resultado)


# Ejecutar la evaluación
evaluar_diabetes()
