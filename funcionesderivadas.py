import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
import math

def procedimMax():
    x = sp.symbols("x")
    funcion = sp.sympify(problema)

    primera_derivada = sp.diff(funcion, x)

    puntos_criticos = sp.solve(primera_derivada, x)

    segunda_derivada = sp.diff(primera_derivada, x)

    st.divider()