meme_dict = {
    "CRINGE": "Algo excepcionalmente raro o embarazoso",
    "LOL": "Una respuesta común a algo gracioso",
    "XD": "Una reacción a algo divertido",
    "BRB": "Me ausentaré momentáneamente",
    "FTW": "Expresa entusiasmo o apoyo por algo",
    "OMG": "Una reacción de sorpresa o asombro",
    "CREEPY": "Algo aterrador o siniestro",
    "AGGRO": "Algo excepcionalmente agresivo o raro",
    "ROFL": "Una respuesta bromista o divertida",
    "SHEESH": "Respuesta de ligera desaprobacion",
    "TTYL": "Una respuesta a una despedida con la intención de hablar más tarde",
    "AFK": "Voy a estar lejos del teclado o inactividad",
    "GG": "Indica disfrutar un juego o ganar un videojuego ",
    "IMO": "Indica una expresion de en mi opinión",
    "IRL": "Respuesta de en la vida real",
    "TL;DR": "Tu texto es bastante largo; No lo leí",
    "FOMO": "Miedo a perderse algo)",
    "ICYMI": "Reaccion hacia por si te lo perdiste)",
    "BRUH": "Expresión de incredulidad o desaprobación",
    "BFF": "Expresion de mejores amigos por siempre)",
    }
    
    
print("Bienvenido al diccionario de memes╰(*°▽°*)╯")
print("Por favor escribe cinco palabras que no entiendas en el diccionario")
    
for i in range(5):
    word = input("Escribe una palabra que no entiendas (en mayúsculas): ")

    if word in meme_dict.keys():
        print("Significado de", word, ":", meme_dict[word])
    else:
        print("Lo siento, no tengo información sobre la palabra", word)
