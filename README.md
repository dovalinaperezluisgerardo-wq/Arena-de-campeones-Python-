# ⚔️ Arena de Campeones

Videojuego RPG de combate y exploración desarrollado en Python.

El jugador puede elegir entre diferentes clases, combatir enemigos, explorar el Castillo del Abismo, conseguir oro, comprar armas, utilizar pociones, subir de nivel, conseguir llaves y enfrentarse a un jefe final.

El proyecto fue desarrollado como práctica de Programación Orientada a Objetos (POO), utilizando herencia, polimorfismo, manejo de archivos JSON, estructuras de datos y generación de eventos aleatorios.

---

## 🎮 Características

- ⚔️ Sistema de combate por turnos
- 🧙 3 clases jugables
- ⚔️ Guerrero
- 🏹 Arquero
- 🔮 Mago
- 👹 Diferentes tipos de enemigos
- 👑 Jefes finales diferentes según la clase
- 📈 Sistema de niveles y experiencia
- 💰 Sistema de oro
- 🏪 Tienda
- 🎒 Inventario
- ⚔️ Sistema de armas
- 💚 Sistema de pociones
- 🗝️ Sistema de llaves
- 🏰 Exploración del Castillo del Abismo
- 🌳 Jardín
- 📚 Biblioteca
- 💰 Sala del Tesoro
- 🧩 Acertijos
- 👤 NPCs
- 💚 Sistema de afinidad
- 🎲 Eventos aleatorios
- 📦 Cofres
- ⚠️ Trampas
- 💾 Guardado y carga mediante JSON
- 🗺️ Sistema de mapa
- 📊 Escalado de enemigos según el nivel del jugador

---

## 🧠 Tecnologías utilizadas

- Python 3
- Programación Orientada a Objetos
- Herencia
- Polimorfismo
- Clases y objetos
- Listas
- Diccionarios
- Funciones
- JSON
- Manejo de archivos
- Random
- Time
- OS

---

## 📂 Estructura del proyecto

Actualmente el proyecto está desarrollado principalmente en un archivo:

Arena-de-Campeones/
│
├── Video juego.py
├── README.md
├── .gitignore




---

## ▶️ Cómo ejecutar

Necesitas tener instalado Python 3.

Desde la terminal puedes ejecutar:

    python "Video juego.py"

En algunos sistemas puede ser necesario utilizar:

    python3 "Video juego.py"

El nombre del archivo contiene un espacio, por lo que se recomienda utilizar comillas.

---

# 🎮 Cómo jugar

Al comenzar una partida puedes elegir entre tres clases.

## ⚔️ Guerrero

Especializado en fuerza y combate cuerpo a cuerpo.

Características:

- Alta vida
- Alta fuerza
- Ataques con espada
- Ataque especial Corte Celestial

## 🏹 Arquero

Especializado en velocidad y ataques a distancia.

Características:

- Alta velocidad
- Ataques con arco
- Ataque especial Flecha Carmesí

## 🔮 Mago

Especializado en ataques mágicos.

Características:

- Alta fuerza
- Ataques mágicos
- Ataque especial Eclipse Oscuro

---

# ⚔️ Sistema de combate

Los combates funcionan por turnos.

Durante el turno del jugador se pueden realizar diferentes acciones:

    1. Atacar
    2. Ataque Especial
    3. Beber poción
    4. Huir

No todos los enemigos permiten escapar.

Los enemigos cuentan con inteligencia básica y pueden:

- Atacar
- Usar ataques especiales
- Recuperar vida
- Huir cuando está permitido

---

# 📈 Sistema de niveles

El jugador obtiene experiencia al derrotar enemigos.

Cuando alcanza la experiencia necesaria:

- Aumenta de nivel
- Aumenta la fuerza
- Aumenta la velocidad
- Aumenta la vida máxima
- Recupera completamente la vida

La experiencia necesaria para subir de nivel aumenta progresivamente.

---

# 💰 Sistema económico

El jugador puede obtener oro mediante:

- Combates
- Cofres
- Pergaminos
- Eventos

El oro puede utilizarse en la tienda para comprar:

- Pociones
- Armas

---

# 🎒 Inventario

El jugador puede almacenar armas y equiparlas.

Cada clase tiene armas diferentes.

## Guerrero

- Espada de hierro
- Espada legendaria

## Arquero

- Arco de roble
- Arco de dragón

## Mago

- Grimorio menor
- Grimorio ancestral

---

