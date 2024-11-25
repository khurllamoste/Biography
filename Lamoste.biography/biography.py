from pathlib import Path

import streamlit as st
from PIL import Image


# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "_file_" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
biography_file = current_dir / "assets" / "Lamoste.pdf"
profile_pic = current_dir / "assets" / "profile-pic.png"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "My Biograpy | Khurl Vince Xavier L. Lamoste"
PAGE_ICON = ":glasess:"
NAME = "Khurl Vince Xavier L. Lamoste"
DESCRIPTION = """
A 1st year Computer Engineering student at Surigao del Norte State University
"""
BIRTH_DATE = "Birth Date: October 11, 2006"
BIRTH_PLACE = "Birth Place: Manila"
EMAIL = "klamoste1@ssct.edu.ph"
SOCIAL_MEDIA = {
    "Facebook": "https://www.facebook.com/khhhhuuuurrrrrrrlll",
}


st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)


#---PROFILE PIC and DOCUMENT ---
with open(css_file) as f:
    css_content = f.read()
    st.markdown("<style>{}</style>".format(css_content), unsafe_allow_html=True)
with open(biography_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)

# ---Insert Section ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=260)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.write(BIRTH_DATE)
    st.write(BIRTH_PLACE)
    st.download_button(
        label="📄Download_Biography",
        data=PDFbyte,
        file_name=biography_file.name,
        mime="application/octet-stream",        
    )
    st.write("📨", EMAIL)

#-- Social LInks ----
st.write("#")
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")

# --- About Me---
st.write("#")
st.subheader("About Me")
st.write("---")
st.write(
    """
    Hi, I’m  Khurl Vince Xavier L. Lamoste, an 18 years old and a first-year computer engineering student passionate about technology, problem-solving, and creating impactful solutions. 
    I’ve always been fascinated by how computers work and how they drive innovation across industries. 
    This interest led me to pursue a degree in computer engineering to explore the intricate relationship between hardware and software.
    """    
)

#---- Educational Attainment -----
st.write("#")
st.subheader("Educational Attainment")
st.write("---")
st.write(
    """
- 🏫 Elementary School :(Pautao Elementary School) Yr: 2013-2018
- 🏫 Junior High School :(Bacuag National Agro-Industrial School) Yr: 2018-2022
- 📖 Senior High School:(Bacuag National Agro-Industrial School) Yr: 2022-2024
- 🏛️ College :(Surigao del Norte State University) Yr: 2024--

"""
)

#----Achievement----
st.write("#")
st.subheader(" Achievement")
st.write("---")
st.write(
    """
- 🎖️ Elementary School :(Graduate with Perfect Attendance)
- 🎖️ High School :(Graduate with Honors and Perfect Attendance)
- 👩🏻‍🎓 Senior High School :(Graduate with Honors and Perfect Attendance)
"""
)

comment = st.text_input("Comment about me", " ")