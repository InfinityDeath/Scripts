def tabla():
  n1= int(input("\nINGRESE EL PRIMER NÚMERO ENTERO POSITIVO DEL 1 AL 9: "))
  while not(n1 > 0 and n1 < 10):
    if n1 <= 0 or n1 >= 10:
      n1 = int(input("\nERROR\nPARA UTILIZAR ESTE SCRIPT, DEBE INGRESAR 2 NÚMEROS ENTEROS POSITIVOS DEL 1 AL 9.\nEl PRIMER NÚMERO INDICARÁ EL NÚMERO DE FILAS DE UNA TABLA DIBUJADA POR ASTERISCOS\nEL SEGUNDO NÚMERO INDICARÁ LA CANTIDAD DE COLUMNAS DE LA TABLA\nPor favor, ingrese el primer número correctamente: "))

  n2= int(input("\nINGRESE EL SEGUNDO NÚMERO ENTERO POSITIVO DEL 1 AL 9: "))
  while not(n2 > 0 and n2 < 10):
    if n2 <= 0 or n2 >= 10:
      n2 = int(input("\nERROR\nPARA UTILIZAR ESTE SCRIPT, DEBE INGRESAR 2 NÚMEROS ENTEROS POSITIVOS DEL 1 AL 9.\nEl PRIMER NÚMERO INDICARÁ EL NÚMERO DE FILAS DE UNA TABLA DIBUJADA POR ASTERISCOS\nEL SEGUNDO NÚMERO INDICARÁ LA CANTIDAD DE COLUMNAS DE LA TABLA\nPor favor, ingrese el segundo número correctamente: "))

  for i in range(n1):
    for e in range(n2):
      print("*", end='')
    print("")
