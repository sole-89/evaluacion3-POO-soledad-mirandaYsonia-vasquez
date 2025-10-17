# main.py
# =======================================
# Ejercicio 2 — Turnos para cafetería escolar
# =======================================
from clases.colaborador import Colaborador
from clases.franja import Franja
from clases.plan_semanal import PlanSemanal
from clases.politica_turno import TurnoFijo

def main():
    print("==============================================")
    print("☕ SISTEMA DE TURNOS - CAFETERÍA ESCOLAR ☕")
    print("==============================================\n")

    # Crear colaboradores
    col1 = Colaborador(1, "Laura", 20, "manana")
    col2 = Colaborador(2, "Pedro", 20, "tarde")
    col3 = Colaborador(3, "Sofía", 25, "indistinto")

    colaboradores = [col1, col2, col3]

    # Crear franjas de trabajo
    franjas = [
        Franja("Lunes", "08:00", "12:00"),
        Franja("Lunes", "12:00", "16:00"),
        Franja("Martes", "08:00", "12:00"),
        Franja("Martes", "12:00", "16:00"),
        Franja("Miércoles", "08:00", "12:00"),
        Franja("Miércoles", "12:00", "16:00"),
    ]

    # Crear plan semanal con política Fija
    plan = PlanSemanal("Semana 42", franjas, colaboradores)
    politica = TurnoFijo()
    plan.generar_plan(politica)

    # Mostrar resultado
    plan.mostrar_plan()

    print("\n==============================================")
    print("✅ FIN DEL PROCESO DE PRUEBA")
    print("==============================================")

if __name__ == "__main__":
    main()
