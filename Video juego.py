import random
import time
import json
import os

def pedir_entero(mensaje, minimo=None, maximo=None):
    while True:
        entrada = input(mensaje).strip()
        try:
            numero = int(entrada)
        except ValueError:
            print("❌ Ingresa un número entero válido.")
            continue
        if minimo is not None and numero < minimo:
            print(f"❌ El número debe ser al menos {minimo}.")
            continue
        if maximo is not None and numero > maximo:
            print(f"❌ El número debe ser máximo {maximo}.")
            continue
        return numero

class Personaje:
    def __init__(self, nombre, vida, fuerza, velocidad, arma, categoria):
        self.nombre = nombre
        self.vida_base = vida
        self.fuerza_base = fuerza
        self.velocidad_base = velocidad
        self.arma = arma
        self.categoria = categoria
        self.derrotados = []
        self.oro = 0
        self.pociones = 2
        self.inventario = []
        self.atributo_arma = None
        self.nivel = 1
        self.experiencia = 0
        self.exp_para_subir = 100
        self.llaves = 0
        self.posicion = "entrada"
        self.pasadizo_1_clase = None
        self.pasadizo_3_clase = None
        self.pasadizo_2_completado = False
        self.pasadizo_1_mundo = None
        self.bibliotecario_derrotado = False
        self.biblioteca_pergamino = False
        self.biblioteca_acertijo = False
        self.tesoro_guardian_derrotado = False
        self.npcs_afinidad = {}
        self.plantas_encontradas = 0
        self.max_plantas = 2
        self.cofres_sala_tesoro = 0
        self.max_cofres_sala_tesoro = 3
        self.descanso_jardin_usado = False
        self.puede_huir = True
        self.aplicar_nivel()

    def aplicar_nivel(self):
        multiplicador = 1 + (self.nivel - 1) * 0.10
        self.fuerza = int(self.fuerza_base * multiplicador)
        self.velocidad = int(self.velocidad_base * multiplicador)
        self.max_vida = int(self.vida_base * multiplicador)
        self.vida = self.max_vida

    def ganar_experiencia(self, cantidad):
        self.experiencia += cantidad
        print(
            f"✨ Ganaste {cantidad} de experiencia. ({self.experiencia}/{self.exp_para_subir})"
        )
        while self.experiencia >= self.exp_para_subir:
            self.experiencia -= self.exp_para_subir
            self.nivel += 1
            self.exp_para_subir = int(self.exp_para_subir * 1.5)
            self.aplicar_nivel()
            print(
                f"🌟 ¡Subiste a NIVEL {self.nivel}! Vida y fuerza aumentaron. Vida restaurada por completo."
            )

    def Ataque(self):
        return self.fuerza

    def Daño_Recibido(self, fuerza):
        self.vida -= fuerza
        if self.vida < 0:
            self.vida = 0

    def ataque_especial(self):
        return self.fuerza + 100

    def Saludo(self):
        print("\n" + "=" * 41)
        print("⚔️ ¡BIENVENIDO A TU PRIMER COMBATE! ⚔️")
        print("=" * 41)
        print("           DATOS DEL PERSONAJE")
        print(
            f"""
             {self.categoria} : {self.nombre}
             Nivel: {self.nivel}
             vida: {self.vida}
             Fuerza: {self.fuerza}
             Velocidad: {self.velocidad}
             arma: {self.arma}"""
        )
        print("=" * 41)

    def curacion(self):
        self.vida += 300
        if self.vida > self.max_vida:
            self.vida = self.max_vida

    def curacion_enemiga(self):
        self.vida += 200
        if self.vida > self.max_vida:
            self.vida = self.max_vida

    def usar_pocion(self):
        if self.pociones <= 0:
            print("\n❌ No te quedan pociones.")
            return
        self.pociones -= 1
        self.curacion()
        print(
            f"\n💚 Usaste una poción mágica. Vida: {self.vida}/{self.max_vida} HP. Pociones restantes: {self.pociones}"
        )

    def ganador(self, enemigo):
        return self.nombre if self.vida > 0 else enemigo.nombre

    def enemigo_turnos(self, enemigo):
        time.sleep(1)
        if enemigo.puede_huir:
            opciones = ["atacar", "ataque_especial", "recuperarte", "huir"]
            probabilidades = [0.50, 0.25, 0.20, 0.05]
        else:
            opciones = ["atacar", "ataque_especial", "recuperarte"]
            probabilidades = [0.55, 0.30, 0.15]

        resultado = random.choices(opciones, weights=probabilidades, k=1)[0]

        time.sleep(1)
        if resultado == "atacar":
            attac = enemigo.Ataque()
            print(f"\n💥¡El {enemigo.categoria} usó Ataque, recibiste {attac} de daño")
            self.Daño_Recibido(attac)
        elif resultado == "ataque_especial":
            attac = enemigo.ataque_especial()
            print(f"\n🔥¡El enemigo usó su super ataque, recibiste {attac} de daño")
            self.Daño_Recibido(attac)
        elif resultado == "recuperarte":
            enemigo.curacion_enemiga()
            print(
                f"\n💚 El {enemigo.categoria} enemigo se curó. Vida actual: {enemigo.vida}/{enemigo.max_vida}"
            )
        elif resultado == "huir":
            print("\n🏳️ ¡Tu enemigo ha huido del combate por miedo!")
            return "huyo"
        time.sleep(1)

    def enemigos_restantes(self):
        todas_las_clases = [Guerrero, Arquero, Mago]
        return [
            cls
            for cls in todas_las_clases
            if not isinstance(self, cls) and cls not in self.derrotados
        ]

    def sistema_de_combates(self, enemigo):
        time.sleep(1)
        adios = False
        while self.vida > 0 and enemigo.vida > 0:
            porcentaje = self.vida / self.max_vida
            llenos = int(porcentaje * 20)
            vacios = 20 - llenos
            porcentaje_evil = enemigo.vida / enemigo.max_vida
            lleno = int(porcentaje_evil * 20)
            vacio = 20 - lleno
            print(f"\n{'='*15} TU TURNO {'='*15}")
            print("\n                ESTADO")
            print("  Tú:    " + "█" * llenos + "░" * vacios)
            print(f"               ❤️{self.vida} HP")
            print("Enemigo: " + "█" * lleno + "░" * vacio)
            print(f"               🖤{enemigo.vida} HP")
            print("-" * 40)
            print(" 1  Atacar")
            print(" 2  Ataque Especial")
            print(f" 3  Beber poción (+300 HP) — Te quedan: {self.pociones}")
            if enemigo.puede_huir:
                print(" 4  Huir")
            print("-" * 35)
            time.sleep(1)
            movimiento = input("👉 Escoge un movimiento (1-4):").strip()

            if movimiento == "1":
                daño = self.Ataque()
                print(f"\n⚔️ ¡Atacas! Daño del ataque: {daño}")
                enemigo.Daño_Recibido(daño)
            elif movimiento == "2":
                daño_max = self.ataque_especial()
                print(f"\n🌟 ¡💥 IMPACTO DIVINO! Super ataque causa {daño_max} de daño")
                enemigo.Daño_Recibido(daño_max)
            elif movimiento == "3":
                self.usar_pocion()
            elif movimiento == "4":
                if not enemigo.puede_huir:
                    print("\n🚫 ¡No puedes huir de este enemigo! Debes enfrentarlo.")
                    continue
                adios = True
                print("\n🏃💨 Has escapado del enemigo con éxito.")
                break
            else:
                print("\n❌ Movimiento Inválido. Intenta de nuevo.")
                continue
            time.sleep(1)
            if enemigo.vida > 0:
                print(f"\n{'='*10} TURNO DEL ENEMIGO {'='*10}")

                resultado_enemigo = self.enemigo_turnos(enemigo)

                if resultado_enemigo == "huyo":
                    print("\n🏁 El enemigo escapó. El combate ha terminado.")
                    time.sleep(1)
                    return "enemigo_huyo"
        print("\n" + "=" * 40)
        if adios:
            print("🏁 El combate ha terminado porque huiste.")
            return "huyo"
        Ganador = self.ganador(enemigo)
        if Ganador == self.nombre:
            print(f"\n🎉 🏆¡VICTORIA! El ganador absoluto🏆 🎉 es: {Ganador.upper()}")
            self.derrotados.append(type(enemigo))
            recompensa_oro = ORO_RECOMPENSA.get(type(enemigo), 50)
            recompensa_exp = EXP_RECOMPENSA.get(type(enemigo), 30)
            self.oro += recompensa_oro
            print(f"💰 Ganaste {recompensa_oro} de oro. Oro total: {self.oro}")
            self.ganar_experiencia(recompensa_exp)
            if getattr(enemigo, "otorga_llave", False):
                self.llaves += 1
                print(f"\n🔑 Obtuviste una llave. Llaves: {self.llaves}/2")
            return "victoria"
        else:
            print(
                f"💀 ¡DERROTA! El ganador es el {Ganador.upper()}. Mejor suerte la próxima.💀"
            )
            return "derrota"

    def menu_post_combate(self):
        time.sleep(1)
        while True:
            print("\n" + "=" * 40)
            print("        ¿QUÉ DESEAS HACER?")
            print(" 1) Continuar explorando")
            print(" 2) Tienda")
            print(" 3) Inventario (equipar arma / poción)")
            print(" 4) Salir")
            print(" 5) Guardar partida")
            print("=" * 40)
            try:
                opcion = input("👉 Elige una opción (1-5): ").strip()
            except EOFError:
                print("Se cerró la entrada del programa.")
                return "salir"

            if opcion == "1":
                return "continuar"
            elif opcion == "2":
                return "tienda"
            elif opcion == "3":
                return "inventario"
            elif opcion == "4":
                return "salir"
            elif opcion == "5":
                self.guardar()
            else:
                print("\n❌ Opción inválida, intenta de nuevo.")
            time.sleep(1)

    def catalogo_tienda(self):
        catalogo = dict(POCIONES)
        armas_de_mi_clase = ARMAS_DISPONIBLES.get(type(self), {})
        catalogo.update(armas_de_mi_clase)
        return catalogo

    def guardar(self):
        datos = {
            "clase": type(self).__name__,
            "nombre": self.nombre,
            "nivel": self.nivel,
            "vida": self.vida,
            "vida_base": self.vida_base,
            "fuerza_base": self.fuerza_base,
            "velocidad_base": self.velocidad_base,
            "oro": self.oro,
            "pociones": self.pociones,
            "inventario": self.inventario,
            "llaves": self.llaves,
            "experiencia": self.experiencia,
            "exp_para_subir": self.exp_para_subir,
            "derrotados": [cls.__name__ for cls in self.derrotados],
            "arma": self.arma,
            "posicion": self.posicion,
            "pasadizo_1_clase": (
                self.pasadizo_1_clase.__name__ if self.pasadizo_1_clase else None
            ),
            "pasadizo_3_clase": (
                self.pasadizo_3_clase.__name__ if self.pasadizo_3_clase else None
            ),
            "pasadizo_2_completado": self.pasadizo_2_completado,
            "bibliotecario_derrotado": self.bibliotecario_derrotado,
            "biblioteca_pergamino": self.biblioteca_pergamino,
            "biblioteca_acertijo": self.biblioteca_acertijo,
            "tesoro_guardian_derrotado": self.tesoro_guardian_derrotado,
            "npcs_afinidad": self.npcs_afinidad,
            "plantas_encontradas": self.plantas_encontradas,
            "cofres_sala_tesoro": self.cofres_sala_tesoro,
            "descanso_jardin_usado": self.descanso_jardin_usado,
        }
        if self.atributo_arma:
            datos["valor_atributo_arma"] = getattr(self, self.atributo_arma)

        try:
            with open("partida.json", "w") as archivo:
                json.dump(datos, archivo, indent=4)
            print("\n💾 Partida guardada correctamente.")
        except (PermissionError, OSError) as e:
            print(f"\n❌ No se pudo guardar aquí (el sistema no lo permite): {e}")

    def comprar(self, nombre_item):
        catalogo = self.catalogo_tienda()
        if nombre_item not in catalogo:
            print("\n❌ Ese artículo no existe en la tienda.")
            return

        item = catalogo[nombre_item]

        if item["tipo"] == "arma" and nombre_item in self.inventario:
            print(f"\n⚠️ Ya posees {nombre_item}. No se cobró de nuevo.")
            return

        if self.oro < item["precio"]:
            print(
                f"\n❌ No tienes suficiente oro. Te faltan {item['precio'] - self.oro} de oro."
            )
            return

        self.oro -= item["precio"]

        if item["tipo"] == "pocion":
            self.pociones += 1
            print(f"\n💰 Compraste una poción. Ahora tienes {self.pociones} pociones.")
        else:
            self.inventario.append(nombre_item)
            print(
                f"\n💰 Compraste {nombre_item} por {item['precio']} de oro. Ve al inventario para equipártela."
            )

    def equipar(self, nombre_arma):
        if nombre_arma not in self.inventario:
            print(f"\n❌ No posees {nombre_arma}. Cómprala primero en la tienda.")
            return
        poder_nuevo = self.catalogo_tienda()[nombre_arma]["poder"]
        setattr(self, self.atributo_arma, poder_nuevo)
        self.arma = nombre_arma
        print(f"\n🗡️ Equipaste {nombre_arma}. Tu poder de ataque ha mejorado.")

    def tienda(self):
        time.sleep(1)
        while True:
            catalogo = self.catalogo_tienda()
            opciones = list(catalogo.keys())
            print("\n" + "=" * 40)
            print(f"🏪 TIENDA — Oro: {self.oro} 💰   Pociones: {self.pociones}")
            print("=" * 40)
            for i, nombre in enumerate(opciones, start=1):
                print(f" {i}) {nombre} — {catalogo[nombre]['precio']} oro")
            print(f" {len(opciones)+1}) Salir de la tienda")

            eleccion = pedir_entero(
                "👉 ¿Qué deseas comprar?: ", minimo=1, maximo=len(opciones) + 1
            )
            if eleccion == len(opciones) + 1:
                break
            self.comprar(opciones[eleccion - 1])

    def generar_jefe_final(self):
        clase_jefe = JEFES_FINALES[type(self)]
        jefe = clase_jefe("El Jefe Final")
        escalar_enemigo(jefe, self.nivel, 2)
        jefe.puede_huir = False
        return jefe

    def inventario_jugador(self):
        while True:
            porcentaje = self.vida / self.max_vida
            llenos = int(porcentaje * 20)
            vacios = 20 - llenos
            print("\n" + "=" * 40)
            print("🎒 INVENTARIO  Tú: " + "█" * llenos + "░" * vacios)
            print(
                f" Nivel: {self.nivel}          ❤️Vida: {self.vida}/{self.max_vida} HP"
            )
            print(f" Oro: {self.oro} 💰            Pociones: {self.pociones}")
            if self.inventario:
                print(" Armas en posesión:")
                for arma in self.inventario:
                    print(f"  - {arma}")
            else:
                print(" (No tienes armas compradas todavía)")
            print(" -----")
            print(" 1) Equipar un arma")
            print(" 2) Beber poción")
            print(" 3) Salir del inventario")
            print("=" * 40)
            time.sleep(1)
            eleccion = pedir_entero("👉 Elige una opción: ", minimo=1, maximo=3)
            if eleccion == 1:
                if not self.inventario:
                    print("\n❌ No tienes armas para equipar.")
                    continue
                nombre_arma = input("   Escribe el nombre exacto del arma: ").strip()
                self.equipar(nombre_arma)
            elif eleccion == 2:
                self.usar_pocion()
            elif eleccion == 3:
                break
            time.sleep(1)

