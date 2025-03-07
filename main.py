meme_dict = {
            "CRINGE": "Algo excepcionalmente raro o embarazoso",
            "LOL": "Una respuesta común a algo gracioso",
            "ROFL":"Una respuesta a una broma",
            "SHEESH":"LIGERA DESAPROBACION",
            "CREEPY":"Aterrador,siniestro",
            "AGGRO":"Ponerse agresivo/enojado"
            }

word = input("Escribe una palabra que no entiendas (¡Blop Mayus activado!): ")

if word in meme_dict.keys():
    print(meme_dict[word])
else:
    print("Esa palabra no esta")
