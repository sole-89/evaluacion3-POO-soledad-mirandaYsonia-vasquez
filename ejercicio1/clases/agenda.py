# agenda.py
# ==========================
# Modelo: Agenda
# ==========================
from datetime import timedelta

class Agenda:
    """Contenedor de citas y árbitro de choques."""

    def __init__(self):
        self._citas = []

    def agregar(self, cita):
        """Agrega una cita validando id único y ausencia de solape."""
        if any(c.id_cita == cita.id_cita for c in self._citas):
            raise ValueError(f"Ya existe una cita con id {cita.id_cita}.")
        #  Comprobamos solapamiento sin incluir la propia cita (por si ya está)
        if self.existe_solape(cita.profesional, cita.inicio, cita.fin, exclude_id=cita.id_cita):
            raise ValueError("El profesional ya tiene una cita en ese horario.")
        self._citas.append(cita)
        print(f" Cita {cita.id_cita} agregada correctamente.")

    def existe_solape(self, profesional, inicio, fin, exclude_id=None):
        """Detecta solapamientos entre citas no canceladas.
        exclude_id: id_cita a ignorar para evitar comparar una cita consigo misma.
        """
        for c in self._citas:
            if exclude_id is not None and c.id_cita == exclude_id:
                continue  # Ignora la cita actual

            if c.profesional == profesional and c.estado != "cancelada":
                if inicio < c.fin and c.inicio < fin:
                    return True
        return False

    def listar_citas(self):
        """Muestra todas las citas registradas."""
        if not self._citas:
            print("No hay citas registradas.")
            return
        print("\n=== LISTADO DE CITAS ===")
        for c in self._citas:
            print(c)