class Guerrero(Personaje):
    def __init__(self, nombre):
        super().__init__(nombre, 1300, 230, 60, "Espada", "Guerrero")
        self.espada = 1.5
        self.atributo_arma = "espada"

    def Ataque(self):
        ataque = self.fuerza * self.espada
        print(f"\n🗡️ El guerrero {self.nombre} atacó ferozmente con su Espada.")
        return int(ataque)

    def ataque_especial(self):
        furia = 1.3
        super_ataque = self.fuerza * self.espada * furia
        print(f"\n✨🗡️ ¡El guerrero {self.nombre} usó su Corte Celestial!")
        return int(super_ataque)

class Arquero(Personaje):
    def __init__(self, nombre):
        super().__init__(nombre, 1100, 130, 80, "Arco", "Arquero")
        self.arco = 2
        self.atributo_arma = "arco"

    def Ataque(self):
        disparo = self.fuerza * self.arco + 100
        print(f"\n🏹 El arquero {self.nombre} soltó su flecha con precisión.")
        return int(disparo)

    def ataque_especial(self):
        flecha_de_fuego = 1.5
        super_ataque = self.fuerza * flecha_de_fuego * self.arco
        print(f"\n🔥🏹 ¡El arquero {self.nombre} disparó su Flecha Carmesí!")
        return int(super_ataque)

