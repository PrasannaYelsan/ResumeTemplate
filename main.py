import io

import streamlit as st
import time
import datetime
import pandas as pd
import numpy as np
from PIL import Image
from streamlit_star_rating import st_star_rating

st.set_page_config(page_title="Prasanna Yelsangikar Resume", page_icon="logo.png", layout="wide")


def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
local_css("style.css")


with st.container():
    # st.markdown(f'<div style="text-align: center class="titles"">Prasanna Yelsangikar</div>',
    #             unsafe_allow_html=True)
    st.markdown(f'<div style="text-align: center; font-size: 51px">Prasanna Yelsangikar</div>', unsafe_allow_html=True)
    st.markdown(f'<div style="text-align: center;font-size: 18px; ">Software Automation Engineer</div>', unsafe_allow_html=True)
    st.markdown(f'<hr style="width: 100%; size:10; align:center">', unsafe_allow_html=True)

#    st.text('')


co1,co2 = st.columns((7,1))
with co1:
    st.text('')
    st.text('\n')
    st.markdown(f'<div style="text-align: left; font-size: 20px">PROFILE SUMMARY</div>', unsafe_allow_html=True)
    st.markdown(f'<hr width = "100%"; size = "0"; align="center";>', unsafe_allow_html=True)
    #st.write("""When using this command, Mapbox provides the map tiles to render map content. Note that Mapbox is a third-party product, the use of which is governed by Mapbox's Terms of Use.Mapbox requires users to register and provide a token before users can request map tiles. Currently, Streamlit provides this token for you, but this could change at any time. We strongly recommend all users create and use their own personal Mapbox token to avoid any disruptions to their experience. You can do this with the""")
    st.markdown('1. Currently working as Automation Module Lead in **Global Edge Software Limited** part of Capgemini, Bangalore ')
    st.markdown('2. Graduate MCA with 10+ years of automation experience in Agile and Scrum environments')
    st.markdown('3. Experienced in SQL queries, Automotive concepts Like basics of CAN, UDS and BIOS Firmware ')
    st.markdown('4. Experienced in Automation Testing using Pytest and Jenkins with CI/CD.')

with co2:
    st.markdown(f'<div style="text-align: left; font-size: 20px">WORK EXPERIENCE</div>', unsafe_allow_html=True)
    st.markdown(f'<hr style="width: 100%; size:10; align:center">', unsafe_allow_html=True)
    st.text('\n')
    expe_col1, expe_col2 = st.columns((5,1))
    with expe_col1:
        st.markdown(
            f'<div style="text-align: left; font-size: 17px">1. From Global Edge (Capgemini) have been deputed to multiple client locations over my career tenure as below</div>',
            unsafe_allow_html=True)

        st.write('✔. **Volvo International Bangalore**  \n  \t Automation framework development support for Telematics feature using Python & PyTest')
        # #st.write("\t Automation framework development support for Telematics feature using Python & PyTest")
        st.write('✔. **Harman International Bangalore**  \n  \t TATA HMI or Infotainment Automation using C# and Python')
        #st.markdown(f'<div style="text-align: left; font-size: 17px">TATA HMI or Infotainment Automation using C# and Python</div>', unsafe_allow_html=True)
        st.write('✔. **Honda India Bangalore**  \n  \t Test Automation Framework and Validation of Front Camera Module (FCM) using Python and Robot Framework')
        #st.markdown( f'<div style="text-align: left; font-size: 17px">Test Automation Framework and Validation of Front Camera Module (FCM) using Python and Robot Framework</div>',unsafe_allow_html=True)
        st.write('**2. Happiest Minds Bangalore**  \n  \t Arista EOS AutoTest using Python')
        st.write('**3. Dexcel Designs** and deputed to client Intel Technologies  \n  \t Automation Validating Intel Braswell and Intel Haswell Tablet using Python & PyTest')
        st.write('**4. Utthunga Technologies Bangalore** and deputed to Emerson  \n  \t Automate ProLink III™ Product features using Python & Unittest')

    with expe_col2:
        st.write("\n")
        expe_col2.markdown('Jan 2020 to Till Date')
        st.write("\n")
        expe_col2.markdown('Jan 2017 to Dec 2020')
        st.write("\n")
        expe_col2.markdown('Jan 2016 to Jan 2017')
        st.write("\n")
        expe_col2.markdown('Apr 2015 to Jan 2016')
        st.write("\n")
        expe_col2.markdown('Jun 2012 to Jun 2015')
        st.write("\n")
        expe_col2.markdown('Oct 2010 to Jun 2012')

    st.text('')

st.text('')
co12,co22 = st.columns((7,1))
with co12:
    pass

