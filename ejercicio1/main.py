# main.py
# =======================================
# Ejercicio 1 — Agenda de peluquería y barbería
# =======================================
from datetime import datetime, timedelta
from clases.servicio import CorteCabello, Coloracion
from clases.cita import Cita
from clases.agenda import Agenda

def main():
    print("========================================================")
    print("💈 SISTEMA DE GESTIÓN DE CITAS - PELUQUERÍA Y BARBERÍA 💈")
    print("======================================================\n")

    # ------------------------------------------
    # 1️⃣ CREACIÓN DE SERVICIOS DISPONIBLES
    # ------------------------------------------
    print(" Creando servicios disponibles...\n")
    corte = CorteCabello()
    color = Coloracion()
    print(f" Servicio 1: Corte de Cabello ({corte.duracion_min()} min)")
    print(f" Servicio 2: Coloración ({color.duracion_min()} min)\n")

    # ------------------------------------------
    # 2️⃣ CREACIÓN DE LA AGENDA GENERAL
    # ------------------------------------------
    agenda = Agenda()

    # ------------------------------------------
    # 3️⃣ CREACIÓN Y CONFIRMACIÓN DE CITAS
    # ------------------------------------------
    print(" Creando y confirmando citas...\n")

    # Cita 1
    cita1 = Cita(1, "María López", "Carla", datetime.now() + timedelta(hours=1))
    cita1.asignar_servicio(corte)
    agenda.agregar(cita1)  #  primero se agrega
    cita1.confirmar("Confirmación inicial", agenda)  #  luego se confirma
    print(f" Cita {cita1.id_cita} confirmada para {cita1.cliente} a las {cita1.inicio.strftime('%H:%M')}.\n")

    # Cita 2 — Intento de solapamiento (debe fallar)
    print(" Intentando agregar una cita que se solapa...\n")
    try:
        cita2 = Cita(2, "Ana Díaz", "Carla", datetime.now() + timedelta(hours=1, minutes=15))
        cita2.asignar_servicio(color)
        agenda.agregar(cita2)
        cita2.confirmar("Intento de confirmar solapada", agenda)
    except ValueError as e:
        print(f" Error al confirmar cita 2: {e}\n")

    # ------------------------------------------
    # 4️⃣ CANCELACIÓN DE UNA CITA
    # ------------------------------------------
    print(" Cancelando cita 1...\n")
    cita1.cancelar("Cliente no podrá asistir")
    print(f" Cita {cita1.id_cita} cancelada correctamente.\n")

    # ------------------------------------------
    # 5️⃣ LISTADO FINAL DE CITAS
    # ------------------------------------------
    print(" Estado final de todas las citas:\n")
    agenda.listar_citas()

    print("\n====================================================")
    print(" FIN DEL PROCESO DE PRUEBA")
    print("====================================================\n")

if __name__ == "__main__":
    main()
