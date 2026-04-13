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
      "answer": "Las señales de tránsito pueden ser reglamentarias, preventivas e informativas. Cada una cumple la función de regular, advertir o informar a los usuarios de la vía."
    }
  ],
  "prioridad": [
    {
      "patterns": ["rotonda", "quién pasa primero en rotonda", "prioridad en rotonda", "cómo funciona la rotonda"],
      "answer": "Los vehículos que ya circulan dentro de la rotonda tienen prioridad sobre los que desean ingresar."
    },
    {
      "patterns": ["paso peatonal", "prioridad peatón", "peatón cruza", "reglas peatón"],
      "answer": "El conductor debe reducir la velocidad y detenerse si es necesario para permitir el paso seguro de los peatones."
    },
    {
      "patterns": ["intersección sin señales", "quién tiene prioridad", "cruce sin semáforo", "derecho de vía"],
      "answer": "En una intersección sin señalización, tiene prioridad el vehículo que viene por la derecha."
    }
  ],
  "circulacion": [
    {
      "patterns": ["reglas de tránsito", "normas de circulación", "cómo conducir", "reglas básicas"],
      "answer": "Debes conducir por el lado derecho de la vía, respetar señales y semáforos, y mantener una conducta responsable en todo momento."
    },
    {
      "patterns": ["uso del cinturón", "cinturón obligatorio", "seguridad en el carro", "protección conductor"],
      "answer": "El uso del cinturón de seguridad es obligatorio para todos los ocupantes del vehículo y reduce el riesgo de lesiones graves."
    },
    {
      "patterns": ["uso del celular", "puedo usar celular manejando", "distracciones al conducir", "hablar por teléfono"],
      "answer": "No se debe usar el celular mientras se conduce, ya que distrae y aumenta significativamente el riesgo de accidentes."
    }
  ],
  "velocidad": [
    {
      "patterns": ["límite de velocidad", "velocidad máxima", "cuánto es permitido", "velocidad en carretera"],
      "answer": "Los límites de velocidad dependen de la vía, pero generalmente son de 40 a 60 km/h en zonas urbanas y hasta 90 o 100 km/h en autopistas."
    },
    {
      "patterns": ["exceso de velocidad", "qué pasa si voy rápido", "multa velocidad", "riesgo por velocidad"],
      "answer": "Exceder los límites de velocidad aumenta el riesgo de accidentes y puede resultar en multas y sanciones."
    },
    {
      "patterns": ["velocidad en lluvia", "manejar con lluvia", "ajustar velocidad", "clima y conducción"],
      "answer": "Debes reducir la velocidad cuando hay lluvia o poca visibilidad para mantener el control del vehículo."
    }
  ],
  "defensiva": [
    {
      "patterns": ["conducción defensiva", "manejo seguro", "qué es manejo defensivo", "cómo evitar accidentes"],
      "answer": "La conducción defensiva consiste en anticiparse a los riesgos y actuar con precaución para evitar accidentes."
    },
    {
      "patterns": ["distancia de seguridad", "qué tan cerca manejar", "espacio entre carros", "seguir vehículo"],
      "answer": "Debes mantener una distancia segura con el vehículo de adelante para poder reaccionar ante cualquier imprevisto."
    },
    {
      "patterns": ["anticipar peligros", "prevenir accidentes", "riesgos en carretera", "reacción conductor"],
      "answer": "Debes estar atento al entorno y anticipar posibles situaciones peligrosas como frenadas bruscas o peatones."
    }
  ],
  "seguridad": [
    {
      "patterns": ["seguridad vial", "qué es seguridad vial", "importancia seguridad", "evitar accidentes"],
      "answer": "La seguridad vial busca prevenir accidentes y proteger la vida de todos los usuarios de la vía mediante normas y buenas prácticas."
    },
    {
      "patterns": ["conducir con alcohol", "manejar borracho", "alcohol y conducción", "riesgo alcohol"],
      "answer": "Está prohibido conducir bajo los efectos del alcohol, ya que reduce la capacidad de reacción y aumenta el riesgo de accidentes."
    },
    {
      "patterns": ["estado del vehículo", "revisión del carro", "mantenimiento vehículo", "seguridad mecánica"],
      "answer": "Es importante mantener el vehículo en buen estado mecánico, revisando frenos, luces y llantas regularmente."
    }
  ]
}

stopwords = [
    "a", "al", "algo", "como", "con", "de", "del", "el", "ella",
    "en", "entre", "era", "es", "esta", "este", "ha", "la",
    "las", "lo", "los", "más", "me", "mi", "no", "nos", "o",
    "para", "pero", "por", "que", "se", "sin", "sobre",
    "su", "sus", "un", "una", "y"
]

def limpiar_texto(texto):
    texto = texto.lower()

    # quitar tildes
    texto = ''.join(
        c for c in unicodedata.normalize('NFD', texto)
        if unicodedata.category(c) != 'Mn'
    )

    # eliminar signos
    for signo in string.punctuation:
        texto = texto.replace(signo, "")

    palabras = texto.split()

    # quitar stopwords
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


# busca respuesta

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
        return f"🐝 ¡Muy bien! {respuesta} 🚗✨ ¡Sigue así, lo estás haciendo genial!"
    else:
        return "🐝 Ups... creo que no entendí muy bien 🤔 ¿Puedes decirlo con otras palabras? ¡Estoy aquí para ayudarte! 💛"

# -------------------------------
# CHAT PRINCIPAL
# -------------------------------
while True:
    textobase = input("🐝 ¡Hola! Soy Caspi 🚦 ¿Qué quieres aprender? \nTú: ")

    if textobase.lower() in ["salir", "exit"]:
        print("🐝 ¡Gracias por aprender conmigo! 🚗✨ ¡Hasta pronto!")
        break

 