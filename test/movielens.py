import streamlit as st

# Displaying a header with text and emojis
st.header('All About Movies :movie_camera:')
st.title('Movie Lens')

if st.button('Start'):
    # Set the query parameters for the new page
    query_params = {"page": "other"}
    # Generate the URL for the new page
    new_url = st.experimental_set_query_params(**query_params)
    # Redirect to the new page
    st.experimental_rerun()

# Check if the page query parameter is set to "other"
if st.experimental_get_query_params().get("page") == "other":
    # Display the content of the other page
    st.write("This is the other page")
