import streamlit as st
import pandas as pd
import random

# --- Data Loading Function ---
def load_meals_data(uploaded_file=None):
    # This function now provides more feedback on its execution
    
    if uploaded_file:
        try:
            st.info(f"Attempting to read uploaded file: '{uploaded_file.name}'. File size: {uploaded_file.size} bytes") # Debug info
            
            # Determine file type and read accordingly
            if uploaded_file.name.endswith('.csv'):
                df = pd.read_csv(uploaded_file)
            elif uploaded_file.name.endswith(('.xls', '.xlsx')):
                df = pd.read_excel(uploaded_file)
            else:
                st.error("Unsupported file type. Please upload a CSV or Excel file.")
                return pd.DataFrame() # Return empty DataFrame on unsupported type

            # Ensure expected columns are present, including 'country'
            required_columns = ['meal_name', 'category', 'best_seller', 'country']
            
            # Debug: show columns found in file
            st.info(f"Columns found in the file: {df.columns.tolist()}")
            
            # Check for missing columns
            missing_cols = [col for col in required_columns if col not in df.columns]
            if missing_cols:
                st.error(f"Critical Error: Your uploaded file is missing required columns. Please ensure it has: {', '.join(required_columns)}. Missing: {', '.join(missing_cols)}")
                return pd.DataFrame() # Returns empty DataFrame on missing columns
            
            # Debug: show first few rows
            if not df.empty:
                st.info(f"First 3 rows of loaded data:\n{df.head(3).to_string()}")
            else:
                st.warning("Warning: The file was read, but the DataFrame is empty. Please check your file content.")

            # Convert 'best_seller' to boolean for easier filtering
            # Ensure the column exists before attempting conversion
            if 'best_seller' in df.columns:
                df['best_seller'] = df['best_seller'].astype(str).str.lower().isin(['yes', 'true'])
            
            st.success("File successfully processed into DataFrame.") # Debug success
            return df
        except Exception as e:
            st.error(f"Error reading file: {e}. Please check your file content and format.")
            st.info("Ensure your CSV/Excel file is not open in another program and is correctly formatted.")
            return pd.DataFrame()
    else:
        # Option to load hardcoded data for testing
        if st.sidebar.checkbox("Load Hardcoded Sample Data (for testing)", value=False, key='load_hardcoded_checkbox'): 
            data = {
                'meal_name': ["Sample Noodles", "Sample Soup", "Sample Sandwich", "Sample Salad", "Sample Chili"],
                'category': ["Warm Meal", "Soup", "Sandwich", "Salad", "Warm Meal"],
                'best_seller': [True, False, False, False, True],
                'country': ["China", "Italy", "USA", "USA", "Mexico"]
            }
            df = pd.DataFrame(data)
            st.sidebar.info("Loaded hardcoded sample data.") # Debug info
            return df
        
        # This message will only show if no file is uploaded AND hardcoded data is not selected
        st.sidebar.warning("No meal data loaded. Please upload a file or select 'Load Hardcoded Sample Data' above.")
        return pd.DataFrame()

# --- Streamlit App Setup ---
st.set_page_config(page_title="Personalized Meal Suggestions", layout="centered")

st.title("🍽️ Your Personal Meal Suggestion App")

st.markdown("""
Welcome! Upload your meal list or use the sample data to get personalized meal suggestions.
""")

# --- Sidebar for Data Upload and Filters ---
st.sidebar.header("Options")

uploaded_file = st.sidebar.file_uploader("Upload your Meal List (CSV or Excel)", type=['csv', 'xlsx', 'xls'])

# Use a session state variable to track if a file was previously uploaded and loaded
# This prevents re-loading the hardcoded data if a file was just removed, etc.
if 'last_uploaded_file_id' not in st.session_state:
    st.session_state.last_uploaded_file_id = None

current_file_id = uploaded_file.file_id if uploaded_file else None

# Only load data if a file is explicitly uploaded/changed, or if it's the very first run and nothing else is loaded
if uploaded_file is not None and current_file_id != st.session_state.last_uploaded_file_id:
    # A new file has been uploaded or the existing one changed
    st.session_state.meals_df = load_meals_data(uploaded_file)
    st.session_state.last_uploaded_file_id = current_file_id
