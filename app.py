import streamlit as st

def main():
  st.header("This is title.")
  name=st.text_input("enter your name:")


  col1 , col2 = st.columns(2, gap="small")

  with col1:
    if st.button("Hi", type="primary", key='btn1', width='stretch'):
      print("hi", name)

  with col2:
    if st.button("Bye", type="secondary", key='btn2', width='stretch'):
      print("bye", name)    
      
main()