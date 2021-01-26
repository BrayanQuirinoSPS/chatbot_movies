from database.connection import Connection
from utils import functions
from utils import constants
from utils.kerboards import get_main_keyboard,get_clear_keyboard

import config
import telebot
import math

bot = telebot.TeleBot(config.API_TOKEN) 
iteration=0
it=0
consulta=[]

def iterations(hits):
    global iteration
    iteration=math.ceil(len(hits)/10)
    #print(iteration)
def more_res(hits):
    global iteration
    global it
    actual=[]
    if(len(hits)<=10):
        if iteration==0:
            return None
        else:
            actual=[]
            for i in range(0,len(hits)):
                actual.append(hits[i])
    elif(it!=iteration):
        it+=1
        rl=(it-1)*10
        rr=(it)*10
        if it==iteration:
            rr=len(hits)
            it=0
            iteration=0
        for i in range(rl,rr):
            actual.append(hits[i])
    return actual

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, f"Hola {message.from_user.first_name} con este podrás buscar películas para ver en SPSFLIX. Ejecuta **__/help__** para saber más.",parse_mode='MARKDOWN')

@bot.message_handler(commands=['help'])
def send_help(message):
    bot.send_message(message.chat.id, constants.HELP,parse_mode='MARKDOWN')

@bot.message_handler(commands=['more'])
def send_more(message):
    global it
    global iteration
    global consulta
    try:
        con= Connection()
        if consulta:
            mensajes=functions.crear_mensajes(more_res(consulta))
            if it!=iteration:
                for mensaje in mensajes:
                    bot.send_message(message.chat.id,mensaje)
            else:
                bot.send_message(message.chat.id,'Parece que no hay más resultados. :(')
        else:
            bot.send_message(message.chat.id,'Parece que no hay más resultados. :(')
        con.close_connection()
    except Exception as e:
        print(e)

@bot.message_handler(commands=['moviebyname'])
def send_movie_by_name(message):
    movie=message.text[13:]
    global it
    global iteration
    global consulta
    print(movie)
    if(movie):
        try:
            con= Connection()
            hits=con.get_movie_by_title(movie)
            if hits:
                consulta=functions.consulta(hits)
                iterations(consulta)
                mensajes=functions.crear_mensajes(more_res(consulta))
                if it!=iteration:
                    for mensaje in mensajes:
                        bot.send_message(message.chat.id,mensaje)
                else:
                    bot.send_message(message.chat.id,'Parece que no hay más resultados. :(')
            else: 
                bot.send_message(message.chat.id,'Parece que no hay resultados. :(')
            con.close_connection()
        except Exception as e:
            print(e)
    else:
        bot.send_message(message.chat.id,'Parece que no has escrito el título de la película.\nIntenta escribir /moviebyname <title>\nEjemplo "/moviebyname Slow Action"')
        

@bot.message_handler(commands=['peliculapornombre'])
def send_pelicula_por_nombre(message):
    movie=message.text[19:]
    global it
    global iteration
    global consulta
    print(movie)
    if(movie):
        try:
            con= Connection()
            hits=con.get_movie_by_title(movie)
            if hits:
                consulta=functions.consulta(hits)
                iterations(consulta)
                mensajes=functions.crear_mensajes(more_res(consulta))
                if it!=iteration:
                    for mensaje in mensajes:
                        bot.send_message(message.chat.id,mensaje)
                else:
                    bot.send_message(message.chat.id,'Parece que no hay más resultados. :(')
            else: 
                bot.send_message(message.chat.id,'Parece que no hay resultados. :(')
            con.close_connection()
        except Exception as e:
            print(e)
    else:
        bot.send_message(message.chat.id,'Parece que no has escrito el titulo de la película.\nIntenta escribir /peliculapornombre <titulo>\nEjemplo "/peliculapornombre Slow Action"',parse_mode='HTML')

@bot.message_handler(commands=['moviebyoverview'])
def send_movie_by_overview(message):
    overview=message.text[17:]
    global it
    global iteration
    global consulta
    print(overview)
    if(overview):
        try:
            con= Connection()
            hits=con.get_movie_by_overview(overview)
            #print(hits)
            if hits:
                consulta=functions.consulta(hits)
                #print(consulta)
                iterations(consulta)
                mensajes=functions.crear_mensajes(more_res(consulta))
                if it!=iteration:
                    for mensaje in mensajes:
                        bot.send_message(message.chat.id,mensaje)
                else:
                    bot.send_message(message.chat.id,'Parece que no hay más resultados. :(')
            else: 
                bot.send_message(message.chat.id,'Parece que no hay resultados. :(')
            con.close_connection()
        except Exception as e:
            print(e)
    else:
        bot.send_message(message.chat.id,'Parece que no has escrito el resumen de la película.\nIntenta escribir /moviebyoverview <overview>\nEjemplo "/moviebyoverview The extraordinary story"')
@bot.message_handler(commands=['peliculaporsinopsis'])
def send_pelicula_por_sinopsis(message):
    overview=message.text[21:]
    global it
    global iteration
    global consulta
    print(overview)
    if(overview):
        try:
            con= Connection()
            hits=con.get_movie_by_overview(overview)
            if hits:
                consulta=functions.consulta(hits)
                iterations(consulta)
                mensajes=functions.crear_mensajes(more_res(consulta))
                if it!=iteration:
                    for mensaje in mensajes:
                        bot.send_message(message.chat.id,mensaje)
                else:
                    bot.send_message(message.chat.id,'Parece que no hay más resultados. :(')
            else: 
                bot.send_message(message.chat.id,'Parece que no hay resultados. :(')
            con.close_connection()
        except Exception as e:
            print(e)
    else:
        bot.send_message(message.chat.id,'Parece que no has escrito el resumen de la película.\nIntenta escribir /peliculaporsinopsis <sinopsis>\nEjemplo "/peliculaporsinopsis The extraordinary story"')

