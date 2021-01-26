# @SPS_Peliculas_Bot

## chatbot_movies
This is  bot to find a movie. 
Este es un bot para encontrar películas.
Con el podrás buscar películas en el banco de SPSFLIX. ♥

## Dependencies
- ast
- elasticsearch
- json
- math
- requests
- telebot

## Programado

- moviebyname \- \<title\> Search a movie by name. 
- peliculapornombre \- \<titulo\> Busca una película por su nombre. 
- moviebyoverview \- \<overview\> Search a movie by overview. 
- peliculaporsinopsis \- \<sinopsis\> Busca una película por sinopsis 
- moviebyscore \- \<score\> Search a movie by score. 
- peliculaporcalificacion \- \<calificacion\> Busca una película por la calificación. 
- moviebyruntime \- \<runtime-on\-minutes\> Search a movie by runtime.
- peliculaporduracion \- \<duracion-en\-minutos\> Busca una película por duración. 
- recommendation \- Give you a random movie. 
- recomendacion \- Te da una recomendación aleatoria. 
- keyboard \- Show a kerboard with options. Muestra el teclado con opciones.
- more \- Show more movies. Muestra más resultados. 

## No programado

- Buscar de cualquier forma. 
- Agregar imagenes al dataset.
- Traducir el overview. Incluso mandarlo como audio.
- Recomendar diario una película sin pedirlo (Mensajes programados) 


## Dataset
[Movies-Dataset](https://www.kaggle.com/rounakbanik/the-movies-dataset) +45,000 Movies.

## Pasos para replicar
Nota: Importante tener abiertos los puertos en la maquina virtual.
- elasticsearch: 9200
- kibana: 5601
- excelastic: 9999
- notebook: 8888

1. Instalar Java, Elasticsearch y Kibana en Ubuntu. Confuifurar archivos .yml (/documentacion/Manual_Elasticsearch_Azure.docx)
2. Ejecuar los servicios, **sudo service elasticsearch start** , **sudo service kibana start**
3. Descargar [excelastic-1.3.8.jar](https://github.com/codingchili/excelastic/releases/download/1.3.8/excelastic-1.3.8.jar) de [Excelastic](https://github.com/codingchili/excelastic/releases) si no, descargar ./elastic/excelastic/excelastic-1.3.8.jar.
4. Ejecurar excelastic **java -Xmx2g -jar excelastic-1.3.2.jar**
5. Entrat a http://ip_off_your_VM:9999
6. Dar nombre al nuevo **index** (chatbot_movie) y subir tu archivo .xlsx
7. Limpiar los valores nulos en Dev Tools.(/documentacion/some_queries.txt)
8. Ejecutar **virtualenv env** y **source ./ambiente/env/bin/activate**
9. Instalar las librerias necesarias.
10. Ejecutar **python3 main.py**

## Extras
- [Code languages table](http://www.lingoes.net/en/translator/langcode.htm)
- Para ejecutar notebook en una VM by conectarse de forma remota basta con ejecutar:
    1. **jupyter notebook --generate-config**
    2. Encontrar la linea **#c.NotebookApp.ip = 'localhost'** y cambiarla por **c.NotebookApp.ip = '0.0.0.0'**
    3. Encontrar la linea **#c.NotebookApp.open_browser = True** y cambiarla por **c.NotebookApp.open_browser = False**
    4. **jupyter notebook**
    


### Brayan Quirino \- 25/01/2021