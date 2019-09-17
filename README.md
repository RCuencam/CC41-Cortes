# Complejidad Algorítmica
## Trabajo Parcial
### Seción CC41 - Tema: Problema de corte y empaquetamiento 2D
### Integrantes:

* Claudia
* Rodrigo
* Joaquín Aguirre

### INTRODUCCIÓN

Nuestro proyecto se basa en encontrar la solución a un problema sobre optimización de espacios. Para este proyecto estaremos implementando los algoritmos de: Fuerza Bruta, Backtracking y Divide y Vencerás. Lo que se espera de este proyecto es comparar los algoritmos implementados y analizar la eficencia de cada uno de ellos en la problemática presentada.

### PROBLEMA

(Cando se quiere trabajar con grandes cantidades de datos, se necesita acceder a determinada información de forma rápida eficiente, veloz y consumiendo la menor cantidad de recursos posibles. Esto representa un problema considerable en la mayoría de proyectos de software destinados a un gran público o empresas con un gran número de clientes.  
En el proceso de desarrollo de software, una de las partes más importantes es que sea escalable conservando la usabilidad y los tiempos de carga. Para que nuestro programa cumpla con los requisitos establecidos se deberá crear una estructura capaz de soportar un millón de datos y ser capaz de ubicar, indexar y mostrar los datos en tiempo logarítmico.) 


### OBJETIVOS

**Objetivo General:** 
- Al finalizar el curso,el estudiante genera distintos algoritmos de corte y empaquetamiento basándose en técnicas tales como Fuerza Bruta, Divide-y-Vencerás y BackTracking teniendo en cuenta las restricciones impuestas en clases.

**Objetivos Específicos:**
1. **Crear** algoritmos que solucione el problema de cortes y empaquetamientode con distintos métodos por integrante.
2. **Implementar una interfaz** que le permita al usuario ingresar los datos necesarios y que el programa sea capaz de mostrar  los distintos resultados o implementar la posibilidad de ueasr archivos para la carga y escritura de estos.
3. **Hallar** la complejidad de los algoritmos propuestos.
4. **Generar** archivos de entrada, siguiendo el formato establecido
5. **Analizar** la eficiencia de las soluciones mediante:
- Porcentaje de desperdicio para el empaquetamiento y número de cortes (para los recortes)
- Tablas de comparación: tiempo de ejecución de algoritmo vs entrada de datos, memoria consumida por algoritmo vs entrada de datos 
6. **Presentar**  conclusiones finales en función de los datos levantados en el punto anterior.

### MARCO CONCEPTUAL

#### FUERZA BRUTA

En informática, la búsqueda por fuerza bruta es una técnica trivial pero muy usada, que consiste en enumerar sistemáticamente todos los posibles candidatos para la solución de un problema, con el fin de chequear si dicho candidato satisface la solución al mismo.

Por ejemplo, un algoritmo de fuerza bruta para encontrar el divisor de un número natural n consistiría en enumerar todos los enteros desde 1 hasta n, chequeando si cada uno de ellos divide n sin generar resto. Otro ejemplo de búsqueda por fuerza bruta, en este caso para solucionar el problema de las ocho reinas (posicionar ocho reinas en el tablero de ajedrez de forma que ninguna de ellas ataque al resto), consistiría en examinar todas las combinaciones de posición para las 8 reinas (en total 64! /56! = 178.462.987.637.760 posiciones diferentes), comprobando en cada una de ellas si las reinas se atacan mutuamente.

La búsqueda por fuerza bruta es sencilla de implementar y, siempre que exista, encuentra una solución. Sin embargo, su coste de ejecución es proporcional al número de soluciones candidatas, el cual es exponencialmente proporcional al tamaño del problema. Por el contrario, la búsqueda por fuerza bruta se usa habitualmente cuando el número de soluciones candidatas no es elevado, o bien cuando éste puede reducirse previamente usando algún otro método heurístico.

Es un método utilizado también cuando es más importante una implementación sencilla que una mayor rapidez. Este puede ser el caso en aplicaciones críticas donde cualquier error en el algoritmo puede acarrear serias consecuencias; también es útil como método "base" cuando se desea comparar el desempeño de otros algoritmos metaheurísticos. La búsqueda de fuerza bruta puede ser vista como el método metaheurístico más simple.

La búsqueda por fuerza bruta no se debe confundir con backtracking, método que descarta un gran número de conjuntos de soluciones, sin enumerar explícitamente cada una de las mismas.


#### BACKTRACKING



#### DIVIDE Y VENCERÁS