elif 'meals_df' not in st.session_state:
    # Initial run, no file yet, so check if hardcoded should load
    st.session_state.meals_df = load_meals_data(None)
    st.session_state.last_uploaded_file_id = None # No file loaded

# If no file uploaded and hardcoded checkbox was just unselected, ensure df is empty
if uploaded_file is None and not st.session_state.get('load_hardcoded_checkbox', False) and 'meals_df' in st.session_state and not st.session_state.meals_df.empty:
     # This part ensures filters disappear if hardcoded data is toggled off and no file is present
     st.session_state.meals_df = pd.DataFrame()


# --- Display Filters and Suggestions (ONLY if data is loaded) ---
if not st.session_state.meals_df.empty:
    st.sidebar.success("Meal data loaded successfully! Filters are available.") # Confirmation message

    st.sidebar.markdown("---")
    st.sidebar.header("Filter Suggestions")

    # Category selection (multiselect)
    all_categories = st.session_state.meals_df['category'].unique().tolist()
    selected_categories = st.sidebar.multiselect("Select Category", sorted(all_categories))

    st.sidebar.markdown("---") # Add a separator for country filter
    st.sidebar.subheader("Filter by Country")
    
    # Initialize selected_countries in session_state if not present
    if 'selected_countries' not in st.session_state:
        st.session_state.selected_countries = []

    # Create checkboxes for each country (mobile-friendly)
    temp_selected_countries = []
    all_countries = sorted(st.session_state.meals_df['country'].unique().tolist()) # Get countries from current data
    for country in all_countries:
        # Use st.checkbox with a unique key and initial value based on session_state
        if st.sidebar.checkbox(country, key=f"country_checkbox_{country}", value=(country in st.session_state.selected_countries)):
            temp_selected_countries.append(country)
    st.session_state.selected_countries = temp_selected_countries # Update the session state after all checkboxes are processed

    show_best_sellers = st.sidebar.checkbox("Show Only Best Sellers")
    search_query = st.sidebar.text_input("Search by Meal Name", placeholder="e.g., chicken, soup")

    # --- Apply Filters ---
    filtered_df = st.session_state.meals_df.copy()

    if selected_categories:
        filtered_df = filtered_df[filtered_df['category'].isin(selected_categories)]

    # Apply country filter based on checkboxes
    if st.session_state.selected_countries:
        filtered_df = filtered_df[filtered_df['country'].isin(st.session_state.selected_countries)]

    if show_best_sellers:
        filtered_df = filtered_df[filtered_df['best_seller'] == True]

    if search_query:
        # Case-insensitive search on meal_name
        filtered_df = filtered_df[filtered_df['meal_name'].str.contains(search_query, case=False, na=False)]

    # --- Display Meal Suggestions ---

    st.subheader("Your Meal Suggestions:")

    # "Surprise Me!" button
    col1, col2 = st.columns([1, 3]) # Use columns for better layout
    with col1:
        if st.button("✨ Surprise Me!"):
            if not st.session_state.meals_df.empty:
                random_meal = st.session_state.meals_df.sample(1).iloc[0]
                st.info(f"**{random_meal['meal_name']}** ({random_meal['category']}) from {random_meal['country']}")
                if random_meal['best_seller']:
                    st.write("🏆 This is a **Best Seller!**")
            else:
                st.warning("Your meal database is empty! Please add some meals first to get a surprise.")
    with col2:
        st.write("Get a random meal from your entire collection.")

    st.markdown("---") # Separator

    if not filtered_df.empty:
        # Display meals in a grid-like fashion or cards
        cols = st.columns(3) # Display up to 3 meals per row
        for index, row in filtered_df.iterrows():
            with cols[index % 3]: # Cycle through the columns
                st.info(f"**{row['meal_name']}**")
                st.markdown(f"Category: `{row['category']}`")
                st.markdown(f"Country: `{row['country']}`")
                if row['best_seller']:
                    st.markdown("🏆 **Best Seller!**")
                st.markdown("---") # Separator for each meal card

    else:
        st.info("No meals found matching your current filters. Try adjusting your search criteria or uploading a different file!")

# This block only executes if no data is loaded at all
else:
    # The warning is already handled within load_meals_data for better context
    pass 

st.markdown("---")
st.write("Built with ❤️ using Streamlit")