st.text('')
with co22:
    st.markdown(f'<div style="text-align: left; font-size: 20px">AWARDS & RECOGNITION(S) </div>', unsafe_allow_html=True)
    st.markdown(f'<hr style="width: 100%; size:10; align:center">', unsafe_allow_html=True)
    st.text('\n')
    st.markdown('1. From **Dell India** counterpart for delivering **One Click Intel® Driver Installation Automation Tool** without any Interactions')
    st.markdown('2. **Young Turk award** Appreciation from Global Edge India counterpart for delivering **ADAS (FCM) Automation using Python Robot Framework.**')

st.text(' ')
st.text('')
skills_co11,skills_col2, skills_col3 = st.columns((2, 2, 2))
with skills_co11:
    st.markdown(f'<div style="text-align: left; font-size: 20px">PROGRAMMING SKILLS</div>', unsafe_allow_html=True)
    st.markdown(f'<hr style="width: 90%; size:10; align:center">', unsafe_allow_html=True)
    s_col1,s_col2 = st.columns((2,2))
    with s_col1:
        st.markdown(f'<div style="text-align: left; font-size: 18px">Python</div>', unsafe_allow_html=True)
        st.markdown(f'<div style="text-align: left; font-size: 18px">C Sharp</div>', unsafe_allow_html=True)
        st.markdown(f'<div style="text-align: left; font-size: 18px">SQL</div>', unsafe_allow_html=True)
        st.markdown(f'<div style="text-align: left; font-size: 18px">Basics Of Docker</div>',unsafe_allow_html=True)
        st.markdown(f'<div style="text-align: left; font-size: 18px">Basics of CAN/UDS</div>', unsafe_allow_html=True)
        st.markdown(f'<div style="text-align: left; font-size: 18px">Software Automation Testing</div>', unsafe_allow_html=True)

    with s_col2:
        python_stars = st_star_rating(label="", maxValue=5, defaultValue=3, key="rating1", size=13)
        # st.write(python_stars)
        csharp_stars = st_star_rating(label="", maxValue=5, defaultValue=3, key="rating2", size=13)
        # st.write(csharp_stars)
        sql_stars = st_star_rating(label="", maxValue=5, defaultValue=3, key="rating3", size=13)
        # st.write(sql_stars)
        dock_stars = st_star_rating(label="", maxValue=5, defaultValue=3, key="rating4", size=13)
        can_stars = st_star_rating(label="", maxValue=5, defaultValue=3, key="rating5", size=13)
        # st.write(can_stars)
        automation_stars = st_star_rating(label="", maxValue=5, defaultValue=4, key="ratings", size=13)
        # st.write(automation_stars)


with skills_col2:
    st.markdown(f'<div style="text-align: left; font-size: 20px">INTERESTS & HOBBIES </div>', unsafe_allow_html=True)
    st.markdown(f'<hr style="width: 0090%; size:10; align:center">', unsafe_allow_html=True)
    i_col1, i_col2 = st.columns((2, 2))
    with i_col1:
        st.markdown(f'<div style="text-align: left; font-size: 18px">Web Design & Development</div>', unsafe_allow_html=True)
        st.markdown(f'<div style="text-align: left; font-size: 18px">Playing Cricket</div>', unsafe_allow_html=True)
        st.markdown(f'<div style="text-align: left; font-size: 18px">IOT Projects</div>', unsafe_allow_html=True)
        st.markdown(f'<div style="text-align: left; font-size: 18px">Gadgets</div>', unsafe_allow_html=True)
        st.markdown(f'<div style="text-align: left; font-size: 18px">Cycling</div>', unsafe_allow_html=True)

    with i_col2:
        web_stars = st_star_rating(label="", maxValue=5, defaultValue=3, key="rating6", size=13)
        # st.write(python_stars)
        playing_stars = st_star_rating(label="", maxValue=5, defaultValue=3, key="rating7", size=13)
        # st.write(csharp_stars)
        iot_stars = st_star_rating(label="", maxValue=5, defaultValue=3, key="rating8", size=13)
        # st.write(sql_stars)
        gadgets_stars = st_star_rating(label="", maxValue=5, defaultValue=3, key="rating9", size=13)
        # st.write(can_stars)
        cycling_stars = st_star_rating(label="", maxValue=5, defaultValue=4, key="rating10", size=13)
        # st.write(automation_stars)