class Mago(Personaje):
    def __init__(self, nombre):
        super().__init__(nombre, 1000, 350, 50, "Libro", "Mago")
        self.libro = 140
        self.atributo_arma = "libro"

    def Ataque(self):
        hechizo = self.fuerza + self.libro
        print(f"\n🔮 El mago {self.nombre} lanzó un hechizo elemental.")
        return int(hechizo)

    def ataque_especial(self):
        baston_magico = 1.9
        super_ataque = self.fuerza + self.velocidad * baston_magico
        print(f"\n🌑🔮 ¡El mago {self.nombre} lanzó el Eclipse Oscuro!")
        return int(super_ataque)

class BibliotecarioMaldito(Personaje):
    def __init__(self, nombre="Bibliotecario Maldito"):
        super().__init__(
            nombre, 950, 240, 70, "Libro Maldito", "Bibliotecario Maldito"
        )
        self.libro = 180
        self.atributo_arma = "libro"
        self.puede_huir = False
    def Ataque(self):
        print("\n📚💀 El Bibliotecario Maldito lanza libros embrujados.")
        return self.fuerza + self.libro

    def ataque_especial(self):
        print("\n🕯️📜 ¡El Bibliotecario Maldito invoca pergaminos malditos!")
        return self.fuerza + self.libro + 180

class Goblin(Personaje):
    def __init__(self, nombre="Goblin"):
        super().__init__(nombre, 400, 60, 90, "Daga oxidada", "Goblin")
        self.atributo_arma = None

    def Ataque(self):
        print(f"\n🗡️👺 El Goblin ataca con su daga oxidada.")
        return self.fuerza

    def ataque_especial(self):
        print(f"\n👺💢 ¡El Goblin se lanza con furia!")
        return self.fuerza + 40

class GoblinRey(Personaje):
    def __init__(self, nombre="Goblin Rey"):
        super().__init__(nombre, 900, 150, 70, "Cetro de Guerra", "Goblin Rey")
        self.atributo_arma = None
        self.puede_huir = False

    def Ataque(self):
        print(f"\n👑🗡️ El Goblin Rey golpea con su cetro de guerra.")
        return self.fuerza

    def ataque_especial(self):
        print(f"\n👑💢 ¡El Goblin Rey convoca a su guardia real!")
        return self.fuerza + 70

class Esqueleto(Personaje):
    def __init__(self, nombre="Esqueleto"):
        super().__init__(nombre, 500, 70, 50, "Hueso afilado", "Esqueleto")
        self.atributo_arma = None

    def Ataque(self):
        print(f"\n🦴💀 El Esqueleto golpea con un hueso afilado.")
        return self.fuerza

    def ataque_especial(self):
        print(f"\n💀🌪️ ¡El Esqueleto gira atacando con furia ósea!")
        return self.fuerza + 50

