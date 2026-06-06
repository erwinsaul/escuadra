"""
Módulo para la conversión de temperaturas.
Implementa conversiones entre Celsius, Fahrenheit y Kelvin.
"""

def celsius_a_fahrenheit(c):
    """
    Convierte grados Celsius a Fahrenheit.
    Fórmula utilizada: F = C * (9/5) + 32
    """
    return c * (9 / 5) + 32

def fahrenheit_a_celsius(f):
    """
    Convierte grados Fahrenheit a Celsius.
    Fórmula utilizada: C = (F - 32) * (5/9)
    """
    return (f - 32) * (5 / 9)

def celsius_a_kelvin(c):
    """
    Convierte grados Celsius a Kelvin.
    Fórmula utilizada: K = C + 273.15
    """
    return c + 273.15

def kelvin_a_celsius(k):
    """
    Convierte Kelvin a grados Celsius.
    Fórmula utilizada: C = K - 273.15
    """
    if k < 0:
        raise ValueError("Error: La temperatura en Kelvin no puede ser negativa (bajo cero absoluto).")
    return k - 273.15