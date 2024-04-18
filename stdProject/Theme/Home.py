import streamlit as st
import base64

# Define function to set background image with zoom out effect
def set_bg_with_zoom_out(main_bg):
    '''
    A function to set the background image with a zoom out effect.

    Returns
    -------
    The background.
    '''
    # Set background name
    main_bg_ext = "bg"

    st.markdown(
         f"""
         <style>
         .stApp {{
             background: url(data:image/{main_bg_ext};base64,{base64.b64encode(main_bg.read()).decode()});
             background-size: contain; /* Zoom out effect */
             background-repeat: no-repeat;
             background-position: center;
         }}
         .gif-container {{
             position: absolute;
             top: 0;
             left: 0;
             margin-top: 0px; /* Adjust vertical position as needed */
             margin-left: 900px; /* Adjust horizontal position as needed */             
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

# Path to the background image
bg_path = r'C:\Users\WALID\Desktop\Chatbot\stdProject\Bg.jpg'
gif_url = "https://media2.giphy.com/media/kLano1oGCDDmlwttPh/giphy-downsized.gif"  # Replace with the URL of your GIF

# Place the GIF in a container with custom CSS for positioning
st.markdown(
    f'<div class="gif-container"><img src="{gif_url}" width="100"></div>',
    unsafe_allow_html=True
)

# Read the image file
with open(bg_path, "rb") as bg_file:
    # Set the background with zoom out effect
    set_bg_with_zoom_out(bg_file)

# Main content
st.title("")
st.sidebar.success("Selected a page above.")
