import ast
import math

def consulta(hits):
    cons=[]
    aux_dic={}
    for hit in hits:
        aux_dic={
            'Idiomas disponibles':get_row(ast.literal_eval(res['_source']['spoken_languages'])),
            'Idioma original':res['_source']['original_language'],
            'Genero':get_row(ast.literal_eval(res['_source']['genres'])),
            'Titulo':res['_source']['title'],
            'Adultos':get_adults(ast.literal_eval(res['_source']['adult'])),
            'Votos':res['_source']['vote_count'],
            'Calificacion':res['_source']['vote_average'],
            'Fecha':res['_source']['release_date'][:10],
            'Sinopsis':res['_source']['overview'].replace('\n','').replace('\t',''),
            'Duracion':f'{format(res["_source"]["runtime"]/60,".1f")} horas/{res["_source"]["runtime"]} minutos.'
        }
        cons.append(aux_dic)
    return cons
def get_row(dics):
    #print(dics)
    lista=[]
    for i in dics:
        lista.append(i['name'])
    return(', '.join(lista))

def get_adults(adult):
    if(adult)
        return 'Si'
    return 'No'

def print_movies(movies):
    message=''
    for movie in movies:
        message+= f'Título: {movie["Titulo"]}\nDuración: {movie["Duracion"]}\nGenero: {movie["Genero"]}\nIdiomas disponibles: {movie["Idiomas disponibles"]}\nIdioma original: {movie["Idioma original"]}:{movie['Idioma original']}:\nVotos: {movie["Votos"]}\nCalificación: {movie["Calificion"]}\nFecha: {movie["Fecha"]}\nAdultos: {movie["Adultos"]}\nSinopsis: {movie["Sinopsis"]}\n'
    return message

def crear_mensajes(movies):
    mensaje='Películas:\n'
    line=''
    mensajes=[]
    for movie in movies:
        line=f'Título: {movie["Titulo"]}\nDuración: {movie["Duracion"]}\nGenero: {movie["Genero"]}\nIdiomas disponibles: {movie["Idiomas disponibles"]}\nIdioma original: {movie["Idioma original"]}:{movie['Idioma original']}:\nVotos: {movie["Votos"]}\nCalificación: {movie["Calificion"]}\nFecha: {movie["Fecha"]}\nAdultos: {movie["Adultos"]}\nSinopsis: {movie["Sinopsis"]}\n'
        if acortador(mensaje,line):
            mensajes.append(mensaje)
            mensaje=''
        mensaje+=line
        #print(mensajes)
    mensajes.append(mensaje)
    return mensajes

def acortador(ori,suma):
    if len(ori+suma)>=2999:
        return True
    return False