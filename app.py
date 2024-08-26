import os.path
from glob import glob
import streamlit as st
from data.EMA.ema import EMA
from data.PharmGKB.pharmgkb import PharmGKB
from agents.csv_agent import CSVAgent

# Download data and convert to csv format
[data.download() for data in [PharmGKB(), EMA()]]

# Create CSV agent
csv_agent = CSVAgent()

#########################################################

# Title
st.title("Clinical Annotations")

# Input tables
tables = [os.path.basename(table) for table in glob("data/PharmGKB/files/*.csv")]
table_option = st.selectbox("Select a table:", tables)

csv_agent.set_table(f"data/PharmGKB/files/{table_option}")

# Space
st.write("")

# Create container for Input and Run buttons
container = st.container()

with container:
    # Input box para que el usuario escriba su query
    query = st.text_area("Enter your query here:", height=150)

    # Botón de "Run" alineado con la esquina izquierda de la caja de pregunta
    if st.button("Run"):
        if query:
            # Mostrar el mensaje de carga
            with st.spinner("Loading..."):
                # Llamada a la función execute con el query ingresado por el usuario
                result = csv_agent.execute(query)
            # Mostrar el resultado en un área de texto del mismo tamaño que la de entrada
            st.text_area("Result:", value=result["output"], height=150)
        else:
            st.warning("Please enter a query before running.")