# 🏰 Castillo del Abismo

El mapa principal contiene tres pasadizos.

## Pasadizo 1

Contiene una bifurcación con tres zonas:

- Sala del Tesoro
- Jardín
- Biblioteca

## Pasadizo 2

Contiene un cofre protegido por varios enemigos.

## Pasadizo 3

Contiene un enemigo poderoso que entrega una llave.

## Pasadizo Central

Se encuentra bloqueado inicialmente.

Para acceder al jefe final se necesitan las dos llaves.

---

# 📚 Biblioteca

La biblioteca contiene:

- Pergaminos
- Acertijos
- Bibliotecario Maldito
- Una puerta secreta

Después de derrotar al Bibliotecario Maldito se desbloquea una puerta secreta.

---

# 🌳 Jardín

El jardín permite:

- Recuperar toda la vida una vez
- Buscar plantas medicinales
- Obtener pociones
- Hablar con el jardinero
- Encontrar enemigos

El jugador puede encontrar un número limitado de plantas medicinales.

---

# 💰 Sala del Tesoro

La Sala del Tesoro contiene varios cofres.

Los cofres pueden contener:

- Oro
- Pociones
- Armas
- Nada

La sala también está protegida por un Goblin Rey.

---

# 👤 NPCs

El juego cuenta con un sistema básico de afinidad.

Los niveles disponibles son:

    Hostil
    Desconfiado
    Neutral
    Amistoso
    Leal

Actualmente existe un jardinero que utiliza el sistema de NPC y afinidad.

También existen clases preparadas para futuros NPCs:

- Sabio
- Mercader
- Aliado

---

# 💾 Guardado de partida

El juego utiliza JSON para guardar el progreso.

El archivo utilizado es:

    partida.json

Se guardan datos como:

- Clase
- Nombre
- Nivel
- Vida
- Fuerza
- Velocidad
- Oro
- Pociones
- Inventario
- Experiencia
- Llaves
- Enemigos derrotados
- Progreso de los pasadizos
- Biblioteca
- Jardín
- Sala del Tesoro
- Afinidad de NPCs

---

# 🐛 Bugs y problemas conocidos

Esta sección documenta problemas encontrados durante la revisión del código.

Estos problemas forman parte del estado actual del proyecto y pueden utilizarse como tareas para futuras contribuciones.

## 🔴 Prioridad alta

### 1. `aplicar_nivel()` mezcla dos responsabilidades

El método:

    aplicar_nivel()

calcula las estadísticas del personaje pero también establece:

    self.vida = self.max_vida

Esto significa que cada vez que se llama `aplicar_nivel()`, la vida se restaura completamente.

Esto puede producir comportamientos inesperados cuando se utiliza el método para modificar estadísticas sin intención de curar al personaje.

Sería recomendable separar:

    actualizar_estadisticas()

de:

    restaurar_vida()

---

### 2. El escalado de enemigos también restaura su vida

La función:

    escalar_enemigo()

llama a:

    enemigo.aplicar_nivel()

Como `aplicar_nivel()` restaura la vida, el escalado también reinicia la vida del enemigo.

Actualmente normalmente se ejecuta antes del combate, pero puede convertirse en un problema si el sistema se modifica posteriormente.

---

### 3. Los enemigos pueden curarse indefinidamente

Los enemigos pueden elegir:

    recuperarte

y utilizar:

    enemigo.curacion_enemiga()

No existe un límite de curaciones.

Esto puede provocar combates demasiado largos o difíciles de terminar.

Una posible solución sería establecer:

    max_curaciones

o un número limitado de usos por combate.

---

### 4. El jugador puede gastar una poción con la vida completa

Actualmente el jugador puede elegir:

    3) Beber poción

aunque tenga:

    vida == max_vida

La poción se consume aunque la curación real sea 0.

Sería mejor impedirlo y mostrar un mensaje indicando que la vida ya está completa.

---

### 5. El sistema de enemigos derrotados utiliza clases

El juego guarda enemigos derrotados mediante:

    type(enemigo)

Esto significa que se registra la clase del enemigo y no una instancia específica.

Por ejemplo, si se derrota un enemigo de determinada clase, esa clase puede considerarse derrotada aunque posteriormente existan otras instancias del mismo tipo.

Esto puede causar problemas si el juego incorpora múltiples enemigos del mismo tipo en diferentes zonas.

Sería mejor utilizar identificadores únicos para enemigos o eventos específicos del mapa.

---

