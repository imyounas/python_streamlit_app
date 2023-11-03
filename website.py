import streamlit as st
from PIL import Image
import requests
from streamlit_lottie import st_lottie

st.set_page_config(page_title="My Webpage", page_icon=":tada:", layout="wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style/style.css")

# ---- LOAD ASSETS ----
lottie_coding = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_fcfjwiyb.json")


# ---- HEADER SECTION ----
with st.container():
    st.subheader("Hi, I am Imran :wave:")
    st.title("An old developer lost in the storm !")
    st.write(
        "I am passionate about solving complex business problems."
    )
    st.write("[Learn More >](https://devstudiointl.com)")

# ---- WHAT I DO ----
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What I do")
        st.write("##")
        st.write(
            """
            I can build cloud native apps using:
            - C#, XAML (MAUI, WPF), NodeJS, Python, Java, C++.
            - with SQL Server, MySQL, PostgreSQL, MongoDB.
            - on Azure, AWS Cloud Services
            I can also get you a dedicated team of developers that will work with your onshore team <<>>
            

            If this sounds interesting to you, consider contacting me.
            """
        )
        st.write("[DevSTudio International >](https://devstudiointl.com)")
    with right_column:
        st_lottie(lottie_coding, height=300, key="coding")