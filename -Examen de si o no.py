from io import open_code


nombre_apellido = input('Por favor escriba su nombre y apellido\r\n')
total = 0
print('Este es una examen de V o F, otras respuestas no seran admitidas')
print('Pregunta 1:\r\n2x9 es igual a 18 ¿V o F?')
Rcorrect = ['V', 'v', 'Verdadero', 'Si', 'si', 's']
Rfalso = ['F', 'f', 'Falso', 'No', 'no', 'n']
p1 = True
while p1 == True:

    respuesta_1 = input()
    if respuesta_1 in Rcorrect:
        total += 1
        p1= False
    elif respuesta_1 in Rfalso:
        total += 0
        p1= False
    else:
        print('Esa no es una respuesta admitida.\r\nSolo se admiten respuestas del siguiente tipo: V, F, Si, No.')

print('Pregunta 2:\r\nWalt Disney aun vive, ¿V o F?')
p2 = True
while p2 == True:

    respuesta_2 = input()
    if respuesta_2 in Rcorrect:
        total += 0
        p2= False
    elif respuesta_2 in Rfalso:
        total += 1
        p2= False
    else:
        print('Esa no es una respuesta admitida.\r\nSolo se admiten respuestas del siguiente tipo: V, F, Si, No.')

print('Estamos cerca del final!! \r\n Argentina es un pais de Europa, ¿V o F?')
p3 = True
while p3 == True:

    respuesta_3 = input()
    if respuesta_3 in Rcorrect:
        total += 0
        p3= False
    elif respuesta_3 in Rfalso:
        total += 1
        p3= False
    else:
        print('Esa no es una respuesta admitida.\r\nSolo se admiten respuestas del siguiente tipo: V, F, Si, No.')

print('Esta es la pregunta final!!! \r\n Los pulpos tienen 3 corazones, ¿V o F?')
p4 = True
while p4 == True:
    respuesta_4 = input()
    if respuesta_4 in Rcorrect:
        total += 1
        p4= False
    elif respuesta_4 in Rfalso:
        total += 0
        p4= False
    else:
        print('Esa no es una respuesta admitida.\r\nSolo se admiten respuestas del siguiente tipo: V, F, Si, No.')

if total == 4:
    print(f'Tuvo un puntaje de {total}, por lo tanto tuvo un puntaje PERFECTO!!!')
elif total >= 2:
    print(f'Su puntaje fue {total}, aprueba.')
else:
    print(f'Tristemente su puntaje fue de {total}, por lo tanto... Desaprueba...')

print(f'{nombre_apellido}, puede volver a intentarlo cuantas veces quiera. Gracias por participar!')