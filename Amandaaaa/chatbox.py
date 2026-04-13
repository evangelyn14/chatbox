import string
import unicodedata


base_conocimiento = {
  "señales": [
    {
      "patterns": ["alto", "pare", "señal de alto", "detenerse en alto"],
      "answer": "Debes detener el vehículo completamente antes de continuar, verificando que no haya otros vehículos o peatones."
    },
    {
      "patterns": ["ceda", "ceda el paso", "señal de ceder", "dar prioridad"],
      "answer": "Debes reducir la velocidad y permitir el paso a otros vehículos o peatones antes de continuar."
    },
    {
      "patterns": ["señales de tránsito", "tipos de señales", "señales viales", "clasificación de señales"],
      "answer": "Las señales de tránsito pueden ser reglamentarias, preventivas e informativas."
    }
  ],
  "prioridad": [
    {
      "patterns": ["rotonda", "quién pasa primero en rotonda", "prioridad en rotonda", "cómo funciona la rotonda"],
      "answer": "Los vehículos que ya circulan dentro de la rotonda tienen prioridad sobre los que desean ingresar."
    },
    {
      "patterns": ["paso peatonal", "prioridad peatón", "peatón cruza", "reglas peatón"],
      "answer": "Debes reducir la velocidad y detenerte para permitir el paso seguro de los peatones."
    },
    {
      "patterns": ["intersección sin señales", "quién tiene prioridad", "cruce sin semáforo", "derecho de vía"],
      "answer": "Tiene prioridad el vehículo que viene por la derecha."
    }
  ],
  "circulacion": [
    {
      "patterns": ["reglas de tránsito", "normas de circulación", "cómo conducir", "reglas básicas"],
      "answer": "Debes conducir por el lado derecho, respetar señales y actuar con responsabilidad."
    },
    {
      "patterns": ["uso del cinturón", "cinturón obligatorio", "seguridad en el carro"],
      "answer": "El cinturón de seguridad es obligatorio para todos los ocupantes."
    },
    {
      "patterns": ["uso del celular", "puedo usar celular manejando", "distracciones al conducir"],
      "answer": "No debes usar el celular mientras conduces."
    }
  ],
  "velocidad": [
    {
      "patterns": ["límite de velocidad", "velocidad máxima", "velocidad en carretera"],
      "answer": "Generalmente 40-60 km/h en ciudad y hasta 90-100 km/h en autopistas."
    },
    {
      "patterns": ["exceso de velocidad", "multa velocidad", "riesgo por velocidad"],
      "answer": "Aumenta el riesgo de accidentes y genera sanciones."
    },
    {
      "patterns": ["velocidad en lluvia", "manejar con lluvia"],
      "answer": "Debes reducir la velocidad por seguridad."
    }
  ],
  "defensiva": [
    {
      "patterns": ["conducción defensiva", "manejo seguro"],
      "answer": "Consiste en anticiparse a los riesgos y conducir con precaución."
    },
    {
      "patterns": ["distancia de seguridad", "espacio entre carros"],
      "answer": "Debes mantener distancia para reaccionar ante imprevistos."
    }
  ],
  "seguridad": [
    {
      "patterns": ["seguridad vial", "importancia seguridad"],
      "answer": "Busca prevenir accidentes y proteger vidas."
    },
    {
      "patterns": ["conducir con alcohol", "manejar borracho"],
      "answer": "Está prohibido y es muy peligroso."
    }
  ]
}

stopwords = [
    "a","al","como","con","de","del","el","en","la","las","lo","los",
    "para","por","que","se","un","una","y"
]

def limpiar_texto(texto):
    texto = texto.lower()

    texto = ''.join(
        c for c in unicodedata.normalize('NFD', texto)
        if unicodedata.category(c) != 'Mn'
    )

    for signo in string.punctuation:
        texto = texto.replace(signo, "")

    palabras = texto.split()

    resultado = []
    for palabra in palabras:
        if palabra not in stopwords:
            resultado.append(palabra)

    return resultado

def similitud(frase_usuario, pattern):
    tokens_usuario = limpiar_texto(frase_usuario)
    tokens_pattern = limpiar_texto(pattern)

    coincidencias = 0
    for palabra in tokens_usuario:
        if palabra in tokens_pattern:
            coincidencias += 1

    return coincidencias

def obtener_respuesta(mensaje):
    mejor_score = 0
    mejor_respuesta = None

    for categoria in base_conocimiento.values():
        for item in categoria:
            for pattern in item["patterns"]:
                score = similitud(mensaje, pattern)

                if score > mejor_score:
                    mejor_score = score
                    mejor_respuesta = item["answer"]

    return mejor_respuesta, mejor_score


def responder(mensaje):
    respuesta, score = obtener_respuesta(mensaje)

    if respuesta and score > 0:
        return f"🐝 ¡Muy bien! {respuesta} 🚗✨"
    else:
        return "🐝 No entendí muy bien 🤔 intenta otra pregunta 💛"


print("🐝 ¡Hola! Soy Caspi 🚦 Aprende conmigo sobre educación vial")

while True:
    textobase = input("\nTú: ")

    if textobase.lower() in ["salir", "exit"]:
        print("🐝 ¡Hasta pronto! 🚗✨")
        break

    print("Caspi:", responder(textobase))
