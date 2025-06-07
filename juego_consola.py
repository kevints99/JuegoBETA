import random

class Personaje:
    def __init__(self, vida, ataque, defensa):
        self.__vida = self.__validar_valor(vida)
        self.__ataque = ataque
        self.__defensa = defensa

    def __validar_valor(self, valor):
        return max(0, min(100, valor))

    def get_vida(self):
        return self.__vida

    def set_vida(self, nueva_vida):
        self.__vida = self.__validar_valor(nueva_vida)

    def get_ataque(self):
        return self.__ataque

    def set_ataque(self, nuevo_ataque):
        self.__ataque = nuevo_ataque

    def get_defensa(self):
        return self.__defensa

    def set_defensa(self, nueva_defensa):
        self.__defensa = nueva_defensa

    def esta_vivo(self):
        return self.__vida > 0

    def atacar(self, objetivo):
        raise NotImplementedError("Este método debe ser implementado por las subclases.")


class Guerrero(Personaje):
    def atacar(self, objetivo):
        daño_base = self.get_ataque() * 1.2
        daño_final = max(0, daño_base - objetivo.get_defensa())
        objetivo.set_vida(objetivo.get_vida() - daño_final)
        print(f"⚔️ Guerrero ataca e inflige {daño_final:.1f} de daño.")


class Mago(Personaje):
    def atacar(self, objetivo):
        daño_final = self.get_ataque()  # Ignora la defensa
        objetivo.set_vida(objetivo.get_vida() - daño_final)
        print(f"✨ Mago lanza un hechizo e inflige {daño_final:.1f} de daño (ignora defensa).")


class Arquero(Personaje):
    def atacar(self, objetivo):
        if self.get_ataque() > objetivo.get_defensa():
            daño_final = (self.get_ataque() - objetivo.get_defensa()) * 2
            print("🏹 Arquero hace un disparo crítico.")
        else:
            daño_final = max(0, self.get_ataque() - objetivo.get_defensa())
        objetivo.set_vida(objetivo.get_vida() - daño_final)
        print(f"🏹 Arquero ataca e inflige {daño_final:.1f} de daño.")


def batalla(jugador1, jugador2):
    turno = 0
    while jugador1.esta_vivo() and jugador2.esta_vivo():
        print(f"\n--- Turno {turno + 1} ---")
        if turno % 2 == 0:
            jugador1.atacar(jugador2)
        else:
            jugador2.atacar(jugador1)

        print(f"🧍 Vida Jugador 1: {jugador1.get_vida():.1f}")
        print(f"🧍 Vida Jugador 2: {jugador2.get_vida():.1f}")
        turno += 1

    ganador = "Jugador 1" if jugador1.esta_vivo() else "Jugador 2"
    print(f"\n🎉 ¡{ganador} ha ganado la batalla!")


if __name__ == "__main__":
    guerrero = Guerrero(100, 30, 20)
    mago = Mago(80, 40, 10)

    batalla(guerrero, mago)
