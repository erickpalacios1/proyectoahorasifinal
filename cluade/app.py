import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import math
import sympy as sp
from funciones import (
    validar_funcion,
    calcular_integral_definida,
    obtener_resultado_decimal,
    generar_datos_grafica,
    calcular_derivada,
    calcular_recta_tangente,
    encontrar_criticos,
    generar_datos_derivada,
)

# ── Sidebar ───────────────────────────────────────────────────────────────────
st.sidebar.title("Que quieres Calcular?")
page = st.sidebar.radio(
    "Opciones",
    [
        "Inicio",
        "Geometria Analitica",
        "Aplicacion de derivadas",
        "Integrales Definidas",
    ],
)

# ── Inicio ────────────────────────────────────────────────────────────────────
if page == "Inicio":
    st.title("🧮 Bienvenidos a la calculadora!")
    st.markdown(
        "La calculadora puede calcular geometria analitica, "
        "aplicaciones de derivadas e integrales definidas"
    )

# ── Geometría Analítica ───────────────────────────────────────────────────────
if page == "Geometria Analitica":
    st.title("Calculadora de Geometría Analítica")
    tema = st.selectbox(
        "¿Qué quieres calcular?",
        [
            "Distancia entre dos puntos",
            "Punto medio",
            "Ecuación de la recta (dos puntos)",
            "Pendiente e intersección",
            "Ecuación de la circunferencia",
        ],
    )

    st.divider()

    if tema == "Distancia entre dos puntos":
        st.subheader("Distancia entre dos puntos")
        st.latex(r"d = \sqrt{(x_2 - x_1)^2 +    (y_2 - y_1)^2}")

        col1, col2 = st.columns(2)
        with col1:
            st.write("**Punto A**")
            x1 = st.number_input("x₁", value=0.0)
            y1 = st.number_input("y₁", value=0.0)
        with col2:
            st.write("**Punto B**")
            x2 = st.number_input("x₂", value=3.0)
            y2 = st.number_input("y₂", value=4.0)

        if st.button("Calcular"):
            d = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
            st.success(f"Distancia = {d:.4f}")

            fig, ax = plt.subplots()
            ax.plot([x1, x2], [y1, y2], "bo-", linewidth=2, markersize=8)
            ax.annotate(f"A({x1}, {y1})", (x1, y1), textcoords="offset points", xytext=(8, 8))
            ax.annotate(f"B({x2}, {y2})", (x2, y2), textcoords="offset points", xytext=(8, 8))
            ax.annotate(
                f"d = {d:.3f}", ((x1 + x2) / 2, (y1 + y2) / 2),
                textcoords="offset points", xytext=(8, 8), color="red"
            )
            ax.axhline(0, color="gray", linewidth=0.8)
            ax.axvline(0, color="gray", linewidth=0.8)
            ax.grid(True)
            st.pyplot(fig)

    elif tema == "Punto medio":
        st.subheader("Punto Medio")
        st.latex(r"M = \left(\frac{x_1+x_2}{2},\ \frac{y_1+y_2}{2}\right)")

        col1, col2 = st.columns(2)
        with col1:
            st.write("**Punto A**")
            x1 = st.number_input("x₁", value=1.0)
            y1 = st.number_input("y₁", value=2.0)
        with col2:
            st.write("**Punto B**")
            x2 = st.number_input("x₂", value=5.0)
            y2 = st.number_input("y₂", value=8.0)

        if st.button("Calcular"):
            mx, my = (x1 + x2) / 2, (y1 + y2) / 2
            st.success(f"Punto medio M = ({mx:.4f}, {my:.4f})")

            fig, ax = plt.subplots()
            ax.plot([x1, x2], [y1, y2], "bo--", linewidth=1.5, markersize=8)
            ax.plot(mx, my, "ro", markersize=10, label=f"M({mx:.2f}, {my:.2f})")
            ax.annotate(f"A({x1},{y1})", (x1, y1), textcoords="offset points", xytext=(6, 6))
            ax.annotate(f"B({x2},{y2})", (x2, y2), textcoords="offset points", xytext=(6, 6))
            ax.annotate("M", (mx, my), textcoords="offset points", xytext=(6, 6), color="red", fontsize=10)
            ax.grid(True)
            ax.legend()
            st.pyplot(fig)

    elif tema == "Ecuación de la recta (dos puntos)":
        st.subheader("Ecuación de la Recta")
        st.latex(r"m = \frac{y_2 - y_1}{x_2 - x_1}, \quad y - y_1 = m(x - x_1)")

        col1, col2 = st.columns(2)
        with col1:
            st.write("**Punto A**")
            x1 = st.number_input("x₁", value=1.0)
            y1 = st.number_input("y₁", value=2.0)
        with col2:
            st.write("**Punto B**")
            x2 = st.number_input("x₂", value=4.0)
            y2 = st.number_input("y₂", value=8.0)

        if st.button("Calcular"):
            if x1 == x2:
                st.warning(f"Recta vertical: x = {x1}")
            else:
                m = (y2 - y1) / (x2 - x1)
                b = y1 - m * x1
                st.success(f"Pendiente m = {m:.4f} | Intercepto b = {b:.4f}")
                st.latex(rf"y = {m:.4f}\,x + {b:.4f}")

                fig, ax = plt.subplots()
                xs = np.linspace(min(x1, x2) - 2, max(x1, x2) + 2, 300)
                ax.plot(xs, m * xs + b, "b-", linewidth=2, label=f"y = {m:.2f}x + {b:.2f}")
                ax.plot([x1, x2], [y1, y2], "ro", markersize=8)
                ax.annotate(f"A({x1},{y1})", (x1, y1), textcoords="offset points", xytext=(6, 6))
                ax.annotate(f"B({x2},{y2})", (x2, y2), textcoords="offset points", xytext=(6, 6))
                ax.grid(True)
                ax.legend()
                st.pyplot(fig)

    elif tema == "Pendiente e intersección":
        st.subheader("Pendiente e Intersección con los ejes")
        st.latex(r"y = mx + b")

        m = st.number_input("Pendiente (m)", value=2.0)
        b = st.number_input("Intercepto (b)", value=-3.0)

        if st.button("Graficar"):
            y_int = b
            x_int = -b / m if m != 0 else None

            st.write(f"**Intercepto en Y:** (0, {y_int:.4f})")
            if x_int is not None:
                st.write(f"**Intercepto en X:** ({x_int:.4f}, 0)")
            else:
                st.write("Recta horizontal, no corta el eje X.")

            fig, ax = plt.subplots()
            xs = np.linspace(-8, 8, 300)
            ax.plot(xs, m * xs + b, "b-", linewidth=2, label=f"y = {m}x + {b}")
            ax.plot(0, y_int, "go", markersize=9, label=f"(0, {y_int:.2f})")
            if x_int is not None:
                ax.plot(x_int, 0, "ro", markersize=9, label=f"({x_int:.2f}, 0)")
            ax.axhline(0, color="gray", linewidth=0.8)
            ax.axvline(0, color="gray", linewidth=0.8)
            ax.set_xlim(-8, 8)
            ax.set_ylim(-10, 10)
            ax.grid(True)
            ax.legend()
            st.pyplot(fig)

    elif tema == "Ecuación de la circunferencia":
        st.subheader("Ecuación de la Circunferencia")
        st.latex(r"(x - h)^2 + (y - k)^2 = r^2")

        col1, col2, col3 = st.columns(3)
        with col1:
            h = st.number_input("Centro h", value=2.0)
        with col2:
            k = st.number_input("Centro k", value=3.0)
        with col3:
            r = st.number_input("Radio r", value=4.0, min_value=0.01)

        if st.button("Calcular"):
            st.success(f"Centro: ({h}, {k})  |  Radio: {r}")
            st.latex(rf"(x - {h})^2 + (y - {k})^2 = {r**2}")

            fig, ax = plt.subplots()
            theta = np.linspace(0, 2 * np.pi, 360)
            ax.plot(h + r * np.cos(theta), k + r * np.sin(theta), "b-", linewidth=2)
            ax.plot(h, k, "ro", markersize=8)
            ax.annotate(f"C({h},{k})", (h, k), textcoords="offset points", xytext=(6, 6), color="red")
            ax.plot([h, h + r], [k, k], "g--", linewidth=1.5, label=f"r = {r}")
            ax.annotate(
                f"r={r}", (h + r / 2, k),
                textcoords="offset points", xytext=(0, 8), ha="center", color="green"
            )
            ax.set_aspect("equal")
            ax.grid(True)
            ax.legend()
            st.pyplot(fig)