class Planta(Personaje):
    def __init__(self, nombre="Planta Carnívora"):
        super().__init__(nombre, 350, 55, 30, "Espinas", "Planta")
        self.atributo_arma = None

    def Ataque(self):
        print(f"\n🌿 La {self.categoria} te azota con sus espinas.")
        return self.fuerza

    def ataque_especial(self):
        print(f"\n🌿☠️ ¡La {self.categoria} libera esporas tóxicas!")
        return self.fuerza + 30

class Lobo(Personaje):
    def __init__(self, nombre="Lobo Salvaje"):
        super().__init__(nombre, 450, 90, 110, "Garras", "Lobo")
        self.atributo_arma = None

    def Ataque(self):
        print(f"\n🐺 El {self.categoria} muerde con fuerza.")
        return self.fuerza

    def ataque_especial(self):
        print(f"\n🐺💨 ¡El {self.categoria} embiste a toda velocidad!")
        return self.fuerza + 35

class CaballeroOscuro(Personaje):
    def __init__(self, nombre):
        super().__init__(nombre, 2200, 280, 70, "Espada Maldita", "Caballero Oscuro")
        self.espada = 2.0
        self.atributo_arma = "espada"

    def Ataque(self):
        ataque = self.fuerza * self.espada
        print(f"\n🖤⚔️ El Caballero Oscuro ataca con su espada maldita.")
        return int(ataque)

    def ataque_especial(self):
        super_ataque = self.fuerza + 300
        print(f"\n🌑✨ ¡El Caballero Oscuro invoca su Golpe del Vacío!")
        return int(super_ataque)

class Cazador(Personaje):
    def __init__(self, nombre):
        super().__init__(nombre, 1900, 220, 100, "Ballesta Maldita", "Cazador")
        self.arco = 2.8
        self.atributo_arma = "arco"

    def Ataque(self):
        disparo = self.fuerza * self.arco
        print(f"\n🏹🖤 El Cazador dispara con precisión letal.")
        return int(disparo)

    def ataque_especial(self):
        super_ataque = self.fuerza + 280
        print(f"\n👻🏹 ¡El Cazador lanza su Flecha Fantasma!")
        return int(super_ataque)

class Nigromante(Personaje):
    def __init__(self, nombre):
        super().__init__(nombre, 1800, 420, 65, "Cetro de Huesos", "Nigromante")
        self.libro = 260
        self.atributo_arma = "libro"

    def Ataque(self):
        hechizo = self.fuerza + self.libro
        print(f"\n💀🔮 El Nigromante invoca energía necrótica.")
        return int(hechizo)

    def ataque_especial(self):
        super_ataque = self.fuerza + self.velocidad * 1.8 + 200
        print(f"\n☠️🔮 ¡El Nigromante desata su Ritual de la Muerte!")
        return int(super_ataque)

POCIONES = {
    "pocion_de_vida": {"tipo": "pocion", "precio": 50},
}

ARMAS_DISPONIBLES = {
    Guerrero: {
        "espada de hierro": {"tipo": "arma", "poder": 1.8, "precio": 150},
        "espada legendaria": {"tipo": "arma", "poder": 2.2, "precio": 300},
    },
    Arquero: {
        "arco de roble": {"tipo": "arma", "poder": 2.5, "precio": 150},
        "arco de dragon": {"tipo": "arma", "poder": 3.2, "precio": 300},
    },
    Mago: {
        "grimorio menor": {"tipo": "arma", "poder": 200, "precio": 150},
        "grimorio ancestral": {"tipo": "arma", "poder": 320, "precio": 300},
    },
}

ORO_RECOMPENSA = {
    Guerrero: 200,
    Arquero: 150,
    Mago: 180,
    BibliotecarioMaldito: 140,
    Planta: 40,
    Lobo: 55,
    GoblinRey: 160,
}
EXP_RECOMPENSA = {
    Guerrero: 75,
    Arquero: 50,
    Mago: 80,
    BibliotecarioMaldito: 60,
    Planta: 20,
    Lobo: 28,
    GoblinRey: 70,
}

JEFES_FINALES = {
    Guerrero: CaballeroOscuro,
    Arquero: Cazador,
    Mago: Nigromante,
}

CLASES_JUGABLES = {
    "Guerrero": Guerrero,
    "Arquero": Arquero,
    "Mago": Mago,
}

TODAS_LAS_CLASES = {
    "Guerrero": Guerrero,
    "Arquero": Arquero,
    "Mago": Mago,
    "Goblin": Goblin,
    "GoblinRey": GoblinRey,
    "Esqueleto": Esqueleto,
    "Planta": Planta,
    "Lobo": Lobo,
    "CaballeroOscuro": CaballeroOscuro,
    "Cazador": Cazador,
    "Nigromante": Nigromante,
    "BibliotecarioMaldito": BibliotecarioMaldito,
}

AMBIENTE_PASADIZO = [
    "Escuchas gotas de agua cayendo en la oscuridad.",
    "Un frío recorre tu espalda.",
    "Algo se mueve entre las sombras, pero no ves nada.",
    "El silencio es casi absoluto.",
    "Escuchas pasos lejanos... o tal vez es tu imaginación.",
]

# --- NUEVO: escalado de nivel de enemigos ---
def escalar_enemigo(enemigo, nivel_jugador, diferencia):
    enemigo.nivel = max(1, nivel_jugador + diferencia)
    enemigo.aplicar_nivel()
    return enemigo

def abrir_cofre(jugador, contar_cofre=False):
    if contar_cofre:
        if jugador.cofres_sala_tesoro >= jugador.max_cofres_sala_tesoro:
            print("\n📭 Ya no quedan más cofres en esta sala.")
            return

        jugador.cofres_sala_tesoro += 1

    print("\n📦 ¡Encontraste un cofre!")
    resultado = random.choices(
        ["oro", "pocion", "arma", "vacio"], weights=[50, 25, 20, 5], k=1
    )[0]

    if resultado == "oro":
        cantidad = random.randint(30, 120)
        jugador.oro += cantidad
        print(f"💰 El cofre tenía {cantidad} de oro.")
    elif resultado == "pocion":
        jugador.pociones += 1
        print(f"💚 El cofre tenía una poción. Ahora tienes {jugador.pociones}.")
    elif resultado == "arma":
        armas_de_mi_clase = list(ARMAS_DISPONIBLES.get(type(jugador), {}).keys())
        candidatas = [a for a in armas_de_mi_clase if a not in jugador.inventario]
        if candidatas:
            arma_ganada = random.choice(candidatas)
            jugador.inventario.append(arma_ganada)
            print(
                f"⚔️ ¡El cofre tenía un arma especial: {arma_ganada}! Ve al inventario para equipártela."
            )
        else:
            jugador.oro += 100
            print(
                "⚔️ El cofre tenía un arma, pero ya posees todas las de tu clase. Recibiste 100 de oro."
            )
    else:
        print("📭 El cofre estaba vacío.")

