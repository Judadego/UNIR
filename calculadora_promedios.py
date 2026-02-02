#----------------------------------------------------------#
#                SISTEMA DE CALIFICACIONES                 #
#  CALCULO DE PROMEDIO, ANALISIS DE MATERIAS APROBADAS Y   #
#                      REPROBADAS                          #
# Responsable : Julian David Delgado Gonzalez              #
# Iniciativa: Trabajo 1 Syntaxis Python                    #
# UNIR CURSO DE PROGRAMACION EN PYTHON                     $
# Fecha creación: 01 de Febrero de 2026                    #
# Fecha Modificacion: N/A                                  #
#----------------------------------------------------------#
#umbral = 5
opcion = 0
mensaje = ''
separador = '----------------------------------------'

#Funcion principal
def main():
    umbral = 5
    calificaciones = []
    materias = []
    reprobadas = []
    aprobadas = []
    promedio = 0
    
    #bienvenida
    opcion = 1                                                           
    ingreso_inf(opcion)                                                  #bienvenida
    
    #ingreso de materias y calificaciones
    calificaciones, materias = ingresar_calificaciones()   
    
    if len(calificaciones) > 0:    
        #calculo de promedio                                
        promedio = calcular_promedio(calificaciones)                         
        print(f'El promedio es: {promedio}')

        #Estado aprobado o reprobado
        aprobadas,reprobadas = determinar_estado(calificaciones,umbral)  

        #muestra el estado hallado    
        muestra_estado(aprobadas,reprobadas,materias)      

        #encuentra nota menor y mayor                  
        indice_menor, indice_mayor = encontrar_extremos(calificaciones)   

        #muestra nota mayor y menor    
        muestra_extremos(indice_menor,indice_mayor,materias,calificaciones)  
    
    else:
        print("\n[!] No se ingresaron materias. No hay datos para calcular.")
    
    #agradecimiento                           
    ingreso_inf(-1)                                                  


def ingresar_calificaciones():
    calificaciones = []
    materias = []
    opcion = 0
    #ingreso confirmacion para continuar y/n
    opcion = 4 
    opcion = ingreso_inf(opcion)
    while opcion != -1:
        #ingresa materias
        opcion = 2
        materia = ingreso_inf(opcion)
        #ingresa calificaciones
        opcion = 3
        calificacion = ingreso_inf(opcion)
        #ingreso confirmacion para continuar y/n
        opcion = 4 
        opcion = ingreso_inf(opcion)
        #agregamos calificaciones a la lista
        calificaciones.append(calificacion)
        #agregamos materias a la lista
        materias.append(materia)
        #muestra resultados si confirmacion para continuar es n
        if opcion == -1:
            mostrar_resultados(materias, calificaciones)
    return   calificaciones,materias                   


#muestra resultados guardados
def mostrar_resultados(materias,calificaciones):
    print(separador)
    print('|Muestra de resultados ingresados      |')
    print(separador)
    
    for materia, calificacion in zip(materias , calificaciones):
        print(f'{materia.upper()} = {calificacion}')
            
#calcula el promedio
def calcular_promedio(calificaciones):
    if len(calificaciones) == 0:
        return 0
    else:
        suma = sum(calificaciones)
        promedio = suma / len(calificaciones)
        return promedio
    
#determina si aprueba o reprueba
def determinar_estado(calificaciones, umbral):

    aprobadas = []
    reprobadas = []
    for i,calificacion in enumerate(calificaciones):
        if calificacion >= umbral:
            aprobadas.append(i)
        else:
            reprobadas.append(i)
    return aprobadas, reprobadas

#muestra las materias reprobadas y aprobadas
def muestra_estado(aprobadas,reprobadas,materias):
    print(separador)
    print('Lista de materias aprobadas')
    print(separador)
    for indice in aprobadas:
        print(f'{materias[indice]} ')

    print(separador)
    print('Lista de materias reprobadas')
    print(separador)
    for indice in reprobadas:
        print(f'{materias[indice]} ')
        
#identifica la nota mas alta y mas baja
def encontrar_extremos(calificaciones):
    if len(calificaciones) != 0:
        cali_mayor = calificaciones[0]
        cali_menor = calificaciones[0]
        indice_mayor = 0
        indice_menor = 0
    else:
        return None, None
    
    for i,calificacion in enumerate(calificaciones):
        if calificacion >= cali_mayor:
            cali_mayor = calificacion
            indice_mayor = i
        if calificacion < cali_menor:
            cali_menor = calificacion
            indice_menor = i
    
    return indice_menor, indice_mayor

#muestra extremos
def muestra_extremos(indice_menor,indice_mayor,materias,calificaciones):
            
    print(separador)
    print(f'La materia con más calificación es {materias[indice_mayor]} con una calificación de {calificaciones[indice_mayor]}')
    
    print(separador)
    print(f'La materia con menos calificación es {materias[indice_menor]} con una calificación de {calificaciones[indice_menor]}')

def ingreso_inf(opcion):
    separador = '----------------------------------------'
    print(separador)
    #opcion 1 bienvenida 
    if opcion == 1 or opcion == -1:
        opcion = opcion_1(opcion)
        return opcion
    #opcion 2 pide materia
    elif opcion == 2:
        mensaje = 'Ingresa la materia: '
        materia = ingreso_alfa(mensaje)
        return materia
    #opcion 3 pide calificaciones
    elif opcion == 3:
        mensaje = 'Ingresa la calificación: '
        calificacion = ingreso_num(mensaje)
        return calificacion
    #continuar ingresando
    elif opcion == 4:
        valida,opcion = opcion_4()
        return opcion
        

#opcion numero 1 Bienvenida y despedida.
def opcion_1(opcion):
    if opcion == 1:
        mensaje = 'Bienvenido al Sistema de Calificaciones.'
    else:
        mensaje = 'Gracias por usar el sistema de calificaciones.'
    print(mensaje)
    opcion = 0
    return opcion

#opcion numero 4 confirmacion para continuar o finalizar
def opcion_4():
        while True:
            ingreso = input('¿Ingresar más calificaciones? (y/n): ').lower().strip()            
            if ingreso == 'y':
                opcion = 0
                return True,opcion
            elif ingreso == 'n':
                opcion = -1
                return True,opcion
            else:
                print('Entrada inválida. Por favor, ingresa "y" o "n".')
            
def ingreso_alfa(mensaje):

    materia = ''    
    while materia == '':
        materia = input(mensaje).upper().strip()
        if materia == '':
            mensaje = 'Entrada inválida. La materia no puede ser vacía. Intenta de nuevo.\nIngresa la materia: '
    return materia


##infreso de variables numericas
def ingreso_num(mensaje):
    
    while True:
        try:
            calificacion = float(input(mensaje))          
            if 0 <= calificacion <= 10:
                return calificacion
            else:
                mensaje = 'Error: La calificación debe estar entre 0.0 y 10.0. Intenta de nuevo.\nIngresa la calificación:  '
        
        except ValueError:
            mensaje = 'Entrada inválida. Por favor, \ningresa un número (ej: 8.5): '
    
if __name__ == '__main__':
    main()