from database import Connection
from utils import functions
from utils import constants

import telebot

bot = telebot.TeleBot(config.API_TOKEN) 
iteration=0
it=0

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

@bot.message_handler(commands=['moviebyname'])
def send_simplenote(message):
    movie=message.text[12:]
    con= new Connection()
        hits=con.get_movie_by_title(movie)
        if hits:
            consulta=functions.consulta(hits)
            iterations(consulta)
            mensaje=functions.print_movies(more_res(consulta))
        if it!=iteration
            bot.send_message(message.chat.id,mensaje)
        else:
            bot.send_message(message.chat.id,'Parece que no hay más resultados. :(')
    con.close_connection()

@bot.message_handler(commands=['peliculapornombre'])
def send_simplenote(message):
    movie=message.text[19:]
    con= new Connection()
        hits=con.get_movie_by_title(movie)
        if hits:
            consulta=functions.consulta(hits)
            iterations(consulta)
            mensaje=functions.print_movies(more_res(consulta))
        if it!=iteration
            bot.send_message(message.chat.id,mensaje)
        else:
            bot.send_message(message.chat.id,'Parece que no hay más resultados. :(')
    con.close_connection()

@bot.message_handler(commands=['moviebyoverview'])
def send_simplenote(message):
    overview=message.text[17:]
    con= new Connection()
        hits=con.get_movie_by_overview(overview)
        if hits:
            consulta=functions.consulta(hits)
            iterations(consulta)
            mensaje=functions.print_movies(more_res(consulta))
        if it!=iteration
            bot.send_message(message.chat.id,mensaje)
        else:
            bot.send_message(message.chat.id,'Parece que no hay más resultados. :(')
    con.close_connection()

@bot.message_handler(commands=['peliculaporsinopsis'])
def send_simplenote(message):
    overview=message.text[21:]
    con= new Connection()
        hits=con.get_movie_by_overview(overview)
        if hits:
            consulta=functions.consulta(hits)
            iterations(consulta)
            mensaje=functions.print_movies(more_res(consulta))
        if it!=iteration
            bot.send_message(message.chat.id,mensaje)
        else:
            bot.send_message(message.chat.id,'Parece que no hay más resultados. :(')
    con.close_connection()


@bot.message_handler(commands=['moviebyscore'])
def send_simplenote(message):
    score=float(message.text[14:])
    con= new Connection()
        hits=con.get_movie_by_score(score)
        if hits:
            consulta=functions.consulta(hits)
            iterations(consulta)
            mensaje=functions.print_movies(more_res(consulta))
        if it!=iteration
            bot.send_message(message.chat.id,mensaje)
        else:
            bot.send_message(message.chat.id,'Parece que no hay más resultados. :(')
    con.close_connection()