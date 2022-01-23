def descomponer(num):
  
  if num <= 9999 and num >= 0:
    u = num // 1 % 10
    d = num // 10 % 10
    c = num // 100 % 10
    m = num // 1000 % 10

    u = int(str(u))
    d = int(str(d)+"0")
    c = int(str(c)+"00")
    m = int(str(m)+"000")

    print("La descomposición del número *"+str(num)+"* es:\n")
    print("Unidades: {:04}".format(u))
    print("Decenas:  {:04}".format(d))
    print("Centenas: {:04}".format(c))
    print("Miles:    {:04}".format(m))
  
  else:
    print("ERROR\nEl script solo descompone números enteros positivos del 0 al 9999 , trate de ingresar un número dentro de ese rango.")
