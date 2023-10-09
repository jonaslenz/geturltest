import streamlit as st


from io import BytesIO
from zipfile import ZipFile
import urllib.request
    

with ZipFile(BytesIO(url.read())) as my_zip_file:
        # with open(("unzipped_and_read_" + contained_file + ".file"), "wb") as output:
        for line in my_zip_file.open(contained_file).readlines():
            print(line)
            # output.write(line)


from io import BytesIO
from zipfile import ZipFile
from urllib.request import urlopen
# or: requests.get(url).content


link = "https://zenodo.org/record/7826010/files/adampdixon/dissertation-ecology.zip?download=1"
f = urlopen(link)

with ZipFile(BytesIO(f.read())) as my_zip_file:
    for contained_file in my_zip_file.namelist():
        # with open(("unzipped_and_read_" + contained_file + ".file"), "wb") as output:
        for line in my_zip_file.open(contained_file).readlines():
            st.write(line)
            # output.write(line)


