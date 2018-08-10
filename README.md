# Test Fullstack Tech-K

## Objetivo
---
Por medio de este test se evaluarán algunos de tus conocimientos que nos interesan como desarrollador.

## Instrucciones de uso
---
1. Hacer un fork del proyecto
2. Instalar cliente de [Docker](https://www.docker.com/)
3. Instalar [Docker Compose](https://docs.docker.com/compose/)
4. Levantar el proyecto:
    * `$ cd path/to/project/fullstack/techk`
    * `$ docker-compose up`
    * Verificar correcto funcionamiento en [http://localhost:8000/](http://localhost:8000/)
5. Desarrollar lo que se indica. Si existen supuestos, estos deben definirse claramente en el README
6. Entregar desarrollo por medio de un pull-request y notificar envío por email


## Instrucciones de desarrollo
---
Desarrollar un scraper que permita obtener información de [esta página web](http://books.toscrape.com/index.html), almacenarla en BBDD y luego visualizarla en una interfaz web. 

Lo anterior será bajo el uso del framework [Django 2.0.5](https://www.djangoproject.com/).

### *Web Scraping*

Se requiere obtener del [sitio web](http://books.toscrape.com/index.html) la siguiente información:

* Listado de categorías (travel, mystery, etc.)
* Información de cada libro:
  * Category
  * Title
  * Thumbnail
  * Price
  * Stock
  * Product Description
  * UPC

***Nota:*** Se recomienda usar las librerías [Requests](http://docs.python-requests.org/en/master/) y [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) para resolver este punto.

#### *Supuestos*
* Sólo se obtiene la información directamente accesible en el [enlace entregado](http://books.toscrape.com/index.html), es decir, sólo lo que se puede obtener desde la primera página del home. No se obtendrá toda la información que contiene el sitio si no es accesible desde dicho lugar, pues esto es lo que se especificó en las instrucciones. Sólo se obtendrá de forma indirecta la información que se especificó como requerida que no se pueda obtener de forma directa. De todos modos en este caso obtener la información del resto de libros no implicaría mucho trabajo adicional.
    * Como corolario se asumirá que no se requiere trabajar con grandes cantidades de datos que a su vez requieran tratamiento especial, por ejemplo para evitar problemas de falta de memoria. Tales casos no son muy difíciles de manejar, si se quisiera hacer.
* Sólo se almacenará la URL de la thumbnail, pues no se especifica si se requiere almacenar sólo eso o el archivo de imagen propiamente tal, además de que en el JSON de muestra sólo se almacena la URL. Estoy asumiendo el caso más simple, aunque almacenar el archivo de imagen es bastante fácil.
* Se está asumiendo que el sitio web está correcta y consistentemente formateado, es decir, todas las páginas similares están construidas siguiendo los mismos patrones y no hay casos extraños como por ejemplo un libro cuya página no tenga el título, o donde la información como el upc no esté en una tabla con el mismo orden las de los demás libros. En pocas palabras, se asume que los inputs "se portan bien". Tomar en cuenta esos casos requeriría algo de trabajo, pero no mucho, dada la pequeña cantidad de datos que se recolectan.

### *Backend*

La información obtenida por el scraper (en la sección anterior) debe ser almacenada en una BBDD sqlite. Para ello se debe modelar la BBDD, crear los modelos de Django y sus respectivas migraciones.

#### *Supuestos*
* Sólo se incluirán en la BBDD los datos que contiene el JSON de ejemplo, es decir, no se incluirán campos de fecha de creación o última edición del registro, etc., pues estos no se piden.
* Se asume que la base de datos debe limpiarse cada vez que se vuelve a recolectar datos.

### *Frontend*

La información obtenida por el scraper debe ser presentada en forma de tabla. El diseño queda a libre elección del desarrollador.

¿Qué considera?
* Un botón que inicie/ejecute el scraper para obtener los datos del sitio web(*)
* Un listado de Categorías obtenidas por el scraper.
* Al seleccionar una categoría, la tabla sólo mostrará libros de esa categoría
* La tabla debe tener un buscador por los atributos que posee
* Se debe poder eliminar registros de la tabla que se presente

***Notas:***
(*): Si no se dispone de los datos obtenidos por el scraper, debido a la no realización de esta etapa, los datos deben ser ser cargados desde un archivo en formato JSON. Este archivo debe contener la información mínima para que la interfaz web funcione correctamente, es decir:
* Al menos 3 categorías
* Al menos 5 libros por categoría
* Estructura del archivo JSON es de la siguiente forma:
```
[{
    "categories": [
        {
            "id": 1,
            "name": "Travel"
        }, {
            "id": 2,
            "name": "Mystery"
        }, {
            "id": 3,
            "name": "Historical Fiction"
        }
    ],
    "books": [
        {
            "id": 1;
            "category_id": 1,
            "title": "It's Only the Himalayas",
            "thumbnail_url": "http://books.toscrape.com/media/cache/6d/41/6d418a73cc7d4ecfd75ca11d854041db.jpg",
            "price": "£45.17",
            "stock": true,
            "product_description": "Wherever you go, whatever you do, just ...",
            "upc": "a22124811bfa8350"
        }
    ]
}]
```

## Restricciones
---
* No se debe usar el Admin de Django
* Usar ORM de Django (no raw queries)


## Bonus
---
* Webscraping usando la librería `Requests` y `BeautifulSoup`
    * Hecho
* Uso de alguna librería en el frontend. Idealmente `React`
    * No hecho
* Uso de `Django Rest Framework` para la comunicación entre frontend y backend
    * No hecho
* Uso de test (unittest con [pytest](https://docs.pytest.org/en/latest/))
    * No hecho


## En qué nos fijaremos 
---
* Correcto uso del ORM
* Correcto modelamiento la BBDD
* Correcto uso de GIT
* Patrones de diseño
* Orden del código

## Conclusiones

* No logré aprender a hacer funcionar el par de librerías que probé -incluyendo `React`- en el tiempo que me quedó luego de hacer funcionar y mejorar el scraper, la BBDD y la vista básica que construí. Tuve problemas instalando y configurando las librerías y el tiempo lamentablemente no me fue suficiente para resolver los problemas que tuve además de para aprender a usar `Django`, `BeautifulSoup` y `Requests`.

    * Considero que con algo de tutoría podría aprender a hacer funcionar `React` o alguna librería similar en alrededor de una semana adicional. Creo que la instalación y configuración me es más complicada de lo que me sería su uso y aplicación propiamente tales. De lo que pude leer en documentación y tutoriales el uso de `React` no parece tan complicado.

* Por lo anterior sólo terminé teniendo una web estática donde automáticamente se lleva a cabo el scraping y se muestran los resultados en tablas que son casi más placeholders que otra cosa, pero al menos muestran datos reales obtenidos desde la BBDD. Dicho de otro modo, logré hacer el scraper, el backend, pero del frontend sólo logré hacer un esqueleto muy básico y apenas funcional para mostrar los datos de la BBDD sin poder interactuar con ellos más allá de eso.

    * Tenía la idea de quizá usar `Bootstrap` para el estilo del frontend, si lograba tener tiempo para ello, ya que la he usado antes y me gustan los resultados que se obtienen usándola. Lamentablemente no logré llegar a ese punto.

* Desde un principio consideré muy probable que terminaría no haciendo unit tests, pues es el tema con el que menos familiarizado estoy. Nunca he trabajado con este tipo de tests, por lo que adrede lo dejé como última prioridad entre los requisitos.

    * No tendría problema en aprender a hacer unit tests. De hecho es probable que lo haga más temprano que tarde por iniciativa propia. Por lo que entiendo no es tan complicado hacerlos.

* Quiero destacar lo cómodo que encontré trabajar con `BeautifulSoup`. Es una librería muy intuitiva de usar, una vez que se aprende las lógicas que usa.

    * Mientras investigaba sobre `BeautifulSoup` me topé con `[Scrapy](https://doc.scrapy.org/)`. No leí mucho al respecto, pero lo poco que ví parecía interesante. Imagino que deben conocerla, pero la menciono en caso que no sea así.

* En general el ejercicio me pareció suficientemente completo y al grano para lo que se requiere hoy en día de un desarrollador fullstack novato. Tiene también suficiente complejidad potencialmente implícita -dependiendo de los supuestos que uno haga o no- como para abordar varios aspectos adicionales que se podrían querer evaluar.

    * Trataré de seguir desarrollando esta aplicación en mi tiempo libre el próximo mes hasta que logre cumplir con todos los requisitos, porque la encuentro un buen ejercicio para aprender a utilizar estas varias tecnologías que encuentro valiosas para mi desarrollo profesional.