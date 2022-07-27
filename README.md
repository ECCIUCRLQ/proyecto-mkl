
# Introducción

Para el proyecto se espera poder crear una simulación de una cámara. El dispositivo se conecta a un puerto PCI virtualmente, mediante el programa SIMICS. Dicho programa es una herramienta que se puede utilizar para desarrollar y simular dispositivos que se conectan a la computadora. Es una forma de emulación que se utiliza generalmente para poder desarrollar software para hardware que aun no está terminado.
El objetivo de la cámara es poder hacer que el dispositivo simule la captura de una imagen y luego se le aplique un filtro.



## Filtros

- Desaturación: A los pixeles se les asignara un valor entre 1 y 0 con respecto a los valores R, G, y B, donde 0 es negro y 1 es blanco.

- Saturación: A cada pixel se le realizara un incremento a los valores R, G, y B basado en un porcentaje de los valores originales.

- Sepia: A los pixeles se les asignara un valor entre 1 y 0 con respecto a los valores R, G, y B, donde 0 es cafe y 1 es amarillo.

- Triste: A todos los pixeles se les incrementará el valor B para poder así crear una imagen más azul.
	
- Invertir colores*

<sub><sup>*No es fijo</sup></sub>
## Conocimientos y Hablidades Blandas
- Trabajo en equipo

- Manejo del tiempo

- Manejo de la incertidumbre

- Comprensión de lectura

- Comprensión de problemas

- Conocimientos técnicos de computadoras

- Conocimientos básicos de ingles

- Conocimientos de programación en c++

- Conocimientos de programación en ensamblador

## Diseño
El proyecto consta de cinco partes: simulación de Simics, implementación del driver en lenguaje C, la implementación de los filtros en lenguaje ensamblador, interfaz de usuario y pruebas de validación.
Para la primera parte se utiliza la herramienta Intel Simics para crear un entorno de hardware. Esto se realizará con el fin de utilizar una conexión PCI en conjunto con la simulación de una dispositivo PCI basado en una cámara fotográfica. La cámara podrá tomar una fotografía y aplicarle diferentes filtros.

La implementación en el lenguaje C consta de:
- Un lente de cámara que simula la captura de una imagen en formato .bmp.

- Un driver que toma dicha fotografía y la envía a post procesamiento para la aplicación de filtros.

- Una interfaz de usuario que permite la visualización de la imagen original y el resultado con los diferentes filtros.

Para la implementación en lenguaje ensamblador se recibe una imagen en formato de un mapa de bits, a este se le puede aplicar uno de varios filtros, devolviendo la imagen de resultado.
Por ultimo se realizarán varias pruebas de usuario mediante un programa de pruebas.

![Diagrama](https://raw.githubusercontent.com/ECCIUCRLQ/proyecto-mkl/main/PI%20-%20Diagrama.jpeg)


## Autores

- Kevin Hernández (B83735)
- Moises Arias (C08789)
- Lucy Camacho (C01544)

