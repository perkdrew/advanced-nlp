import streamlit as st
import numpy as np
import pandas as pd 

def main():
    st.title("Gene and Protein Tagger")
    html_temp = """
    <div style="background-color:seagreen;padding:10px">
    <h2 style="color:white;text-align:center;">Named-Entity Recognition with BioBERT</h2>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)
    user_input = st.text_area("Submit biomedical text here:")
    result=""
    if st.button("Predict"):
        #result = biobert prediction
        #st.success('The output is {}'.format(result))
        pass
    if st.button("Supplements"):
        st.text("BioBERT info")

if __name__=='__main__':
    main()