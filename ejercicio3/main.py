# main.py
# =======================================
# Ejercicio 3 — Canchas Vecinales
# =======================================
from datetime import datetime, timedelta
from clases.cancha import Cancha
from clases.reserva import Reserva
from clases.tarifa import TarifaDiurna, TarifaFinDeSemana
from clases.politica_cancelacion import CancelacionFlexible, CancelacionEstricta

def main():
    print("===============================================")
    print("⚽  SISTEMA DE RESERVAS - CANCHAS VECINALES  ⚽")
    print("===============================================\n")

    # ------------------------------------------------------------
    # 1️⃣ CREACIÓN DE CANCHA Y BLOQUEO DE MANTENCIÓN
    # ------------------------------------------------------------
    cancha1 = Cancha(1, "Cancha Municipal")

    inicio_mant = datetime.now() + timedelta(days=1, hours=10)
    fin_mant = datetime.now() + timedelta(days=1, hours=12)
    cancha1.bloquear_mantencion(inicio_mant, fin_mant)

    print(" Mantención agendada correctamente:")
    print(f"   Desde: {inicio_mant.strftime('%Y-%m-%d %H:%M')}")
    print(f"   Hasta: {fin_mant.strftime('%Y-%m-%d %H:%M')}\n")

    reservas = []  # listado general de reservas

    # ------------------------------------------------------------
    # 2️⃣ RESERVA VÁLIDA ANTES DE MANTENCIÓN
    # ------------------------------------------------------------
    print(" Creando y confirmando reserva 1...\n")

    r1 = Reserva(
        1,
        cancha1,
        "Pedro Soto",
        datetime.now() + timedelta(days=1, hours=8),
        datetime.now() + timedelta(days=1, hours=9, minutes=30),
    )

    tarifa1 = TarifaDiurna()
    r1.cotizar(tarifa1)
    r1.confirmar("Confirmación normal", reservas)
    reservas.append(r1)
    print(f" Reserva {r1.id_reserva} confirmada correctamente para {r1.cliente}.\n")

    # ------------------------------------------------------------
    # 3️⃣ RESERVA EN HORARIO DE MANTENCIÓN (DEBE FALLAR)
    # ------------------------------------------------------------
    print(" Intentando crear reserva 2 en horario de mantención...\n")

    try:
        r2 = Reserva(
            2,
            cancha1,
            "Ana López",
            datetime.now() + timedelta(days=1, hours=10, minutes=30),
            datetime.now() + timedelta(days=1, hours=11, minutes=30),
        )
        r2.cotizar(TarifaFinDeSemana())
        r2.confirmar("Intento en horario de mantención", reservas)
        reservas.append(r2)
    except ValueError as e:
        print(f" Error en reserva 2: {e}\n")

    # ------------------------------------------------------------
    # 4️⃣ CANCELACIÓN DE RESERVA CON POLÍTICA FLEXIBLE
    # ------------------------------------------------------------
    print(" Cancelando reserva 1 con política flexible...\n")
    politica_flex = CancelacionFlexible()
    penal = r1.cancelar("Cliente canceló su asistencia", politica_flex)
    print(f" Reserva {r1.id_reserva} cancelada. Penalización: ${penal['monto_penalizacion']} ({penal['motivo']})\n")

    # ------------------------------------------------------------
    # 5️⃣ ESTADO FINAL DE TODAS LAS RESERVAS
    # ------------------------------------------------------------
    print(" ESTADO FINAL DE RESERVAS\n---------------------------")
    for r in reservas:
        print(r)

    print("\n===============================================")
    print(" FIN DEL PROCESO DE PRUEBA")
    print("===============================================")

if __name__ == "__main__":
    main()
