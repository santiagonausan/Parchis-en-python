import random
"""""
JUEGO PARQUES SIMPLE
"""

def main():    
    """"
Funcion principal para el programa, se encarga de mostrar el menu, y de manejar el estado de juego.
"""
    print("Seleccione una opcion.\n1. Juego Normal\n2. Modo desarrollador\n3. Reglas\n4. Créditos")
    seleccion = int(input())
    if seleccion == 1:
        modo_normal()
    elif seleccion == 2:
        modo_desarrollador()
    elif seleccion == 3:
        reglas()
    elif seleccion == 4:
        creditos()


def creditos():
    """"
Funcion que se encarga de mostrar los créditos del juego.

"""
        
    print("Hola!\nBienvenido al juego de parques, a continuación encontrarás los créditos del juego. ")
    input("Use cualquier tecla para continuar...\n")
    print("Juego Desarrollado por David Santiago Nausan Rodríguez. ")
    input("Use cualquier tecla para continuar...\n")
    print("Universidad Nacional de Colombia. ")
    input("Use cualquier tecla para continuar...\n")
    print("Facultad de Ingeniería. ")
    input("Use cualquier tecla para continuar...\n")
    print("Realizado en 2025. ")
    print("Fin de los créditos. ")
    main()  
    

def reglas():
    """"
Funcion que se encarga de mostrar las reglas del juego, las reglas se almacenan dentro de esta funcion para que el codigo sea mas legible.
Incluye arte ASCII para el titulo de las reglas
"""
    print (r"______ _____ _____  _       ___   _____ ")
    print (r"| ___ \  ___|  __ \| |     / _ \ /  ___|")
    print (r"| |_/ / |__ | |  \/| |    / /_\ \\ `--. ")
    print (r"|    /|  __|| | __ | |    |  _  | `--. \\")
    print (r"| |\ \| |___| |_\ \| |____| | | |/\__/ /")
    print (r"\_| \_\____/ \____/\_____/\_| |_/\____/ ")
        
    print("Hola!\nBienvenido al juego de parques, a continuación encontrarás instrucciones sobre el juego. ")
    input("Use cualquier tecla para continuar...\n")
    print ("-|REGLAS BÁSICAS|-\nEl juego debe ser jugado exactamente por 4 jugadores, a cada jugador se le asigna un color distinto. Todos los jugadores tienen en su posesión 4 fichas. \nEl objetivo del juego es llevar las fichas hasta la meta .Durante el transcurso del juego, siempre se usan dos dados estándar de 6.")
    input("Use cualquier tecla para continuar...\n")
    print("===============================================================================")
    print ("Al comenzar el juego, cada jugador empieza con sus fichas en la cárcel.\nPara poder sacarlas, deben usar los dados y sacar 5, sea por el resultado de cualquiera de los dos dados, o por la combinación del resultado de ambos dados.\nPor cada 5 que saque el jugador, puede sacar una ficha. Si el jugador no saca 5 al tener todas las fichas en la cárcel, debe pasar su turno.")
    input("Use cualquier tecla para continuar...\n")
    print("===============================================================================")
    print ("Una vez tenga fichas en juego, si no saca 5 tiene la opción de mover sus fichas. \nSi solo tiene una ficha, debe moverse el equivalente al resultado de ambos dado.\nSi tiene más de una ficha, puede escoger entre mover una sola ficha el resultado total de ambos dados, o mover dos dados con el dado de su elección.")
    print("Cada jugador tiene una meta distinta. Dentro del tablero también pueden encontrar casillas especiales, como la salida y el seguro. \nLa salida indica donde se ponen las fichas de cada color al salir de la cárcel. \nEl seguro permite que las fichas estén a salvo de ataques enemigos.")
    input("Use cualquier tecla para continuar...\n")
    print("===============================================================================")
    print ("Para capturar una ficha enemiga, es decir, devolverla a su respectivo color, es necesario pasar o tocar la ficha,es decir,sacar más o igual que la distancia a la ficha enemiga.\nPor ejemplo: Asumiendo que nuestra ficha está en la casilla #5, y hay una ficha enemiga en la casilla #8:")
    print ("[ ],[ ],[ ],[ ],[F],[ ],[ ],[FE],[ ],[ ]")                                    
    print (" 1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10")
    print ("Si sacamos 3:")
    print ("[ ],[ ],[ ],[ ],[],[ ],[ ],[F],[ ],[ ], F -> FE")                                    
    print (" 1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10")
    print ("Si sacamos mas de 3, por ejemplo, 5:")
    print ("[ ],[ ],[ ],[ ],[],[ ],[ ],[ ],[ ],[F], F-> FE")                                    
    print (" 1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10")
    input("Use cualquier tecla para continuar...\n")
    print("===============================================================================")
    print("Finalmente, una ficha en un seguro o salida no puede ser capturada. Cada casilla puede tener máximo dos fichas, esto genera un bloqueo\nSi existe un bloqueo, cualquier ficha puede llegar maximo hasta una casilla menos del bloqueo.")
    print("Si existe un bloqueo en la salida, al sacar 5 no es posible sacar fichas de la carcel, por lo que es obligatorio mover una ficha de la salida.\nTambien es posible sacar y mover en el mismo turno, si un dado da 5.\nPrimero se debe mover la ficha de la salida, y luego se puede sacar una ficha de la carcel.")
    print("Si no hay movimientos posibles, se salta el turno")
    print("Si una ficha captura a otra, se pueden efectuar 20 movimientos con cualquier ficha de dicho equipo, siempre y cuando sea posible, considerando las reglas anteriores.")
    print ("Si una ficha llega a su llegada, entonces se pueden efectuar 10 movimientos con cualquier ficha de dicho equipo, siempre y cuando sea posible, considerando las reglas anteriores.")
    input("Use cualquier tecla para continuar...\n")
    print("===============================================================================")
    print ("Si el lanzamiento de los dados resulta en dados iguales (si los dados son par) entonces el lanzamiento del equipo actual se repite")
    print ("Si un equipo saca tres pares consecutivos, la úlitma ficha que haya movido deberá regresar a la cárcel.")    
    print ("Un equipo ganará si todas sus fichas están en la llegada.")
    print("===============================================================================")
    print("Fin de las reglas")
    main()  
    
       
def crear_jugadores():
    """
    Funcion para crear jugadores, almacena datos simples como su nombre,color,etc
    """
    playerlist = []
    color_list = ["🔴","🟠","🟡","🟢","🔵","🟣","⚫","⚪"]
    name_list = []
    
    for i in range(1,5):
        numerojugador = "Jugador"+str(i)
        numerojugador = {"Nombre" : '', 'Color': '','Piezas' : {}}
        valido = False
        nombrevalido = False
        while nombrevalido == False:
            nombre = input("Ingrese el nombre para el jugador "+str(i)+":\n")
            if nombre not in name_list:
                name_list.append(nombre)
                numerojugador["Nombre"] = nombre                       
                nombrevalido = True      
            else:
                print ("Ese nombre ya esta en uso! Seleccione un nuevo nombre.")
            
        for opcion_color in color_list:
            print (color_list.index(opcion_color), "-->" ,opcion_color)            
        while valido == False:
            try:
                color = int(input("Seleccione un color de la lista usando numeros:"))
                if 0 <= color <= len(color_list)-1:                                        
                    numerojugador['Color'] = color_list[color]
                    color_list.pop(color)
                    valido = True                    
                else:
                    print("Error en seleccion! Intente nuevamente.")
            except ValueError:
                print ("Error en seleccion! Asegurese de ingresar un numero entero")
        for i in range (1,5):         
            pieza = str(i) + numerojugador["Color"] 
            numerojugador["Piezas"][pieza] = 0           
             
        playerlist.append(numerojugador)
        print("===============================================================================")
    
    print("Lista de jugadores final:")
    
    for player in playerlist:
        print (player)
        
    return playerlist


def check_condicion(jugador:dict):
    """""
    Funcion para revisar la condicion en la que se encuentra el jugador.
    Condicion 1 - Todas las fichas estan en carcel, el jugador solo puede sacar fichas.
    Condicion 2 - El jugador tiene al menos una ficha en la carcel, puede sacar o mover fichas.
    Condicion 3 - El jugador no tiene fichas en la carcel, solo puede mover fichas.
    """
    encarcel = 0
    for pieza in jugador["Piezas"]:
        if jugador["Piezas"][pieza][1] == True:
            encarcel +=1
    if encarcel == 4:
        return 1 , "Todas tus fichas estan en carcel."
    elif encarcel > 0 and encarcel < 4:  
        return 2 , "Tienes" ,encarcel, "ficha(s) en carcel, y", 4 - encarcel, "ficha(s) libres."
    else: 
        return 3 ,  "No tienes fichas en la carcel! Todas tus fichas estan libres."
     
