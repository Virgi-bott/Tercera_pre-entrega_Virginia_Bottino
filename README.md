# Tercera_pre-entrega_Virginia_Bottino

La idea del proyecto es una pagina para conectar a personas que reman y organizar salidas. 

Se puede ingresar al panel de administración de Django utilizando el nombre de usuario "ADMIN" y la contraseña "ADMIN".

Consta de 3 BD a las que se pueden insertar datos a traves de formularios: 
 - Travesias: donde se publican y pueden ver todas las salidas a organizar. 
 - Clubes: es un registro de clubes que quieren formar parte del proyecto.
 - Kayakistas: es un registro de personas que reman. Esta BD tiene un buscador.

Desde la pagina principal hay un boton para registrarse como kayakista o como club y tambien para ver las travesias publicadas. 
En la barra superior a la izquierda está siempre la opción para volver al Inicio y a la derecha los botones 'Kayakistas', 'Travesias' y 'Clubes'. 
Al entrar a cada una de estas urls se ve la lista de registros y una opción para agregar registro. En el caso de 'Kayakistas' hay además un botón de búsqueda.
