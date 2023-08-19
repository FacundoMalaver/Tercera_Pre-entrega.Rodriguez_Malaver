# Tercera Pre-entrega
Alumno:Rodirguez Malaver, Facundo

## Primeros pasos:
- Lo pirmero, una vez descargado el archivo, es posicionarse con el comando 'cd' en la carpeta 'tercera'. Un vez ahi, utilizamos el comando 'python manage.py runserver' el cual nos dara la direccion url de la pagina.
- Una vez en la pagina, tenemos varias opciones disponibles. Podemos dirigirnos a cualquiera de los botones en la parte superior de la pantalla, o usar la funcion de 'buscar comision' en la pagina de inicio. A continuacion adjunto una pequeña descripcion de las funciones de cada pagina a la que los botones nos dirigen.

## Clases:
- Profesores: Incluye el nombre y apellido (los cuales muestra abajo del formulario), el email y la profesion. El campo email debe ser rellenado con el formato de un correo electronico para ser aceptado (eg. example@example.com). Una vez todos los campos estan rellendos, apretamos 'Guardar profesor' y deberia aparecer el nuevo profesor en la lista debajo del formato.
- Entregables: Incluye nombre y fecha de entrega (con ejemplos de como tiene que introducirse la fecha para ser aceptada). La checkbox de entrega tiene que ser verificada para poder guardar la entrega, la cual aparecera debajo del formato en una lista.
- Cursos: Incluye el nombre del curso y el numero de comision.
- Estudiantes: Incluye el nombre y appellido del estudiante y su email. Igual que en Profesores, el email tiene que tener el formato correspondiente para ser aceptado.
- Sedes: Incluye el nombre de la sede, la direccion, y el telefono para contactarse con esa sede en especifico. El telefono es un atributo de tipe Integer, asi que solo acepta numeros.

## Busqueda de comisiones:
-Se puede buscar comisiones mediante el input en la pagina de inicio. Simplemente inserte el numero de la comision que esta buscando, o un sucesion de numeros que forman parte del numero de comision completo, y el usuario sera redirigido a una lista con la/s comision/es que contengan esos numeros.

## Admin:
-Si se quiere confirmar cualquier informacion o agregar salteando los formularios, se puede ingresar a traves de /admin. 
Usuario: admin
Contraseña: admin