### 6. Posible pérdida de progreso si cambia la estructura del JSON

El sistema carga información desde:

    partida.json

Si el formato del archivo cambia en futuras versiones, las partidas antiguas pueden dejar de funcionar correctamente.

Aunque existen algunos valores predeterminados mediante `.get()`, no todos los campos tienen migraciones compatibles.

Sería recomendable implementar versiones del formato de guardado.

Ejemplo:

    "save_version": 1

---

## 🟠 Prioridad media

### 7. Una partida guardada sobrescribe la anterior

El método `guardar()` utiliza:

    open("partida.json", "w")

Esto reemplaza completamente el archivo anterior.

Actualmente solamente existe una partida guardada.

Una mejora futura sería permitir:

- Múltiples partidas
- Diferentes archivos de guardado
- Copias de seguridad

---

### 8. El archivo `partida.json` debería estar en `.gitignore`

El archivo contiene datos de una partida local.

No debería formar parte del repositorio.

Se recomienda agregar:

    partida.json

al `.gitignore`.

---

### 9. El nombre del archivo principal contiene un espacio

Actualmente:

    Video juego.py

Funciona correctamente, pero puede ser menos cómodo para terminales y herramientas externas.

Una alternativa más habitual sería:

    video_juego.py

No es un bug funcional.

Es principalmente una mejora de organización.

---

### 10. El jugador comienza directamente en nivel 3

El código contiene:

    jugador.nivel = 3

Esto puede ser intencional, pero significa que el jugador no experimenta los niveles 1 y 2.

Si se desea una progresión RPG tradicional, sería mejor iniciar en nivel 1.

---

### 11. Los enemigos pequeños pueden quedar demasiado débiles

Algunos enemigos utilizan:

    nivel_jugador - 2

para su escalado.

La función limita el resultado mínimo a nivel 1, pero cuando el jugador alcanza niveles altos puede existir una diferencia importante entre las estadísticas del jugador y las del enemigo.

Esto puede hacer que determinados encuentros pierdan dificultad.

---

### 12. Los enemigos pueden recuperar vida aunque estén cerca de su vida máxima

La curación se limita mediante:

    if self.vida > self.max_vida:
        self.vida = self.max_vida

No rompe el juego, pero puede provocar turnos poco útiles para la IA.

Podría añadirse una condición para que el enemigo solo se cure cuando tenga un porcentaje determinado de vida.

---

### 13. No existe defensa o reducción de daño

Actualmente el daño recibido se resta directamente:

    self.vida -= fuerza

No existen estadísticas como:

- Defensa
- Armadura
- Resistencia mágica

Esto limita la profundidad del sistema de combate.

---

### 14. No existe probabilidad de golpe crítico

Todos los ataques tienen un resultado prácticamente determinista según las estadísticas.

Una mejora futura sería implementar:

- Probabilidad crítica
- Daño crítico
- Evasión
- Precisión

---

### 15. Las armas modifican directamente el atributo de ataque

El sistema utiliza:

    setattr(self, self.atributo_arma, poder_nuevo)

Funciona, pero hace que las armas dependan directamente de atributos específicos como:

    espada
    arco
    libro

Un sistema de objetos más independiente podría hacer que las armas tengan sus propias estadísticas.

---

# 🟡 Problemas de arquitectura y mantenimiento

### 16. El archivo principal es demasiado grande

Actualmente gran parte del juego se encuentra en:

    Video juego.py

A medida que el proyecto crezca será difícil mantenerlo.

Una posible estructura futura sería:

    Arena-de-Campeones/
    │
    ├── main.py
    ├── personajes.py
    ├── enemigos.py
    ├── combate.py
    ├── escenarios.py
    ├── inventario.py
    ├── tienda.py
    ├── guardado.py
    ├── npcs.py
    ├── datos.py
    └── README.md

---

### 17. Existe código repetido entre clases

Varias clases de enemigos tienen estructuras similares para:

    Ataque()

y:

    ataque_especial()

A medida que aumente el número de enemigos, mantener este código será más complicado.

Podría crearse una arquitectura de enemigos más configurable.

---

### 18. Los nombres de métodos no siguen completamente PEP 8

Actualmente existen métodos como:

    Ataque()
    Daño_Recibido()
    Saludo()

La convención habitual de Python utiliza:

    ataque()
    dano_recibido()
    saludo()

Esto no provoca un error funcional, pero mejora la legibilidad y el estándar profesional del código.

---

### 19. El sistema de NPC está parcialmente implementado

