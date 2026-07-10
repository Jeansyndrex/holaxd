def validar_codigo(codigo, dicc_juegos):
  if not codigo or codigo.strip() == "":
    return False
  if codigo.upper() in dicc_juegos:
    return False
  return True

def validar_titulo(titulo):
  return titulo is not None and titulo.strip() != ""

def validar_plataforma(plataforma):
  return plataforma is not None and plataforma.strip() != ""

def validar_genero(genero):
  return genero is not None and genero.strip() != ""

def validar_clasificacion(clasificacion):
  return clasificacion in ['E', 'T', 'M']

def validar_multiplayer(multiplayer):
  return multiplayer.lower() in ['s', 'n']

def validar_editor(editor):
  return editor is not None and editor.strip() != ""

def validar_precio(precio_str):
  try:
    precio = int(precio_str)
    return precio > 0
  except ValueError:
    return False

def validar_stock(stock_str):
  try:
    stock = int(stock_str)
    return stock >= 0
  except ValueError:
    return False


def leer_opcion():
  while True:
    try:
      opcion_str = input("Seleccione una opcion del menu: ")
      opcion = int(opcion_str)
      if 1 <= opcion <= 6:
        return opcion
      else:
        print("Debe seleccionar una opción válida")

    except ValueError:
      print("Debe seleccionar una opción válida")

def stock_plataforma(plataforma, dicc_juegos, dicc_inventario):
  total_stock = 0
  plataforma_buscar = plataforma.strip().lower()
  for codigo, datos in dicc_juegos.items():
    if datos[1].lower() == plataforma_buscar:
      if codigo in dicc_inventario:
        total_stock += dicc_inventario[codigo][1]
  print(f"\nTotal disponible para esta plataforma: '{plataforma}': {total_stock}")

def busqueda_precio(p_min, p_max, dicc_juegos, dicc_inventario):
  resultados = []
  for codigo, datos_inv in dicc_inventario.items():
    precio = datos_inv[0]
    stock = datos_inv[1]
    if p_min <= precio <= p_max and stock > 0:
      if codigo in dicc_juegos:
        titulo = dicc_juegos[codigo][0]
        resultados.append(f"{titulo}--{codigo}")

  if resultados:
    resultados.sort()
    print("\nSe encontraron juegos en su rango de presupuesto:")
    for juego in resultados:
      print(f"- {juego}")

  else:
    print("\nNo tenemos juegos en ese rango de presupuesto :c (Cara triste).")

def buscar_codigo(codigo, dicc):
  return codigo.upper() in dicc

def actualizar_precio(codigo, nuevo_precio, dicc_inventario):
  if buscar_codigo(codigo, dicc_inventario):
    dicc_inventario[codigo.upper()][0] = nuevo_precio
    return True
  return False

def agregar_juego(codigo, titulo, plataforma, genero, clasificacion, multiplayer, editor, precio, stock, dicc_juegos, dicc_inventario):
  cod_upper = codigo.upper()
  if cod_upper in dicc_juegos:
    return False
  mp_bool = True if multiplayer.lower() == 's' else False
  dicc_juegos[cod_upper] = [titulo.strip(), plataforma.strip(), genero.strip(), clasificacion, mp_bool, editor.strip()]
  dicc_inventario[cod_upper] = [int(precio), int(stock)]

  return True


