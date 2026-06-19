import pandas as pd

# ========================================
# EJERCICIO 1: Crear un DataFrame
# ========================================

datos = {
    "Nombre": ["Ana", "Luis", "Marta", "Pedro"],
    "Edad": [23, 30, 25, 27],
    "Ciudad": ["Madrid", "Barcelona", "Valencia", "Sevilla"],
    "Puntaje": [85, 90, 78, 92]
}

df = pd.DataFrame(datos)

print("DataFrame original:")
print(df)

# ========================================
# EJERCICIO 2: Filtrar datos
# ========================================

mayores_25 = df[df["Edad"] > 25]

print("\nPersonas con edad mayor a 25:")
print(mayores_25)

# ========================================
# EJERCICIO 3: Estadísticas básicas
# ========================================

edad_media = df["Edad"].mean()
edad_maxima = df["Edad"].max()
edad_minima = df["Edad"].min()
puntaje_medio = df["Puntaje"].mean()

print("\nEstadisticas:")
print("Edad media:", edad_media)
print("Edad maxima:", edad_maxima)
print("Edad minima:", edad_minima)
print("Puntaje medio:", puntaje_medio)

# ========================================
# EJERCICIO 4: Agregar nueva columna
# ========================================

df["Aprobado"] = df["Puntaje"].apply(
    lambda x: "Sí" if x >= 80 else "No"
)

print("\nDataFrame con columna 'Aprobado':")
print(df)