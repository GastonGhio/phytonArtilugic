
"""
Secuencia de escape Significado
-\n Nueva línea (new line). El cursor pasa a la primera posición de la línea siguiente.
-\t Tabulador. El cursor pasa a la siguiente posición de tabulación.
-\\ Barra diagonal inversa
-\v Tabulación vertical.
\ooo Carácter ASCII en notación octal.
\xhh Carácter ASCII en notación hexadecimal.
\xhhhh Carácter Unicode en notación hexadecimal.



Metacaracteres
Metacaracteres - delimitadores
Esta clase de metacaracteres nos permite delimitar dónde queremos buscar los patrones de búsqueda.


Metacaracter Descripción
^ inicio de línea.
$ fin de línea.
\A inicio de texto.
\Z fin de texto.
. cualquier caracter en la línea.
(\b) encuentra límite de palabra.
\B encuentra distinto a límite de palabra


\w un caracter alfanumérico (incluye "_").
\W un caracter no alfanumérico.
\d un caracter numérico.
\D un caracter no numérico.
\s cualquier espacio (lo mismo que [ \t\n\r\f]).
\S un no espacio.


Metacaracter Descripción
(*) cero o más, similar a {0,}.
+ una o más, similar a {1,}.
(?) cero o una, similar a {0,1}.
{n} exactamente n veces.
{n,} por lo menos n veces.
{n,m} por lo menos n pero no más de m veces.
(*?) cero o más, similar a {0,}?.
+? una o más, similar a {1,}?.
(??) cero o una, similar a {0,1}?.
{n}? exactamente n veces.
{n,}? por lo menos n veces.
I N T R O D U C C I O N
MBA Ignacio Urteaga Instituto Da 103 ta Science Argentina
{n,m}? por lo menos n pero no más de m veces.

"""

