# Condiciones Anidadas elif

sensorNivelAgua = int(input("Digite el nivel de agua actual: "))

if(sensorNivelAgua >= 0 and sensorNivelAgua < 20):
    print(f'Peligro, el nivel {sensorNivelAgua} es peligroso')
elif(sensorNivelAgua >= 20 and sensorNivelAgua < 400):
    print(f'Seguro, el nivel {sensorNivelAgua} es seguro')
elif(sensorNivelAgua >= 400):
    print(f'Peligro, el nivel {sensorNivelAgua} es peligroso')
else:
    print("Digite un nivel correcto")