def caer_en_trampa(jugador):
    print("\n⚠️ ¡Caíste en una trampa!")
    if random.random() < 0.5:
        daño = random.randint(50, 150)
        oro_perdido = min(jugador.oro, random.randint(20, 80))
        jugador.Daño_Recibido(daño)
        jugador.oro -= oro_perdido
        print(f"🩸 Perdiste {daño} de vida y {oro_perdido} de oro.")
    else:
        enemigo_menor = random.choice([Goblin(), Esqueleto()])
        escalar_enemigo(enemigo_menor, jugador.nivel, -2)
        print(
            f"👹 ¡La trampa era una emboscada! Un {enemigo_menor.categoria} te ataca."
        )
        jugador.sistema_de_combates(enemigo_menor)

def evento_en_pasadizo(jugador):
    resultado = random.choices(
        ["nada", "monstruo", "trampa", "cofre"], weights=[55, 20, 15, 10], k=1
    )[0]
    if resultado == "monstruo":
        enemigo_menor = random.choice([Goblin(), Esqueleto()])
        escalar_enemigo(enemigo_menor, jugador.nivel, -2)
        print(
            f"\n👹 ¡Un {enemigo_menor.categoria} de bajo nivel te embosca en el pasadizo!"
        )
        jugador.sistema_de_combates(enemigo_menor)
    elif resultado == "trampa":
        caer_en_trampa(jugador)
    elif resultado == "cofre":
        abrir_cofre(jugador, contar_cofre=False)

def presentar_jefe_final(jefe):
    print("\n" + "=" * 40)
    print("Mientras avanzas...")
    time.sleep(1)
    print("El castillo comienza a temblar.")
    time.sleep(1)
    print("Las antorchas se apagan.")
    time.sleep(1)
    print("Una enorme puerta negra aparece frente a ti.")
    time.sleep(1)
    print('Sobre ella se puede leer...\n"EL TRONO DEL REY MALDITO"')
    time.sleep(1)
    print("\nHas llegado al final del castillo.")
    print(f"\nJefe Final\n{jefe.categoria.upper()}\nNivel {jefe.nivel}")
    print("=" * 40)

def mostrar_mapa(jugador):
    estado_1 = "✅" if jugador.pasadizo_1_clase in jugador.derrotados else "❌"
    estado_2 = "✅" if jugador.pasadizo_2_completado else "❓"
    estado_3 = "✅" if jugador.pasadizo_3_clase in jugador.derrotados else "❌"

    estado_medio = "🔓 ABIERTO" if jugador.llaves >= 2 else f"🔒 {jugador.llaves}/2"

    nombre_1 = (
        jugador.pasadizo_1_clase.__name__
        if jugador.pasadizo_1_clase in jugador.derrotados
        else "???"
    )
    nombre_3 = (
        jugador.pasadizo_3_clase.__name__
        if jugador.pasadizo_3_clase in jugador.derrotados
        else "???"
    )

    arriba = "Tu:👤" if jugador.posicion == "entrada" else " "
    p1 = "Tu:👤" if jugador.posicion == "pasadizo1" else " "
    p2 = "Tu:👤" if jugador.posicion == "pasadizo2" else " "
    p3 = "Tu:👤" if jugador.posicion == "pasadizo3" else " "
    centro = "Tu:👤" if jugador.posicion == "centro" else " "

    print(
        f"""

{'='*48}
        🏰 CASTILLO DEL ABISMO 🏰
{'='*48}

                  {arriba}
                    │
       ──────────────────────────
      │             │            │
    {p1}           {p2}           {p3}
 Pasadizo 1    Pasadizo 2   Pasadizo 3
      │             │            │
 [{nombre_1}] {estado_1}   Guardianes {estado_2}   [{nombre_3}] {estado_3}
      │             │            │
                  {centro}

       ─────────────┼────────────
      |     Pasadizo Central     |
      |        {estado_medio}            |

               👑 JEFE 👑
{'='*48}
"""
    )

class Escenario:
    def __init__(self, nombre, descripcion):
        self.nombre = nombre
        self.descripcion = descripcion
        self.direcciones = {}

    def explorar(self, jugador):
        raise NotImplementedError("Cada escenario define su propio explorar()")

class Bifurcacion(Escenario):
    def __init__(self):
        super().__init__(
            "Bifurcación", "El camino se divide en tres direcciones distintas."
        )

    def explorar(self, jugador):
        print(f"\n🔀 {self.nombre}\n{self.descripcion}")

class SalaDelTesoro(Escenario):
    def __init__(self):
        super().__init__(
            "Sala del Tesoro", "Montones de oro brillan bajo la luz tenue de antorchas."
        )

    def explorar(self, jugador):
        print(f"\n💰 {self.nombre}\n{self.descripcion}")
        while True:
            estado = " (ya derrotado)" if jugador.tesoro_guardian_derrotado else ""
            print("\n¿Qué haces?")
            print(
                f" 1) Abrir un cofre ({jugador.cofres_sala_tesoro}/{jugador.max_cofres_sala_tesoro})"
            )
            print(" 2) Investigar con cuidado (cuidado con las trampas)")
            print(f" 3) Enfrentar al guardián del tesoro{estado}")
            print(" 4) Salir de la sala")
            opcion = pedir_entero("👉 Elige: ", minimo=1, maximo=4)

            if opcion == 1:
                if jugador.cofres_sala_tesoro >= jugador.max_cofres_sala_tesoro:
                    print("\n📭 Ya no quedan más cofres en esta sala.")
                else:
                    abrir_cofre(jugador, contar_cofre=True)
            elif opcion == 2:
                evento_en_pasadizo(jugador)
                if jugador.vida <= 0:
                    return
            elif opcion == 3:
                self._enfrentar_guardian(jugador)
                if jugador.vida <= 0:
                    return
            elif opcion == 4:
                return

    def _enfrentar_guardian(self, jugador):
        if jugador.tesoro_guardian_derrotado:
            print("\n✅ Ya derrotaste al guardián del tesoro.")
            return
        print("\n🐉 Un Goblin Rey, mucho más grande que los demás, custodia el tesoro.")
        guardian = GoblinRey()
        escalar_enemigo(guardian, jugador.nivel, 0)
        resultado = jugador.sistema_de_combates(guardian)
        if resultado == "victoria":
            jugador.tesoro_guardian_derrotado = True
            print("\n🏆 El Goblin Rey cae. Encuentras un cofre bajo su trono.")
            abrir_cofre(jugador, contar_cofre=True)