with skills_col3:
    st.markdown(f'<div style="text-align: left; font-size: 20px">Languages</div>', unsafe_allow_html=True)
    st.markdown(f'<hr style="width: 90%; size:10; align:center">', unsafe_allow_html=True)
    l_col1, l_col2 = st.columns((2, 2))
    with l_col1:
        st.markdown(f'<div style="text-align: left; font-size: 18px">English</div>', unsafe_allow_html=True)
        st.markdown(f'<div style="text-align: left; font-size: 18px">Kannada</div>', unsafe_allow_html=True)
        st.markdown(f'<div style="text-align: left; font-size: 18px">Hindi</div>', unsafe_allow_html=True)
        st.markdown(f'<div style="text-align: left; font-size: 18px">Telagu</div>', unsafe_allow_html=True)

    with l_col2:
        st.markdown(f'<div style="text-align: left; font-size: 18px">Speak, Listen, Write</div>', unsafe_allow_html=True)
        st.markdown(f'<div style="text-align: left; font-size: 18px">Speak, Listen, Write</div>', unsafe_allow_html=True)
        st.markdown(f'<div style="text-align: left; font-size: 18px">Speak, Listen, Write</div>', unsafe_allow_html=True)
        st.markdown(f'<div style="text-align: left; font-size: 18px">Listen</div>', unsafe_allow_html=True)

#################  Sidebar related #####################
with st.sidebar:
    # opening the image
    image = Image.open('Profile_image.png')
    st.image(image)
    st.subheader("CONTACTS")
    st.sidebar.markdown(f'<div style="color:white;">➖➖➖➖➖➖➖➖➖➖➖➖</div>',
                    unsafe_allow_html=True)
    layout1, layout2=st.sidebar.columns((0.2,1.5))
    with layout1:
        image1 = Image.open('location.png')
        st.image(image1,width = 25)

    with layout2:
        st.markdown(f'<div style="color:white;"> Bangalore </div>',
                    unsafe_allow_html=True)

    layout11, layout21=st.sidebar.columns((0.2,1.5))
    with layout11:
        image11 = Image.open('email.JPG')
        st.image(image11,width = 25)
    with layout21:
        st.markdown(f'<div style="color:white;"><a href="mailto:prasann.yelsangikar@gmail.com">Prasanna.yelsangikar@gmail.com</a></div>',
                    unsafe_allow_html=True)

    layout21, layout22=st.sidebar.columns((0.2,1.5))
    with layout21:
        image13 = Image.open('Phone.JPG')
        st.image(image13,width = 25)
    with layout22:
        st.markdown(f'<div style="color:white;">+91-xxxxxxxxxx</div>',
                    unsafe_allow_html=True)
    st.markdown(f'<div style="color:white;font-size:12px;">Please take more my contacts details on Naukri</div>',
                    unsafe_allow_html=True)
    #st.sidebar.markdown('******')
    st.subheader("EDUCATION")
    st.sidebar.markdown(f'<div style="color:white;">➖➖➖➖➖➖➖➖➖➖➖➖</div>',
                        unsafe_allow_html=True)

    layou, layou1 = st.sidebar.columns((2,0.1))
    with layou:
        st.markdown(f'<div style="color:white;font-weight: bold; font-style: italic;font-size:14px;">Master in Computer Science (MCA) </div>',unsafe_allow_html=True)
        st.sidebar.markdown(f'<div style="color:white;">March-2005 to May-2008'+'<br/>'+'Gulbarga University'+'</div>',
                            unsafe_allow_html=True)
    with layou1:
        pass
    st.sidebar.markdown('******')
    layo, layo1 = st.sidebar.columns((2, 0.1))
    with layo:
        st.markdown(
            f'<div style="color:white;font-weight: bold; font-style: italic;font-size:14px;">Bachelor of Science (BSC) </div>',
            unsafe_allow_html=True)
        st.sidebar.markdown(
            f'<div style="color:white;">March-2002 to May-2005' + '<br/>' + 'Gulbarga University' + '</div>',
            unsafe_allow_html=True)
    with layo1:
        pass

    st.sidebar.markdown('******')
    st.subheader("DOWNLOAD RESUME")
    st.sidebar.markdown(f'<div style="color:white;">➖➖➖➖➖➖➖➖➖➖➖➖</div>',
                        unsafe_allow_html=True)
    #doc_download = open("./images/Resume.docx")

    # with open("Resume.docx", "rb") as file:
    #     btn = st.download_button(
    #         label="Click to Download",
    #         data=file,
    #         file_name="Resume.docx",
    #         mime="docx"
    #     )

    # lan_layou, lan_layou1 = st.sidebar.columns((2, 0.1))
    # with lan_layou:
    #     st.markdown(f'<div style="color:white;font-size:16px;">1. English' + '<br/>' + '2. Kannada' + '<br/>' + '3. Hindi' + '</div>',
    #         unsafe_allow_html=True)
    #
    # with lan_layou1:
    #     pass


hide_main_menu = """
    <style>
    #MainMenu {visbility : hidden;}
    footer {visbility : hidden;}
    header {visbility : hidden;}
    </style>
    """

st.markdown(hide_main_menu,unsafe_allow_html=True)