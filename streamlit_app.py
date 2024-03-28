import streamlit as st
from st_functions import st_button, load_css
from PIL import Image
from datetime import datetime

load_css()

col1, col2, col3 = st.columns(3)
col2.image(Image.open('profile.png'))

st.header('Ingrid Stevens')

st.info('Data and AI Enthusiast: passionate about using and building with open source models (esp. on Apple Silicon) and sharing what I learn with others!')

icon_size = 20


st_button('medium', 'https://medium.com/@ingridwickstevens', 'Read my Articles on Medium', icon_size)

st_button('linkedin', 'https://www.linkedin.com/in/ingridwstevens/', 'Connect with me on LinkedIn', icon_size)

st_button('github', 'https://github.com/ingridstevens', 'See what I\'m up to on GitHub', icon_size)

st_button('cup', 'https://www.buymeacoffee.com/ingridstevens', 'Buy me a Coffe (❤️ thanks!)', icon_size)



st.markdown("---")
# Footer with auto-updated year
current_year = datetime.now().year
# st.markdown(f"© {current_year} Ingrid Stevens. All rights reserved.")