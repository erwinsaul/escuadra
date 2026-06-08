from typing import Dict

def calculator_momento_mx(longitud: float, carga: float, tipo_carga: str = 'puntual_central') -> Dict[str, float]:
    """
    Calcula el momento de flexión en un elemento civil.

    Args:
        longitud (float): La longitud del elemento.
        carga (float): La carga aplicada al elemento.
        tipo_carga (str): El tipo de carga ('puntual_central' o 'distribuida').

    Returns:
        Dict[str, float]: Un diccionario con los siguientes campos:
            - momento_mx: El momento de flexión en N.mm
            - posición: La posición del punto de aplicación de la carga (en metros)
            - unidad: La unidad del momento de flexión

    Raises:
        ValueError: Si el tipo_carga no es 'puntual_central' ni 'distribuida',
                   o si longitud <= 0 o carga <= 0.
    """
    if tipo_carga not in ['puntual_central', 'distribuida']:
        raise ValueError("El tipo de carga debe ser 'puntual_central' o 'distribuida'")
    
    if longitud <= 0 or carga <= 0:
        raise ValueError("La longitud y la carga deben ser mayores que cero")
    
    if tipo_carga == 'puntual_central':
        momento = carga * longitud / 4
    elif tipo_carga == 'distribuida':
        momento = carga * (longitud ** 2) / 8
    
    return {
        'momento_mx': float(momento),
        'posición': longitud / 2,
        'unidad': 'N.mm'
    }
