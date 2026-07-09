"""
Módulo CLI de Escuadra.
Punto de entrada principal con subcomandos para las herramientas.
"""

import argparse
import sys
import json
import argcomplete

from escuadra.cli_interactivo import ejecutar_interactivo
from escuadra.core.registry import descubrir_herramientas


def verificar_entorno():
    if sys.version_info < (3, 10):
        print("Error: Escuadra requiere Python 3.10 o superior.")
        sys.exit(1)

    try:
        import importlib.util
        if importlib.util.find_spec("PySide6") is None:
            raise ImportError
    except ImportError:
        print(
            "Error: PySide6 no está instalado.\n"
            "Instálelo ejecutando:\n"
            "    pip install PySide6"
        )
        sys.exit(1)


__version__ = "0.1.0"


def obtener_modulos_disponibles():
    """
    Obtiene las herramientas disponibles desde el registry.
    """
    return {
        herramienta.nombre
        for herramienta in descubrir_herramientas()
    }


def herramienta_no_disponible(nombre_herramienta):
    """Muestra mensaje para herramientas no implementadas."""
    print(
        f"La herramienta '{nombre_herramienta}' aún está en construcción "
        "y no está disponible."
    )


def ejecutar_herramienta(args):
    """
    Ejecuta el subcomando correspondiente si el módulo existe.
    """

    herramienta = args.herramienta

    modulos_disponibles = obtener_modulos_disponibles()

    if herramienta not in modulos_disponibles:
        herramienta_no_disponible(herramienta)
        return

    try:
        modulo = __import__(
            f"escuadra.modulos.{herramienta}",
            fromlist=["ejecutar"]
        )

    except (ModuleNotFoundError, ImportError):
        herramienta_no_disponible(herramienta)
        return

    kwargs = vars(args).copy()

    kwargs.pop("herramienta")
    salida_json = kwargs.pop("json")

    resultado = modulo.ejecutar(**kwargs)

    if salida_json:
        print(
            json.dumps(
                {
                    "herramienta": herramienta,
                    "parametros": kwargs,
                    "resultado": resultado,
                },
                ensure_ascii=False,
                indent=2
            )
        )
    else:
        print(resultado)


def main():
    """Punto de entrada principal del CLI de Escuadra."""

    try:
        verificar_entorno()

        parser = argparse.ArgumentParser(
            prog="escuadra",
            description="Herramientas de cálculo de ingeniería civil y eléctrica."
        )

        parser.add_argument(
            "--version",
            "-v",
            action="version",
            version=f"%(prog)s {__version__}"
        )

        parser.add_argument(
            "--json",
            action="store_true",
            help="Muestra la salida en formato JSON"
        )

        subparsers = parser.add_subparsers(
            title="herramientas",
            dest="herramienta",
            help="Herramienta a ejecutar"
        )

        subparsers.add_parser(
            "interactivo",
            help="Modo interactivo paso a paso (REPL)"
        )

        herramientas = descubrir_herramientas()

        for herramienta in herramientas:
            subparsers.add_parser(
                herramienta.nombre,
                help=herramienta.descripcion
            )

        argcomplete.autocomplete(parser)

        args = parser.parse_args()

        if args.herramienta is None:
            parser.print_help()
            sys.exit(0)

        if args.herramienta == "interactivo":
            ejecutar_interactivo()
            return

        ejecutar_herramienta(args)

    except KeyboardInterrupt:
        print("\nOperación cancelada por el usuario.")
        sys.exit(130)


if __name__ == "__main__":
    main()