Existen clases:

    Sabio
    Mercader
    Aliado

pero actualmente no todas tienen una función real dentro del mundo.

Esto puede considerarse código preparado para futuras características.

---

### 20. La afinidad de NPC tiene pocas consecuencias

La afinidad actualmente cambia entre:

    Hostil
    Desconfiado
    Neutral
    Amistoso
    Leal

Sin embargo, todavía existen pocas consecuencias jugables.

Podría ampliarse para permitir:

- Descuentos
- Misiones
- Recompensas
- Información secreta
- Nuevas rutas
- Ayuda durante combates

---

# 🧪 Pruebas recomendadas

Antes de considerar estable una versión futura se recomienda probar:

- Crear una partida nueva.
- Elegir Guerrero.
- Elegir Arquero.
- Elegir Mago.
- Combatir enemigos.
- Ganar combates.
- Perder combates.
- Intentar huir.
- Intentar huir de enemigos que no permiten escapar.
- Utilizar pociones.
- Utilizar una poción con vida completa.
- Intentar utilizar una poción sin tener ninguna.
- Comprar armas.
- Comprar una misma arma dos veces.
- Comprar sin suficiente oro.
- Equipar armas.
- Abrir cofres.
- Abrir todos los cofres de la sala.
- Encontrar plantas.
- Intentar encontrar más plantas después del límite.
- Descansar en el jardín.
- Intentar descansar dos veces.
- Resolver el acertijo correctamente.
- Resolver el acertijo incorrectamente.
- Derrotar al Bibliotecario Maldito.
- Entrar a la puerta secreta.
- Conseguir las dos llaves.
- Intentar entrar al jefe sin las dos llaves.
- Entrar al jefe final.
- Derrotar al jefe final.
- Guardar partida.
- Cerrar el programa.
- Cargar partida.
- Cargar un JSON corrupto.
- Cargar un JSON incompleto.
- Modificar manualmente el JSON.
- Introducir letras donde se esperan números.
- Introducir números fuera del rango permitido.

---

# 🚀 Mejoras futuras

- Separar el proyecto en varios módulos.
- Crear un sistema de misiones.
- Agregar más NPCs.
- Agregar más enemigos.
- Agregar más jefes.
- Agregar más zonas del castillo.
- Crear más armas.
- Crear más objetos.
- Crear habilidades especiales.
- Añadir efectos de estado.
- Añadir críticos.
- Añadir defensa.
- Añadir evasión.
- Mejorar la inteligencia artificial de los enemigos.
- Mejorar el balance de estadísticas.
- Mejorar el sistema de guardado.
- Añadir múltiples partidas guardadas.
- Añadir pruebas automatizadas.
- Mejorar la interfaz de terminal.
- Crear documentación técnica.
- Crear una versión gráfica del juego.

---

# 🤝 Contribuciones

Este proyecto está abierto a sugerencias, correcciones y mejoras.

Si encuentras un bug, proporciona:

1. Descripción del problema.
2. Pasos para reproducirlo.
3. Comportamiento esperado.
4. Comportamiento obtenido.
5. Mensaje de error o traceback, si existe.

También son bienvenidas las contribuciones relacionadas con:

- Combate
- Personajes
- Enemigos
- Exploración
- Inventario
- Tienda
- NPCs
- Guardado
- Balance
- Arquitectura del código

---

# 🎯 Objetivo del proyecto

El objetivo de este proyecto es desarrollar un videojuego RPG utilizando Python y practicar conceptos de programación mediante un proyecto completo.

Los principales conceptos utilizados son:

- Programación Orientada a Objetos
- Herencia
- Polimorfismo
- Encapsulamiento
- Clases
- Objetos
- Listas
- Diccionarios
- Funciones
- Manejo de archivos
- JSON
- Manejo de errores
- Generación aleatoria
- Sistemas de combate
- Sistemas de progresión
- Persistencia de datos

El proyecto seguirá evolucionando con nuevas características y correcciones.

---

# 📌 Estado del proyecto

🟡 En desarrollo

El juego actualmente es funcional, pero todavía existen bugs, aspectos de balance y sistemas que pueden mejorarse.

Las sugerencias, reportes de bugs y contribuciones son bienvenidos.

---

# 👨‍💻 Autor

## Luis Gerardo Dovalina Pérez

Proyecto personal desarrollado como práctica de programación en Python.

---

# 📜 Licencia

Este proyecto utiliza la licencia MIT.