def line():
    print("TO DO")
    A = float(input("Ingrese el coeficiente A: "))
    B = float(input("Ingrese el coeficiente B: "))
    X1 = float(input("Ingrese el coeficiente X1: "))
    X2 = float(input("Ingrese el coeficiente X2: "))

    Y1 = A * X1 + B
    Y2 = A * X2 + B

    print("El coeficiente A de su ecuación de la recta es:", A)
    print("El coeficiente B de su ecuación de la recta es:", B)
    print("El coeficiente X1 de su ecuación de la recta es:", X1)
    print("El coeficiente X2 de su ecuación de la recta es:", X2)

    print("La ecuación es: Y = ", A, "X +", B)

    print("El punto P1 es:", "(", X1, ",", Y1, ")")
    print("El punto P2 es:", "(", X2, ",", Y2, ")")

    distancia = math.sqrt((X2 - X1)**2 + (Y2 - Y1)**2)

    print("La distancia entre ellos es:", distancia)
line()
