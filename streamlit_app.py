import streamlit as st

# so the 
# steps: 
# 1. we get the raw data. we clean the raw data. 
# 2. we make the 2 file types: the plot-level, and the point-level. 
# 3. with those, we get the imagery data from gee. 
# 4. we clean whatever needs cleaning in that. 
# 5. we now have a modeling dataset. 
# 6. user has to choose: do we want categorical or continuous? 
# 7. if continuous, what attribute (% forest is a good starting point). 
# 8. what model do you want to try? (rf is a good starting point). 
# 9. if RF, then, based on whatever model you chose, and the variable type, do the featureselection. 
# 10. once you've done that, build the "final" model and apply it to make the map


st.title("Welcome to Our Interactive Geospatial Pipeline")

st.write(
    "We are a group of students from Purdue National Data Mine Network (NDMN) program, and our goal is to create an interactive pipeline that integrates pre-processing, machine learning models, and validation strategies for robust geospatial analysis, specifically tailored to Costa Rica's population. This project has been made possible with guidance from our mentors at the USDA Forest Service."
)

# step 1: Data Upload
st.header("Step 1: Upload Raw Data")
raw_data = st.file_uploader("Upload your dataset", type=["csv", "xlsx"])

if raw_data:
    st.write("Data uploaded successfully!")
    # add code here to read and display the uploaded data

# step 2: Pre-Processing Options
st.header("Step 2: Data Pre-Processing")

if raw_data:
    cleaning_option = st.selectbox("Choose Pre-Processing Strategy", ["Clean Nulls", "Remove Outliers", "Normalize Data"])
    st.write(f"Pre-Processing: {cleaning_option}")
    # add your preprocessing code based on this selection

# step 3: Data Type Selection
st.header("Step 3: Data Type Selection")
data_type = st.radio("What type of target variable?", ("Categorical", "Continuous"))

if data_type == "Continuous":
    attribute = st.selectbox("Choose the attribute for continuous variable", ["% Forest", "% Urban", "Elevation"])
    st.write(f"Selected Attribute: {attribute}")

# step 4: Model Selection
st.header("Step 4: Model Selection")
model_type = st.selectbox("Choose the model", ["Random Forest", "SVM", "Logistic Regression"])
st.write(f"Selected Model: {model_type}")
# add further code to show more options or hyperparameters based on the model

# step 5: Model Training
if model_type == "Random Forest":
    st.write("Training Random Forest Model...")
    # add code to train the model with selected attributes

# step 6: Model Validation
st.header("Step 6: Model Validation")
st.write("Select the validation strategy (e.g., cross-validation, train-test split)")
validation_method = st.selectbox("Validation Method", ["Cross-Validation", "Train-Test Split"])
st.write(f"Selected Validation: {validation_method}")

# final Steps
st.header("Final Step: Model Prediction")
st.write("Apply the trained model to generate predictions.")
# add code for prediction and visualizing results like maps



st.header("Pipeline Outline")

# description of the steps in the pipeline (brief)
st.write("""
This pipeline allows you to go through the following steps:
1. **Pre-Processing**: Clean and prepare your data.
2. **Machine Learning Application**: Choose and apply machine learning models.
3. **Model Validation**: Validate the model with different strategies.
""")

col1, col2, col3 = st.columns(3)

with col1:
    st.header("Pre-Processing")
    # Add user selection for pre-processing steps
    pre_process = st.selectbox("Select Pre-Processing Step", ["Remove Nulls", "Remove Outliers", "Normalize Data"])
    st.write(f"You chose: {pre_process}")

with col2:
    st.header("Machine Learning Application")
    # Allow user to select model
    model_choice = st.selectbox("Select Model", ["Random Forest", "SVM", "Logistic Regression"])
    st.write(f"Model chosen: {model_choice}")

with col3:
    st.header("Model Validation")
    # Allow user to choose validation strategy
    validation_choice = st.selectbox("Select Validation Method", ["Cross-Validation", "Train-Test Split"])
    st.write(f"Validation Method chosen: {validation_choice}")
