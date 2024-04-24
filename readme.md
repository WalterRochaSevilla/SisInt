# Reporte del Proyecto

1. **Nombre completo del autor(a):** {Walter Marcelo Rocha Sevilla}
2. **Breve descripción del proyecto:**
   - ** El proyecto consta de 5 clases sin contar Main**
         - *** corner_piece***
         - *** Cara***
         - *** leer_desde_txt***
         - *** cubo***
         - *** cube_solver***
3. **Requerimientos del entorno de programación:** {en teoría ningun requisito, todo lo programé en un entorno en linea virtializado así que no sabría si tiene un requerimento especial}
4. **Manual de uso:**
    - **Formato de codificación para cargar el estado de un cubo desde el archivo de texto:**
      - El formato de codificación será: [color,color,color,color,color,color,color,color,color],[color,color,color,color,color,color,color,color,color]...
        - donde color será uno entre:
          - blanco
          - rojo
          - azul
          - verde
          - naranja
          - amarillo
    - **Instrucciones para ejecutar el programa:** {en teoría solamente de debe de cambiar la ruta desde main para que el codigo funcione por si solo}
5. **Diseño e implementación:**
    - **Breve descripción del modelo del problema:**
      - Se modeló el cubo como un alista de listas donde se almacena los estados de las 9 "piezas" que existen en cada cara
      - Se utilizó el modelo de Lista de Listas para poder mantener un orden con las caras de modo que dependiendo del color de la pieza central de cada cara se asigna un numiro para la misma
          - blanco:1
          - rojo:2
          - azul:3
          - verde:4
          - naranja:5
          - amarillo:6
      - Se utilizó un modelo de miezas (modelando las 26 posibles piezas legales) de modo que solo existen esas y no puede haber ciertas combinaciones como una "Arista" u "Esquina" que posea más de 1 vez el mismo color o que las caras opuestas (usando el modelo de dado en el que la suma de las caras dan 7 si son opuestas) jamás se encontrarán en una sola pieza, valga decir jamás existirá una pieza como (amarillo, blanco) o (rojo,rojo,verde)
      - Para comprobar si es que una pieza es Legal primero deberemos de crear una pieza siguiendo una logica que está guardada en el archivo creacion de piezas.txt, donde juntando n cantidad de caras donde n:{1-3} se conseguirá formar una pieza, siendo así que la logica implementada es que una pieza se representa por "[]", donde tendrá entre 1 y 3 parentesis que simbolizan una cara de una pieza, de tal manera que se cumple la lógica de(Número de pieza 1-9, Número de cara 1-6), para luego buscar si la pieza está definida en uno de 3 diccionariós teniendo un diccionario de centros, uno de aristas y uno de esquinas (están guardados como "posibles combinaciónes")
    - **Explicación y justificación de algoritmo(s), técnicas, heurísticas seleccionadas:**
      - El algoritmo aplicado es A* con la HEURÍSTICA de la distancia manhattan de una pieza a su posible estado de solución
        - El motivo de estas, es por que fueron sugerencia de la IA
      - Elegí modelar las 26 piezas y guardarlas en un diccionarió ya que lo primero que se me ocurrió al ver que teniamos un universo pequeó junto con una cantidad limitada de elementos fu en una HASH SIMPLE (TUAD)
    - **En caso de usar modelos lingüísticos, incluir los prompts clave:**
      - Teniendo una implementacion del cubo rubik del tipo : (mandé mi implementación) ayudame a modelar los posibles movimientos
      - Teniendo una implementacion del cubo rubik del tipo : (mandé mi implementación) ayudame a definir el mejor algoritmo de búsqueda y su Heurística
      - Teniendi en cuenta el siguiente (mandé un pseudocodigó que hice y un pequeño esboze en c++) ayudame a convertirlo a python (No conozco python)
6. **Trabajo Futuro:** 
      - Volver verdaderamente funcional al programa (solo pude implementar lógica basada en mi pseudocódigo)
      - refactorizar bastante parte del codigó
      - me gustaría cambiar el algorítmo de búsqueda por un Alpha-beta, modelando todos los movimientos de un cubo