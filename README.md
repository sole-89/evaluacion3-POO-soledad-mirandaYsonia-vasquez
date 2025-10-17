# 🧠 Evaluación 3 — Programación Orientada a Objeto Seguro
**Carrera: Analista Programador  
**Sede: Puente Alto  
**Docente: Michael Arjel Mayerovich  
**Estudiantes: Soledad Miranda
               Sonia Vasquez
**Fecha de entrega: 18/10/2025  

---

## 📋 Descripción General

Este repositorio contiene el desarrollo de la **Evaluación Sumativa N°3** del módulo *Programación Orientada a Objeto Seguro*, correspondiente a la Unidad: **Fundamentos de la POO y Control de Versiones con Git**.

El objetivo es aplicar **Programación Orientada a Objetos en Python**, utilizando **clases, abstracción, encapsulamiento, polimorfismo, trazabilidad y manejo de reglas de negocio**, según los criterios establecidos en la rúbrica del módulo.

Cada ejercicio está contenido en su propia carpeta (`ejercicio1/`, `ejercicio2/`, etc.) y se ejecuta desde un archivo `main.py`.

---

## 🧩 Estructura del Proyecto

```
│
├── ejercicio1/
│   ├── clases/
│   │   └── *.py
│   └── main.py
│
├── ejercicio2/
│   ├── clases/
│   │   └── *.py
│   └── main.py
│
├── ejercicio3/
│   ├── clases/
│   │   └── *.py
│   └── main.py
│
├── ejercicio4/
│   ├── clases/
│   │   ├── material.py
│   │   ├── suscriptor.py
│   │   ├── retiro.py
│   │   ├── bono.py
│   │   └── aviso.py
│   └── main.py
│
└── README.md
```

---

## 🧮 Ejercicios desarrollados

| Nº | Ejercicio | Descripción | Conceptos aplicados |
|----|------------|--------------|----------------------|
| **E1** | Agenda de peluquería y barbería | Sistema de citas con control de solapamiento, trazabilidad y estados válidos. | Encapsulamiento, validaciones, eventos. |
| **E2** | Turnos para cafetería escolar | Planificación semanal con políticas polimórficas (Fijo/Rotativo/Flexible). | Polimorfismo, abstracción, métricas derivadas. |
| **E3** | Canchas vecinales | Sistema de reservas con tarifas y políticas de cancelación polimórficas. | Herencia, manejo de estados, penalización. |
| **E4** | Reciclaje domiciliario con puntos de incentivo | Registro de retiros por material, cálculo de puntos, bono semanal y avisos. | Polimorfismo, trazabilidad, encapsulamiento, bono automático. |

---

## ⚙️ Ejecución

Para probar cualquier ejercicio:

1. Abre la carpeta del ejercicio (por ejemplo, `cd ejercicio4`).
2. Ejecuta el archivo principal:

   ```bash
   python3 main.py
   ```

3. El script mostrará en consola las operaciones realizadas y los eventos registrados.

---

## 🧱 Dependencias

- Python 3.10 o superior  
- No requiere librerías externas (todo es estándar de Python).  

---

## 🧰 Reglas de Evaluación (resumen)

- Cada clase se encuentra encapsulada y valida sus atributos.  
- Los métodos implementan reglas de negocio según el enunciado.  
- Se utilizan clases abstractas y subclases para aplicar **polimorfismo**.  
- Todo evento del dominio genera trazabilidad con timestamp.  
- No se utilizan bases de datos; los modelos operan **en memoria**.  
- Estrategia de peso en ejercicio 4: **rechazo por exceso de bolsa**.  

---

## 🧾 Observaciones

- El proyecto respeta la estructura de carpetas y buenas prácticas del módulo.  
- Se incluyó la clase opcional **`Aviso`** (con `AvisoApp` y `AvisoEmail`) en el ejercicio 4 para reforzar el uso de abstracción.  
- Todos los scripts son ejecutables y demuestran las reglas de negocio descritas.  

---

## 🔗 Control de Versiones

- Rama creada según formato indicado (`evaluacion3_[nombre_apellido]`)  
- Proyecto publicado en repositorio remoto de GitHub.  
- Commits documentados con mensajes descriptivos por ejercicio.  
