# Local Image Descriptors

## Ejemplo capítulo 2

El ejemplo del capítulo 2 encuentra la correspondencia de puntos entre dos imágenes utilizando el detector de esquinas de Harris y la correlación cruzada normalizada.

Las imágenes de entrada son dos fotografías de un cuaderno tomadas desde dos posiciones diferentes.

El código inicia calculando el valor de respuesta de Harris para cada pixel de la primera imagen utilizando la función ``compute_harris_response`` con sigma=5. El siguiente paso es escoger los pixeles con un valor de respuesta mayor al umbral (el 20% del valor de respuesta máximo) y que estén separados por una distancia mínima de 51, esto se hace con la función ``get_harris_points``.

Para comparar los puntos seleccionados con los de otra imagen es necesario almacenar los valores alrededor de cada punto, lo cual se hace con la función ``get_descriptor``. Estos parches o recortes servirán como descriptores para los puntos de interés.

Luego se realizan los pasos anteriormente mencionados en la segunda imagen. Con la función ``match_twosided`` se realiza la correlación cruzada normalizada entre cada uno de los parches de la primera imagen y los de la segunda imagen. Los valores más altos del resultado de esta operación permiten encontrar la correspondencia de puntos entre las dos imágenes.

Los valores de sigma y la distancia mínima entre puntos en el código son más altos que los valores en el ejemplo del libro. Por lo tanto, son menos los puntos que se tienen en cuenta. De esta manera es más fácil evaluar el resultado a simple vista y el tiempo de cómputo es mejor.

El resultado de este algoritmo puede verse en la imagen ``matching_harris.png`` en la carpeta resultados.


## Capítulo 2 ejercicio 2 (ch02-ex1.py)


