from data.PharmGKB.pharmgkb import PharmGKB
from utils.utils import tsv_to_csv, read_file
from agents.csv_agent import CSVAgent

import streamlit as st


# Create PharmGKB instance
pharmgkb = PharmGKB()

# Download content
pharmgkb.download()

# Create CSV agent
csv_agent = CSVAgent()

#########################################################


# Cambiar el título de la página
st.title("Clinical Annotations")

# Añadir un poco de espacio en blanco para mejorar la estética
st.write("")

# Crear un contenedor para el input y el botón Run
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
