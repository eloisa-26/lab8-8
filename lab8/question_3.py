def minutos_por_usuario(reproducciones: list) -> dict:
    """
    Input:
        list: list de diccionarios con el usuario, artista y minutos
    Output:
        dict: diccionario con el par nombre - minutos totales de cada usuario
    """
def minutos_por_usuario(reproducciones: list) :
    totales = {}
    for reproduccion in reproducciones:
        usuario = reproduccion["usuario"]
        minutos = reproduccion["minutos"]
        if usuario in totales:
            totales[usuario] += minutos
        else:
            totales[usuario] = minutos
    return totales
    

def artistas_por_usuario(reprodicciones: list) -> dict:
    """
    Input:
        list: list de diccionarios con el usuario, artista y minutos
    Output:
        dict: diccionario con el par nombre - lista de los artistas de cada usuario
    """
def artistas_por_usuario(reproducciones: list) -> dict:
    historial = {}
    for reproduccion in reproducciones:
        usuario = reproduccion["usuario"]
        artista = reproduccion["artista"]
        if usuario in historial:
            historial[usuario].append(artista)
        else:
            historial[usuario] = [artista]
    return historial
 
def usuario_mas_activo(reproducciones: list) -> str:
    """
    Input:
        list: list de diccionarios con el usuario, artista y minutos
    Output:
        str: nombre del usuario con más minutos
    """
    def usuario_mas_activo(reproducciones: list) -> str:
        usuario_top: str = ""
        minutos_top: int = 0
        for reproduccion in reproducciones:
            usuario = reproduccion["usuario"]
            minutos = reproduccion["minutos"]
            if minutos > minutos_top:
                minutos_top = minutos
                usuario_top = usuario
        return usuario_top

if __name__ == "__main__":
    reproducciones = [
        {"usuario" : "sofia" , "artista" : "Wolf Alice"   , "minutos" : 60 },
        {"usuario" : "daniel", "artista" : "Milo J"       , "minutos" : 30 },
        {"usuario" : "sofia" , "artista" : "Fleetwood Mac", "minutos" : 42 },
        {"usuario" : "carlos", "artista" : "Americania"   , "minutos" : 21 },
        {"usuario" : "elena" , "artista" : "Tame Impala"  , "minutos" : 25 },
        {"usuario" : "carlos", "artista" : "Dua Lipa"     , "minutos" : 56 },
        {"usuario" : "sofia" , "artista" : "MGMT"         , "minutos" : 43 },
        {"usuario" : "carlos", "artista" : "Dua Lipa"     , "minutos" : 20 }
    ]

    print(minutos_por_usuario(reproducciones))  # -> {“sofia” : 145, “daniel” : 30, “carlos” : 97, “elena” : 25} 
    print(artistas_por_usuario(reproducciones)) # -> {“sofia” : [“Wolf ALice”, “Fleetwood Mac”, MGMT],  
    #                                            #     “daniel” : [“Milo J”],  
    #                                            #     “carlos” : [“Americania”, “Dua Lipa”],  
    #                                            #     “elena”  : [“Tame Impala”]} 
    print(usuario_mas_activo(reproducciones))   # -> sofia