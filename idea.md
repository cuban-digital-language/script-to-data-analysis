- frecuencia de palabras diarias

  - normalizada
  - conjuntos disjuntos en el tiempo

- Palabras correctas

  - Etimologias
  - acepciones
  - frases idemoaticas

- Palabras incorrectas

  - Ingles
  - emojis
  - #
  - @
  - teclado
  - leguaje unisex

- Pipeline:
  get_words -> -emojis (frequency comp.) -> -number words -> -symbols (frequency comp.) -> correct vs errors
  correct (frequency comp.) -> etymology -> exceptions
  errors -> english (frequency comp.) -> # (frequency comp.) -> @ (frequency comp.) -> Neutro -> Teclado
