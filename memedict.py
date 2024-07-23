meme_dict = {
            "CRINGE": "Sentimiento de verguenza ajena hacia cosas embarazosas y/o raras",
            "LOL": "Una respuesta común a algun chiste y/o algo gracioso",
            "FYP": "'for you page', significa: pagina de 'para ti', generalmente usado en apps como TikTok o Instagram",
            "IDK": "'I DONT KNOW' significa: yo no se/no se.",
            "esteesuneasteregg": "UN EASTER EGG?!?!!? WAOOOOOOOSSS XDDDD",
            }
word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")

if word in meme_dict.keys():
    # ¿Qué debemos hacer si se encuentra la palabra?
    print(meme_dict[word])
else:
    # ¿Qué hacer si no se encuentra la palabra?
    print("la palabra no esta en el diccionario.")