@bot.message_handler(commands=['moviebyscore'])
def send_movie_by_score(message):
    sco=message.text[14:]
    global it
    global iteration
    global consulta
    #print(score)
    if(sco):
        score=float(sco)
        try:
            con= Connection()
            hits=con.get_movie_by_score(score)
            #print(hits[0])
            if hits:
                consulta=functions.consulta(hits)
                #print(consulta)
                iterations(consulta)
                mensajes=functions.crear_mensajes(more_res(consulta))
                if it!=iteration:
                    for mensaje in mensajes:
                        bot.send_message(message.chat.id,mensaje)
                else:
                    bot.send_message(message.chat.id,'Parece que no hay más resultados. :(')
            else: 
                bot.send_message(message.chat.id,'Parece que no hay resultados. :(')
            con.close_connection()
        except Exception as e:
            print(e)
    else:
        bot.send_message(message.chat.id,'Parece que no has escrito la calificación de la película.\nIntenta escribir /moviebyscore <score>\nEjemplo "/moviebyscore 7.9"')

@bot.message_handler(commands=['peliculaporcalificacion'])
def send_pelicula_por_calificacion(message):
    sco=message.text[25:]
    global it
    global iteration
    global consulta
    #print(score)
    if(sco):
        score=float(sco)
        try:
            con= Connection()
            hits=con.get_movie_by_score(score)
            if hits:
                consulta=functions.consulta(hits)
                iterations(consulta)
                mensajes=functions.crear_mensajes(more_res(consulta))
                if it!=iteration:
                    for mensaje in mensajes:
                        bot.send_message(message.chat.id,mensaje)
                else:
                    bot.send_message(message.chat.id,'Parece que no hay más resultados. :(')
            else: 
                bot.send_message(message.chat.id,'Parece que no hay resultados. :(')
            con.close_connection()
        except Exception as e:
            print(e)
    else:
        bot.send_message(message.chat.id,'Parece que no has escrito la calificación de la película.\nIntenta escribir /peliculaporcalificacion <calificacion>\nEjemplo "/peliculaporcalificacion 7.9"')

@bot.message_handler(commands=['moviebyruntime'])
def send_movie_by_runtime(message):
    runt=message.text[16:]
    global it
    global iteration
    global consulta
    #print(runtime)
    if(runt):
        runtime=int(runt)
        try:
            con= Connection()
            hits=con.get_movie_by_runtime(runtime)
            if hits:
                consulta=functions.consulta(hits)
                iterations(consulta)
                mensajes=functions.crear_mensajes(more_res(consulta))
                if it!=iteration:
                    for mensaje in mensajes:
                        bot.send_message(message.chat.id,mensaje)
                else:
                    bot.send_message(message.chat.id,'Parece que no hay más resultados. :(')
            else: 
                bot.send_message(message.chat.id,'Parece que no hay resultados. :(')
            con.close_connection()
        except Exception as e:
            print(e)
    else:
        bot.send_message(message.chat.id,'Parece que no has escrito la duración de la película.\nIntenta escribir /moviebyruntime <runtime>\nEjemplo "/moviebyruntime 86"')

@bot.message_handler(commands=['peliculaporduracion'])
def send_pelicula_por_duracion(message):
    runt=message.text[21:]
    global it
    global iteration
    global consulta
    #print(runtime)
    if(runt):
        runtime=int(runt)
        try:
            con= Connection()
            hits=con.get_movie_by_runtime(runtime)
            if hits:
                consulta=functions.consulta(hits)
                iterations(consulta)
                mensajes=functions.crear_mensajes(more_res(consulta))
                if it!=iteration:
                    for mensaje in mensajes:
                        bot.send_message(message.chat.id,mensaje)
                else:
                    bot.send_message(message.chat.id,'Parece que no hay más resultados. :(')
            else: 
                bot.send_message(message.chat.id,'Parece que no hay resultados. :(')
            con.close_connection()
        except Exception as e:
            print(e)
    else:
        bot.send_message(message.chat.id,'Parece que no has escrito la duración de la película.\nIntenta escribir /peliculaporduracion <duracion>\nEjemplo "/peliculaporduracion 86"')

@bot.message_handler(commands=['recomendacion','recommendation'])
def send_simplenote(message):
    global consulta
    try:
        con= Connection()
        hits=con.get_recommendation()
        if hits:
            consulta=functions.consulta(hits)
            mensaje=functions.print_movies(consulta)
            bot.send_message(message.chat.id,mensaje)
        con.close_connection()
    except Exception as e:
        print(e)
        bot.send_message(message.chat.id, 'Parce que hubo un error con la BD :(')



@bot.message_handler(commands=['keyboard'])
def handle_keyboard(message):
    markup = get_main_keyboard()
    bot.send_message(message.chat.id, "Elige una opción: ", reply_markup=markup)

@bot.message_handler(func=lambda message: True)
def send_response(message):
    text = message.text
    global consulta
    if text == "recomendacion" or text=='recommendation':
        con= Connection()
        hits=con.get_recommendation()
        if hits:
            consulta=functions.consulta(hits)
            mensaje=functions.print_movies(consulta)
            bot.send_message(message.chat.id,mensaje)
        con.close_connection()
    elif text == "Hide Keyboard":
        markup = get_clear_keyboard()
        bot.send_message(message.chat.id,"Escribe /keyboard para mostrar de nuevo el teclado", reply_markup=markup)
    else:
        bot.reply_to(message,"No entiendo tu mensaje. Escribe: /help para obtener ayuda")


bot.polling()
