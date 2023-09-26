Hemos entendido como generalidad que Python es un lenguaje interpretado. Interpretado significa que no hay un proceso de compilación que traduzca el código fuente a algún código nativo que entienda tu computadora. La documentación de Python confirma esto, pero también menciona la presencia de un compilador:

"Python es un lenguaje interpretado, a diferencia de los compilados, aunque la distinción puede ser borrosa debido a la presencia del compilador de bytecode".

Tenemos un compilador, pero de bytecode. El bytecode es un código intermedio, generalmente independiente del sistema operativo. Entonces, ¿Python también es un lenguaje compilado? En 2003, Fredrik Lundh, en su artículo "Compiling Python Code" (Compilación de código Python), comienza de la siguiente manera:

"El código fuente de Python se compila automáticamente en bytecode de Python por el intérprete CPython. El código compilado se almacena generalmente en archivos PYC (o PYO) y se regenera cuando el código fuente se actualiza o cuando es necesario".

Entonces, ¿Python es un lenguaje interpretado o compilado? ¿Ambas cosas? Hay acalorados debates entre los desarrolladores, cada uno con su propia opinión. Una respuesta interesante se encuentra en Stack Overflow, de hecho, es la respuesta más valorada:

"En primer lugar, interpretado/compilado no es una propiedad del lenguaje, sino una propiedad de la implementación (...) Python es compilado. No se compila previamente al código de máquina (es decir, "compilado" según la definición restringida y equivocada, pero también común), solo se compila al bytecode".

Esto significa que alguien podría implementar Python completamente compilado, completamente interpretado o ambos, el lenguaje sigue siendo el mismo. Ser compilado/interpretado es más una propiedad de la implementación de Python que del lenguaje en sí.
