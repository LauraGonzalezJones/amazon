
import pandas as pd

# Leer el archivo CSV de Amazon
datos = pd.read_csv(
    "amazon.csv",
    usecols=["asin", "stars", "price", "categoryName"]
)

# Mostrar las primeras cinco filas
print(datos.head())

# Mostrar la cantidad total de registros
print("Cantidad de registros:", len(datos))

# GRAFICO 1: Calificaciones de productos Amazon

import matplotlib.pyplot as plt

# Seleccionar calificaciones validas
calificaciones = datos["stars"]
calificaciones = calificaciones[
    calificaciones.between(1, 5)
]

# Crear grafico
plt.figure(figsize=(9, 5))
plt.hist(calificaciones, bins=20, edgecolor="black")

plt.title("Distribucion de calificaciones Amazon")
plt.xlabel("Calificacion en estrellas")
plt.ylabel("Cantidad de productos")

plt.tight_layout()
plt.savefig("grafico_calificaciones.png")
plt.show()


# GRAFICO 2: Cantidad de productos por categoria

# Contar los productos de cada categoria
categorias = datos["categoryName"].value_counts()

# Seleccionar las 10 categorias con mas productos
top_categorias = categorias.head(10)

# Crear el grafico
plt.figure(figsize=(12, 7))

plt.barh(
    top_categorias.index[::-1],
    top_categorias.values[::-1],
    color="steelblue"
)

plt.title("Top 10 categorias con mas productos en Amazon")
plt.xlabel("Cantidad de productos")
plt.ylabel("Categorias")

plt.tight_layout()

# Guardar el grafico
plt.savefig("grafico_categorias.png", bbox_inches="tight")

# Mostrar el grafico
plt.show()


# GRAFICO 3: Precio mediano por categoria

# Convertir los precios a numeros
datos["price"] = pd.to_numeric(
    datos["price"], errors="coerce"
)

# Seleccionar productos con precios mayores a cero
productos_precio = datos[datos["price"] > 0]

# Calcular el precio mediano por categoria
precios_categoria = productos_precio.groupby(
    "categoryName"
)["price"].median()

# Seleccionar las mismas 10 categorias del grafico anterior
top_precios = precios_categoria.reindex(
    top_categorias.index
).dropna().sort_values()

# Crear el grafico
plt.figure(figsize=(12, 7))

plt.barh(
    top_precios.index,
    top_precios.values,
    color="steelblue"
)

plt.title("Precio mediano por categoria en Amazon")
plt.xlabel("Precio mediano (reales brasilenos)")
plt.ylabel("Categorias")

plt.tight_layout()

# Guardar el grafico
plt.savefig("grafico_precios.png", bbox_inches="tight")

# Mostrar el grafico
plt.show()
