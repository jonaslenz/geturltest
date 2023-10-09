import streamlit as st
from urllib.request import urlopen

link = "https://get.api-feiertage.de?years=2024&states=sn"
f = urlopen(link)
myfile = f.read()
st.write(myfile)

