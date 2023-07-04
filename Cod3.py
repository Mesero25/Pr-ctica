def evaluar_trastornos_alimentarios():
    preguntas = [
        "¿Tienes miedo intenso a subir de peso o engordar?",
        "¿Te saltas comidas o sigues dietas restrictivas con frecuencia?",
        "¿Experimentas atracones de comida y luego te sientes culpable?",
        "¿Utilizas métodos poco saludables para controlar tu peso, como vómitos autoinducidos o uso de laxantes?",
        "¿Te sientes insatisfecho/a con tu apariencia física a pesar de que otros te digan lo contrario?",
        "¿Tienes preocupación constante por la cantidad de calorías y grasa que consumes?",
        "¿Te aíslas socialmente debido a tu relación con la comida o tu imagen corporal?",
        "¿Has experimentado una importante pérdida o aumento de peso en poco tiempo?",
        "¿Tienes distorsión de la imagen corporal, es decir, te ves más gordo/a de lo que realmente eres?"
    ]

    respuestas = []

    for pregunta in preguntas:
        respuesta = input(pregunta + " (sí/no) ")
        respuestas.append(respuesta)

    puntos = 0

    # Asignar puntos basados en las respuestas
    for respuesta in respuestas:
        if respuesta.lower() == "sí":
            puntos += 1

    # Determinar si hay indicadores de trastornos alimentarios
    if puntos >= 4:
        resultado = "Existen indicios de trastornos alimentarios. Es importante que busques ayuda profesional para una evaluación más detallada."
    else:
        resultado = "No se detectan indicios claros de trastornos alimentarios. Sin embargo, si tienes preocupaciones, te recomendamos consultar a un profesional de la salud."

    # Mostrar el resultado
    print("\nResultado:")
    print(resultado)


# Ejecutar la evaluación
evaluar_trastornos_alimentarios()
