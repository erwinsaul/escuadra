"""
Operaciones básicas de matrices usando listas de listas.
"""


def sumar(a: list[list[float]], b: list[list[float]]) -> list[list[float]]:
    """
    Suma dos matrices de iguales dimensiones.

    Args:
        a: Primera matriz.
        b: Segunda matriz.

    Returns:
        Nueva matriz con la suma elemento a elemento.

    Raises:
        ValueError: Si las dimensiones no son compatibles.

    Examples:
        >>> sumar([[1, 2], [3, 4]], [[5, 6], [7, 8]])
        [[6, 8], [10, 12]]
    """
    _validar_dimensiones(a, b)
    return [[a[i][j] + b[i][j] for j in range(len(a[0]))] for i in range(len(a))]


def restar(a: list[list[float]], b: list[list[float]]) -> list[list[float]]:
    """
    Resta dos matrices de iguales dimensiones.

    Args:
        a: Primera matriz.
        b: Segunda matriz.

    Returns:
        Nueva matriz con la resta elemento a elemento.

    Raises:
        ValueError: Si las dimensiones no son compatibles.

    Examples:
        >>> restar([[5, 6], [7, 8]], [[1, 2], [3, 4]])
        [[4, 4], [4, 4]]
    """
    _validar_dimensiones(a, b)
    return [[a[i][j] - b[i][j] for j in range(len(a[0]))] for i in range(len(a))]


def multiplicar(a: list[list[float]], b: list[list[float]]) -> list[list[float]]:
    """
    Multiplica dos matrices (producto matricial).

    Args:
        a: Primera matriz de dimensiones m x n.
        b: Segunda matriz de dimensiones n x p.

    Returns:
        Nueva matriz de dimensiones m x p.

    Raises:
        ValueError: Si las dimensiones no son compatibles para multiplicación.

    Examples:
        >>> multiplicar([[1, 2], [3, 4]], [[5, 6], [7, 8]])
        [[19, 22], [43, 50]]
    """
    filas_a = len(a)
    cols_a = len(a[0])
    cols_b = len(b[0])

    if cols_a != len(b):
        raise ValueError(
            f"Dimensiones incompatibles para multiplicación: "
            f"{filas_a}x{cols_a} y {len(b)}x{cols_b}"
        )

    return [
        [sum(a[i][k] * b[k][j] for k in range(cols_a)) for j in range(cols_b)]
        for i in range(filas_a)
    ]


def _validar_dimensiones(a: list[list[float]], b: list[list[float]]) -> None:
    """Valida que dos matrices tengan las mismas dimensiones."""
    if len(a) != len(b) or len(a[0]) != len(b[0]):
        raise ValueError(
            f"Dimensiones incompatibles: {len(a)}x{len(a[0])} y {len(b)}x{len(b[0])}"
        )
