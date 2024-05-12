import time
print('Hola en este programa conocera sobre palabras actuales que algunos no saben el significado por favor ingrese su palabra que no sabe el significado en mayusculas')
meme_dict = {
            "CRINGE": "Algo excepcionalmente raro o embarazoso",
            "LOL": "Una respuesta común a algo gracioso",
            "ROFL": "una respuesta a una broma",
            "SHEESH": "ligera desaprobación",
            "CREEPY": "aterrador, siniestro",
            "AGGRO": "ponerse agresivo/enojado",
            }
for i in range(5):
    time.sleep(2)
    word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")
    if word in meme_dict.keys():
        print(meme_dict[word])
    else:
        print('Lo sentimos no tenemos regristrado esa palabra')
