import threading
import time


class LectoresEscritores:

    def __init__(self):
        self.cantidad_lectores = 0
        self.escritor_activo = False
        self.lock = threading.Lock()
        self.cv = threading.Condition(self.lock)

    def lector(self, id):
        with self.cv:
            self.cv.wait_for(lambda: not self.escritor_activo)
            self.cantidad_lectores += 1

        # Simular lectura
        print(f"Lector {id} está leyendo.")
        time.sleep(0.1)

        with self.cv:
            self.cantidad_lectores -= 1
            if self.cantidad_lectores == 0:
                self.cv.notify()

    def escritor(self, id):
        with self.cv:
            self.cv.wait_for(lambda: not self.escritor_activo and self.
                             cantidad_lectores == 0)
            self.escritor_activo = True

        # Simular escritura
        print(f"Escritor {id} está escribiendo.")
        time.sleep(0.1)

        with self.cv:
            self.escritor_activo = False
            self.cv.notify_all()


def crear_hilos(le):
    hilos = []
    for i in range(5):
        hilos.append(threading.Thread(target=le.lector, args=(i, )))
        hilos.append(threading.Thread(target=le.escritor, args=(i, )))
    return hilos


def main():
    le = LectoresEscritores()
    hilos = crear_hilos(le)

    for h in hilos:
        h.start()

    for h in hilos:
        h.join()


if __name__ == "__main__":
    main()
