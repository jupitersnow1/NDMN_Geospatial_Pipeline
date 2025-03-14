import streamlit as st
import pandas as pd
import geopandas as gpd
import mapclassify
from utils.section1.data_load import load_data
from utils.section2.data_processing import inspect_and_convert
from utils.section2.mapping import plot_geometry
from streamlit_folium import st_folium

st.title("Welcome to Our Interactive Geospatial Pipeline")

st.write(
   "We are a group of students from Purdue National Data Mine Network (NDMN) program, "
   "and our goal is to create an interactive pipeline that integrates pre-processing, machine learning models, "
   "and validation strategies for robust geospatial analysis, specifically tailored to Costa Rica's population. "
   "This project has been made possible with guidance from our mentors at the USDA Forest Service."
)

# ---------------------------   Step 1: Data Upload ---------------------------
with st.expander("Step 1: Upload Raw Data", expanded=False):
    raw_data = st.file_uploader("Upload your dataset", type=["csv", "xlsx"])

    if raw_data:
        df = load_data(raw_data)
        if isinstance(df, pd.DataFrame):
            st.session_state["data"] = df
            st.success("Data uploaded successfully!")
        else:
            st.error("Invalid data format. Please check your file.")
    st.divider()

# -------------------------- Step 2: Data Inspection ----------------------------
with st.expander("Step 2: Data Inspection", expanded=False):
    if "data" in st.session_state:
        gdf = inspect_and_convert(st.session_state["data"])
        if gdf is not None and not gdf.empty:
            st.session_state["gdf"] = gdf
            st.write(gdf.head())
        else:
            st.warning("Conversion failed or no valid geometries found.")
    else:
        st.warning("Please upload a dataset first.")


# ------------------------- Step 3: Geospatial Visualization -------------------------
# Ensures a persistent storage key
if "map_" not in st.session_state:
    st.session_state["map_"] = None

@st.cache_resource
def plot_geometry_cached(_gdf):
    """Creates a quick interactive map."""
    return _gdf.explore(color="orange")

with st.expander("Step 3: Visualize Geometry", expanded=False):
    if "gdf" in st.session_state:
        if st.session_state["map_"] is None:  # Compute once
            with st.spinner("Generating map..."):
                st.session_state["map_"] = plot_geometry_cached(st.session_state["gdf"])

        if st.session_state["map_"]:
            if "visualized_success" not in st.session_state:
                st.success("Successfully visualized geometries!")
                st.session_state["visualized_success"] = True  # Avoid multiple messages

            st_folium(st.session_state["map_"], width=700, height=500)
    else:
        st.warning("No geospatial data available. Please check your dataset.")