def modo_desarrollador(): 
    
    seguros = [11, 16, 28, 33, 45, 50, 62, 67]
    
    ListaJugadores = [
                    {"Nombre" : 'J1', 'Color' :'🔴', 'Piezas': {'1🔴': [0,True,1,0], '2🔴': [0,True,1,0], '3🔴': [0,True,1,0], '4🔴': [0,True,1,0]},"Salida" : 55,},
                    {"Nombre" : 'J2', 'Color': '🟠', 'Piezas': {'1🟠': [0,True,1,0], '2🟠': [0,True,1,0], '3🟠': [0,True,1,0], '4🟠': [0,True,1,0]},"Salida" : 38},
                    {"Nombre" : 'J3', 'Color' :'🟡', 'Piezas': {'1🟡': [0,True,1,0], '2🟡': [0,True,1,0], '3🟡': [0,True,1,0], '4🟡': [0,True,1,0]},"Salida" : 4},
                    {"Nombre" : 'J4', 'Color': '🟢', 'Piezas': {'1🟢': [0,True,1,0], '2🟢': [0,True,1,0], '3🟢': [0,True,1,0], '4🟢': [0,True,1,0]},"Salida" : 21}]
    
    cbd1 = " "+ListaJugadores[0]["Color"]+" "
    cbd2 = " "+ListaJugadores[1]["Color"]+" "
    cbd3 = " "+ListaJugadores[2]["Color"]+" "
    cbd4 = " "+ListaJugadores[3]["Color"]+" "
    cbd1carcel = ["    ","    ","    ","    "]
    cbd2carcel = ["    ","    ","    ","    "]
    cbd3carcel = ["    ","    ","    ","    "]
    cbd4carcel = ["    ","    ","    ","    "]
        
    tablero = [
            ["--0-","--1-","--2-","--3-","--4-","--5-","--6-","--7-","--8-","--9-","-10-","-11-","-12-","-13-","-14-","-15-","-16-","-17-","-18-","-19-","-20-","-21-","-22-","-23-","-24-"],
            ["--1-",cbd1,cbd1,cbd1,cbd1,cbd1,cbd1,cbd1,cbd1,cbd1,cbd1,cbd1,cbd1,cbd1,cbd2,cbd2,cbd2,cbd2,cbd2,cbd2,cbd2,cbd2," "+cbd2],
            ["--2-",cbd1,"    ","    ","    ","    ","    ","    ","    ","    ","[  ]","[  ]","<  >","<  >","[  ]","[  ]","    ","    ","    ","    ","    ","    ","    ","    ",cbd2[1:]],
            ["--3-",cbd1,"    ","    ","    ","    ","    ","    ","    ","    ","[  ]","[  ]","|  |","|  |","[  ]","[  ]","    ","    ","    ","    ","    ","    ","    ","    ",cbd2[1:]],
            ["--4-",cbd1,"    ","    ","    ","    ","    ","    ","    ","    ","[  ]","[  ]","|  |","|  |","[  ]","[  ]","    ","    ","    ","    ","    ","    ","    ","    ",cbd2[1:]],
            ["--5-",cbd1,"    ","    ","    ","    ","    ","    ","    ","    ","[  ]","[  ]","|  |","|  |","[  ]","[  ]","    ","    ","    ","    ","    ","    ","    ","    ",cbd2[1:]],
            ["--6-",cbd1,"   |","    ","    ","|   ","    ","    ","    ","    ","(  )","(  )","|  |","|  |","<  >","<  >","    ","    ","    ","    ","   |","    ","    ","|   ",cbd2[1:]],
            ["--7-",cbd1,"   |","    ","    ","|   ","    ","    ","    ","    ","[  ]","[  ]","|  |","|  |","[  ]","[  ]","    ","    ","    ","    ","   |","    ","    ","|     ",cbd2[1:]],
            ["--8-",cbd1,"    ","‾‾‾‾","‾‾‾‾","    ","    ","    ","    ","    ","[  ]","[  ]","|  |","|  |","[  ]","[  ]","    ","    ","    ","    ","    ","‾‾‾‾","‾‾‾‾","    ",cbd2[1:]],
            ["--9-",cbd1,"    ","    ","    ","    ","    ","    ","    ","    ","[  ]","[  ]","|  |","|  |","[  ]","[  ]","    ","    ","    ","    ","    ","    ","    ","    ",cbd2[1:]],
            ["-10-",cbd1,"[  ]","[  ]","[  ]","[  ]","<  >","[  ]","[  ]","[  ]","|  /","    ","    ","    ","    ","\\  |","[  ]","[  ]","[  ]","(  )","[  ]","[  ]","[  ]","[  ]",cbd2[1:]],
            ["-11-",cbd1,"[  ]","[  ]","[  ]","[  ]","<  >","[  ]","[  ]","[  ]","| / ","    ","    ","    ","    "," \\ |","[  ]","[  ]","[  ]","(  )","[  ]","[  ]","[  ]","[  ]",cbd2[1:]],
            ["-12-",cbd3[:-1] ," <  >","|  |","|  |","|  |","|  |","|  |","|  |","|  |","    ","    ","    ","    ","    ","    ","|  |","|  |","|  |","|  |","|  |","|  |","|  |","<  >",cbd2[1:]],
            ["-13-",cbd3[:-1] ," <  >","|  |","|  |","|  |","|  |","|  |","|  |","|  |","    ","    ","    ","    ","    ","    ","|  |","|  |","|  |","|  |","|  |","|  |","|  |","<  >",cbd2[1:]],
            ["-14-",cbd3[:-1] ," [  ]","[  ]","[  ]","[  ]","(  )","[  ]","[  ]","[  ]","| \\ ","    ","    ","    ","    "," / |","[  ]","[  ]","[  ]","<  >","[  ]","[  ]","[  ]","[  ]",cbd4[1:]],
            ["-15-",cbd3[:-1] ," [  ]","[  ]","[  ]","[  ]","(  )","[  ]","[  ]","[  ]","|  \\","    ","    ","    ","    ","/  |","[  ]","[  ]","[  ]","<  >","[  ]","[  ]","[  ]","[  ]",cbd4[1:]],
            ["-16-",cbd3[:-1],"    ","    ","    ","    ","    ","    ","    ","    ","[  ]","[  ]","|  |","|  |","[  ]","[  ]","    ","    ","    ","    ","    ","    ","    ","    ",cbd4[1:]],
            ["-17-",cbd3[:-1],"    ","    ","    ","    ","    ","    ","    ","    ","[  ]","[  ]","|  |","|  |","[  ]","[  ]","    ","    ","    ","    ","    ","    ","    ","    ",cbd4[1:]],
            ["-18-",cbd3[:-1],"   |","    ","    ","|   ","    ","    ","    ","      ","[  ]","[  ]","|  |","|  |","[  ]","[  ]","    ","    ","    ","    ","   |","    ","    ","|     ",cbd4[1:]],
            ["-19-",cbd3[:-1],"   |","    ","    ","|   ","    ","    ","    ","      ","<  >","<  >","|  |","|  |","(  )","(  )","    ","    ","    ","    ","   |","    ","    ","|     ",cbd4[1:]],
            ["-20-",cbd3[:-1],"    ","‾‾‾‾","‾‾‾‾","    ","    ","    ","    ","    ","[  ]","[  ]","|  |","|  |","[  ]","[  ]","    ","    ","    ","    ","    ","‾‾‾‾","‾‾‾‾","    ",cbd4[1:]],
            ["-21-",cbd3[:-1],"    ","    ","    ","    ","    ","    ","    ","    ","[  ]","[  ]","|  |","|  |","[  ]","[  ]","    ","    ","    ","    ","    ","    ","    ","    ",cbd4[1:]],
            ["-22-",cbd3[:-1],"    ","    ","    ","    ","    ","    ","    ","    ","[  ]","[  ]","|  |","|  |","[  ]","[  ]","    ","    ","    ","    ","    ","    ","    ","    ",cbd4[1:]],
            ["-23-",cbd3[:-1],"    ","    ","    ","    ","    ","    ","    ","    ","[  ]","[  ]","<  >","<  >","[  ]","[  ]","    ","    ","    ","    ","    ","    ","    ","    ",cbd4[1:]],
            ["-24-",cbd3,cbd3,cbd3,cbd3,cbd3,cbd3,cbd3,cbd3,cbd3,cbd4,cbd4,cbd4,cbd4,cbd4,cbd4,cbd4,cbd4,cbd4,cbd4,cbd4]]
    
    tableroreferencia = [
            ["--0-","--1-","--2-","--3-","--4-","--5-","--6-","--7-","--8-","--9-","-10-","-11-","-12-","-13-","-14-","-15-","-16-","-17-","-18-","-19-","-20-","-21-","-22-","-23-","-24-"],
            ["--1-",cbd1,cbd1,cbd1,cbd1,cbd1,cbd1,cbd1,cbd1,cbd1,cbd1,cbd1,cbd1,cbd1,cbd2,cbd2,cbd2,cbd2,cbd2,cbd2,cbd2,cbd2," "+cbd2],
            ["--2-",cbd1,"    ","    ","    ","    ","    ","    ","    ","    ","[  ]","[  ]","<  >","<  >","[  ]","[  ]","    ","    ","    ","    ","    ","    ","    ","    ",cbd2[1:]],
            ["--3-",cbd1,"    ","    ","    ","    ","    ","    ","    ","    ","[  ]","[  ]","|  |","|  |","[  ]","[  ]","    ","    ","    ","    ","    ","    ","    ","    ",cbd2[1:]],
            ["--4-",cbd1,"    ","    ","    ","    ","    ","    ","    ","    ","[  ]","[  ]","|  |","|  |","[  ]","[  ]","    ","    ","    ","    ","    ","    ","    ","    ",cbd2[1:]],
            ["--5-",cbd1,"    ","    ","    ","    ","    ","    ","    ","    ","[  ]","[  ]","|  |","|  |","[  ]","[  ]","    ","    ","    ","    ","    ","    ","    ","    ",cbd2[1:]],
            ["--6-",cbd1,"   |","    ","    ","|   ","    ","    ","    ","    ","(  )","(  )","|  |","|  |","<  >","<  >","    ","    ","    ","    ","   |","    ","    ","|      ",cbd2[1:]],
            ["--7-",cbd1,"   |","    ","    ","|   ","    ","    ","    ","    ","[  ]","[  ]","|  |","|  |","[  ]","[  ]","    ","    ","    ","    ","   |","    ","    ","|      ",cbd2[1:]],
            ["--8-",cbd1,"    ","‾‾‾‾","‾‾‾‾","    ","    ","    ","    ","    ","[  ]","[  ]","|  |","|  |","[  ]","[  ]","    ","    ","    ","    ","    ","‾‾‾‾","‾‾‾‾","    ",cbd2[1:]],
            ["--9-",cbd1,"    ","    ","    ","    ","    ","    ","    ","    ","[  ]","[  ]","|  |","|  |","[  ]","[  ]","    ","    ","    ","    ","    ","    ","    ","    ",cbd2[1:]],
            ["-10-",cbd1,"[  ]","[  ]","[  ]","[  ]","<  >","[  ]","[  ]","[  ]","|  /","    ","    ","    ","    ","\\  |","[  ]","[  ]","[  ]","(  )","[  ]","[  ]","[  ]","[  ]",cbd2[1:]],
            ["-11-",cbd1,"[  ]","[  ]","[  ]","[  ]","<  >","[  ]","[  ]","[  ]","| / ","    ","    ","    ","    "," \\ |","[  ]","[  ]","[  ]","(  )","[  ]","[  ]","[  ]","[  ]",cbd2[1:]],
            ["-12-",cbd3[:-1],"<  >","|  |","|  |","|  |","|  |","|  |","|  |","|  |","    ","    ","    ","    ","    ","    ","|  |","|  |","|  |","|  |","|  |","|  |","|  |","<  >",cbd2[1:]],
            ["-13-",cbd3[:-1],"<  >","|  |","|  |","|  |","|  |","|  |","|  |","|  |","    ","    ","    ","    ","    ","    ","|  |","|  |","|  |","|  |","|  |","|  |","|  |","<  >",cbd2[1:]],
            ["-14-",cbd3[:-1],"[  ]","[  ]","[  ]","[  ]","(  )","[  ]","[  ]","[  ]","| \\ ","    ","    ","    ","    "," / |","[  ]","[  ]","[  ]","<  >","[  ]","[  ]","[  ]","[  ]",cbd4[1:]],
            ["-15-",cbd3[:-1],"[  ]","[  ]","[  ]","[  ]","(  )","[  ]","[  ]","[  ]","|  \\","    ","    ","    ","    ","/  |","[  ]","[  ]","[  ]","<  >","[  ]","[  ]","[  ]","[  ]",cbd4[1:]],
            ["-16-",cbd3[:-1],"    ","    ","    ","    ","    ","    ","    ","    ","[  ]","[  ]","|  |","|  |","[  ]","[  ]","    ","    ","    ","    ","    ","    ","    ","    ",cbd4[1:]],
            ["-17-",cbd3[:-1],"    ","    ","    ","    ","    ","    ","    ","    ","[  ]","[  ]","|  |","|  |","[  ]","[  ]","    ","    ","    ","    ","    ","    ","    ","    ",cbd4[1:]],
            ["-18-",cbd3[:-1],"   |","    ","    ","|   ","    ","    ","    ","     ","[  ]","[  ]","|  |","|  |","[  ]","[  ]","    ","    ","    ","    ","   |","    ","    ","|      ",cbd4[1:]],
            ["-19-",cbd3[:-1],"   |","    ","    ","|   ","    ","    ","    ","     ","<  >","<  >","|  |","|  |","(  )","(  )","    ","    ","    ","    ","   |","    ","    ","|      ",cbd4[1:]],
            ["-20-",cbd3[:-1],"    ","‾‾‾‾","‾‾‾‾","    ","    ","    ","    ","    ","[  ]","[  ]","|  |","|  |","[  ]","[  ]","    ","    ","    ","    ","    ","‾‾‾‾","‾‾‾‾","    ",cbd4[1:]],
            ["-21-",cbd3[:-1],"    ","    ","    ","    ","    ","    ","    ","    ","[  ]","[  ]","|  |","|  |","[  ]","[  ]","    ","    ","    ","    ","    ","    ","    ","    ",cbd4[1:]],
            ["-22-",cbd3[:-1],"    ","    ","    ","    ","    ","    ","    ","    ","[  ]","[  ]","|  |","|  |","[  ]","[  ]","    ","    ","    ","    ","    ","    ","    ","    ",cbd4[1:]],
            ["-23-",cbd3[:-1],"    ","    ","    ","    ","    ","    ","    ","    ","[  ]","[  ]","<  >","<  >","[  ]","[  ]","    ","    ","    ","    ","    ","    ","    ","    ",cbd4[1:]],
            ["-24-",cbd3,cbd3,cbd3,cbd3,cbd3,cbd3,cbd3,cbd3,cbd3,cbd4,cbd4,cbd4,cbd4,cbd4,cbd4,cbd4,cbd4,cbd4,cbd4,cbd4]]

    coords1 = [(14,2),(14,3),(14,4),(14,5),(14,6),(14,7),(14,8),(14,9),(16,10),(17,10),(18,10),(19,10),(20,10),(21,10),(22,10),(23,10),(23,12),
               (23,14),(22,14),(21,14),(20,14),(19,14),(18,14),(17,14),(16,14),(15,16),(15,17),(15,18),(15,19),(15,20),(15,21),(15,22),(15,23),(13,23),
               (11,23),(11,22),(11,21),(11,20),(11,19),(11,18),(11,17),(11,16),(9,15),(8,15),(7,15),(6,15),(5,15),(4,15),(3,15),(2,15),(2,13),(2,11),
               (3,11),(4,11),(5,11),(6,11),(7,11),(8,11),(9,11),(10,9),(10,8),(10,7),(10,6),(10,5),(10,4),(10,3),(10,2),(12,2)]
    
    coords2 = [(15,2),(15,3),(15,4),(15,5),(15,6),(15,7),(15,8),(15,9),(16,11),(17,11),(18,11),(19,11),(20,11),(21,11),(22,11),(23,11),(23,13),
               (23,15),(22,15),(21,15),(20,15),(19,15),(18,15),(17,15),(16,15),(14,16),(14,17),(14,18),(14,19),(14,20),(14,21),(14,22),(14,23),(12,23),
               (10,23),(10,22),(10,21),(10,20),(10,19),(10,18),(10,17),(10,16),(9,14),(8,14),(7,14),(6,14),(5,14),(4,14),(3,14),(2,14),(2,12),(2,10),
               (3,10),(4,10),(5,10),(6,10),(7,10),(8,10),(9,10),(11,9),(11,8),(11,7),(11,6),(11,5),(11,4),(11,3),(11,2),(13,2)]
    
    
    running = True    
    while running == True:
        """"
        Aqui se encuentra el codigo para revisar que las piezas esten en carcel, en caso de estarlo, son ubicadas en la casilla apropiada.
        """        
        for jugador in ListaJugadores:
            listacarcel = []           
            if cbd1 == " " + jugador["Color"] + " ":
                for ficha in jugador["Piezas"]:
                    if jugador["Piezas"][ficha][1] == True:
                        listacarcel.append(" "+ficha)
                    else:
                        listacarcel.append("    ")
                        
                cbd1carcel = listacarcel
                
            elif cbd2 == " " + jugador["Color"] + " ":
                for ficha in jugador["Piezas"]:
                    if jugador["Piezas"][ficha][1] == True:
                        listacarcel.append(ficha)
                    else:
                        listacarcel.append("    ")
                        
                cbd2carcel = listacarcel
                
            elif cbd3 == " " + jugador["Color"] + " ":
                for ficha in jugador["Piezas"]:
                    if jugador["Piezas"][ficha][1] == True:
                        listacarcel.append(ficha)
                    else:
                        listacarcel.append("    ")
                        
                cbd3carcel = listacarcel

            elif cbd4 == " " + jugador["Color"] + " ":
                for ficha in jugador["Piezas"]:
                    if jugador["Piezas"][ficha][1] == True:
                        listacarcel.append(ficha)
                    else:
                        listacarcel.append("    ")
                        
                cbd4carcel = listacarcel
                                                
                
            if listacarcel != []:
                print ("Fichas de",jugador["Nombre"],"en carcel:",listacarcel)
            else:
                print("El jugador",jugador["Nombre"],"no tiene fichas en carcel.")
                
        """"
        Aqui se encuentra el check encargado de reemplazar las carceles en el board con la info de cada carcel.
        """          
            
        tablero[6][3] = cbd1carcel[0]
        tablero[6][4] = cbd1carcel[1]
        tablero[7][3] = cbd1carcel[2]
        tablero[7][4] = cbd1carcel[3]
        
        tablero[6][21] = cbd2carcel[0]
        tablero[6][22] = cbd2carcel[1]
        tablero[7][21] = cbd2carcel[2]
        tablero[7][22] = cbd2carcel[3]
                
        tablero[18][3] = cbd3carcel[0]
        tablero[18][4] = cbd3carcel[1]
        tablero[19][3] = cbd3carcel[2]
        tablero[19][4] = cbd3carcel[3]
        
        tablero[18][21] = cbd4carcel[0]
        tablero[18][22] = cbd4carcel[1]
        tablero[19][21] = cbd4carcel[2]
        tablero[19][22] = cbd4carcel[3]
                        
        
        """"
        Abajo, se encuentra el codigo para mover piezas
        """                    
        for linea in tablero:
            print(*linea)
        print ("Porfavor, seleccione un color para este turno.")
        for jugador in ListaJugadores:
            print (ListaJugadores.index(jugador),"-->",jugador["Color"])
        jugador = int(input())        
        jugador = ListaJugadores[jugador]
        print("Has seleccionado a: ",jugador['Nombre'],"Con las fichas: ",jugador['Piezas'])        
        print ("Porfavor, seleccione la ficha a mover")
        fichanum = 1
        for ficha in jugador["Piezas"]:
            print (fichanum, "-->" ,ficha)
            fichanum += 1
        ficha = input()+jugador["Color"]
        print("Has seleccionado la ficha:",ficha)
        jugador["Piezas"][ficha][3] = jugador["Piezas"][ficha][0] 
        PasaTurno = False
        
        if jugador["Piezas"][ficha][1] == True: 
            print("Esta ficha se encuentra en la carcel. Sacando automáticamente.")
            jugador["Piezas"][ficha][0] = jugador["Salida"]
            pos = jugador["Piezas"][ficha][0] 
                         
            if tablero[coords1[pos][0]][coords1[pos][1]] != tableroreferencia[coords1[pos][0]][coords1[pos][1]]:
                print("Ya hay una ficha en salida! Revisando segundo carril")
                if tablero[coords2[pos][0]][coords2[pos][1]] != tableroreferencia[coords2[pos][0]][coords2[pos][1]]:
                    print("Hay dos fichas en salida! Pasa turno.")      
                    PasaTurno = True
                else:
                    jugador["Piezas"][ficha][1] = False                
                    jugador["Piezas"][ficha][2] = 2
                    tablero[coords2[pos][0]][coords2[pos][1]] = ficha
                
                              
            else:
                jugador["Piezas"][ficha][1] = False                
                tablero[coords1[pos][0]][coords1[pos][1]] = ficha

        else: 
            print("Esta ficha esta en juego. Cuanto deseas mover esta ficha?")  
            distancia = int(input())            
            jugador["Piezas"][ficha][0] += distancia 
            jugador["Piezas"][ficha][0] %= len(coords1) 
            pos = jugador["Piezas"][ficha][0] #Establece la posicion actual de la ficha 
            
            
            """"
            Checks para colision de piezas, incluyendo check para fichas enemigas
            """
            
            if pos >= len(coords1):
                pos = (jugador["Piezas"][ficha][3] + pos) % 68
                jugador["Piezas"][ficha][0] = (jugador["Piezas"][ficha][0]) % len(coords1)
            
            if jugador["Piezas"][ficha][2] == 1: #Verifica fichas ubicadas en el grid 1
                if tablero[coords1[pos][0]][coords1[pos][1]] == tableroreferencia[coords1[pos][0]][coords1[pos][1]]: #Verifica si la casilla en el grid1 esta libre
                    
                    jugador["Piezas"][ficha][0] = pos
                    jugador["Piezas"][ficha][2] = 1                                  
                elif tablero[coords2[pos][0]][coords2[pos][1]] == tableroreferencia[coords2[pos][0]][coords2[pos][1]]:#Verifica si la casilla en el grid2 esta libre
                    
                    jugador["Piezas"][ficha][0] = pos                    
                    jugador["Piezas"][ficha][2] = 2    #Cambia el indice de la ficha a 2, puesto que ahora se encuentra en el grid2
                else: #Else para correr las instrucciones si ninguna casilla esta disponible.
                    ("Parece que hay un bloqueo! Tu ficha sera puesta una casilla atras.")
                    pos = pos-1
                    if tablero[coords1[pos][0]][coords1[pos][1]] == tableroreferencia[coords1[pos][0]][coords1[pos][1]]: #Verifica si la casilla en el grid1 esta libre
                        jugador["Piezas"][ficha][0] = pos
                        jugador["Piezas"][ficha][2] = 1    #Cambia el indice de la ficha a 2, puesto que ahora se encuentra en el grid2
                    elif tablero[coords2[pos][0]][coords2[pos][1]] == tableroreferencia[coords2[pos][0]][coords2[pos][1]]:#Verifica si la casilla en el grid2 esta libre                        
                        jugador["Piezas"][ficha][2] = 2    #Cambia el indice de la ficha a 2, puesto que ahora se encuentra en el grid2
                        jugador["Piezas"][ficha][0] = pos
                    
            elif jugador["Piezas"][ficha][2] == 2: #Verifica fichas ubicadas en el grid 2
                if tablero[coords2[pos][0]][coords2[pos][1]] == tableroreferencia[coords2[pos][0]][coords2[pos][1]]: #Verifica si la casilla en el grid1 esta libre
                    jugador["Piezas"][ficha][2] = 2    #Cambia el indice de la ficha a 1, puesto que ahora se encuentra en el grid1             
                elif tablero[coords1[pos][0]][coords1[pos][1]] == tableroreferencia[coords1[pos][0]][coords1[pos][1]]:#Verifica si la casilla en el grid2 esta libre                    
                    jugador["Piezas"][ficha][2] = 1    #Cambia el indice de la ficha a 1, puesto que ahora se encuentra en el grid1
                else: #Else para correr las instrucciones si ninguna casilla esta disponible.
                    if tablero[coords2[pos][0]][coords2[pos][1]] == tableroreferencia[coords2[pos][0]][coords2[pos][1]]: #Verifica si la casilla en el grid1 esta libre                        
                        jugador["Piezas"][ficha][0] = pos
                        jugador["Piezas"][ficha][2] = 2    #Cambia el indice de la ficha a 1, puesto que ahora se encuentra en el grid1                    
                    elif tablero[coords1[pos][0]][coords1[pos][1]] == tableroreferencia[coords1[pos][0]][coords1[pos][1]]:#Verifica si la casilla en el grid2 esta libre                        
                        jugador["Piezas"][ficha][0] = pos
                        jugador["Piezas"][ficha][2] = 1    #Cambia el indice de la ficha a 1, puesto que ahora se encuentra en el grid1        
                        
            
            for jugador2 in ListaJugadores: #Check para colisiones.
                contadorfichas = 0
                for ficha2 in jugador2["Piezas"]:
                    if jugador["Color"] != jugador2["Color"]:                        
                        if jugador["Piezas"][ficha][0] >= jugador2["Piezas"][ficha2][0] > jugador["Piezas"][ficha][3]:
                            contadorfichas +=1                            
                        if contadorfichas > 1:
                            if jugador2["Piezas"][ficha2][1] == False:
                                print ("Colision detectada! De las fichas",ficha,ficha2)
                                jugador["Piezas"][ficha][0] = jugador2["Piezas"][ficha2][0]-1
                            
                        elif contadorfichas == 1:
                            if ficha2[1] == jugador2["Color"]:                                
                                if jugador2["Piezas"][ficha2][0] not in seguros:                                
                                    print(ficha,"comiendo a",ficha2)
                                    jugador2["Piezas"][ficha2][1] = True
                                    jugador["Piezas"][ficha][0] = jugador2["Piezas"][ficha2][0]
                                
     
                    else:
                        if ficha != ficha2 and jugador["Piezas"][ficha][2] ==jugador2["Piezas"][ficha2][2]:                            
                            if jugador["Piezas"][ficha][0] >= jugador2["Piezas"][ficha2][0] > jugador["Piezas"][ficha][3]:
                                print ("Colision detectada! De las fichas",ficha,ficha2)
                                jugador["Piezas"][ficha][0] = jugador["Piezas"][ficha][0] - (jugador["Piezas"][ficha][0]-jugador2["Piezas"][ficha2][0])-1
                            else:
                                if jugador["Piezas"][ficha][0] < jugador["Piezas"][ficha][3]:
                                    if jugador["Piezas"][ficha][3] + distancia >= jugador2["Piezas"][ficha2][0] > jugador["Piezas"][ficha][3]:
                                        jugador["Piezas"][ficha][0] = jugador2["Piezas"][ficha2][0] - 1                           
                                        pass
                                
            
            

        for jugador in reversed(ListaJugadores): #Loop para mostrar las fichas en el tablero          
            for ficha in jugador["Piezas"]:                
                if jugador["Piezas"][ficha][1] == False:
                    oldpos = jugador["Piezas"][ficha][3]
                    pos = jugador["Piezas"][ficha][0] 
                    if pos != oldpos:
                        if pos >= len(coords1):                            
                            pos = (jugador["Piezas"][ficha][3] + pos) % 68
                        if oldpos > len(coords1):                            
                            pos = (jugador["Piezas"][ficha][3] + pos) % 68
                        if jugador["Piezas"][ficha][2] == 2:
                            tablero[coords2[pos][0]][coords2[pos][1]] = ficha
                            tablero[coords2[oldpos][0]][coords2[oldpos][1]] = tableroreferencia[coords2[oldpos][0]][coords2[oldpos][1]]
                            if tablero[coords1[oldpos][0]][coords1[oldpos][1]] == ficha:
                                tablero[coords1[oldpos][0]][coords1[oldpos][1]] = tableroreferencia[coords1[oldpos][0]][coords1[oldpos][1]]
                        elif jugador["Piezas"][ficha][2] == 1:
                            tablero[coords1[pos][0]][coords1[pos][1]] = ficha
                            tablero[coords1[oldpos][0]][coords1[oldpos][1]] = tableroreferencia[coords1[oldpos][0]][coords1[oldpos][1]]
                            if tablero[coords2[oldpos][0]][coords2[oldpos][1]] == ficha:
                                tablero[coords2[oldpos][0]][coords2[oldpos][1]] = tableroreferencia[coords2[oldpos][0]][coords2[oldpos][1]]
                    else:   
                        if pos >= len(coords1):                            
                            pos = (jugador["Piezas"][ficha][3] + pos) % 68
                        if oldpos > len(coords1):                            
                            pos = (jugador["Piezas"][ficha][3] + pos) % 68
                        if jugador["Piezas"][ficha][2] == 2:
                            tablero[coords2[pos][0]][coords2[pos][1]] = ficha
                            tablero[coords1[pos][0]][coords1[pos][1]] = tableroreferencia[coords1[oldpos][0]][coords1[oldpos][1]]
                        elif jugador["Piezas"][ficha][2] == 1:
                            tablero[coords1[pos][0]][coords1[pos][1]] = ficha
                            tablero[coords2[pos][0]][coords1[pos][1]] = tableroreferencia[coords2[oldpos][0]][coords2[oldpos][1]]
  
        
        
        
