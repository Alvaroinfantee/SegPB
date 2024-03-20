
import streamlit as st
import pandas as pd

# Setting the page config to include favicon and title
st.set_page_config(
    page_title="ID Verification System",
    page_icon=r"PuebloBavaroLogo.png",  # Adjust the path as needed
    layout="centered"
)

# Load data from the Excel file
file_path = r'DBColegio.xlsx'  # Adjust the path as needed
data = pd.read_excel(file_path)

# Display the logo
st.image(r"PuebloBavaroLogo.png", width=400)  # Adjust the path as needed

# Setting up the Streamlit interface
st.title('ID Verification System')

# Input for the ID
user_id = st.text_input('Ingresa el código:', '')

# Function to check the ID and return name if found
def check_id_and_get_name(user_id):
    if user_id.isdigit():  # Ensure the input is a digit to prevent errors
        user_id = int(user_id)
        if user_id in data['id'].values:
            # Get the name of the person with the given ID
            name = data.loc[data['id'] == user_id, 'nombre'].values[0]
            return True, name  # Return both the check result and the name
        else:
            return False, None
    else:
        return None, None  # Return None if the input is not a digit

# Display result
if user_id:  # Only proceed if user_id is not an empty string
    result, name = check_id_and_get_name(user_id)
    if result is True:
        st.success(f'Access Concedido a {name}')
        st.balloons()  # Adds celebration balloons for positive result
    elif result is False:
        st.error('Acceso Denegado')
    elif result is None:
        st.warning('Please enter a valid numerical ID')
