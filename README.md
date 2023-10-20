<h1 align="center">  🚀Proyecto Final Grupal (Bootcamp Henry / Data Science) 🚀 </h1>
<h1 align="center"> APP de Recomendacion de restaurantes </h1>

![WhatsApp Image 2023-09-16 at 16 17 55](https://github.com/Constanzafl/Proyecto_Final/assets/121994442/88fa5090-2e4b-46e5-8329-e28e41d0a7e1)

### Autores del proyecto y roles
* Fausto Ezquerra ➡️ Data Analyst [Linkedin](https://www.linkedin.com/in/faustoezquerra/)
* Maria Constanza Florio ➡️ Data Engineer [Linkedin](https://www.linkedin.com/in/mar%C3%ADa-constanza-florio-1926b5158/)
* Joaquin Millan ➡️ Data Analyst [Linkedin](https://www.linkedin.com/in/jmillanlanhozo/)
* Martin Peñas ➡️ Data Science [Linkedin](https://www.linkedin.com/in/martinepenas/)
* Nicolas Yapur ➡️ Data Engineer [Linkedin](https://www.linkedin.com/in/nicolas-yapur-55982513b/)


## 📚 Resumen 📚
* En este trabajo grupal simulamos un ambiente laboral, en el cual somos una consultora especializada en Business Intelligence y se nos proveen 2 datasets de informacion turistica y reseñas de Google y YELP. Nuestro Cliente es del ambito del turismo, y tenemos que crear un producto que sea rentable y resuelva lo que el cliente quiere. Elegimos como Cliente al Estado de Florida, siendo nosotros una consultora llamada Kangaroo.
* Nuestro cliente desea mejorar la experiencia gastronomica de sus turistas, motivo por el cual procesando y analizando los datos que tenemos, ofrecemos la creacion de una APP de recomendacion de restaurantes, que se ajuste a las preferencias de cada persona.  


## 🌈 Descripcion del proyecto 🌈
*En un mundo en constante movimiento, la experiencia gastronómica juega un papel fundamental en la satisfacción de los viajeros. En este sentido, el Estado de Florida está comprometido en elevar la calidad de la experiencia de sus turistas, y es por eso que ha decidido contratar a Kangaroo, una consultora startup especializada en Business Intelligence.
* Kangaroo se ha destacado por su capacidad de transformar datos en soluciones prácticas y personalizadas. En esta ocasión, hemos llevado nuestra experiencia al mundo de la gastronomía turística. Sabemos que cuando estamos de viaje, elegir el lugar perfecto para comer puede ser un desafío abrumador. ¿Dónde ir? ¿Qué opciones se adaptan a nuestras preferencias? ¿Cómo evitar perder tiempo valioso explorando opciones que no son adecuadas?
* La respuesta a estos desafíos se llama “Kanguro Viajero”, nuestra innovadora aplicación web diseñada para simplificar la vida de los viajeros.
* A través de un análisis de datos exhaustivo y la implementación de un avanzado modelo de recomendación, Kanguro Viajero está diseñada para ofrecerte una experiencia gastronómica personalizada y sin complicaciones.
* Imagina simplemente que el turista ingrese sus preferencias y ubicación, y en segundos reciba una lista de restaurantes que se ajusten perfectamente a sus necesidades. Kanguro Viajero le permitirá disfrutar de la deliciosa comida de Florida de manera eficiente y satisfactoria, sin perder tiempo en búsquedas interminables.


## 🌈 Objetivos 🌈
* Crear una APP de recomendación de restaurantes llamada "Kanguro Viajero" en la cual el usuario coloca sus preferencias y su localización y esta devuelve distintas recomendaciones.
* Armar un Datalake con todos los datos iniciales.
* Crear un DataWarehouse que contenga data recopilada, procesada y específica.
* Generar un pipeline de procesamiento de data automatizado
* Crear un dashboard visualmente atractivo e interactivo, que integre los datos del análisis exploratorio de datos realizado.

## ✔️ Alcance ✔️
* Recopilación, limpieza y análisis de datos obtenidos de datasets de Google Maps y Yelp para obtener información sobre lugares de interés.
* Desarrollo de modelos de machine learning para analizar y clasificar las reseñas de los usuarios y los lugares en función de sus sentimientos.
* Implementación de un motor de recomendación que sugiere lugares a los usuarios en función de sus preferencias y localización.
* Diseño y desarrollo de un dashboard que permite visualizar el análisis de los datos.
* Puesta en marcha de proyecto en MVP donde se pueda observar la app en funcionamiento.

## ❌ Fuera de alcance ❌
* Este proyecto no abarca recomendación de hoteles u otras atracciones turísticas ni otros estados que no sean Florida. 

## 📈 KPIs 📈
### **Evolución Anual del Rating:** Indicador que mide la evolución del rating promedio del restaurante seleccionado en el año y mes seleccionados respecto al mismo periodo del año pasado.
* **Objetivo:** controlar la evolución en ratings de los restaurantes, se quiere estar al menos 5% arriba.
* **Temporalidad:** anual/mensual.
### **Estado de Rating:** Indicador que mide el rating promedio para el año y mes seleccionados y el restaurante seleccionada y lo compara contra el rating promedio histórico.
* **Objetivo:** medir que el rating esté por encima del rating histórico.
* **Temporalidad:** anual/mensual.
### **Crecimiento de Ratings/Popularidad:** Indicador que mide la cantidad de ratings dados a un restaurante seleccionado en un año y mes seleccionados y lo compara con la cantidad de ratings respecto al mes pasado.
* **Objetivo:** medirla evolución instantánea en popularidad de los restaurantes.
* **Temporalidad:** mensual.
### **Crecimiento de Popularidad Anual:** Indicador que mide la cantidad de ratings dados a un restaurante seleccionado en una fecha seleccionada y lo compara con la cantidad de ratings respecto al mismo periodo del año pasado.
* **Objetivo:** medirla evolución sostenida en popularidad de los restaurantes.
* **Temporalidad:** mensual.
### **Crecimiento en cantidad de Clientes:** Indicador que mide el crecimiento en la cantidad de clientes comparando la cantidad de nuevos clientes en el  periodo actual respecto al mismo periodo del pasado año. Se puede medir restaurantes o categoría de restaurantes.
* **Objetivo:** medir el crecimiento sostenido en cuanto a clientes del restaurante o categoría de restaurantes .
* **Temporalidad:** anual/mensual.
### **Crecimiento lineal en Clientes:** Indicador que mide el crecimiento lineal en la cantidad de clientes basado en los clientes que dejaron su calificación del restaurante o categoría de restaurantes.
* **Objetivo:** medir crecimiento o estancamiento del restaurante o categoría de restaurantes.
* **Temporalidad:** anual/mensual.
 

### **KPI’s posibles posteriores a la implementación del producto:**
### **Éxito de la APP:** lograr la descarga de la app desde el lanzamiento, en un periodo de 1 año, de hasta un 60% de los turistas. 
* **Objetivo:** que los turistas usen nuestra app como sistema de recomendación. Indicador numérico = cantidad de descargas de la aplicación KanguroViajero sobre total de turistas.
* **Plazo:** un año. Meta: Promover utilización de nuestra app en un 60% 

## 🖥️ Metodología de trabajo 🖥️

![Ventajas-del-uso-de-metodologías-ágiles-1024x562](https://github.com/Constanzafl/Proyecto_Final/assets/121994442/d515d49b-cc88-438f-9795-3ce879fbb699)

La solución propuesta se llevará a cabo siguiendo una metodología de desarrollo ágil para garantizar la entrega efectiva y oportuna de la aplicación, el dashboard y el MVP, con un enfoque constante basado en la calidad y disminución de errores. Dado que la productividad es clave para el equipo, planteamos la gestión de tareas en un Diagrama de Gantt y un tablero de Kanban, ambos realizados sobre Notion. Allí se plantea la tarea, el tiempo y los responsables, para evitar la duplicidad de trabajo e incrementar la colaboración entre los integrantes una vez culminada la tarea asignada.  

## 📈 Stack tecnológico utilizado 📈
* Lenguajes: Python
* Ingeniería de datos: Google Cloud, Google Storage, Google Function, Big Query, python, SQL
* Análisis y visualización de datos: Matplotlib, Seaborn, Power Bi, Folium, Streamlit.
* Modelo de machine learning: Python ScikitLearn, NLP, NLTK
* Gestión de proyecto: Notion, Google Meet, Github, GitKraken

## 📶 Pipeline 📶

![Captura de pantalla 2023-10-04 173208](https://github.com/Constanzafl/Proyecto_Final/assets/121994442/da9c6092-a756-43e6-bda0-9d9106a83776)


* **Automatización de Data Warehouse y la carga incremental**: Google Cloud.
* Iniciamos configurando dos buckets en **Cloud Storage**: "data_lake_kanguro" y "data_procesada_kanguro". En el primero, subimos nuestros datos manualmente, mientras que en el segundo implementamos **Cloud Functions** para simplificar el proceso.
* Creamos dos funciones:
* *ETL_bucket_a_bucket_limpio:* Esta función se activa automáticamente cada vez que se añaden nuevos archivos a "data_lake_kanguro". Su tarea principal es ejecutar nuestro proceso ETL para procesar los datos recién cargados y, a continuación, trasladarlos al bucket "data_procesada_kanguro".
* *De_bucket_limpio_a_BigQuery:* La segunda función entra en acción cuando se carga un archivo en el bucket "data_procesada_kanguro". Su propósito es tomar los datos procesados y cargarlos de manera eficiente en BigQuery, asegurando que nuestra base de datos esté siempre actualizada con la información más reciente.
* Esta automatización garantiza que nuestros datos fluyan desde su origen en "data_lake_kanguro" hasta BigQuery, lo que simplifica la gestión de nuestro Data Warehouse y permite un análisis en tiempo real de los datos procesados. Además, al eliminar la intervención manual, hemos mejorado significativamente la eficiencia de nuestro proceso de datos.

* **Integración  y Visualización de Datos en Power BI:**
Para visualizar nuestros datos y los resultados de nuestro modelo, conectamos Power BI a las fuentes de datos de Big Query, donde están almacenados los datos procesados. Finalmente, en Power BI, creamos visualizaciones para mostrar KPIs, tendencias y otros insights de nuestros datos. Programamos actualizaciones regulares para garantizar que nuestros informes estén siempre actualizados y disponibles para la toma de decisiones.

[Dashboard Power BI](https://drive.google.com/file/d/1rpCtNlTB724mwJsMxIxo_Lab74d8w2DZ/view?usp=share_link)

* **Modelos de Machine Learning en Streamlit:** Desplegamos nuestros modelos de recomendación de Machine Learning en Streamlit para ofrecer una experiencia interactiva en nuestra aplicación de recomendación de restaurantes.

[Streamlit App](https://kangurorestaurants.streamlit.app/)

## 📂 Datos 📂
* Dividimos la organizacion de las carpetas por las semanas de trabajo en los diferentes Sprints. 
* **Sprint 1:** dentro de esta carpeta tenemos dos carpetas en donde realizamos el ETL y EDA inicial de los datos.
* **Sprint 2:** tenemos tambien dos carpetas que se llaman EDA y ETL. En la carpeta ETL tenemos el archivo ETL.py que es el que usamos para la funcion de Google Functions. Dentro de la carpeta EDA tenemos EDA general de los estados, de metadata, de YELP y el EDA especifico del estado de Florida. 
* **Sprint 3:** en este sprint se encuentran los modelos de Machine Learning que corren en nuestro deploy en streamlit y el dashboard en Power BI.
  
## Links de referencia
* **WEB del proyecto**: [WEB](https://6531312fde714.site123.me/)

* **Diagramas**: [Notion](https://kanguroviajero.notion.site/Kangaroo-App-Diagrama-de-Gantt-Kanban-26d34977a62e4eb884f72eada7cb8d6a?pvs=4)

* **Informes**: [Sprint 1](https://drive.google.com/file/d/1ZRq2sJPvwazXdwUK57UKDH6O_FC5vKw9/view?usp=drive_link), [Sprint 2](https://drive.google.com/file/d/1O270C-11ELrtx7Z6CIESt2t6YwxdC8yI/view?usp=drive_link), [Sprint 3](https://drive.google.com/file/d/12ldJN-be1jKQRF-tJbLQ-XhnJNMASHh-/view?usp=sharing)


* **Presentaciones**: [Sprint 1](https://docs.google.com/presentation/d/1FVXSwmO8zaS5nYGG2wB0RIGuWHioSkzidErcHXnijwA/edit#slide=id.g2472c1f28cd_0_64),[Sprint 2](https://gamma.app/docs/Consultora-Kangaroo-ob1ol8xxi4un9f0), [Sprint 3](https://drive.google.com/file/d/11i8fTyiTrEDtGHC7ooVxOqx5fir5oD4I/view?usp=share_link)

* **APP de Recomendacion de Restaurants**: [Streamlit App](https://kangurorestaurants.streamlit.app/)

* **Github del Streamlit:** [Git Hub Streamlit](https://github.com/Constanzafl/Proyecto_final_streamlit)


