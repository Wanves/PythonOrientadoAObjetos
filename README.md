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
