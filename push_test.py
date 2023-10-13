import streamlit as st
from github import Github
from github import Auth

st.title("Test push to github repo")

filename = st.text_input(filename)
filecontent = st.text_area(content)
message = st.text_input(commit message)

if st.button('Commit'):
  auth = Auth.Token(st.secrets["github_push"])
  g = Github(auth=auth)
  repo = g.get_repo("jonaslenz/geturltest")
  repo.create_file(filename, message, filecontent, branch="main")
  g.close()
  
