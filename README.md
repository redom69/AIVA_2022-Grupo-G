# AIVA_2022-Grupo-G
Repositorio de la asignatura Aplicaciones Industriales y Comerciales del Máster en Visión Artificial (URJC)

## Detección de actividad en vídeos de tienda
Este repositorio está destinado al desarrollo de un proyecto consistente en la detección de la actividad en vídeos de tiendas. Para ello, distinguiremos entre tres grupos de usuarios del centro comercial:
  - Usuario que entra a la tienda.
  - Usuario que se detiene y no entra en la tienda.
  - Usuario que no se detiene.

Este sistema que pretendemos desarrollar es especialmente útil para comerciantes que desean realizar un estudio sobre el interés que generan sus tiendas. Por lo que pretendemos ofrecer una solución completa con una información que les sea de utilidad.

Adjuntamos, a continuación, un fotograma de uno de los vídeos de muestra.

![MicrosoftTeams-image](https://user-images.githubusercontent.com/50777475/159759097-5dd14399-462b-469c-906b-d2053bc64d24.png)


Este proyecto está siendo realizado por: 
  - Jairo Carrillo Huélamo &#8594; j.carrilloh.2016@alumnos.urjc.es
  - Daniel Hernández Puerto &#8594; d.hernandezp.2016@alumnos.urjc.es
  - Águeda Sierra Carreto &#8594; a.sierra.2017@alumnos.urjc.es


## Ejecución del proyecto

Este proyecto ha sido desarrollado en dos entornos de programacion, en Google Colab y en Pycharm, pero el proyecto entero ha sido montado en Pycharm. La explicación que vendrá a continuación servirá para ejecutar el proyecto en Pycharm. Primero descargaremos o clonaremos el proyecto y lo sincronizaremos con el IDE. Una vez listo y montado el proyecto ejecutaremos el comando ***pip install -r requirements.txt***. Una vez relizados estos pasos ya se podra ejecutar el proyecto. 

**Importante** comprobar que la version de Python que se esta utilizando es la *3.9.0*

~~~
  git clone https://github.com/redom69/AIVA_2022-Grupo-G.git
~~~ 

El proyecto consta, actualmente, de 3 directorios principales, el directorio *src* donde encontraremos todo el código referente a la ejecucción del algoritmo. El directorio *test* que servirá para ejecutar los test unitarios del proyecto y la carpeta de *docs* que contendrá todo lo referido a la documentación del proyecto.

Para ejecutar el proyecto habrá que hacer una pequeña configuración inicial dependiendo si se quiere ejecutar solo un vídeo o el directorio completo, de momento hay que insertar la ruta de la que se quiere extraer el video manualmente. Una vez insertada esta ruta ya se podrá ejecutar el fichero main del proyecto.

~~~
  Ejemplo de ruta : "../dataset/OneLeaveShopReenter1front.mpg"
~~~ 

Para ejeutar los test es igual que para la ejecución del programa principal, primero configuraremos el video que deseamos leer y posteriormente este nos proporcionará los resultados de los test unitarios.


## Despliegue

Se ha desarrollado una imagen Docker con el objeto de facilitar el despliegue de la aplicación. Es necesario tener instalado docker en la máquina donde se desea realizar el despliegue.

Pasos a seguir para el despliegue:

- Descargarse la imagen docker redom69/aiva-2022-grupo-g que se encuentra alojada en DockerHub. Para ello ejecutar:

~~~
  docker pull redom69/aiva-2022-grupo-g
~~~ 

- Lanzar un contenedor con la imagen docker:

~~~
  docker run --name ComVision redom69/aiva-2022-grupo-g   
~~~ 

- Puede visualizar que el contenedor está ejecutándose, utilizando el comando:

~~~
  docker ps
~~~ 
