nombres = ["ana","hugo","valeria"]
edades = [65,29,42]
ciudades = ["lima","madrid","mexico"]

combinados = list(zip(nombres,edades,ciudades))

for nombre,edad,ciudad in combinados:
    print(f"{nombre} tiene la edad {edad} años y vive en {ciudad}")