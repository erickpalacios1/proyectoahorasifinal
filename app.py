import streamlit as st
import matplotlib.pyplot as plt
import math
import numpy as np
import sympy as sp
from streamlit_option_menu import option_menu

with st.sidebar:
    selected = option_menu("Calculadora pro",[
    "Inicio",
    "Geometria Analitica",
    "Aplicacion de derivadas",
    "Integrales Definidas",
    ],
   icons=["house", "calculator" ,"calculator","calculator"], 
   menu_icon="gear", 
   default_index=0,
   orientation="vertical")#con style=puedes modificar el tamao del texto y creo que los colores mas pero nose

if selected =="Inicio":
    st.title("Calculadora de Calculo", text_alignment="center")
    st.header("proyecto final de programacion I",divider=None,text_alignment="center")
    st.image("https://i0.wp.com/erasmusbravioo.com/wp-content/uploads/2024/07/subcat-2152-1.jpg?fit=800%2C440&ssl=1",use_container_width=True)
    colum1, colum2 = st.columns(2)
    with colum1:
        st.markdown("### 📌sobre la aplicacion", text_alignment="left")
        st.markdown("Esta herramienta interactiva fue desarrollada para resolver problemas fundamentales de Cálculo Diferencial e Integral. La aplicación permite a los usuarios ingresar funciones matemáticas y obtener resultados precisos acompañados, en muchos casos, del procedimiento paso a paso y su respectiva representación gráfica.",text_alignment="justify")
        st.markdown("### ✨ Características Principales",text_alignment="left")
        st.markdown("""
        - ⚡ **Cálculo de derivadas** (primeras y orden superior).
        - 🔄 **Cálculo de integrales** (definidas e indefinidas).
        - 🎯 **Evaluación de límites** (laterales y al infinito).
        - 📈 **Gráficas interactivas** en 2D.
        - 📝 **Procedimiento paso a paso** para facilitar el aprendizaje.
        """,text_alignment="justify")
        with colum2:
            st.markdown("### 🎓 Datos del Proyecto")
            st.markdown(""" 
                        - Estudiantes: 
                        - **Luis Fernando Chumacero Carvajal**.
                        - **Erick Gabriel Palacios Lahor**.
                        - **Carrera: Ingeniería de Sistemas**.
                        - **Universidad: Universidad Privada del Valle (Univalle)**.
                        - **Docente: ING. Condo**.
                        - **Gestión: 2026**""",text_alignment="justify")

    
    