class NPC:
    NIVELES_AFINIDAD = ["Hostil", "Desconfiado", "Neutral", "Amistoso", "Leal"]

    def __init__(self, nombre, tipo):
        self.nombre = nombre
        self.tipo = tipo
        self.dialogo_inicial = f"{self.nombre} te observa en silencio."

    def obtener_afinidad(self, jugador):
        return jugador.npcs_afinidad.get(self.nombre, "Neutral")

    def mejorar_afinidad(self, jugador):
        actual = self.obtener_afinidad(jugador)
        indice = self.NIVELES_AFINIDAD.index(actual)
        if indice < len(self.NIVELES_AFINIDAD) - 1:
            nueva = self.NIVELES_AFINIDAD[indice + 1]
            jugador.npcs_afinidad[self.nombre] = nueva
            print(f"\n💚 {self.nombre} confía más en ti. Afinidad: {nueva}")

    def hablar(self, jugador):
        print(f'\n💬 {self.nombre}: "{self.dialogo_inicial}"')
        print(f"   (Afinidad actual: {self.obtener_afinidad(jugador)})")

class Sabio(NPC):
    def __init__(self, nombre):
        super().__init__(nombre, tipo="Sabio")
        self.dialogo_inicial = "Los secretos de este castillo no son gratis, viajero."

    def hablar(self, jugador):
        super().hablar(jugador)
        if self.obtener_afinidad(jugador) in ("Amistoso", "Leal"):
            print(f"💡 {self.nombre} te comparte un consejo sobre el castillo.")
        self.mejorar_afinidad(jugador)

class Mercader(NPC):
    def __init__(self, nombre):
        super().__init__(nombre, tipo="Mercader")
        self.dialogo_inicial = "¿Buscas algo especial? Tengo justo lo que necesitas."

    def hablar(self, jugador):
        super().hablar(jugador)
        self.mejorar_afinidad(jugador)

class Aliado(NPC):
    def __init__(self, nombre):
        super().__init__(nombre, tipo="Aliado")
        self.dialogo_inicial = "Cuenta conmigo si me necesitas."

    def hablar(self, jugador):
        super().hablar(jugador)
        self.mejorar_afinidad(jugador)

class Jardin(Escenario):
    def __init__(self):
        super().__init__(
            "Jardín",
            "Un jardín exuberante, extrañamente vivo dentro de un castillo en ruinas.",
        )
        self.jardinero = Sabio("El Jardinero")

    def explorar(self, jugador):
        print(f"\n🌳 {self.nombre}\n{self.descripcion}")
        while True:
            estado_descanso = " (ya usado)" if jugador.descanso_jardin_usado else ""
            print("\n¿Qué haces?")
            print(f" 1) Descansar{estado_descanso}")
            print(" 2) Buscar plantas medicinales")
            print(" 3) Hablar con el jardinero")
            print(" 4) Explorar ")
            print(" 5) Salir del jardín")
            opcion = pedir_entero("👉 Elige: ", minimo=1, maximo=5)

            if opcion == 1:
                if jugador.descanso_jardin_usado:
                    print("\n💧 La fuente ya no tiene más energía para curarte.")
                else:
                    jugador.vida = jugador.max_vida
                    jugador.descanso_jardin_usado = True
                    print(
                        "\n💧 Descansas junto a la fuente. Vida restaurada por completo."
                    )
            elif opcion == 2:
                if jugador.plantas_encontradas >= jugador.max_plantas:
                    print("\n🌿 Ya encontraste todas las plantas medicinales.")
                    continue
                if random.random() < 0.65:
                    jugador.plantas_encontradas += 1
                    jugador.pociones += 1
                    print(f"\n🌿 Encontraste una planta medicinal.")
                    print(
                        f"Plantas encontradas: {jugador.plantas_encontradas}/{jugador.max_plantas}"
                    )
                else:
                    print("\n🍂 Buscaste entre la maleza, pero no encontraste nada ")

            elif opcion == 3:
                self.jardinero.hablar(jugador)
            elif opcion == 4:
                enemigo = random.choice([Planta(), Lobo()])
                escalar_enemigo(enemigo, jugador.nivel, -2)
                print(f"\n⚔️ ¡Un {enemigo.categoria} aparece entre la maleza!")
                jugador.sistema_de_combates(enemigo)
                if jugador.vida <= 0:
                    return
            elif opcion == 5:
                return

class Biblioteca(Escenario):
    def __init__(self, puerta_secreta):
        super().__init__(
            "Biblioteca", "Estantes cubiertos de polvo se alzan hasta el techo."
        )
        self.puerta_secreta = puerta_secreta

    def explorar(self, jugador):
        etiqueta_3 = "Abrir la puerta secreta" if jugador.bibliotecario_derrotado else "Investigar un ruido al fondo"
        print(f"\n📚 {self.nombre}\n{self.descripcion}")
        if jugador.bibliotecario_derrotado and "seguir" not in self.direcciones:
            self.direcciones["seguir"] = self.puerta_secreta
        while True:
            print("\n¿Qué haces?")
            print(" 1) Buscar pergaminos")
            print(" 2) Resolver un acertijo")
            print(f" 3) {etiqueta_3}")
            print(" 4) Salir de la biblioteca")
            opcion = pedir_entero("👉 Elige: ", minimo=1, maximo=4)

            if opcion == 1:
                self._buscar_pergaminos(jugador)
            elif opcion == 2:
                self._resolver_acertijo(jugador)
            elif opcion == 3:
                if jugador.bibliotecario_derrotado:
                    self.puerta_secreta.explorar(jugador)
                    if jugador.vida <= 0:
                        return
                else:
                    self._enfrentar_bibliotecario(jugador)
                    if jugador.vida <= 0:
                        return
            elif opcion == 4:
                return

    def _buscar_pergaminos(self, jugador):
        if jugador.biblioteca_pergamino:
            print("\n📜 Ya revisaste estos estantes.")
            return
        jugador.oro += 40
        jugador.biblioteca_pergamino = True
        print(f"\n📜 Encuentras un pergamino valioso. +40 oro. Total: {jugador.oro}")

    def _resolver_acertijo(self, jugador):
        if jugador.biblioteca_acertijo:
            print("\n🧩 Ya resolviste este acertijo.")
            return
        respuesta = (
            input("\n🧩 'Tengo ciudades, pero no casas. ¿Qué soy?' → ").strip().lower()
        )
        if respuesta in ("un mapa", "mapa"):
            jugador.pociones += 1
            jugador.biblioteca_acertijo = True
            print("✅ ¡Correcto! Ganas una poción.")
        else:
            print("❌ Incorrecto. El libro se cierra de golpe.")

    def _enfrentar_bibliotecario(self, jugador):
        if jugador.bibliotecario_derrotado:
            print("\n✅ Ya derrotaste al guardián de la biblioteca.")
            return
        print("\n📚 Un antiguo bibliotecario sale lentamente entre los estantes.")
        time.sleep(1)
        print("Los libros comienzan a levitar.")
        time.sleep(1)
        print("Las páginas vuelan por toda la sala.")
        time.sleep(1)
        print('"Nadie abandonará esta biblioteca con sus secretos..."')
        time.sleep(1)
        print("\n💀 ¡Ha aparecido el Bibliotecario Maldito!")
        bibliotecario = BibliotecarioMaldito()
        escalar_enemigo(bibliotecario, jugador.nivel, 0)
        resultado = jugador.sistema_de_combates(bibliotecario)
        if resultado == "victoria":
            jugador.bibliotecario_derrotado = True
            self.direcciones["seguir"] = self.puerta_secreta
            print("\n💀 El Bibliotecario Maldito desaparece entre una nube de polvo.")
            time.sleep(1)
            print("📚 Los libros vuelven lentamente a sus estantes.")
            time.sleep(1)
            print("🧱 Una enorme estantería comienza a moverse.")
            time.sleep(1)
            print("🚪 Detrás de ella aparece una puerta secreta.")
            time.sleep(1)
            respuesta = pedir_entero(
                "\n¿Deseas entrar?\n 1) Sí\n 2) No\n👉 Elige: ", minimo=1, maximo=2
            )
            if respuesta == 1:
                self.puerta_secreta.explorar(jugador)
            else:
                print(
                    "\n🚶 Decides no entrar todavía. La puerta secreta seguirá aquí."
                )

