import calculadora_promedios as cp

calificaciones = []
materias = []
reprobadas = []
aprobadas = []
promedio = 0

def main():
    print(cp.encontrar_extremos(calificaciones))
    
    print(cp.calcular_promedio(calificaciones))

    # cp.main()


if __name__ == '__main__':
    main()