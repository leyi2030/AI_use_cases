import streamlit as st
import pandas as pd
import numpy as np

def load_data():
    # Read the Excel file
    credentials = pd.read_excel('Global AI use cases in FS.xlsx', sheet_name='Credentials')

    # Apply filters
    filtered_credentials = credentials[(credentials['Data/AI Implementation'] == 'Y') & 
                                        (credentials['Cred Quality'].isin(['2-Credential Only', '3-Useful Content', '4-Quantified Benefit']))]

    return filtered_credentials

def main():
    st.title("Global AI Use Cases in FS")

    credentials = load_data()

    # Group data by Area, Function, and Use Cases
    grouped_data = credentials.groupby(['Area', 'FS Function', 'Solution Name (Max 5 words)'])

    # Display data
    for (area, function, use_case), projects in grouped_data:
        st.header(f"Area: {area}, Function: {function}, Use Case: {use_case}")
        for index, project in projects.iterrows():
            st.subheader(project['Solution Name (Max 5 words)'])
            st.write("Description:", project['Short Description'])
            st.write("Title:", project['Title'])
            st.write("File Link:", project['File Link'])
            st.markdown(f"[Download](project['File Link'])")

if __name__ == "__main__":
    main()

streamlit run use_cases.py