## DOCUMENTACIÓN DE ENDPOINTS: 


#### NOTA GENERAL:
Todos los endpoints requieren que el usuario esté autenticado y tenga permisos de administrador para realizar acciones específicas. En caso de errores, se proporcionan mensajes claros que indican el problema.

#### LOGIN : 


##### MÉTODO POST / AUTENTICACIÓN
Endpoint : /login

Cuerpo de la solicitud: 
```json
    {
    "username":"nombre",
    "password":"contraseña"
    }
```
Respuesta: 
```json
    {
    "Token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...."
    }
```

#### USERS: 


##### MÉTODO POST 

Endpoint : /users

Cuerpo de la solicitud: 
```json
    {
    "usuario": "nuevo_usuario",
    "contrasenia": "password"
    }
```
Respuesta:
```json 
{
  "Mensaje":"Usuario creado correctamente",
  "Usuario": "nuevo_usuario"
}
```
Mensajes de error:  
    `403 Forbidden`: Solo el admin puede crear nuevos usuarios.  
    `500 Internal Server Error`: Fallo la creación del nuevo usuario.  
 

##### MÉTODO GET

Si el usuario autenticado es administrador, se devuelve la lista completa con detalles de cada usuario. Si el usuario no es administrador, se devuelve una versión minimalista de los datos del usuario.


#### MARCA: 


##### MÉTODO POST


Endpoint : /marcas
201 Created
Cuerpo de la solicitud: 
```json
    {
    "nombre":"Nombre de la marca a crear"
    }
```
Respuesta:
```json
    {
    "Mensaje": "Marca creada exitosamente",
    "marca": {
        "id": 1,
        "nombre": "Samsung"
    }
    }
```
400 Bad Request - Falta el campo nombre:
```json
    {
  "Mensaje": "El nombre de la marca es obligatorio"
    }   
```
Mas mensajes de error:   
    `400`: El campo 'nombre' es obligatorio
    `403 Forbidden`: No está autorizado para crear marcas.  
    `500 Internal Server Error`: Error interno del servidor al procesar la solicitud.
 


##### MÉTODO GET 

Endpoint : /marcas_list

Este endpoint devuelve una lista de todas las marcas disponibles en la base de datos.

Respuesta exitosa:
200 OK:


```json
  {   
    "id": 1,
    "nombre": "Samsung"
  },
  {
    "id": 2,
    "nombre": "Apple"
  },
  {
    "id": 3,
    "nombre": "Motorola"
  },
  {
    "id": 4,
    "nombre": "Nokia"
  },
  {
    "id": 5,
    "nombre": "BlackBerry"
  }
```

##### MÉTODO DELETE

Endpoint : /marca/<int:id>/delete

Respuesta 200:
```json
{
  "Mensaje": "Marca eliminado correctamente"
}
```
Mensajes de error:   
    `403 Forbidden`: "Mensaje": "Solo el administrador puede eliminar marcas.  
    `404 Not found`: "Mensaje": "Marca no encontrado.  
    `500 Internal Server Error`: "Mensaje": "Error al eliminar la marca 

##### MÉTODO PUT 

Endpoint : /marcas/<id>/editar

Cuerpo de la solicitud: 
```json
    {
    "nombre":"dato a actualizar, si se desea",
    }
```
Respuesta:
```json
{
  "200  OK": "La marca esta editada con éxito"
}
```
Mensajes de error:   
    `403 Forbidden`: Solo el administrador puede eliminar marcas.  
    `404 Not found`:Marca no encontrada.  
    `500 Internal Server Error`: Error al eliminar la marca.



#### ACCESORIOS: 

#### MÉTODO GET (para obtener lista de accesorios)
Endpoint: /accesorios_list

Respuesta:

{
  "accesorios": [
    {
      "id": 1,
      "nombre": "Accesorio 1"
    },
    {
      "id": 2,
      "nombre": "Accesorio 2"
    }
  ]
}
##### MÉTODO POST: 

Endpoint : /accesorios

Cuerpo de la solicitud: 
```json
    {
    "nombre":"Nombre del accesorio a crear"
    }
```
Respuesta: 
```json
    {
     "201 Created": "Accesorio creado exitosamente"
    }
```
Mensaje de error:
```json 
{
    "403 Forbidden": "No está autorizado para crear accesorios"
}
```

##### MÉTODO PUT: 
Endpoint : /accesorios/<id>/editar

Respuesta: 
```json
{
  "200 OK":"El accesorio esta editado con éxito"
}
```
Mensaje de error: 
```json
{
    "403 Forbidden": "No está autorizado para editar accesorio."
}
```

##### MÉTODO DELETE: 
Endpoint : /accesorio/ID del accesorio a editar/delete

Respuesta: 
```json
{
  "200 OK":"Accesorio eliminado correctamente"
}
```
Mensaje de error: 
```json
{
    "403 Forbidden": "Solo el administrador puede eliminar accesorios"
}
```


##### MÉTODO GET: 

Endpoint : /accesorios

Respuesta: 
```json
{
  "200 OK": {
    "accesorios": [
      {
        "id": 1,
        "nombre": "Cargador Samsung"
      },
      {
        "id": 3,
        "nombre": "Funda Apple original"
      },
      ...
    ]
  }
}
```

#### CELULAR: 


##### MÉTODO POST: 


Endpoint: /celulares

Cuerpo de la solicitud: 
```json
    {
  "modelo": "Galaxy S20",
  "anio_fabricacion":"2023",
  "precio":"5000000",
  "marca":1, // ID de la marca
    }
```


##### MÉTODO GET: 


Endpoint: /celulares_list

Respuesta: 
```json
{
  "201 OK": {
    "accesorios": [
      [
        1,
        "Cargador Samsung"
      ],
      [
        3,
        "Funda Apple original"
      ],
      [
        4,
        "Cargador Apple"
      ]
    ],
    "marcas": [
      [
        1,
        "Samsumg"
      ],
      [
        2,
        "Apple"
      ],
      [
        3,
        "Motorola"
      ],
      [
        4,
        "Nokia"
      ],
      [
        5,
        "BlackBerry"
      ],
      [
        6,
        "Xiaomi"
      ],
      [
        7,
        "TCL"
      ],
      [
        8,
        "LG"
      ],
      [
        9,
        "Sony"
      ],
      [
        10,
        "ZTE"
      ],
      [
        11,
        "Oppo"
      ],
      [
        12,
        "Otra"
      ]
    ],
    "celulares": [
      {
        "anio_fabricacion": 2023,
        "id": 1,
        "marca": {
          "id": 1,
          "nombre": "Samsumg"
        },
        "modelo": "Galaxy S20",
        "precio": 5000000,
        "tipo": {
          "id": 1,
          "nombre": "Gama alta"
        }
      }
    ],
  }
}
```


