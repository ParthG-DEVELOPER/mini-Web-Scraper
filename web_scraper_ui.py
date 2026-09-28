import streamlit as st
import requests
from bs4 import BeautifulSoup

#######################################################################
st.set_page_config(page_title="Web Scraper", page_icon="🍑", layout="centered")

# Custom CSS for peach background, floating peaches, and the glowing peach silhouette animation
st.markdown(
    """
    <style>
    /* Main app background color */
    .stApp {
        background-color: #ffecd0;
        background-image: linear-gradient(135deg, #ffecd0 0%, #fcb69f 100%);
        overflow-x: hidden;
    }

    /* Floating Peaches Animation */
    @keyframes float {
        0% { transform: translateY(0vh) rotate(0deg); opacity: 0.8; }
        50% { opacity: 1; }
        100% { transform: translateY(-100vh) rotate(360deg); opacity: 0; }
    }

    .floating-peach {
        position: fixed;
        bottom: -10vh;
        font-size: 2rem;
        animation: float 6s ease-in-out infinite;
        z-index: 1;
        user-select: none;
    }

    .p1 { left: 10%; animation-delay: 0s; animation-duration: 5s; }
    .p2 { left: 30%; animation-delay: 2s; animation-duration: 7s; }
    .p3 { left: 50%; animation-delay: 1s; animation-duration: 6s; }
    .p4 { left: 70%; animation-delay: 3s; animation-duration: 8s; }
    .p5 { left: 90%; animation-delay: 1.5s; animation-duration: 5.5s; }

    /* Fullscreen Overlay for Explosion Effect on Load */
    .explosion-overlay {
        position: fixed;
        top: 0;
        left: 0;
        width: 100vw;
        height: 100vh;
        background: rgba(0, 0, 0, 0.2);
        display: flex;
        justify-content: center;
        align-items: center;
        z-index: 9999;
        pointer-events: none;
        animation: fadeOut 2.5s forwards;
    }

    /* Authentic Peach Shape that grows, explodes, and glows */
    @keyframes shadowExplode {
        0% {
            transform: scale(0.1);
            opacity: 0;
            filter: drop-shadow(0px 0px 0px rgba(255, 140, 0, 0));
        }
        40% {
            transform: scale(1.8);
            opacity: 0.9;
            filter: drop-shadow(0px 0px 40px rgba(255, 100, 50, 0.9)) drop-shadow(0px 0px 80px rgba(255, 165, 0, 0.7));
        }
        60% {
            transform: scale(2.2);
            opacity: 1;
            filter: drop-shadow(0px 0px 70px rgba(255, 69, 0, 1)) drop-shadow(0px 0px 120px rgba(255, 200, 0, 0.8));
        }
        100% {
            transform: scale(3.5);
            opacity: 0;
            filter: drop-shadow(0px 0px 150px rgba(255, 150, 100, 0));
        }
    }

    .giant-shadow-peach {
        width: 280px;
        height: 280px;
        fill: #7d3c24; /* Rich dark peach shadow color */
        animation: shadowExplode 1.2s cubic-bezier(0.25, 1, 0.5, 1) forwards;
    }

    @keyframes fadeOut {
        0% { opacity: 1; }
        70% { opacity: 1; }
        100% { opacity: 0; visibility: hidden; }
    }

    /* Floating & Glowing Title Animation */
    @keyframes titleFloat {
        0% { transform: translateY(0px); }
        50% { transform: translateY(-6px); }
        100% { transform: translateY(0px); }
    }

    @keyframes titleGlow {
        0% { text-shadow: 0 0 5px rgba(184, 59, 27, 0.3), 0 0 10px rgba(255, 123, 84, 0.2); }
        50% { text-shadow: 0 0 15px rgba(184, 59, 27, 0.7), 0 0 25px rgba(255, 123, 84, 0.5); }
        100% { text-shadow: 0 0 5px rgba(184, 59, 27, 0.3), 0 0 10px rgba(255, 123, 84, 0.2); }
    }

    .glowing-floating-title {
        text-align: center;
        color: #b83b1b;
        position: relative;
        font-size: 3rem;
        font-weight: 700;
        animation: titleFloat 3s ease-in-out infinite, titleGlow 2.5s ease-in-out infinite;
    }
    </style>

    <!-- Floating Background Peaches -->
    <div class="floating-peach p1">🍑</div>
    <div class="floating-peach p2">🍑</div>
    <div class="floating-peach p3">🍑</div>
    <div class="floating-peach p4">🍑</div>
    <div class="floating-peach p5">🍑</div>
    """,
    unsafe_allow_html=True,
)

# Initialize session state to trigger the pop on initial page load
if "loaded" not in st.session_state:
    st.session_state.loaded = True
    st.markdown(
        """
        <div class="explosion-overlay">
            <!-- Accurate organic peach vector path featuring the classic top cleft and rounded bottom -->
            <svg class="giant-shadow-peach" viewBox="0 0 512 512">
                <path d="M256,110 C215,70 140,90 115,160 C85,225 105,320 180,380 C220,410 256,400 256,400 C256,400 292,410 332,380 C407,320 427,225 397,160 C372,90 297,70 256,110 Z"/>
            </svg>
        </div>
        """,
        unsafe_allow_html=True,
    )

# Floating & Glowing Web Scraper Title
st.markdown(
    "<h1 class='glowing-floating-title'>Web Scraper</h1>",
    unsafe_allow_html=True,
)

# Subheading
st.markdown(
    "<p style='text-align: center; color: #7d3c24; font-size: 1.1rem; position: relative;'>This website gives the information of title and the links</p>",
    unsafe_allow_html=True,
)
#####################################################################
if 'soup_data' not in st.session_state:
    st.session_state.soup_data=None
if 'Verified' not in st.session_state:
    st.session_state.Verified=False
with st.form("URL Form"):
   url=st.text_input("Enter the URL here")
   submit = st.form_submit_button("Submit")


if submit:
   try:
        response = requests.get(url)
        st.session_state.soup_data = BeautifulSoup(response.text, 'html.parser')
        st.session_state.Verified=True
        st.success("The URL Is Verified")
        t=1
   except requests.exceptions.MissingSchema:#Checks for correct format of URL
          st.error("❌ Please enter the url again")
          
   except requests.exceptions.InvalidSchema:
          st.error("❌ Please enter the url again")
          
   except requests.exceptions.ConnectionError:#Checks for connection of the site
           print("❌Please enter the url again")
           



#soup = BeautifulSoup(response.text, 'html.parser')


if st.session_state.Verified:
 if st.button("Get Details"):
  soup=st.session_state.soup_data

# 3. Extract data
# Get the page title text
  try:
   
    page_title = soup.title.string
    st.markdown(":red[TITLE]")
    print()
    st.markdown(f":blue[{page_title}]")
    print()
  except AttributeError:
     st.markdown(":red[NO Definite Title Found On This WebPage]")

#Extracts the link from the sites if any

  st.markdown(":red[LINKS FOUND ARE]")
  print()

  for link in soup.find_all('a'):

    href = link.get('href')
    k=st.markdown(f":blue[{href}]")