class PuertaCustodiada(Escenario):
    def __init__(self, clase_enemigo):
        super().__init__(
            "Puerta Custodiada",
            "Una puerta reforzada bloquea el paso. Sientes una presencia poderosa detrás.",
        )
        self.clase_enemigo = clase_enemigo

    def explorar(self, jugador):
        if self.clase_enemigo in jugador.derrotados:
            print("\n🚪 Esta puerta ya está vacía. Ya derrotaste a su guardián.")
            return
        print(f"\n🚪 {self.descripcion}")
        time.sleep(2)
        enemigo = self.clase_enemigo("Enemigo Oscuro")
        escalar_enemigo(enemigo, jugador.nivel, -1)
        enemigo.puede_huir = False
        enemigo.otorga_llave = True
        print(
            f"\n👿 ¡Tu oponente será un <<< {enemigo.categoria} >>>! (Nivel {enemigo.nivel})"
        )
        jugador.sistema_de_combates(enemigo)

def construir_pasadizo_1(jugador):
    puerta_secreta = PuertaCustodiada(jugador.pasadizo_1_clase)
    biblioteca = Biblioteca(puerta_secreta)
    if jugador.bibliotecario_derrotado:
        biblioteca.direcciones["seguir"] = puerta_secreta

    bifurcacion = Bifurcacion()
    bifurcacion.direcciones = {
        "izquierda": SalaDelTesoro(),
        "centro": Jardin(),
        "derecha": biblioteca,
    }
    return bifurcacion

def explorar_mundo(jugador, escenario_inicial):
    pila_visitados = [escenario_inicial]

    while pila_visitados:
        actual = pila_visitados[-1]
        actual.explorar(jugador)
        if jugador.vida <= 0:
            return

        direcciones = list(actual.direcciones.keys())
        if not direcciones:
            if len(pila_visitados) > 1:
                pila_visitados.pop()
                continue
            else:
                return

        print("\n¿Hacia dónde te mueves?")
        for i, d in enumerate(direcciones, start=1):
            print(f" {i}) {d.capitalize()}")
        if len(pila_visitados) > 1:
            print(f" {len(direcciones)+1}) Regresar")
        print(f" {len(direcciones)+2}) Salir de la exploración")

        eleccion = pedir_entero("👉 Elige: ", minimo=1, maximo=len(direcciones) + 2)
        if eleccion <= len(direcciones):
            print(random.choice(AMBIENTE_PASADIZO))
            evento_en_pasadizo(jugador)
            if jugador.vida <= 0:
                return
            pila_visitados.append(actual.direcciones[direcciones[eleccion - 1]])
        elif eleccion == len(direcciones) + 1 and len(pila_visitados) > 1:
            pila_visitados.pop()
        else:
            return

def pasadizo_puerta(jugador, clase_enemigo):
    if clase_enemigo in jugador.derrotados:
        print("\n🚪 Esta puerta ya está vacía. Ya derrotaste a su guardián.")
        return
    print(random.choice(AMBIENTE_PASADIZO))
    evento_en_pasadizo(jugador)
    if jugador.vida <= 0:
        return
    enemigo = clase_enemigo("Enemigo Oscuro")
    escalar_enemigo(enemigo, jugador.nivel, -1)
    enemigo.puede_huir = False
    enemigo.otorga_llave = True

    print(
    f"\n🚪 Detrás de la puerta aparece un <<< {enemigo.categoria} >>>! (Nivel {enemigo.nivel})")

    jugador.sistema_de_combates(enemigo)

def pasadizo_cofre_custodiado(jugador):
    if jugador.pasadizo_2_completado:
        print("\n📭 Ya saqueaste este cofre. El pasadizo está vacío ahora.")
        return
    print("\n🗝️ Este pasadizo lleva a un cofre... pero está fuertemente custodiado.")
    num_guardianes = random.randint(2, 3)
    for i in range(num_guardianes):
        guardian = random.choice([Goblin(), Esqueleto()])
        escalar_enemigo(guardian, jugador.nivel, -2)
        print(
            f"\n👹 Un {guardian.categoria} guardián se interpone en tu camino ({i+1}/{num_guardianes}).")
        resultado = jugador.sistema_de_combates(guardian)

        if resultado != "victoria":
            return
    print("\n🏆 ¡Has vencido a todos los guardianes!")
    abrir_cofre(jugador)
    jugador.pasadizo_2_completado = True

def elegir_pasadizo(jugador):
    while True:
        mostrar_mapa(jugador)
        print(" 1) Explorar el primer pasadizo (bifurcación)")
        print(" 2) Explorar el segundo pasadizo (cofre custodiado)")
        print(" 3) Explorar el tercer pasadizo (puerta)")
        if jugador.llaves >= 2:
            print(" 4) Entrar al pasadizo del medio → ¡El Jefe Final te espera!")
        else:
            print(f" 4) Pasadizo del medio 🔒 (tienes {jugador.llaves}/2 llaves)")
        print("=" * 40)

        eleccion = pedir_entero("👉 Elige un pasadizo: ", minimo=1, maximo=4)

        if eleccion == 4 and jugador.llaves < 2:
            print("\n🔒 El pasadizo del medio está sellado. Necesitas ambas llaves.")
            continue

        if eleccion == 1:
            jugador.posicion = "pasadizo1"
        elif eleccion == 2:
            jugador.posicion = "pasadizo2"
        elif eleccion == 3:
            jugador.posicion = "pasadizo3"
        elif eleccion == 4:
            jugador.posicion = "centro"
        return eleccion