def modo_normal(): 
    
    seguros = [11, 16, 28, 33, 45, 50, 62, 67]
    
    ListaJugadores = [
                    {"Nombre" : 'J1', 'Color' :'🔴', 'Piezas': {'1🔴': [0,True,1,0], '2🔴': [0,True,1,0], '3🔴': [0,True,1,0], '4🔴': [0,True,1,0]},"Salida" : 55,},
                    {"Nombre" : 'J2', 'Color': '🟠', 'Piezas': {'1🟠': [0,True,1,0], '2🟠': [0,True,1,0], '3🟠': [0,True,1,0], '4🟠': [0,True,1,0]},"Salida" : 38},
                    {"Nombre" : 'J3', 'Color' :'🟡', 'Piezas': {'1🟡': [0,True,1,0], '2🟡': [0,True,1,0], '3🟡': [0,True,1,0], '4🟡': [0,True,1,0]},"Salida" : 4},
                    {"Nombre" : 'J4', 'Color': '🟢', 'Piezas': {'1🟢': [0,True,1,0], '2🟢': [0,True,1,0], '3🟢': [0,True,1,0], '4🟢': [0,True,1,0]},"Salida" : 21}]
    
    cbd1 = " "+ListaJugadores[0]["Color"]+" "
    cbd2 = " "+ListaJugadores[1]["Color"]+" "
    cbd3 = " "+ListaJugadores[2]["Color"]+" "
    cbd4 = " "+ListaJugadores[3]["Color"]+" "
    cbd1carcel = ["    ","    ","    ","    "]
    cbd2carcel = ["    ","    ","    ","    "]
    cbd3carcel = ["    ","    ","    ","    "]
    cbd4carcel = ["    ","    ","    ","    "]
        
    tablero = [
            ["--0-","--1-","--2-","--3-","--4-","--5-","--6-","--7-","--8-","--9-","-10-","-11-","-12-","-13-","-14-","-15-","-16-","-17-","-18-","-19-","-20-","-21-","-22-","-23-","-24-"],
            ["--1-",cbd1,cbd1,cbd1,cbd1,cbd1,cbd1,cbd1,cbd1,cbd1,cbd1,cbd1,cbd1,cbd1,cbd2,cbd2,cbd2,cbd2,cbd2,cbd2,cbd2,cbd2," "+cbd2],
            ["--2-",cbd1,"    ","    ","    ","    ","    ","    ","    ","    ","[  ]","[  ]","<  >","<  >","[  ]","[  ]","    ","    ","    ","    ","    ","    ","    ","    ",cbd2[1:]],
            ["--3-",cbd1,"    ","    ","    ","    ","    ","    ","    ","    ","[  ]","[  ]","|  |","|  |","[  ]","[  ]","    ","    ","    ","    ","    ","    ","    ","    ",cbd2[1:]],
            ["--4-",cbd1,"    ","    ","    ","    ","    ","    ","    ","    ","[  ]","[  ]","|  |","|  |","[  ]","[  ]","    ","    ","    ","    ","    ","    ","    ","    ",cbd2[1:]],
            ["--5-",cbd1,"    ","    ","    ","    ","    ","    ","    ","    ","[  ]","[  ]","|  |","|  |","[  ]","[  ]","    ","    ","    ","    ","    ","    ","    ","    ",cbd2[1:]],
            ["--6-",cbd1,"   |","    ","    ","|   ","    ","    ","    ","    ","(  )","(  )","|  |","|  |","<  >","<  >","    ","    ","    ","    ","   |","    ","    ","|   ",cbd2[1:]],
            ["--7-",cbd1,"   |","    ","    ","|   ","    ","    ","    ","    ","[  ]","[  ]","|  |","|  |","[  ]","[  ]","    ","    ","    ","    ","   |","    ","    ","|     ",cbd2[1:]],
            ["--8-",cbd1,"    ","‾‾‾‾","‾‾‾‾","    ","    ","    ","    ","    ","[  ]","[  ]","|  |","|  |","[  ]","[  ]","    ","    ","    ","    ","    ","‾‾‾‾","‾‾‾‾","    ",cbd2[1:]],
            ["--9-",cbd1,"    ","    ","    ","    ","    ","    ","    ","    ","[  ]","[  ]","|  |","|  |","[  ]","[  ]","    ","    ","    ","    ","    ","    ","    ","    ",cbd2[1:]],
            ["-10-",cbd1,"[  ]","[  ]","[  ]","[  ]","<  >","[  ]","[  ]","[  ]","|  /","    ","    ","    ","    ","\\  |","[  ]","[  ]","[  ]","(  )","[  ]","[  ]","[  ]","[  ]",cbd2[1:]],
            ["-11-",cbd1,"[  ]","[  ]","[  ]","[  ]","<  >","[  ]","[  ]","[  ]","| / ","    ","    ","    ","    "," \\ |","[  ]","[  ]","[  ]","(  )","[  ]","[  ]","[  ]","[  ]",cbd2[1:]],
            ["-12-",cbd3[:-1] ," <  >","|  |","|  |","|  |","|  |","|  |","|  |","|  |","    ","    ","    ","    ","    ","    ","|  |","|  |","|  |","|  |","|  |","|  |","|  |","<  >",cbd2[1:]],
            ["-13-",cbd3[:-1] ," <  >","|  |","|  |","|  |","|  |","|  |","|  |","|  |","    ","    ","    ","    ","    ","    ","|  |","|  |","|  |","|  |","|  |","|  |","|  |","<  >",cbd2[1:]],
            ["-14-",cbd3[:-1] ," [  ]","[  ]","[  ]","[  ]","(  )","[  ]","[  ]","[  ]","| \\ ","    ","    ","    ","    "," / |","[  ]","[  ]","[  ]","<  >","[  ]","[  ]","[  ]","[  ]",cbd4[1:]],
            ["-15-",cbd3[:-1] ," [  ]","[  ]","[  ]","[  ]","(  )","[  ]","[  ]","[  ]","|  \\","    ","    ","    ","    ","/  |","[  ]","[  ]","[  ]","<  >","[  ]","[  ]","[  ]","[  ]",cbd4[1:]],
            ["-16-",cbd3[:-1],"    ","    ","    ","    ","    ","    ","    ","    ","[  ]","[  ]","|  |","|  |","[  ]","[  ]","    ","    ","    ","    ","    ","    ","    ","    ",cbd4[1:]],
            ["-17-",cbd3[:-1],"    ","    ","    ","    ","    ","    ","    ","    ","[  ]","[  ]","|  |","|  |","[  ]","[  ]","    ","    ","    ","    ","    ","    ","    ","    ",cbd4[1:]],
            ["-18-",cbd3[:-1],"   |","    ","    ","|   ","    ","    ","    ","      ","[  ]","[  ]","|  |","|  |","[  ]","[  ]","    ","    ","    ","    ","   |","    ","    ","|     ",cbd4[1:]],
            ["-19-",cbd3[:-1],"   |","    ","    ","|   ","    ","    ","    ","      ","<  >","<  >","|  |","|  |","(  )","(  )","    ","    ","    ","    ","   |","    ","    ","|     ",cbd4[1:]],
            ["-20-",cbd3[:-1],"    ","‾‾‾‾","‾‾‾‾","    ","    ","    ","    ","    ","[  ]","[  ]","|  |","|  |","[  ]","[  ]","    ","    ","    ","    ","    ","‾‾‾‾","‾‾‾‾","    ",cbd4[1:]],
            ["-21-",cbd3[:-1],"    ","    ","    ","    ","    ","    ","    ","    ","[  ]","[  ]","|  |","|  |","[  ]","[  ]","    ","    ","    ","    ","    ","    ","    ","    ",cbd4[1:]],
            ["-22-",cbd3[:-1],"    ","    ","    ","    ","    ","    ","    ","    ","[  ]","[  ]","|  |","|  |","[  ]","[  ]","    ","    ","    ","    ","    ","    ","    ","    ",cbd4[1:]],
            ["-23-",cbd3[:-1],"    ","    ","    ","    ","    ","    ","    ","    ","[  ]","[  ]","<  >","<  >","[  ]","[  ]","    ","    ","    ","    ","    ","    ","    ","    ",cbd4[1:]],
            ["-24-",cbd3,cbd3,cbd3,cbd3,cbd3,cbd3,cbd3,cbd3,cbd3,cbd4,cbd4,cbd4,cbd4,cbd4,cbd4,cbd4,cbd4,cbd4,cbd4,cbd4]]
    
    tableroreferencia = [
            ["--0-","--1-","--2-","--3-","--4-","--5-","--6-","--7-","--8-","--9-","-10-","-11-","-12-","-13-","-14-","-15-","-16-","-17-","-18-","-19-","-20-","-21-","-22-","-23-","-24-"],
            ["--1-",cbd1,cbd1,cbd1,cbd1,cbd1,cbd1,cbd1,cbd1,cbd1,cbd1,cbd1,cbd1,cbd1,cbd2,cbd2,cbd2,cbd2,cbd2,cbd2,cbd2,cbd2," "+cbd2],
            ["--2-",cbd1,"    ","    ","    ","    ","    ","    ","    ","    ","[  ]","[  ]","<  >","<  >","[  ]","[  ]","    ","    ","    ","    ","    ","    ","    ","    ",cbd2[1:]],
            ["--3-",cbd1,"    ","    ","    ","    ","    ","    ","    ","    ","[  ]","[  ]","|  |","|  |","[  ]","[  ]","    ","    ","    ","    ","    ","    ","    ","    ",cbd2[1:]],
            ["--4-",cbd1,"    ","    ","    ","    ","    ","    ","    ","    ","[  ]","[  ]","|  |","|  |","[  ]","[  ]","    ","    ","    ","    ","    ","    ","    ","    ",cbd2[1:]],
            ["--5-",cbd1,"    ","    ","    ","    ","    ","    ","    ","    ","[  ]","[  ]","|  |","|  |","[  ]","[  ]","    ","    ","    ","    ","    ","    ","    ","    ",cbd2[1:]],
            ["--6-",cbd1,"   |","    ","    ","|   ","    ","    ","    ","    ","(  )","(  )","|  |","|  |","<  >","<  >","    ","    ","    ","    ","   |","    ","    ","|      ",cbd2[1:]],
            ["--7-",cbd1,"   |","    ","    ","|   ","    ","    ","    ","    ","[  ]","[  ]","|  |","|  |","[  ]","[  ]","    ","    ","    ","    ","   |","    ","    ","|      ",cbd2[1:]],
            ["--8-",cbd1,"    ","‾‾‾‾","‾‾‾‾","    ","    ","    ","    ","    ","[  ]","[  ]","|  |","|  |","[  ]","[  ]","    ","    ","    ","    ","    ","‾‾‾‾","‾‾‾‾","    ",cbd2[1:]],
            ["--9-",cbd1,"    ","    ","    ","    ","    ","    ","    ","    ","[  ]","[  ]","|  |","|  |","[  ]","[  ]","    ","    ","    ","    ","    ","    ","    ","    ",cbd2[1:]],
            ["-10-",cbd1,"[  ]","[  ]","[  ]","[  ]","<  >","[  ]","[  ]","[  ]","|  /","    ","    ","    ","    ","\\  |","[  ]","[  ]","[  ]","(  )","[  ]","[  ]","[  ]","[  ]",cbd2[1:]],
            ["-11-",cbd1,"[  ]","[  ]","[  ]","[  ]","<  >","[  ]","[  ]","[  ]","| / ","    ","    ","    ","    "," \\ |","[  ]","[  ]","[  ]","(  )","[  ]","[  ]","[  ]","[  ]",cbd2[1:]],
            ["-12-",cbd3[:-1],"<  >","|  |","|  |","|  |","|  |","|  |","|  |","|  |","    ","    ","    ","    ","    ","    ","|  |","|  |","|  |","|  |","|  |","|  |","|  |","<  >",cbd2[1:]],
            ["-13-",cbd3[:-1],"<  >","|  |","|  |","|  |","|  |","|  |","|  |","|  |","    ","    ","    ","    ","    ","    ","|  |","|  |","|  |","|  |","|  |","|  |","|  |","<  >",cbd2[1:]],
            ["-14-",cbd3[:-1],"[  ]","[  ]","[  ]","[  ]","(  )","[  ]","[  ]","[  ]","| \\ ","    ","    ","    ","    "," / |","[  ]","[  ]","[  ]","<  >","[  ]","[  ]","[  ]","[  ]",cbd4[1:]],
            ["-15-",cbd3[:-1],"[  ]","[  ]","[  ]","[  ]","(  )","[  ]","[  ]","[  ]","|  \\","    ","    ","    ","    ","/  |","[  ]","[  ]","[  ]","<  >","[  ]","[  ]","[  ]","[  ]",cbd4[1:]],
            ["-16-",cbd3[:-1],"    ","    ","    ","    ","    ","    ","    ","    ","[  ]","[  ]","|  |","|  |","[  ]","[  ]","    ","    ","    ","    ","    ","    ","    ","    ",cbd4[1:]],
            ["-17-",cbd3[:-1],"    ","    ","    ","    ","    ","    ","    ","    ","[  ]","[  ]","|  |","|  |","[  ]","[  ]","    ","    ","    ","    ","    ","    ","    ","    ",cbd4[1:]],
            ["-18-",cbd3[:-1],"   |","    ","    ","|   ","    ","    ","    ","     ","[  ]","[  ]","|  |","|  |","[  ]","[  ]","    ","    ","    ","    ","   |","    ","    ","|      ",cbd4[1:]],
            ["-19-",cbd3[:-1],"   |","    ","    ","|   ","    ","    ","    ","     ","<  >","<  >","|  |","|  |","(  )","(  )","    ","    ","    ","    ","   |","    ","    ","|      ",cbd4[1:]],
            ["-20-",cbd3[:-1],"    ","‾‾‾‾","‾‾‾‾","    ","    ","    ","    ","    ","[  ]","[  ]","|  |","|  |","[  ]","[  ]","    ","    ","    ","    ","    ","‾‾‾‾","‾‾‾‾","    ",cbd4[1:]],
            ["-21-",cbd3[:-1],"    ","    ","    ","    ","    ","    ","    ","    ","[  ]","[  ]","|  |","|  |","[  ]","[  ]","    ","    ","    ","    ","    ","    ","    ","    ",cbd4[1:]],
            ["-22-",cbd3[:-1],"    ","    ","    ","    ","    ","    ","    ","    ","[  ]","[  ]","|  |","|  |","[  ]","[  ]","    ","    ","    ","    ","    ","    ","    ","    ",cbd4[1:]],
            ["-23-",cbd3[:-1],"    ","    ","    ","    ","    ","    ","    ","    ","[  ]","[  ]","<  >","<  >","[  ]","[  ]","    ","    ","    ","    ","    ","    ","    ","    ",cbd4[1:]],
            ["-24-",cbd3,cbd3,cbd3,cbd3,cbd3,cbd3,cbd3,cbd3,cbd3,cbd4,cbd4,cbd4,cbd4,cbd4,cbd4,cbd4,cbd4,cbd4,cbd4,cbd4]]

    coords1 = [(14,2),(14,3),(14,4),(14,5),(14,6),(14,7),(14,8),(14,9),(16,10),(17,10),(18,10),(19,10),(20,10),(21,10),(22,10),(23,10),(23,12),
               (23,14),(22,14),(21,14),(20,14),(19,14),(18,14),(17,14),(16,14),(15,16),(15,17),(15,18),(15,19),(15,20),(15,21),(15,22),(15,23),(13,23),
               (11,23),(11,22),(11,21),(11,20),(11,19),(11,18),(11,17),(11,16),(9,15),(8,15),(7,15),(6,15),(5,15),(4,15),(3,15),(2,15),(2,13),(2,11),
               (3,11),(4,11),(5,11),(6,11),(7,11),(8,11),(9,11),(10,9),(10,8),(10,7),(10,6),(10,5),(10,4),(10,3),(10,2),(12,2)]
    
    coords2 = [(15,2),(15,3),(15,4),(15,5),(15,6),(15,7),(15,8),(15,9),(16,11),(17,11),(18,11),(19,11),(20,11),(21,11),(22,11),(23,11),(23,13),
               (23,15),(22,15),(21,15),(20,15),(19,15),(18,15),(17,15),(16,15),(14,16),(14,17),(14,18),(14,19),(14,20),(14,21),(14,22),(14,23),(12,23),
               (10,23),(10,22),(10,21),(10,20),(10,19),(10,18),(10,17),(10,16),(9,14),(8,14),(7,14),(6,14),(5,14),(4,14),(3,14),(2,14),(2,12),(2,10),
               (3,10),(4,10),(5,10),(6,10),(7,10),(8,10),(9,10),(11,9),(11,8),(11,7),(11,6),(11,5),(11,4),(11,3),(11,2),(13,2)]
    
    
    running = True    
    while running == True:
        """"
        Aqui se encuentra el codigo para revisar que las piezas esten en carcel, en caso de estarlo, son ubicadas en la casilla apropiada.
        """        
        for jugador in ListaJugadores:
            listacarcel = []           
            if cbd1 == " " + jugador["Color"] + " ":
                for ficha in jugador["Piezas"]:
                    if jugador["Piezas"][ficha][1] == True:
                        listacarcel.append(" "+ficha)
                    else:
                        listacarcel.append("    ")
                        
                cbd1carcel = listacarcel
                
            elif cbd2 == " " + jugador["Color"] + " ":
                for ficha in jugador["Piezas"]:
                    if jugador["Piezas"][ficha][1] == True:
                        listacarcel.append(ficha)
                    else:
                        listacarcel.append("    ")
                        
                cbd2carcel = listacarcel
                
            elif cbd3 == " " + jugador["Color"] + " ":
                for ficha in jugador["Piezas"]:
                    if jugador["Piezas"][ficha][1] == True:
                        listacarcel.append(ficha)
                    else:
                        listacarcel.append("    ")
                        
                cbd3carcel = listacarcel

            elif cbd4 == " " + jugador["Color"] + " ":
                for ficha in jugador["Piezas"]:
                    if jugador["Piezas"][ficha][1] == True:
                        listacarcel.append(ficha)
                    else:
                        listacarcel.append("    ")
                        
                cbd4carcel = listacarcel
                                                
                
            if listacarcel != []:
                print ("Fichas de",jugador["Nombre"],"en carcel:",listacarcel)
            else:
                print("El jugador",jugador["Nombre"],"no tiene fichas en carcel.")
                
        """"
        Aqui se encuentra el check encargado de reemplazar las carceles en el board con la info de cada carcel.
        """          
            
        tablero[6][3] = cbd1carcel[0]
        tablero[6][4] = cbd1carcel[1]
        tablero[7][3] = cbd1carcel[2]
        tablero[7][4] = cbd1carcel[3]
        
        tablero[6][21] = cbd2carcel[0]
        tablero[6][22] = cbd2carcel[1]
        tablero[7][21] = cbd2carcel[2]
        tablero[7][22] = cbd2carcel[3]
                
        tablero[18][3] = cbd3carcel[0]
        tablero[18][4] = cbd3carcel[1]
        tablero[19][3] = cbd3carcel[2]
        tablero[19][4] = cbd3carcel[3]
        
        tablero[18][21] = cbd4carcel[0]
        tablero[18][22] = cbd4carcel[1]
        tablero[19][21] = cbd4carcel[2]
        tablero[19][22] = cbd4carcel[3]
                        
        
        """Aqui esta el codigo para el movimiento y los dados"""

        while True:  # Bucle principal del juego
            for linea in tablero:
                print(*linea)

            # Alternar turnos entre los jugadores
            for jugador in ListaJugadores:
                print("Es el turno de: ", jugador['Nombre'], "Con las fichas: ", jugador['Piezas'])        

                # Lanzar dos dados
                dado1 = random.randint(1, 6)
                dado2 = random.randint(1, 6)
                distancia = dado1 + dado2  # La distancia a mover es la suma de los dos dados
                print(f"Has lanzado los dados: {dado1} y {dado2}. Moverás {distancia} espacios.")

                print("Por favor, seleccione la ficha a mover")
                fichanum = 1
                for ficha in jugador["Piezas"]:
                    print(fichanum, "-->", ficha)
                    fichanum += 1
                ficha = input() + jugador["Color"]
                print("Has seleccionado la ficha:", ficha)
                jugador["Piezas"][ficha][3] = jugador["Piezas"][ficha][0] 
                PasaTurno = False

                if jugador["Piezas"][ficha][1] == True: 
                    print("Esta ficha se encuentra en la cárcel. Sacando automáticamente.")
                    jugador["Piezas"][ficha][0] = jugador["Salida"]
                    pos = jugador["Piezas"][ficha][0] 
                                
                    if tablero[coords1[pos][0]][coords1[pos][1]] != tableroreferencia[coords1[pos][0]][coords1[pos][1]]:
                        print("Ya hay una ficha en salida! Revisando segundo carril")
                        if tablero[coords2[pos][0]][coords2[pos][1]] != tableroreferencia[coords2[pos][0]][coords2[pos][1]]:
                            print("Hay dos fichas en salida! Pasa turno.")      
                            PasaTurno = True
                        else:
                            jugador["Piezas"][ficha][1] = False                
                            jugador["Piezas"][ficha][2] = 2
                            tablero[coords2[pos][0]][coords2[pos][1]] = ficha
                    
                    else:
                        jugador["Piezas"][ficha][1] = False                
                        tablero[coords1[pos][0]][coords1[pos][1]] = ficha

                else: 
                    print("Esta ficha está en juego. Moverás esta ficha automáticamente.")
                    jugador["Piezas"][ficha][0] += distancia 
                    jugador["Piezas"][ficha][0] %= len(coords1) 
                    pos = jugador["Piezas"][ficha][0]  # Establece la posición actual de la ficha 


        """
        Checks para colision de piezas, incluyendo check para fichas enemigas
        """
        
        if pos >= len(coords1):  # <-- Este bloque debe estar alineado con el resto del código.
            pos = (jugador["Piezas"][ficha][3] + pos) % 68
            jugador["Piezas"][ficha][0] = (jugador["Piezas"][ficha][0]) % len(coords1)

            if jugador["Piezas"][ficha][2] == 1: #Verifica fichas ubicadas en el grid 1
                if tablero[coords1[pos][0]][coords1[pos][1]] == tableroreferencia[coords1[pos][0]][coords1[pos][1]]: #Verifica si la casilla en el grid1 esta libre
                    
                    jugador["Piezas"][ficha][0] = pos
                    jugador["Piezas"][ficha][2] = 1                                  
                elif tablero[coords2[pos][0]][coords2[pos][1]] == tableroreferencia[coords2[pos][0]][coords2[pos][1]]:#Verifica si la casilla en el grid2 esta libre
                    
                    jugador["Piezas"][ficha][0] = pos                    
                    jugador["Piezas"][ficha][2] = 2    #Cambia el indice de la ficha a 2, puesto que ahora se encuentra en el grid2
                else: #Else para correr las instrucciones si ninguna casilla esta disponible.
                    ("Parece que hay un bloqueo! Tu ficha sera puesta una casilla atras.")
                    pos = pos-1
                    if tablero[coords1[pos][0]][coords1[pos][1]] == tableroreferencia[coords1[pos][0]][coords1[pos][1]]: #Verifica si la casilla en el grid1 esta libre
                        jugador["Piezas"][ficha][0] = pos
                        jugador["Piezas"][ficha][2] = 1    #Cambia el indice de la ficha a 2, puesto que ahora se encuentra en el grid2
                    elif tablero[coords2[pos][0]][coords2[pos][1]] == tableroreferencia[coords2[pos][0]][coords2[pos][1]]:#Verifica si la casilla en el grid2 esta libre                        
                        jugador["Piezas"][ficha][2] = 2    #Cambia el indice de la ficha a 2, puesto que ahora se encuentra en el grid2
                        jugador["Piezas"][ficha][0] = pos
                    
            elif jugador["Piezas"][ficha][2] == 2: #Verifica fichas ubicadas en el grid 2
                if tablero[coords2[pos][0]][coords2[pos][1]] == tableroreferencia[coords2[pos][0]][coords2[pos][1]]: #Verifica si la casilla en el grid1 esta libre
                    jugador["Piezas"][ficha][2] = 2    #Cambia el indice de la ficha a 1, puesto que ahora se encuentra en el grid1             
                elif tablero[coords1[pos][0]][coords1[pos][1]] == tableroreferencia[coords1[pos][0]][coords1[pos][1]]:#Verifica si la casilla en el grid2 esta libre                    
                    jugador["Piezas"][ficha][2] = 1    #Cambia el indice de la ficha a 1, puesto que ahora se encuentra en el grid1
                else: #Else para correr las instrucciones si ninguna casilla esta disponible.
                    if tablero[coords2[pos][0]][coords2[pos][1]] == tableroreferencia[coords2[pos][0]][coords2[pos][1]]: #Verifica si la casilla en el grid1 esta libre                        
                        jugador["Piezas"][ficha][0] = pos
                        jugador["Piezas"][ficha][2] = 2    #Cambia el indice de la ficha a 1, puesto que ahora se encuentra en el grid1                    
                    elif tablero[coords1[pos][0]][coords1[pos][1]] == tableroreferencia[coords1[pos][0]][coords1[pos][1]]:#Verifica si la casilla en el grid2 esta libre                        
                        jugador["Piezas"][ficha][0] = pos
                        jugador["Piezas"][ficha][2] = 1    #Cambia el indice de la ficha a 1, puesto que ahora se encuentra en el grid1        
                        
            
            for jugador2 in ListaJugadores: #Check para colisiones.
                contadorfichas = 0
                for ficha2 in jugador2["Piezas"]:
                    if jugador["Color"] != jugador2["Color"]:                        
                        if jugador["Piezas"][ficha][0] >= jugador2["Piezas"][ficha2][0] > jugador["Piezas"][ficha][3]:
                            contadorfichas +=1                            
                        if contadorfichas > 1:
                            if jugador2["Piezas"][ficha2][1] == False:
                                print ("Colision detectada! De las fichas",ficha,ficha2)
                                jugador["Piezas"][ficha][0] = jugador2["Piezas"][ficha2][0]-1
                            
                        elif contadorfichas == 1:
                            if ficha2[1] == jugador2["Color"]:                                
                                if jugador2["Piezas"][ficha2][0] not in seguros:                                
                                    print(ficha,"comiendo a",ficha2)
                                    jugador2["Piezas"][ficha2][1] = True
                                    jugador["Piezas"][ficha][0] = jugador2["Piezas"][ficha2][0]
                                
     
                    else:
                        if ficha != ficha2 and jugador["Piezas"][ficha][2] ==jugador2["Piezas"][ficha2][2]:                            
                            if jugador["Piezas"][ficha][0] >= jugador2["Piezas"][ficha2][0] > jugador["Piezas"][ficha][3]:
                                print ("Colision detectada! De las fichas",ficha,ficha2)
                                jugador["Piezas"][ficha][0] = jugador["Piezas"][ficha][0] - (jugador["Piezas"][ficha][0]-jugador2["Piezas"][ficha2][0])-1
                            else:
                                if jugador["Piezas"][ficha][0] < jugador["Piezas"][ficha][3]:
                                    if jugador["Piezas"][ficha][3] + distancia >= jugador2["Piezas"][ficha2][0] > jugador["Piezas"][ficha][3]:
                                        jugador["Piezas"][ficha][0] = jugador2["Piezas"][ficha2][0] - 1                           
                                        pass
                                
            
            

        for jugador in reversed(ListaJugadores): #Loop para mostrar las fichas en el tablero          
            for ficha in jugador["Piezas"]:                
                if jugador["Piezas"][ficha][1] == False:
                    oldpos = jugador["Piezas"][ficha][3]
                    pos = jugador["Piezas"][ficha][0] 
                    if pos != oldpos:
                        if pos >= len(coords1):                            
                            pos = (jugador["Piezas"][ficha][3] + pos) % 68
                        if oldpos > len(coords1):                            
                            pos = (jugador["Piezas"][ficha][3] + pos) % 68
                        if jugador["Piezas"][ficha][2] == 2:
                            tablero[coords2[pos][0]][coords2[pos][1]] = ficha
                            tablero[coords2[oldpos][0]][coords2[oldpos][1]] = tableroreferencia[coords2[oldpos][0]][coords2[oldpos][1]]
                            if tablero[coords1[oldpos][0]][coords1[oldpos][1]] == ficha:
                                tablero[coords1[oldpos][0]][coords1[oldpos][1]] = tableroreferencia[coords1[oldpos][0]][coords1[oldpos][1]]
                        elif jugador["Piezas"][ficha][2] == 1:
                            tablero[coords1[pos][0]][coords1[pos][1]] = ficha
                            tablero[coords1[oldpos][0]][coords1[oldpos][1]] = tableroreferencia[coords1[oldpos][0]][coords1[oldpos][1]]
                            if tablero[coords2[oldpos][0]][coords2[oldpos][1]] == ficha:
                                tablero[coords2[oldpos][0]][coords2[oldpos][1]] = tableroreferencia[coords2[oldpos][0]][coords2[oldpos][1]]
                    else:   
                        if pos >= len(coords1):                            
                            pos = (jugador["Piezas"][ficha][3] + pos) % 68
                        if oldpos > len(coords1):                            
                            pos = (jugador["Piezas"][ficha][3] + pos) % 68
                        if jugador["Piezas"][ficha][2] == 2:
                            tablero[coords2[pos][0]][coords2[pos][1]] = ficha
                            tablero[coords1[pos][0]][coords1[pos][1]] = tableroreferencia[coords1[oldpos][0]][coords1[oldpos][1]]
                        elif jugador["Piezas"][ficha][2] == 1:
                            tablero[coords1[pos][0]][coords1[pos][1]] = ficha
                            tablero[coords2[pos][0]][coords1[pos][1]] = tableroreferencia[coords2[oldpos][0]][coords2[oldpos][1]]
        
            
            
main()     
        