# ── Aplicación de Derivadas ───────────────────────────────────────────────────
if page == "Aplicacion de derivadas":
    st.title("Aplicación de Derivadas")
    st.write("Calcula derivadas, rectas tangentes y puntos críticos de una función.")
    st.latex(r"f'(x) = \lim_{h \to 0} \frac{f(x+h) - f(x)}{h}")
    st.divider()

    subtema = st.selectbox(
        "¿Qué quieres calcular?",
        [
            "Derivada de una función",
            "Recta tangente en un punto",
            "Máximos y mínimos locales",
        ],
    )
    st.divider()

    # ── Subtema 1: Derivada ───────────────────────────────────────────────────
    if subtema == "Derivada de una función":
        st.subheader("Derivada de una función")
        func_str = st.text_input(
            "Función f(x)",
            value="x**3 - 3*x",
            help="Ejemplos: x**3 - 3*x  |  sin(x)  |  x**2 + 2*x + 1",
            key="deriv_func",
        )
        col1, col2 = st.columns(2)
        with col1:
            a_d = st.number_input("Límite izquierdo del gráfico", value=-3.0, step=0.5, key="deriv_a")
        with col2:
            b_d = st.number_input("Límite derecho del gráfico", value=3.0, step=0.5, key="deriv_b")

        if st.button("Calcular derivada"):
            valida, error_msg = validar_funcion(func_str)
            if not valida:
                st.error(f"Función inválida: {error_msg}")
            elif a_d >= b_d:
                st.warning("El límite izquierdo debe ser menor que el derecho.")
            else:
                try:
                    expr, derivada = calcular_derivada(func_str)

                    st.divider()
                    st.subheader("Resultados")
                    st.write("**Función:**")
                    st.latex(rf"f(x) = {sp.latex(expr)}")
                    st.write("**Derivada:**")
                    st.latex(rf"f'(x) = {sp.latex(derivada)}")

                    st.divider()
                    st.subheader("Gráfica")
                    x_vals, y_vals, dy_vals = generar_datos_derivada(func_str, a_d, b_d)

                    fig, ax = plt.subplots(figsize=(8, 5))
                    ax.plot(x_vals, y_vals, "b-", linewidth=2, label=f"f(x) = {func_str}")
                    ax.plot(x_vals, dy_vals, "r--", linewidth=2, label="f'(x)")
                    ax.axhline(0, color="gray", linewidth=0.8)
                    ax.axvline(0, color="gray", linewidth=0.5)
                    ax.set_xlabel("x")
                    ax.set_ylabel("y")
                    ax.set_title("f(x) y su derivada f'(x)")
                    ax.grid(True)
                    ax.legend()
                    st.pyplot(fig)
                except Exception as e:
                    st.error(f"Error al calcular la derivada: {e}")

    # ── Subtema 2: Recta tangente ─────────────────────────────────────────────
    elif subtema == "Recta tangente en un punto":
        st.subheader("Recta Tangente en un Punto")
        func_str = st.text_input(
            "Función f(x)",
            value="x**2",
            help="Ejemplos: x**2  |  sin(x)  |  x**3 - x",
            key="tang_func",
        )
        x0 = st.number_input("Punto x₀", value=1.0, step=0.5, key="tang_x0")

        if st.button("Calcular recta tangente"):
            valida, error_msg = validar_funcion(func_str)
            if not valida:
                st.error(f"Función inválida: {error_msg}")
            else:
                try:
                    expr, derivada, y0, pendiente, tangente = calcular_recta_tangente(func_str, x0)

                    if y0.has(sp.zoo, sp.oo, sp.nan) or pendiente.has(sp.zoo, sp.oo, sp.nan):
                        st.error("La función no está definida en x₀. Elige otro punto.")
                    else:
                        y0_float = float(y0.evalf())
                        m_float = float(pendiente.evalf())
                        x0_str = str(int(x0)) if x0 == int(x0) else f"{x0:.4g}"

                        st.divider()
                        st.subheader("Resultados")

                        st.write("**Función:**")
                        st.latex(rf"f(x) = {sp.latex(expr)}")

                        st.write("**Derivada:**")
                        st.latex(rf"f'(x) = {sp.latex(derivada)}")

                        st.write("**Punto de tangencia:**")
                        st.latex(rf"\left({x0_str},\ {sp.latex(y0)}\right)")

                        st.write("**Pendiente en x₀:**")
                        st.latex(rf"f'({x0_str}) = {sp.latex(pendiente)}")

                        st.write("**Ecuación de la recta tangente:**")
                        st.latex(rf"y = {sp.latex(tangente)}")

                        st.divider()
                        st.subheader("Gráfica")
                        margen = max(abs(x0) * 0.5, 2.5)
                        x_vals, y_vals, _ = generar_datos_derivada(
                            func_str, x0 - margen, x0 + margen
                        )
                        y_tang = m_float * (x_vals - x0) + y0_float

                        fig, ax = plt.subplots(figsize=(8, 5))
                        ax.plot(x_vals, y_vals, "b-", linewidth=2, label=f"f(x) = {func_str}")
                        ax.plot(x_vals, y_tang, "r--", linewidth=2, label=f"Tangente en x₀ = {x0_str}")
                        ax.plot(x0, y0_float, "ro", markersize=10, zorder=5,
                                label=f"({x0_str}, {y0_float:.3f})")
                        ax.axhline(0, color="gray", linewidth=0.8)
                        ax.axvline(0, color="gray", linewidth=0.5)
                        ax.set_xlabel("x")
                        ax.set_ylabel("y")
                        ax.set_title(f"Recta tangente a f(x) en x = {x0_str}")
                        ax.grid(True)
                        ax.legend()
                        st.pyplot(fig)
                except Exception as e:
                    st.error(f"Error al calcular la recta tangente: {e}")

    # ── Subtema 3: Máximos y mínimos ──────────────────────────────────────────
    elif subtema == "Máximos y mínimos locales":
        st.subheader("Máximos y Mínimos Locales")
        st.write("Encuentra los puntos críticos usando f'(x) = 0 y la prueba de la segunda derivada.")
        func_str = st.text_input(
            "Función f(x)",
            value="x**3 - 3*x",
            help="Ejemplos: x**3 - 3*x  |  x**4 - 4*x**2  |  sin(x)",
            key="minmax_func",
        )
        col1, col2 = st.columns(2)
        with col1:
            a_m = st.number_input("Límite inferior del intervalo (a)", value=-3.0, step=0.5, key="minmax_a")
        with col2:
            b_m = st.number_input("Límite superior del intervalo (b)", value=3.0, step=0.5, key="minmax_b")

        if st.button("Encontrar extremos"):
            valida, error_msg = validar_funcion(func_str)
            if not valida:
                st.error(f"Función inválida: {error_msg}")
            elif a_m >= b_m:
                st.warning("El límite inferior debe ser menor que el superior.")
            else:
                try:
                    expr, derivada, segunda, criticos = encontrar_criticos(func_str, a_m, b_m)

                    st.divider()
                    st.subheader("Resultados")

                    st.write("**Función:**")
                    st.latex(rf"f(x) = {sp.latex(expr)}")
                    st.write("**Primera derivada:**")
                    st.latex(rf"f'(x) = {sp.latex(derivada)}")
                    st.write("**Segunda derivada:**")
                    st.latex(rf"f''(x) = {sp.latex(segunda)}")

                    st.divider()
                    if not criticos:
                        st.info(
                            f"No se encontraron puntos críticos en "
                            f"[{a_m:.4g}, {b_m:.4g}]."
                        )
                    else:
                        a_m_str = str(int(a_m)) if a_m == int(a_m) else f"{a_m:.4g}"
                        b_m_str = str(int(b_m)) if b_m == int(b_m) else f"{b_m:.4g}"
                        st.write(f"**Puntos críticos en [{a_m_str}, {b_m_str}]:**")
                        for i, c in enumerate(criticos):
                            st.write(f"**Punto {i + 1} — {c['tipo']}**")
                            col1, col2 = st.columns(2)
                            with col1:
                                st.latex(
                                    rf"x = {sp.latex(c['x_sym'])} \approx {c['x_num']:.4f}"
                                )
                            with col2:
                                st.latex(
                                    rf"f(x) = {sp.latex(c['y_sym'])} \approx {c['y_num']:.4f}"
                                )
                            st.write(f"f''(x) = {c['seg_num']:.4f}")
                            if i < len(criticos) - 1:
                                st.divider()

                    st.divider()
                    st.subheader("Gráfica")
                    x_vals, y_vals, dy_vals = generar_datos_derivada(func_str, a_m, b_m)

                    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 8))

                    ax1.plot(x_vals, y_vals, "b-", linewidth=2, label=f"f(x) = {func_str}")
                    for c in criticos:
                        color = "red" if "Maximo" in c['tipo'] else (
                            "green" if "Minimo" in c['tipo'] else "orange"
                        )
                        ax1.plot(
                            c['x_num'], c['y_num'], "o", color=color,
                            markersize=10, zorder=5,
                            label=f"{c['tipo']}: ({c['x_num']:.2f}, {c['y_num']:.2f})"
                        )
                    ax1.axhline(0, color="gray", linewidth=0.8)
                    ax1.set_ylabel("f(x)")
                    ax1.set_title(f"f(x) = {func_str} con puntos críticos")
                    ax1.grid(True)
                    ax1.legend()

                    ax2.plot(x_vals, dy_vals, "r-", linewidth=2, label="f'(x)")
                    ax2.axhline(0, color="gray", linewidth=1.5, linestyle="--", label="y = 0")
                    for c in criticos:
                        ax2.axvline(
                            c['x_num'], color="purple", linestyle=":", linewidth=1.5, alpha=0.8
                        )
                    ax2.set_xlabel("x")
                    ax2.set_ylabel("f'(x)")
                    ax2.set_title("f'(x) — Primera derivada")
                    ax2.grid(True)
                    ax2.legend()

                    plt.tight_layout()
                    st.pyplot(fig)
                except Exception as e:
                    st.error(f"Error al buscar extremos: {e}")

