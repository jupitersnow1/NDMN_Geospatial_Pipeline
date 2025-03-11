import streamlit as st
from utils.section1.data_load import load_data

st.title("Welcome to Our Interactive Geospatial Pipeline")

st.write(
   "We are a group of students from Purdue National Data Mine Network (NDMN) program, "
   "and our goal is to create an interactive pipeline that integrates pre-processing, machine learning models, "
   "and validation strategies for robust geospatial analysis, specifically tailored to Costa Rica's population. "
   "This project has been made possible with guidance from our mentors at the USDA Forest Service."
)

# Step 1: Data Upload
st.header("Step 1: Upload Raw Data")
raw_data = st.file_uploader("Upload your dataset", type=["csv", "xlsx"])

# debugging: Check if `load_data` is callable
# st.write("Type of load_data:", type(load_data))  # Should print <class 'function'>

if raw_data:
    st.write(f"Uploaded file type: {raw_data.type}")

    try:
        data = load_data(raw_data)
        if data is not None:
            st.success("Data uploaded successfully!")
            st.write(data.head())
        else:
            st.error("Failed to load data.")
    except Exception as e:
        st.error(f"Error loading data: {e}")
