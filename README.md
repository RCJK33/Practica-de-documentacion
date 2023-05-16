# Tabla Hash para Python
Las ***tablas hash*** son utilies para alamacenar grandes cantidades de datos y necesitamos tener un acceso mas rapido y eficiente que los algoritmos de busqueda convencionales.

## Contenido
- [Clase HashTable](#clase-hashtable)
	- [Crear una HashTable](#crear-una-hashtable)
	- [Metodos de la clase HashTable](#metodos-de-la-clase-hashtable)
- [Clase HashElement](#clase-hashelement)

## Clase HashTable
La **tabla hash** alamcena en una arreglo de arreglos, es decir, en una matriz, una ***k*ey** y un **objeto asociado** a la llave en forma de una estructura de tipo **HashElement**, dicha llave no se puede repetir dentro de la tabla.

Para mas infomracion de **HashElement** ir a la seccion [HashElement](#clase-hashelement).

### Crear una HashTable
Para crear una **tabla hash** basta con crear una instancia de la clase de la siguiente manera:

<pre><code>
HashList = HashTable()
	</code></pre>

EL constructor de la clase **HashTable** puede tener 3 parametros descritos a continuacion:

`HashTable(`[length](#param2)`,`[magic_number](#param2)`)`

|No.|parametro|Descripcion|Tipo
|:-:|:-|:-|:-:|
|1|<p id="param1">`length`</p>|Este parametro define el tamaño que tiene la tabla, entre mas grande sea, habra menor numero de colisiones. Se recomienda que este numero debe ser un numero primo.|Entero
|2|<p id="param2">`magic_number`</p>|Este numero sirve para dar una razon de cambio en la ecuacion de la funcion Hash. Pruebe numeos primos relativos a el length. Se recomienda dejar por defecto o usar el numero 1 o 2.|Entero

### Metodos de la clase HashTable
Las tablas hash vienen acompañadas de metodos que permiten manipular la **HashTable** y modificar su contenido.

A continuacion se describen los metodos en una tabla:

**- Metodos publicos -** 
|Nombre|Retorno|Descripcion|
|:-|:-:|:-|
|`containsKey(`**Key**`)`|**True** o **False**|Verifica si la key de tipo **str** existe en la *HashTable*, si es asi, retorna **True**.|
|`add(`**Key**`,`**object**`)`|--|Almacena en la *HashTable* un objeto asociado con la llave de tipo **str**.|
|`put(`**Key**`,`**object**`)`|--|Almacena en la *HashTable* un objeto asociado con la llave de tipo **str** si este ya existe lo reemplazará.|
|`get(`**Key**`)`|**Object** o **None**|Retorna el objeto asociado con la llave de tipo **str** almacendao en la *HashTable*, si este no existe, retornara **None**|
|`remove(`**Key**`)`|--|Elimina en el objeto asociado con la llave de tipo **str** en la *HashTable*, si este no existe, no hará nada|
|`printHashTable()`|--|Mostrara en pantalla todo el contenido de la tabla sin importar si es un indice vacio.|

**- Metodos privados -** 
|Nombre|Retorno|Descripcion|
|:-|:-:|:-|
|`__hash__(`**key**`)`|**int**|Codifica la *key* de tipo **str** en algun numero y retorna el indice en funcion del tamaño de la *HashTable*.|
|`__returnSubIndexByKey(`**key**`)`|**int**|Retorna un sub indice en el que se encuentra el elemento asociado con la *key*.|

## Clase HashElement
La tabla hash alamacena una estructura de tipo **HashElement** que contiene 2 atributos descritos a continuacion:

|Atributo|Tipo|Descripcion|
|:-:|:-:|:-|
|`key`|**str**|Es la llave asociada al elemento almacenado y que es unica en toda *[HashTable](#clase-hashtable)*.|
|`object`|**object**|Es el elemento que se encuentra asociado a la llave de la *[HashTable](#clase-hashtable)*. Dicho elemento puede ser una instancia de cualquier clase o tipo de dato.|