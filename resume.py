import streamlit as st
from streamlit_option_menu import option_menu
from PIL import Image

im=Image.open("favicon.ico")
st.set_page_config(page_title="Stock prices", page_icon=im, layout="wide")
def streamlit_menu(example=1):
    if example == 1:
        selected = option_menu(
            menu_title=None,  
            options=["Home", "Experience", "Education", "Projects", "Contact"],  
            icons=["🏠", "📘", "📚", "🚀", "✉️"],  
            menu_icon="📺",  
            default_index=0,  
            orientation="horizontal",  
        )
        return selected

EXAMPLE_NO = 1

selected = streamlit_menu(example=EXAMPLE_NO)

if selected == "Home":
    st.title(f"You have selected {selected}")
    st.markdown("""
<style>
.big-font {
    font-size:50px;
    font-weight:bold;
    font-family:SANS-SERIF;
    text-align:center;
    
}
</style>
""", unsafe_allow_html=True)

st.markdown('<p class="big-font">Hi, iam</p>', unsafe_allow_html=True)

if selected == "Projects":
    st.title(f"You have selected {selected}")
    st.markdown('<div style="max-width: 300px;">', unsafe_allow_html=True)

    # Card-like structure
    st.markdown('<article class="box style23">', unsafe_allow_html=True)

    # Image (replace the URL with your own image)
    st.markdown('<a href="https://github.com/chandru-git30/Pyspark_Auto_Evaluation" class="image featured">'
                '<img src="https://example.com/your-image-url.png" alt="" />'
                '</a>', unsafe_allow_html=True)

    # Title (replace with your own title)
    st.markdown('<h3><a href="https://github.com/chandru-git30/Pyspark_Auto_Evaluation">Pyspark_Auto_Evaluation</a></h3>', unsafe_allow_html=True)

    # Description (replace with your own description)
    st.markdown('<p>Simplify PySpark Testing with pytest Auto-Evaluation.</p>', unsafe_allow_html=True)

    # Close the card-like structure
    st.markdown('</article>', unsafe_allow_html=True)

    # Close the container
    st.markdown('</div>', unsafe_allow_html=True)

if selected == "Contact":
    st.title(f"You have selected {selected}")

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
local_css("style/style.css")