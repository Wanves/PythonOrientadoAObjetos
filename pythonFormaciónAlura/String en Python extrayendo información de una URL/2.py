import re

url = 'https://www.bytebank.com/cambio?monedaOrigen=usd&monedaDestino=cop&cantidad=100&operacion=venta'
url.find('?')
indice_interrogacion = url.find('?')
base_url = url[:indice_interrogacion]
parametros_url = url[indice_interrogacion + 1:]
print(" ")
print(base_url)
print(" ")
print(parametros_url)
print(" ")

parametro_busqueda = 'operacion'
indice_parametro = parametros_url.find(parametro_busqueda)
indice_valor = indice_parametro + len(parametro_busqueda) + 1

indice_and = parametros_url.find('&', indice_valor)
if indice_and == -1:
    valor = parametros_url[indice_valor:]
else:
    valor = parametros_url[indice_valor:indice_and]
    print(" ")
print(valor)
print(" ")
print('------------------------------')

# url = '   '
# url = url.strip()
# if url == '':
#     print(" ")
#     raise ValueError('La url está vacía')
# print(" ")
# print('-----------------------------------------')
# print(" ")


class Extractor_url:
    def __init__(self, url):
        self.url = self.limpia_url(url)
        self.valida_url()

    def limpia_url(self, url):
        if type(url) == str:
            return url.strip()
        else:
            return ''
        
    def valida_url(self):
        if not self.url:
            raise ValueError('La URL está vacía')

        patron_url = re.compile('(http(s)?://)?(www.)?bytebank.com(.mx)?/cambio')
        match_ = patron_url.match(self.url)
        if not match_:
            print('La url es inválida.')
        
    def get_base(self):
        indice_interrogacion = self.url.find('?')
        base_url = self.url[:indice_interrogacion]
        return base_url

    def get_parametros(self):
        indice_interrogacion = self.url.find('?')
        parametros_url = self.url[indice_interrogacion+1:]
        return parametros_url

    def get_valor_parametros(self, parametro_busqueda):
        parametro_busqueda = parametro_busqueda
        indice_parametro = self.get_parametros().find(parametro_busqueda)
        indice_valor = indice_parametro + len(parametro_busqueda) + 1
        indice_and = self.get_parametros().find('&', indice_valor)
        if indice_and == -1:
            valor = self.get_parametros()[indice_valor:]
        else:
            valor = self.get_parametros()[indice_valor:indice_and]
            print(" ")
        return valor
    
    def __len__(self):
        return len(self.url)
    
    def __str__(self):
        return f'{self.url} Url base: {self.get_base()} Parámetros: {self.get_parametros()}'
    
    def __eq__(self, other):
        return self.url == other.url
        
extractor_url = Extractor_url('https://www.bytebank.com/cambio?monedaOrigen=usd&monedaDestino=cop&cantidad=100&operacion=venta')
extractor_url1 = Extractor_url('https://www.bytebank.com/cambio?monedaOrigen=usd&monedaDestino=cop&cantidad=100&operacion=venta')
valor_parametro = extractor_url.get_valor_parametros('operacion')
print(valor_parametro)

def test(valor):
    if valor:
        print(True)
    else:
        print(False)

print(" ")
test('z')
print(" ")

import re
direccion = 'Calle Cristobal,No. 45, La Loma, 54060-7689'
patron = re.compile('[0-9]{5}[-]?[0-9]{4}')

busqueda = patron.search(direccion)
if busqueda:
    print(" ")
    print(busqueda.group())
    print(" ")

print(len(extractor_url))
print(" ")
print(extractor_url.__str__())
print(" ")
print(extractor_url == extractor_url1)
print(" ")

    
    

# Lo que aprendimos en esta aula:

# Podemos utilizar la palabra clave raise para lanzar una excepción en nuestro programa, informando al usuario qué error ocurrió.
# Más métodos de cadenas: str.replace y str.strip.
# Cómo convertir un código en una clase con atributos y métodos.
# La diferencia entre None, "", 0 y cómo funciona el if en Python.
# El operador not.
# Lo que aprendimos en esta aula:

# Cómo construir y utilizar expresiones regulares, o RegEx, utilizando el módulo re de Python.
# Qué es un match.
# Qué son los cuantificadores e intervalos en RegEx.
# La diferencia entre paréntesis (...) y corchetes [...] en la construcción de patrones.
# Cómo utilizar expresiones regulares para realizar validaciones complejas.
# Lo que aprendimos en esta aula:

# Los métodos especiales son llamados por el propio intérprete de Python de acuerdo con alguna instrucción.
# Cómo implementar métodos especiales en nuestras clases para crear comportamientos personalizados.
# La diferencia entre igualdad (==) e identidad.