# ── Integrales Definidas ──────────────────────────────────────────────────────
if page == "Integrales Definidas":
    st.title("Integrales Definidas")
    st.write("Calcula el área bajo la curva de una función en el intervalo **[a, b]**.")
    st.latex(r"\int_a^b f(x)\, dx")
    st.divider()

    # ── Entrada de datos ──────────────────────────────────────────────────────
    func_str = st.text_input(
        "Función f(x)",
        value="x**2",
        help="Ejemplos: x**2  |  sin(x)  |  cos(x)  |  exp(x)  |  x**3 + 2*x",
    )
    col1, col2 = st.columns(2)
    with col1:
        a = st.number_input("Límite inferior (a)", value=0.0, step=0.5)
    with col2:
        b = st.number_input("Límite superior (b)", value=2.0, step=0.5)

    if st.button("Calcular integral"):

        # ── Validaciones ──────────────────────────────────────────────────────
        valida, error_msg = validar_funcion(func_str)

        if not valida:
            st.error(f"Función inválida: {error_msg}")

        elif b < a:
            st.warning(
                "El límite superior (b) debe ser mayor que el límite inferior (a). "
                "Intercambia los valores e intenta de nuevo."
            )

        elif a == b:
            st.warning("Los límites de integración son iguales. El valor de la integral es 0.")

        else:
            try:
                expr, resultado = calcular_integral_definida(func_str, a, b)

                # Formato limpio de los límites para mostrar en LaTeX
                a_str = str(int(a)) if a == int(a) else f"{a:.4g}"
                b_str = str(int(b)) if b == int(b) else f"{b:.4g}"

                # Detectar integral no evaluada o divergente
                if isinstance(resultado, sp.Integral):
                    st.warning(
                        "SymPy no pudo calcular esta integral de forma analítica. "
                        "Prueba simplificar la función o verificar su sintaxis."
                    )
                elif resultado.has(sp.oo) or resultado.has(sp.zoo) or resultado.has(sp.nan):
                    st.error(
                        "La integral diverge o no converge en el intervalo dado. "
                        "Verifica que f(x) esté definida y acotada en [a, b]."
                    )
                else:
                    decimal_val = obtener_resultado_decimal(resultado)

                    # ── Resultados ────────────────────────────────────────────
                    st.divider()
                    st.subheader("Resultados")

                    st.write("**1. Función ingresada:**")
                    st.latex(rf"f(x) = {sp.latex(expr)}")

                    st.write("**2. Integral planteada:**")
                    st.latex(
                        rf"\int_{{{a_str}}}^{{{b_str}}} {sp.latex(expr)} \, dx"
                    )

                    st.write("**3. Resultado exacto:**")
                    st.latex(
                        rf"\int_{{{a_str}}}^{{{b_str}}} {sp.latex(expr)} \, dx "
                        rf"= {sp.latex(resultado)}"
                    )

                    st.write("**4. Resultado decimal:**")
                    if decimal_val is not None:
                        st.success(f"{decimal_val:.6f}")
                    else:
                        st.info("El resultado es complejo o no se pudo convertir a decimal.")

                    # ── Gráfica ───────────────────────────────────────────────
                    st.divider()
                    st.subheader("Gráfica")
                    try:
                        x_vals, y_vals, x_area, y_area = generar_datos_grafica(
                            func_str, a, b
                        )

                        if decimal_val is not None:
                            titulo = (
                                f"Integral definida de f(x) = {func_str} "
                                f"en [{a_str}, {b_str}]  —  Area = {decimal_val:.4f}"
                            )
                        else:
                            titulo = f"Integral definida de f(x) = {func_str} en [{a_str}, {b_str}]"

                        fig, ax = plt.subplots(figsize=(8, 5))
                        ax.plot(
                            x_vals, y_vals,
                            "b-", linewidth=2, label=f"f(x) = {func_str}"
                        )
                        ax.fill_between(
                            x_area, y_area, 0,
                            alpha=0.35, color="steelblue",
                            label=f"Area integrada [{a_str}, {b_str}]"
                        )
                        ax.axvline(
                            a, color="red", linestyle="--", linewidth=1.5,
                            label=f"a = {a_str}"
                        )
                        ax.axvline(
                            b, color="green", linestyle="--", linewidth=1.5,
                            label=f"b = {b_str}"
                        )
                        ax.axhline(0, color="gray", linewidth=0.8)
                        ax.axvline(0, color="gray", linewidth=0.5)
                        ax.set_xlabel("x")
                        ax.set_ylabel("f(x)")
                        ax.set_title(titulo)
                        ax.grid(True)
                        ax.legend()
                        st.pyplot(fig)

                    except Exception as e:
                        st.error(f"No se pudo generar la gráfica: {e}")

            except ZeroDivisionError:
                st.error(
                    "División por cero: la función no está definida en parte del intervalo."
                )
            except Exception as e:
                st.error(f"Error al calcular la integral: {e}")
