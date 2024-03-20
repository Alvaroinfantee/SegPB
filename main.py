import streamlit as st
import pandas as pd

# Setting the page config to include favicon and title
st.set_page_config(
    page_title="ID Verification System",
    page_icon="PuebloBavaroLogo.png",  # Adjust the path as needed
    layout="centered"
)

# Load data from the Excel file
file_path = 'DBColegio.xlsx'  # Adjust the path as needed
data = pd.read_excel(file_path)


# Setting up the Streamlit interface
st.title('ID Verification System')

# Input for the ID or Cedula
user_input = st.text_input('Ingresar código o cédula:', '')

# Function to check the ID/Cedula and return name if found
def check_input_and_get_name(user_input):
    # Try matching by ID if the input is a digit
    if user_input.isdigit():
        user_input = int(user_input)
        if user_input in data['id'].values:
            name = data.loc[data['id'] == user_input, 'nombre'].values[0]
            return True, name
    # Try matching by Cedula in case ID match fails or input isn't a digit
    if user_input in data['cedula'].values:
        name = data.loc[data['cedula'] == user_input, 'nombre'].values[0]
        return True, name
    return False, None

# Display result
if user_input:  # Only proceed if user_input is not an empty string
    result, name = check_input_and_get_name(user_input)
    if result is True:
        st.success(f'Acceso concedido a {name}')
        st.balloons()  # Adds celebration balloons for positive result
    else:
        st.error('Acceso Denegado')
