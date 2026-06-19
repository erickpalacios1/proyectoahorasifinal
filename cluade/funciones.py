import sympy as sp
import numpy as np


def validar_funcion(func_str):
    """Valida que func_str sea una expresión SymPy parseable en términos de x.
    Retorna (True, None) si es válida, o (False, mensaje_error) si falla."""
    if not func_str or not func_str.strip():
        return False, "La función no puede estar vacía."
    try:
        sp.sympify(func_str)
        return True, None
    except Exception as e:
        return False, str(e)


def calcular_integral_definida(func_str, a, b):
    """Calcula la integral definida ∫_a^b f(x) dx usando SymPy integrate().
    Retorna (expr, resultado): la expresión simbólica y el resultado exacto."""
    x = sp.Symbol('x')
    expr = sp.sympify(func_str)
    resultado = sp.integrate(expr, (x, a, b))
    return expr, resultado


def obtener_resultado_decimal(resultado_exacto):
    """Convierte un resultado de SymPy a float de Python.
    Retorna el valor decimal o None si la conversión no es posible."""
    try:
        val = complex(resultado_exacto.evalf())
        if abs(val.imag) < 1e-10:
            return val.real
        return None
    except Exception:
        return None


def generar_datos_grafica(func_str, a, b):
    """Genera arreglos NumPy para la curva completa y el área de integración.
    Retorna (x_vals, y_vals, x_area, y_area) como arreglos NumPy."""
    x = sp.Symbol('x')
    expr = sp.sympify(func_str)
    f_lambda = sp.lambdify(x, expr, modules=['numpy'])

    rango = abs(float(b) - float(a)) if b != a else 1.0
    margen = max(rango * 0.4, 0.5)
    x_vals = np.linspace(float(a) - margen, float(b) + margen, 600)
    x_area = np.linspace(float(a), float(b), 600)

    y_vals = _evaluar_seguro(f_lambda, x_vals)
    y_area = _evaluar_seguro(f_lambda, x_area)
    return x_vals, y_vals, x_area, y_area


def _evaluar_seguro(f_lambda, x_arr):
    """Evalúa f_lambda sobre x_arr; reemplaza valores no finitos con NaN."""
    try:
        y = np.asarray(f_lambda(x_arr), dtype=float)
        if y.ndim == 0:
            y = np.full(x_arr.shape, float(y))
    except Exception:
        y = np.array([_eval_punto(f_lambda, xi) for xi in x_arr])
    return np.where(np.isfinite(y), y, np.nan)


def _eval_punto(f_lambda, xi):
    """Evalúa f_lambda en un solo punto; retorna NaN ante cualquier error."""
    try:
        v = float(f_lambda(xi))
        return v if np.isfinite(v) else np.nan
    except Exception:
        return np.nan


# ── Funciones para el módulo de Derivadas ────────────────────────────────────

def calcular_derivada(func_str):
    """Calcula la derivada de f(x) con respecto a x usando SymPy diff().
    Retorna (expr, derivada) como expresiones simbólicas."""
    x = sp.Symbol('x')
    expr = sp.sympify(func_str)
    derivada = sp.diff(expr, x)
    return expr, derivada


def calcular_recta_tangente(func_str, x0):
    """Calcula la recta tangente a f(x) en x = x0.
    Retorna (expr, derivada, y0, pendiente, tangente) como expresiones SymPy."""
    x = sp.Symbol('x')
    expr = sp.sympify(func_str)
    derivada = sp.diff(expr, x)
    y0 = expr.subs(x, x0)
    pendiente = derivada.subs(x, x0)
    tangente = sp.expand(pendiente * (x - x0) + y0)
    return expr, derivada, y0, pendiente, tangente


def encontrar_criticos(func_str, a, b):
    """Encuentra y clasifica los puntos críticos de f en [a, b].
    Usa f'(x) = 0 y la prueba de la segunda derivada para determinar el tipo.
    Retorna (expr, derivada, segunda_derivada, lista_criticos)."""
    x = sp.Symbol('x')
    expr = sp.sympify(func_str)
    derivada = sp.diff(expr, x)
    segunda = sp.diff(derivada, x)

    try:
        soluciones = sp.solve(derivada, x)
    except Exception:
        soluciones = []

    criticos = []
    for c in soluciones:
        try:
            if not c.is_real:
                continue
            c_float = float(c.evalf())
            if not (float(a) <= c_float <= float(b)):
                continue

            y_val = expr.subs(x, c)
            seg_num = float(segunda.subs(x, c).evalf())

            if seg_num > 1e-10:
                tipo = "Minimo local"
            elif seg_num < -1e-10:
                tipo = "Maximo local"
            else:
                tipo = "Punto de inflexion posible"

            criticos.append({
                'x_sym': c,
                'x_num': c_float,
                'y_sym': y_val,
                'y_num': float(y_val.evalf()),
                'tipo': tipo,
                'seg_num': seg_num,
            })
        except Exception:
            continue

    return expr, derivada, segunda, criticos


def generar_datos_derivada(func_str, a, b):
    """Genera arreglos NumPy para graficar f(x) y f'(x) en el intervalo [a, b].
    Retorna (x_vals, y_vals, dy_vals)."""
    x = sp.Symbol('x')
    expr = sp.sympify(func_str)
    derivada = sp.diff(expr, x)

    f_lambda = sp.lambdify(x, expr, modules=['numpy'])
    df_lambda = sp.lambdify(x, derivada, modules=['numpy'])

    x_vals = np.linspace(float(a), float(b), 600)
    y_vals = _evaluar_seguro(f_lambda, x_vals)
    dy_vals = _evaluar_seguro(df_lambda, x_vals)
    return x_vals, y_vals, dy_vals
