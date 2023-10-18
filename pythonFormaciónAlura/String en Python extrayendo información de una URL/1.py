# Parámetros en páginas web
# Método find



# https://www.bytebank.com/cambio?moneda_origen=usd&moneda_destino-cop&cantidad-100&operacion=venta

# https://www.bytebank.com/cambio?moneda_origen=usd
texto = 'abcdef'
url = 'www.bytebank.com/cambio?moneda_origen=usd&moneda_destino-cop&cantidad-100&operacion=venta'

base_url = url[0:url.find('/')]
parametros_url = url[url.find('m')+1:]
print(" ")
print(base_url)
print(" ")
print(" ")
print(f'El valor parametro es: {parametros_url}')
print(" ")
print(f'Valor hasta m: {url.find("m")}')
print(" ")
print(f'Valor de la longitud de url: {len(url)}')
print(" ")
print('cambio' in url, url.find('cambio'))
print(" ")
print(f'El valor donde se encuentra la palabra "{url[17:23]}" es: {url.find("cambio")}')
print(" ")

# for i in range(len(url)):
#     print(f'El valor de i es: {i}')




# Lo que aprendimos en esta aula:

# URLs y sus formatos: cómo funcionan las URLs y qué significa cada parte de una URL, como la base y los parámetros.
# El operador de corte [a:b], utilizado para obtener una subcadena desde el índice a hasta el índice b - 1 de la cadena original. Recordemos que b - 1 porque el segundo argumento del corte es exclusivo.
# La cadena original no se modifica al cortarla debido a su inmutabilidad.

# Aprendimos que podemos utilizar el método find para encontrar el índice de un carácter dentro de una cadena, como en url.find("?"). El método find() es muy flexible y se puede utilizar de varias otras formas, como se muestra en la documentación oficial de Python.

# Según esta documentación, el método find() tiene la siguiente estructura: str.find(sub[, start[, end]]).

# sub es un parámetro obligatorio, que representa la subcadena (substring) que queremos buscar. Esto significa que podemos pasar una cadena (y no necesariamente solo un carácter) para encontrar su índice en la cadena original.

# start es un parámetro opcional; si se proporciona, la búsqueda de sub ocurrirá solo a partir del índice start.

# end también es opcional; si se proporciona, la búsqueda irá hasta el índice end.

# El método str.find(sub) retorna -1 si no se encuentra sub en str.

# Siempre que queramos comprender más sobre algún método o ver qué otros métodos existen, podemos recurrir a la documentación oficial del lenguaje. ¡Recomiendo mucho que experimentes con diferentes formas de usar el método find según las opciones descritas anteriormente!

# Por ejemplo, ¿será que podemos verificar si nuestra variable url contiene el carácter "?" antes de realizar el "corte" (slicing)? (Pista: observa lo que devuelve el método find() si no encuentra la subcadena buscada).

# Lo que aprendimos en esta aula:

# Una cadena es una secuencia de caracteres donde cada carácter tiene su propia posición o índice.
# Podemos omitir el primer o segundo argumento del operador de corte para cortar una cadena desde el principio hasta cierto índice, o desde un índice hasta el final. Por ejemplo: str[a:] o str[:b].
# Podemos utilizar el método str.find(<palabra>, <inicio>) para buscar el índice de una palabra a partir de un índice de inicio.
# Si la palabra no se encuentra, el método find() devuelve -1.
# El método len(<cadena>) devuelve el tamaño (es decir, la cantidad de caracteres) de nuestra cadena.
# Observación: ¡el carácter que representa un espacio en blanco (" ") también cuenta! Por ejemplo, len(" ") devuelve 1.