def interes_simple(capital, tasa, tiempo):
    """
    Calcula el interés simple.

    Fórmula:
        I = capital * tasa * tiempo

    Parámetros:
        capital (float): Cantidad inicial de dinero. Debe ser mayor que 0.
        tasa (float): Tasa de interés (en decimal, por ejemplo 0.05 para 5%). Debe ser mayor o igual a 0.
        tiempo (float): Tiempo en años. Debe ser mayor que 0.

    Retorna:
        float: Interés generado.

    Lanza:
        TypeError: Si los valores no son numéricos.
        ValueError: Si los valores son negativos o cero cuando no corresponde.
    """

    # Validar tipos
    if not isinstance(capital, (int, float)):
        raise TypeError("El capital debe ser un número.")
    if not isinstance(tasa, (int, float)):
        raise TypeError("La tasa debe ser un número.")
    if not isinstance(tiempo, (int, float)):
        raise TypeError("El tiempo debe ser un número.")

    # Validar valores
    if capital <= 0:
        raise ValueError("El capital debe ser mayor que 0.")
    if tasa < 0:
        raise ValueError("La tasa no puede ser negativa.")
    if tiempo <= 0:
        raise ValueError("El tiempo debe ser mayor que 0.")

    return capital * tasa * tiempo