if selected == "Geometria Analitica":
    st.title("Calculadora de Geometría Analítica")
    tema = st.selectbox(
        "¿Qué quieres calcular?",
        [
            "Distancia entre dos puntos",
            "Punto medio",
            "Ecuación de la recta (dos puntos)",
            "Pendiente e intersección",
            "Ecuación de la circunferencia",    
            "Parabola",
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
            d = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
            st.success(f"Distancia = {d:.4f}")

            fig, ax = plt.subplots()
            ax.plot([x1, x2], [y1, y2], "bo-", linewidth=2, markersize=8)
            ax.annotate(f"A({x1}, {y1})", (x1, y1), textcoords="offset points", xytext=(8, 8))
            ax.annotate(f"B({x2}, {y2})", (x2, y2), textcoords="offset points", xytext=(8, 8))
            ax.annotate(f"d = {d:.3f}", ((x1+x2)/2, (y1+y2)/2), textcoords="offset points", xytext=(8, 8), color="red")
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
            ax.annotate(f"r={r}", (h + r/2, k), textcoords="offset points", xytext=(0, 8), ha="center", color="green")
            ax.set_aspect("equal")
            ax.grid(True)
            ax.legend()
            st.pyplot(fig)
            
            
    elif tema == "Parabola":
        st.subheader("Parábola")

        tipo = st.selectbox("Tipo de parábola", [
            "Vertical  (x - h)² = 4p(y - k)",
            "Horizontal  (y - k)² = 4p(x - h)"
        ])

        if tipo.startswith("Vertical"):
            st.latex(r"(x - h)^2 = 4p\,(y - k)")
        else:
            st.latex(r"(y - k)^2 = 4p\,(x - h)")

        st.write("**(h, k)** es el vértice y **p** es la distancia del vértice al foco.")

        col1, col2, col3 = st.columns(3)
        with col1:
            h = st.number_input("Vértice h", value=0.0)
        with col2:
            k = st.number_input("Vértice k", value=0.0)
        with col3:
            p = st.number_input("Parámetro p (≠ 0)", value=2.0)

        if st.button("Calcular"):
            if p == 0:
                st.error("El parámetro p no puede ser 0.")
            else:
                lado_recto = abs(4 * p)

                if tipo.startswith("Vertical"):
                    foco = (h, k + p)
                    directriz_texto = f"y = {k - p}"
                    eje_texto = f"x = {h}"
                    st.latex(rf"(x - {h})^2 = {4*p}(y - {k})")
                else:
                    foco = (h + p, k)
                    directriz_texto = f"x = {h - p}"
                    eje_texto = f"y = {k}"
                    st.latex(rf"(y - {k})^2 = {4*p}(x - {h})")

                col_a, col_b, col_c, col_d = st.columns(4)
                with col_a:
                    st.metric("Vértice", f"({h}, {k})")
                with col_b:
                    st.metric("Foco", f"({foco[0]}, {foco[1]})")
                with col_c:
                    st.metric("Directriz", directriz_texto)
                with col_d:
                    st.metric("Lado recto", f"{lado_recto}")

                rango = max(abs(4 * p), 5)
                fig, ax = plt.subplots()

                if tipo.startswith("Vertical"):
                    xs = np.linspace(h - rango, h + rango, 500)
                    ys = k + (xs - h) ** 2 / (4 * p)
                    ax.plot(xs, ys, "b-", linewidth=2, label="Parábola")
                    ax.axhline(k - p, color="green", linestyle="--", linewidth=1.5, label=f"Directriz: {directriz_texto}")
                    ax.axvline(h, color="gray", linestyle=":", linewidth=1.2, label=f"Eje: {eje_texto}")
                else:
                    ys = np.linspace(k - rango, k + rango, 500)
                    xs = h + (ys - k) ** 2 / (4 * p)
                    ax.plot(xs, ys, "b-", linewidth=2, label="Parábola")
                    ax.axvline(h - p, color="green", linestyle="--", linewidth=1.5, label=f"Directriz: {directriz_texto}")
                    ax.axhline(k, color="gray", linestyle=":", linewidth=1.2, label=f"Eje: {eje_texto}")

                ax.plot(h, k, "ko", markersize=8, label=f"Vértice ({h}, {k})")
                ax.annotate(f"V({h},{k})", (h, k), textcoords="offset points", xytext=(8, 8))
                ax.plot(foco[0], foco[1], "ro", markersize=8, label=f"Foco ({foco[0]}, {foco[1]})")
                ax.annotate(f"F({foco[0]},{foco[1]})", (foco[0], foco[1]), textcoords="offset points", xytext=(8, -14), color="red")
                ax.axhline(0, color="gray", linewidth=0.8)
                ax.axvline(0, color="gray", linewidth=0.8)
                ax.grid(True)
                ax.legend()
                st.pyplot(fig)
        



elif selected == "Aplicacion de derivadas":
    st.header("Aplicacion de Derivadas")
    x=sp.symbols("x")
    funcion_texto = st.text_input(
    "Ingrese la función f(x)",
    value="-x**2 + 8*x + 3"
    )

    if st.button("Resolver"):

        try:
            funcion = sp.sympify(funcion_texto)

            primera_derivada = sp.diff(funcion, x)

            puntos_criticos = sp.solve(primera_derivada, x)

            segunda_derivada = sp.diff(primera_derivada, x)

            st.divider()
            col1, col2, col3 = st.columns(3)

            if len(puntos_criticos) > 0:

                punto = puntos_criticos[0]

                valor_segunda = segunda_derivada.subs(x, punto)
                valor_funcion = funcion.subs(x, punto)

                if valor_segunda > 0:
                    tipo = "Mínimo"
                elif valor_segunda < 0:
                    tipo = "Máximo"
                else:
                    tipo = "Indeterminado"

                with col1:
                    st.metric("Punto crítico", f"x = {sp.N(punto)}")

                with col2:
                    st.metric("Clasificación", tipo)

                with col3:
                    st.metric("Valor de f(x)", f"{sp.N(valor_funcion)}")

            tabs = st.tabs([
                "Paso 1",
                "Paso 2",
                "Paso 3",
                "Paso 4",
                "Paso 5",
                "Paso 6",
                "Paso 7"
            ])

            with tabs[0]:
                st.subheader("Identificar la función objetivo")

                st.latex(
                    f"f(x) = {sp.latex(funcion)}"
                )

                st.write(
                    "El objetivo es determinar si la función posee máximos o mínimos."
                )

            with tabs[1]:
                st.subheader("Calcular la primera derivada")

                st.latex(
                    f"f'(x) = {sp.latex(primera_derivada)}"
                )

            with tabs[2]:
                st.subheader("Encontrar puntos críticos")

                st.latex(
                    f"{sp.latex(primera_derivada)} = 0"
                )

                st.write("Soluciones:")

                for p in puntos_criticos:
                    st.latex(
                        f"x = {sp.latex(p)}"
                    )

            with tabs[3]:
                st.subheader("Calcular la segunda derivada")

                st.latex(
                    f"f''(x) = {sp.latex(segunda_derivada)}"
                )

            with tabs[4]:
                st.subheader("Clasificar el punto crítico")

                for p in puntos_criticos:

                    valor = segunda_derivada.subs(x, p)

                    st.latex(
                        f"f''({sp.latex(p)}) = {sp.latex(valor)}"
                    )

                    if valor > 0:
                        st.success(f"x = {p} es un mínimo local")

                    elif valor < 0:
                        st.success(f"x = {p} es un máximo local")

                    else:
                        st.warning(
                            f"x = {p} requiere otro criterio de análisis"
                        )

            with tabs[5]:
                st.subheader("Evaluar la función")

                for p in puntos_criticos:

                    valor = funcion.subs(x, p)

                    st.latex(
                        f"f({sp.latex(p)}) = {sp.latex(valor)}"
                    )

            with tabs[6]:
                st.subheader("Interpretación")

                for p in puntos_criticos:

                    valor_segunda = segunda_derivada.subs(x, p)
                    valor_funcion = funcion.subs(x, p)

                    if valor_segunda > 0:

                        st.write(
                            f"La función presenta un mínimo local en x = {p}."
                        )

                        st.write(
                            f"El valor mínimo es {valor_funcion}."
                        )

                    elif valor_segunda < 0:

                        st.write(
                            f"La función presenta un máximo local en x = {p}."
                        )

                        st.write(
                            f"El valor máximo es {valor_funcion}."
                        )
        except Exception as e:
            st.error(f"Error: {e}")
    #grafica




elif selected == "Integrales Definidas":
    st.header("Integrales definidas")
    x = sp.symbols("x")
    y = sp.symbols("y")

    proplem1 = st.text_input(
        "Ingrese su función respecto a x o y",
        value="x**2 + 8"
    )

    st.divider()
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("**Límite inferior**")
        inferior = st.number_input("Límite inferior", value=0.0, key="li")
    with col2:
        st.markdown("**Límite superior**")
        superior = st.number_input("Límite superior", value=3.0, key="ls")
    st.divider()

    if st.button("Resolver"):
        try:
            expr = sp.sympify(proplem1)
            free = expr.free_symbols
            if y in free and x not in free:
                var = y
            else:
                var = x
            st.subheader("Procedimiento")

            st.write("**Función ingresada:**")
            st.latex(r"\int_{" + str(inferior) + r"}^{" + str(superior) + r"} " + sp.latex(expr) + r" \, d" + str(var))

            antiderivada = sp.integrate(expr, var)
            st.write("**Antiderivada (integral indefinida):**")
            st.latex("F(" + str(var) + ") = " + sp.latex(antiderivada) + " + C")

            st.write("**Aplicando el Teorema Fundamental del Cálculo:**")
            st.latex(
                r"F(" + str(superior) + r") - F(" + str(inferior) + r")"
                + r" = \left[" + sp.latex(antiderivada) + r"\right]_{" + str(inferior) + r"}^{" + str(superior) + r"}"
            )

            val_sup = antiderivada.subs(var, superior)
            val_inf = antiderivada.subs(var, inferior)
            resultado = sp.simplify(val_sup - val_inf)

            st.write("**Resultado:**")
            st.latex(
                sp.latex(val_sup) + " - (" + sp.latex(val_inf) + ") = " + sp.latex(resultado)
            )
            st.success(f"Resultado de la integral definida: {float(resultado):.6f}")

            st.subheader("Gráfica con área sombreada")
            f_num = sp.lambdify(var, expr, "numpy")

            margen = abs(superior - inferior) * 0.5 if superior != inferior else 1.0
            x_min = float(inferior) - margen
            x_max = float(superior) + margen
            x_vals = np.linspace(x_min, x_max, 600)

            try:
                y_vals = f_num(x_vals).astype(float)
            except Exception:
                y_vals = np.array([float(f_num(v)) for v in x_vals])

            x_fill = np.linspace(float(inferior), float(superior), 600)
            try:
                y_fill = f_num(x_fill).astype(float)
            except Exception:
                y_fill = np.array([float(f_num(v)) for v in x_fill])

            fig, ax = plt.subplots(figsize=(8, 5))
            ax.plot(x_vals, y_vals, color="#2563EB", linewidth=2.5, label=f"f({var}) = {sp.latex(expr)}")
            ax.fill_between(x_fill, y_fill, alpha=0.35, color="#3B82F6", label=f"Área ≈ {float(resultado):.4f}")
            ax.axhline(0, color="black", linewidth=0.8)
            ax.axvline(float(inferior), color="#EF4444", linestyle="--", linewidth=1.2, label=f"{var} = {inferior} (inferior)")
            ax.axvline(float(superior), color="#10B981", linestyle="--", linewidth=1.2, label=f"{var} = {superior} (superior)")
            ax.set_xlabel(str(var), fontsize=12)
            ax.set_ylabel(f"f({var})", fontsize=12)
            ax.set_title("Integral Definida", fontsize=14)
            ax.legend()
            ax.grid(True, alpha=0.3)
            st.pyplot(fig)

        except Exception as e:
            st.error(f"Error al resolver: {e}")
        