def main():

  juegos = {
    "G001": ["Eclipse Runner", "PC", "accion", "T", True, "NovaStudio"],
    "G002": ["Puzzle Atlas", "Switch", "puzzle", "E", False, "BrightWorks"],
    "G003": ["Sky Legends", "PS5", "aventura", "T", True, "OrionGames"],
    "G004": ["Racing Pulse", "PC", "carreras", "E", True, "VelocityLab"],
    "G005": ["Mystic Farm", "Switch", "simulacion", "E", False, "GreenSeed"],
    "G006": ["Shadow Tactics", "Xbox", "estrategia", "M", False, "IronGate"]
  }

  inventario = {
    "G001": [9990, 7],
    "G002": [19990, 0],
    "G003": [42990, 3],
    "G004": [14990, 5],
    "G005": [17990, 9],
    "G006": [39990, 2]
  }

  while True:
    print("\n....MENÚ PRINCIPAL....")
    print("1: Stock por plataforma")
    print("2: Búsqueda de juegos por rango de precio")
    print("3: Actualizar precio de juego")
    print("4: Agregar juego")
    print("5: Eliminar juego")
    print("6: Salir")

    opcion = leer_opcion()

    if opcion == 1:
      plat = input("Ingrese el nombre de la plataforma donde quiere buscar: ")
      stock_plataforma(plat, juegos, inventario)

    elif opcion == 2:
      while True:
        try:
          p_min_str = input("¿Cual es su presupuesto minimo?")
          p_max_str = input("¿Cual es su presupuesto maximo?")
          p_min = int(p_min_str)
          p_max = int(p_max_str)
          if p_min >= 0 and p_max >= 0 and p_min <= p_max:
            busqueda_precio(p_min, p_max, juegos, inventario)

            break

          else:
            print("Precio debe ser mayor o igual a cero y el minimo debe ser menor al maximo.")

        except ValueError:
          print("Porfavor ingrese un valor entero (Gracias)")



    elif opcion == 3:
      procesar_otro = 's'
      while procesar_otro.lower() == 's':
        cod = input("Ingrese el código del juego: ")
        nuevo_p_str = input("Ingrese el nuevo precio: ")

        if validar_precio(nuevo_p_str):

          nuevo_p = int(nuevo_p_str)

          if actualizar_precio(cod, nuevo_p, inventario):

            print("El precio del juego fue actualizado....")

          else:
            print("El código no existe")

        else:
          print("Precio inválido, ingrese un precio mayor a cero.")

         

        procesar_otro = input("¿Desea actualizar el precio de otro juego?: ")

    elif opcion == 4:

      print("\n....Registra un nuevo VideoJuego....")

      cod = input("Código: ")

      tit = input("Título: ")

      plat = input("Plataforma: ")

      gen = input("Género: ")

      clas = input("Clasificación (E, T, M): ")

      mult = input("¿Es multiplayer? (s/n): ")

      edit = input("Editor: ")

      prec = input("Precio: ")

      stk = input("Stock: ")


      if not validar_codigo(cod, juegos):
        print("Error 505: El código no puede estar vacio o repetirse.")

      elif not validar_titulo(tit):
        print("Error 506: El título no puede estar vacio.")
      
      elif not validar_plataforma(plat):
        print("Error 507: La plataforma no puede estar vacia.")

      elif not validar_genero(gen):
        print("Error 508: El genero no puede estar vacio.")
      
      elif not validar_clasificacion(clas):
        print("Error 509: La clasificación tiene que ser 'E', 'T' o 'M'.")

      elif not validar_multiplayer(mult):
        print("Error 510: En multiplayer debe ingresar 's' o 'n'.")

      elif not validar_editor(edit):
        print("Error 511: El editor no puede estar vacío.")

      elif not validar_precio(prec):
        print("Error 512: El precio tiene que ser un numero entero mayor a cero.")

      elif not validar_stock(stk):
        print("Error 513: El stock debe ser un numero entero mayor o igual a cero.")

      else:
        exito = agregar_juego(cod, tit, plat, gen, clas, mult, edit, prec, stk, juegos, inventario)

        if exito:
          print("EL juego fue agregado")

        else:
          print("El codigo ya existe")



    elif opcion == 5:
      cod_eliminar = input("¿Cual es el codigo del juego que quiere eliminar?").upper()

      if buscar_codigo(cod_eliminar, juegos):
        del juegos[cod_eliminar]
        del inventario[cod_eliminar]

        print("¡¡Felicidades!! El juego se elimino de ambos catalogos efectivamente.")

      else:
        print("El código no existe.")



    elif opcion == 6:
      print("Terminando el programa... ¡Vuelva luego! jaja")

      break



if __name__ == "__main__":

  main()