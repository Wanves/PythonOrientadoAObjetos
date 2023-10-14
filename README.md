Programación Orientada a Objetos
Antes de nada, empecemos con una introducción básica a la Programación Orientada a Objetos POO o OOP en inglés. Se trata de un paradigma de programación introducido en los años 1970s, pero que no se hizo popular hasta años más tarde.

Este modo o paradigma de programación nos permite organizar el código de una manera que se asemeja bastante a como pensamos en la vida real, utilizando las famosas clases. Estas nos permiten agrupar un conjunto de variables y funciones que veremos a continuación.

Cosas de lo más cotidianas como un perro o un coche pueden ser representadas con clases. Estas clases tienen diferentes características, que en el caso del perro podrían ser la edad, el nombre o la raza. Llamaremos a estas características, atributos.

Por otro lado, las clases tienen un conjunto de funcionalidades o cosas que pueden hacer. En el caso del perro podría ser andar o ladrar. Llamaremos a estas funcionalidades métodos.

Por último, pueden existir diferentes tipos de perro. Podemos tener uno que se llama Toby o el del vecino que se llama Laika. Llamaremos a estos diferentes tipos de perro objetos. Es decir, el concepto abstracto de perro es la clase, pero Toby o cualquier otro perro particular será el objeto.

La programación orientada a objetos está basada en 6 principios o pilares básicos:

Herencia
Cohesión
Abstracción
Polimorfismo
Acoplamiento
Encapsulamiento
Motivación
Una vez explicada la programación orientada a objetos puede parecer bastante lógica, pero no es algo que haya existido siempre, y de hecho hay muchos lenguajes de programación que no la soportan.

En parte surgió debido a la creciente complejidad a la que los programadores se iban enfrentando conforme pasaban los años. En el mundo de la programación hay gran cantidad de aplicaciones que realizan tareas muy similares y es importante identificar los patrones que nos permiten no reinventar la rueda. La programación orientada a objetos intentaba resolver esto.

Uno de los primeros mecanismos que se crearon fueron las funciones, que permiten agrupar bloques de código que hacen una tarea específica bajo un nombre. Algo muy útil ya que permite también reusar esos módulos o funciones sin tener que copiar todo el código, tan solo la llamada.

Las funciones resultaron muy útiles, pero no eran capaces de satisfacer todas las necesidades de los programadores. Uno de los problemas de las funciones es que sólo realizan unas operaciones con unos datos de entrada para entregar una salida, pero no les importa demasiado conservar esos datos o mantener algún tipo de estado. Salvo que se devuelva un valor en la llamada a la función o se usen variables globales, todo lo que pasa dentro de la función queda olvidado, y esto en muchos casos es un problema.

Imaginemos que tenemos un juego con naves espaciales moviéndose por la pantalla. Cada nave tendrá una posición (x,y) y otros parámetros como el tipo de nave, su color o tamaño. Sin hacer uso de clases y POO, tendremos que tener una variable para cada dato que queremos almacenar: coordenadas, color, tamaño, tipo. El problema viene si tenemos 10 naves, ya que nos podríamos juntar con un número muy elevado de variables. Todo un desastre.

En el mundo de la programación existen tareas muy similares al ejemplo con las naves, y en respuesta a ello surgió la programación orientada a objetos. Una herramienta perfecta que permite resolver cierto tipo de problemas de una forma mucho más sencilla, con menos código y más organizado. Agrupa bajo una clase un conjunto de variables y funciones, que pueden ser reutilizadas con características particulares creando objetos.
Python orientado a objetos se refiere a la capacidad del lenguaje de programación Python para soportar y facilitar la programación orientada a objetos (POO). La programación orientada a objetos es un paradigma de programación que se basa en la creación y manipulación de objetos, que son instancias de clases.

En Python, una clase es una plantilla para la creación de objetos. Define las propiedades (atributos) y comportamientos (métodos) que tendrán los objetos creados a partir de ella. Por ejemplo, si estuviéramos creando un programa para gestionar cuentas de banco, podríamos tener una clase llamada `Cuenta` que tendría atributos como número de cuenta, titular y saldo, y métodos como depositar, retirar, etc.

Python proporciona un conjunto de características que facilitan la programación orientada a objetos, incluyendo la encapsulación (ocultamiento de la información), la herencia (la capacidad de una clase de heredar atributos y métodos de otra), el polimorfismo (la capacidad de una clase de comportarse de múltiples maneras) y la abstracción (la capacidad de representar conceptos complejos de manera más simple).

Gracias a estas características, Python es un lenguaje flexible y poderoso para la programación orientada a objetos, permitiendo a los programadores organizar y estructurar su código de manera más eficiente y modular. Esto facilita la reutilización de código y el desarrollo de aplicaciones más escalables y mantenibles.
Hemos entendido como generalidad que Python es un lenguaje interpretado. Interpretado significa que no hay un proceso de compilación que traduzca el código fuente a algún código nativo que entienda tu computadora. La documentación de Python confirma esto, pero también menciona la presencia de un compilador:

"Python es un lenguaje interpretado, a diferencia de los compilados, aunque la distinción puede ser borrosa debido a la presencia del compilador de bytecode".

Tenemos un compilador, pero de bytecode. El bytecode es un código intermedio, generalmente independiente del sistema operativo. Entonces, ¿Python también es un lenguaje compilado? En 2003, Fredrik Lundh, en su artículo "Compiling Python Code" (Compilación de código Python), comienza de la siguiente manera:

"El código fuente de Python se compila automáticamente en bytecode de Python por el intérprete CPython. El código compilado se almacena generalmente en archivos PYC (o PYO) y se regenera cuando el código fuente se actualiza o cuando es necesario".

Entonces, ¿Python es un lenguaje interpretado o compilado? ¿Ambas cosas? Hay acalorados debates entre los desarrolladores, cada uno con su propia opinión. Una respuesta interesante se encuentra en Stack Overflow, de hecho, es la respuesta más valorada:

"En primer lugar, interpretado/compilado no es una propiedad del lenguaje, sino una propiedad de la implementación (...) Python es compilado. No se compila previamente al código de máquina (es decir, "compilado" según la definición restringida y equivocada, pero también común), solo se compila al bytecode".

Esto significa que alguien podría implementar Python completamente compilado, completamente interpretado o ambos, el lenguaje sigue siendo el mismo. Ser compilado/interpretado es más una propiedad de la implementación de Python que del lenguaje en sí.
