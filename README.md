# 4a-docs
Microservicios 

## Tener en cuenta:
1. Clonar el repositorio, ingresar a la carpeta authApp y eliminar la carpeta *migrations*
2. En la raíz del proyecto crear un entorno de python y activarlo
    - python -m venv env
    - source env/bin/activate (Linux) o env\Scripts\activate (windows)
3. Instalar las dependencias
    - pip install -r requirements.txt
4. Generar las migraciones de la aplicación 
    - python manage.py makemigrations authApp
5. Ejecutar las migraciones para la creación de una base de datos denominada *dbg6*
    - python manage_dev.py migrate (*NOTA: Para la ejecución en el local se debe usar manage_dev.py, ya que manage.py se utilizará para el despliegue en Hreoku)
7. Iniciar la aplicación desde la carpeta raíz
    - python manage_dev.py runserver (*NOTA: Para la ejecución en el local se debe usar manage_dev.py, ya que manage.py se utilizará para el despliegue en Hreoku)

Pruebas del microservicio:

[![Run in Postman](https://run.pstmn.io/button.svg)](https://app.getpostman.com/run-collection/45e3d16867042550e655?action=collection%2Fimport)
