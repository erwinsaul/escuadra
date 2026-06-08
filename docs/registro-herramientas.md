# Registro de herramientas (subcomandos CLI)

Este documento describe el proceso para agregar nuevos subcomandos al CLI del proyecto.

---

## 🧩 1. Crear el módulo del comando

Cada subcomando debe implementarse en un archivo independiente dentro de la carpeta de comandos.

Ejemplo:


cli/commands/nuevo_comando.py


---

## 🧩 2. Definir el comando y su parser

Dentro del módulo se define la lógica del comando y su configuración:

```python
import argparse

def ejecutar(args):
    print("Ejecutando nuevo comando")


def add_parser(subparsers):
    parser = subparsers.add_parser(
        "nuevo-comando",
        help="Descripción del nuevo comando"
    )

    parser.add_argument(
        "--opcion",
        help="Descripción de la opción"
    )

    parser.set_defaults(func=ejecutar)