def cargar_partida():
    try:
        with open("partida.json", "r") as archivo:
            datos = json.load(archivo)
    except (FileNotFoundError, json.JSONDecodeError, OSError):
        return None

    claves_necesarias = [
        "clase", "nombre", "nivel", "vida_base", "fuerza_base", "velocidad_base",
        "vida", "oro", "pociones", "inventario", "llaves", "experiencia",
        "exp_para_subir", "derrotados", "arma", "posicion",
        "pasadizo_1_clase", "pasadizo_3_clase", "pasadizo_2_completado",
    ]
    if not all(clave in datos for clave in claves_necesarias):
        print("\n❌ La partida guardada está incompleta o corrupta. Se iniciará una partida nueva.")
        return None

    if datos["clase"] not in CLASES_JUGABLES:
        print("\n❌ La partida guardada contiene una clase desconocida. Se iniciará una partida nueva.")
        return None

    try:
        jugador = CLASES_JUGABLES[datos["clase"]](datos["nombre"])
        jugador.nivel = datos["nivel"]
        jugador.vida_base = datos["vida_base"]
        jugador.fuerza_base = datos["fuerza_base"]
        jugador.velocidad_base = datos["velocidad_base"]
        jugador.aplicar_nivel()
        jugador.vida = datos["vida"]
        jugador.oro = datos["oro"]
        jugador.pociones = datos["pociones"]
        jugador.inventario = datos["inventario"]
        jugador.llaves = datos["llaves"]
        jugador.experiencia = datos["experiencia"]
        jugador.exp_para_subir = datos["exp_para_subir"]
        jugador.derrotados = [TODAS_LAS_CLASES[n] for n in datos["derrotados"]]
        jugador.arma = datos["arma"]
        jugador.posicion = datos["posicion"]

        if jugador.atributo_arma and "valor_atributo_arma" in datos:
            setattr(jugador, jugador.atributo_arma, datos["valor_atributo_arma"])

        if datos["pasadizo_1_clase"]:
            jugador.pasadizo_1_clase = CLASES_JUGABLES[datos["pasadizo_1_clase"]]
        if datos["pasadizo_3_clase"]:
            jugador.pasadizo_3_clase = CLASES_JUGABLES[datos["pasadizo_3_clase"]]
        jugador.pasadizo_2_completado = datos["pasadizo_2_completado"]
        jugador.bibliotecario_derrotado = datos.get(
            "bibliotecario_derrotado", datos.get("biblioteca_mago_derrotado", False)
        )
        jugador.biblioteca_pergamino = datos.get("biblioteca_pergamino", False)
        jugador.biblioteca_acertijo = datos.get("biblioteca_acertijo", False)
        jugador.tesoro_guardian_derrotado = datos.get("tesoro_guardian_derrotado", False)
        jugador.npcs_afinidad = datos.get("npcs_afinidad", {})
        jugador.plantas_encontradas = datos.get("plantas_encontradas", 0)
        jugador.cofres_sala_tesoro = datos.get("cofres_sala_tesoro", 0)
        jugador.descanso_jardin_usado = datos.get("descanso_jardin_usado", False)
        jugador.pasadizo_1_mundo = construir_pasadizo_1(jugador)
    except (KeyError, TypeError, ValueError) as e:
        print(f"\n❌ No se pudo cargar la partida correctamente ({e}). Se iniciará una partida nueva.")
        return None

    print(f"\n💾 Partida cargada: {jugador.nombre}, Nivel {jugador.nivel}.")
    return jugador

# --- EJECUCIÓN DEL JUEGO ---
print("\n      ==============================")
print("     ⚔️  ARENA DE CAMPEONES v2.0  ⚔️ ")
print("      ==============================")

clases_disponibles = {1: Guerrero, 2: Arquero, 3: Mago}
jugador = None

if os.path.exists("partida.json"):
    respuesta = (
        input("\n💾 Se encontró una partida guardada. ¿Deseas cargarla? (s/n): ")
        .strip()
        .lower()
    )
    if respuesta == "s":
        jugador = cargar_partida()

if jugador is None:
    time.sleep(1)
    print("\n🎭 CLASES DISPONIBLES:")
    print(" 1️⃣ : Guerrero")
    print(" 2️⃣ : Arquero")
    print(" 3️⃣ : Mago")
    time.sleep(1)
    avatar = pedir_entero(
        "\n👤 Escribe el índice del personaje deseado (1-3): ", minimo=1, maximo=3
    )
    nombre = input("\n📝 ¿Cuál será tu nombre de héroe?: ").strip()
    time.sleep(1)
    jugador = clases_disponibles[avatar](nombre)
    jugador.nivel = 3
    jugador.aplicar_nivel()
    enemigos_asignables = jugador.enemigos_restantes()
    jugador.pasadizo_1_clase = enemigos_asignables[0]
    jugador.pasadizo_3_clase = enemigos_asignables[1]
    jugador.pasadizo_2_completado = False
    jugador.pasadizo_1_mundo = construir_pasadizo_1(jugador)

jugador.Saludo()

jugando = True
while jugando:
    eleccion = elegir_pasadizo(jugador)

    if eleccion == 1:
        explorar_mundo(jugador, jugador.pasadizo_1_mundo)
    elif eleccion == 2:
        pasadizo_cofre_custodiado(jugador)
    elif eleccion == 3:
        pasadizo_puerta(jugador, jugador.pasadizo_3_clase)
    elif eleccion == 4:
        jefe = jugador.generar_jefe_final()
        presentar_jefe_final(jefe)
        resultado = jugador.sistema_de_combates(jefe)
        if resultado == "victoria":
            print("\n👑 ¡HAS DERROTADO AL JEFE FINAL! GANASTE EL JUEGO 🏆")
        else:
            print("\n💀 El jefe final te detuvo. Fin del juego.")
        break

    if jugador.vida <= 0:
        print("\n💀 Has caído en batalla. Fin del juego.")
        break

    accion = jugador.menu_post_combate()
    while accion in ("tienda", "inventario"):
        if accion == "tienda":
            jugador.tienda()
        else:
            jugador.inventario_jugador()
        accion = jugador.menu_post_combate()
    if accion == "salir":
        jugando = False
time.sleep(1)
