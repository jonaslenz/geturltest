import streamlit as st


from io import BytesIO
from zipfile import ZipFile
from urllib.request import urlopen

st.title("data crawler")
link = st.text_input(label="URL", value="https://zenodo.org/record/6654150/files/lenz2022.zip?download=1")
f = urlopen(link)

with ZipFile(BytesIO(f.read())) as my_zip_file:
    st.header("files in url-zip")
    for contained_file in my_zip_file.namelist():
        st.write(contained_file)

        # with open(("unzipped_and_read_" + contained_file + ".file"), "wb") as output:
        try:
            st.write("accesing README")
            for line in my_zip_file.open(README.md).readlines():
                st.write(line)
        except:
            st.write("no README")


