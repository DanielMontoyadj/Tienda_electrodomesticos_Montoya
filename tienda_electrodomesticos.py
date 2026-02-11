import streamlit as st
import pandas as pd
from datetime import date


st.title("Tienda de Electrodomésticos Montoya")


productos = [
    {"Producto": "Televisores", "Precio": 18000, "Categoría": "Línea blanca"},
    {"Producto": "Microondas", "Precio": 3250, "Categoría": "Cocina"},
    {"Producto": "Licuadora", "Precio": 800, "Categoría": "Cocina"},
    {"Producto": "consolas", "Precio": 22000, "Categoría": "Entretenimiento"},
    {"Producto": "Plancha", "Precio": 1200, "Categoría": "Hogar"},
    {"Producto": "Secadoras", "Precio": 2000, "Categoría": "Entretenimiento"},
    {"Producto": "Cafetera", "Precio": 1200, "Categoría": "Cocina"},
]

df = pd.DataFrame(productos)

st.subheader("Filtro de productos")

precio_max = st.slider(
    "Seleccione el precio máximo:",
    min_value=1000,
    max_value=30000,
    value=30000,
    step=500
)

df_filtrado = df[df["Precio"] <= precio_max]

st.dataframe(df_filtrado, use_container_width=True)

st.subheader("Selección de producto")

producto_seleccionado = st.selectbox(
    "Seleccione un electrodoméstico:",
    df_filtrado["Producto"]
)

producto_info = df[df["Producto"] == producto_seleccionado].iloc[0]

cantidad = st.number_input(
    "Cantidad:",
    min_value=1,
    value=1,
    step=1
)

precio_unitario = producto_info["Precio"]
subtotal_producto = precio_unitario * cantidad

st.markdown("###Resumen del producto###")
st.write(f"**Producto:** {producto_seleccionado}")
st.write(f"**Categoría:** {producto_info['Categoría']}")
st.write(f"**Precio unitario:** L {precio_unitario:,.2f}")
st.write(f"**Cantidad:** {cantidad}")
st.write(f"**Subtotal:** L {subtotal_producto:,.2f}")

st.subheader("Datos del cliente")

nombre_cliente = st.text_input("Nombre del cliente:")
identidad = st.text_input("RTN / Identidad:")
fecha_factura = st.date_input("Fecha:", value=date.today())


st.subheader("Factura")

isv = subtotal_producto * 0.15
total_pagar = subtotal_producto + isv

factura = pd.DataFrame({
    "Producto": [producto_seleccionado],
    "Cantidad": [cantidad],
    "Precio Unitario": [precio_unitario],
    "Subtotal": [subtotal_producto]
})

st.table(factura)

st.markdown("###Totales a pagar")
st.write(f"**Subtotal general:** L {subtotal_producto:,.2f}")
st.write(f"**ISV (15%):** L {isv:,.2f}")
st.write(f"**Total a pagar:** L {total_pagar:,.2f}")


