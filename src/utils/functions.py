import ast
import math

en=u'\xF0\x9F\x87\xBA\xF0\x9F\x87\xB8'
es=u'\xF0\x9F\x87\xAA\xF0\x9F\x87\xB8'   

def consulta(hits):
    cons=[]
    aux_dic={}
    for hit in hits:
        #print(hit['_id'])
        aux_dic={
            'Idiomas disponibles':get_row(ast.literal_eval(hit['_source']['spoken_languages'])),
            'Idioma original':hit['_source']['original_language'],
            'Genero':get_row(ast.literal_eval(hit['_source']['genres'])),
            'Titulo':hit['_source']['title'],
            'Adultos':get_adults(ast.literal_eval(hit['_source']['adult'])),
            'Votos':hit['_source']['vote_count'],
            'Calificacion':hit['_source']['vote_average'],
            'Fecha':hit['_source']['release_date'][:10],
            'Sinopsis':hit['_source']['overview'].replace('\n','').replace('\t',''),
            'Duracion':f'{format(hit["_source"]["runtime"]/60,".1f")} horas/{hit["_source"]["runtime"]} minutos.'
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
    if(adult):
        return 'Si'
    return 'No'

def print_movies(movies):
    message=''
    for movie in movies:
        flag=movie['Idioma original']
        if(movie['Idioma original']=='es'):
            flag=es
        if(movie['Idioma original']=='en'):
            flag=en
        message+= f'Título: {movie["Titulo"]}\nDuración: {movie["Duracion"]}\nGenero: {movie["Genero"]}\nIdiomas disponibles: {movie["Idiomas disponibles"]}\nIdioma original: {movie["Idioma original"]} {flag}\nVotos: {movie["Votos"]}\nCalificación: {movie["Calificacion"]}\nFecha: {movie["Fecha"]}\nAdultos: {movie["Adultos"]}\nSinopsis: {movie["Sinopsis"]}\n\n'
    return message

def crear_mensajes(movies):
    mensaje='Películas:\n'
    line=''
    mensajes=[]
    for movie in movies:
        line=f'Título: {movie["Titulo"]}\nDuración: {movie["Duracion"]}\nGenero: {movie["Genero"]}\nIdiomas disponibles: {movie["Idiomas disponibles"]}\nIdioma original: {movie["Idioma original"]} :{movie["Idioma original"]}:\nVotos: {movie["Votos"]}\nCalificación: {movie["Calificacion"]}\nFecha: {movie["Fecha"]}\nAdultos: {movie["Adultos"]}\nSinopsis: {movie["Sinopsis"]}\n\n'
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
