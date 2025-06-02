import streamlit as st
import pandas as pd
import random

# --- Data Loading Function ---
def load_meals_data(uploaded_file=None):
    if uploaded_file:
        try:
            st.info(f"Reading file: **{uploaded_file.name}** ({uploaded_file.size} bytes)")

            # Read file based on extension
            if uploaded_file.name.endswith('.csv'):
                df = pd.read_csv(uploaded_file)
            elif uploaded_file.name.endswith(('.xls', '.xlsx')):
                df = pd.read_excel(uploaded_file)
            else:
                st.error("Unsupported file type. Upload a CSV or Excel file.")
                return pd.DataFrame()

            # Ensure required columns exist
            required_columns = ['meal_name', 'category', 'best_seller', 'country']
            missing_cols = [col for col in required_columns if col not in df.columns]

            if missing_cols:
                st.error(f"Missing columns: {', '.join(missing_cols)}.\nPlease include: {', '.join(required_columns)}.")
                return pd.DataFrame()

            # Display first few rows for context
            if not df.empty:
                st.info(f"First 3 rows:\n{df.head(3).to_string()}")
            else:
                st.warning("Warning: File read, but no data found.")

            # Convert 'best_seller' to boolean
            df['best_seller'] = df['best_seller'].astype(str).str.lower().isin(['yes', 'true'])

            st.success("File loaded successfully!")
            return df

        except Exception as e:
            st.error(f"Error reading file: {e}. Check file format/content.")
            return pd.DataFrame()
    else:
        # Optionally load sample data
        if st.sidebar.checkbox("Load Hardcoded Sample Data (for testing)", key='load_hardcoded_checkbox'):
            data = {
                'meal_name': ["Sample Noodles", "Sample Soup", "Sample Sandwich", "Sample Salad", "Sample Chili"],
                'category': ["Warm Meal", "Soup", "Sandwich", "Salad", "Warm Meal"],
                'best_seller': [True, False, False, False, True],
                'country': ["China", "Italy", "USA", "USA", "Mexico"]
            }
            st.sidebar.success("Sample data loaded!")
            return pd.DataFrame(data)
        else:
            st.sidebar.warning("No data loaded. Upload a file or enable sample data.")
            return pd.DataFrame()

# --- App Setup ---
st.set_page_config(page_title="Personalized Meal Suggestions", layout="centered")
st.title("🍽️ Personalized Meal Suggestions")
st.markdown("Upload your meal list or use sample data to find the perfect meal suggestions.")

# --- Sidebar: File Upload & Data ---
st.sidebar.header("Options")
uploaded_file = st.sidebar.file_uploader("Upload Meal List (CSV or Excel)", type=['csv', 'xlsx', 'xls'])

# Initialize session_state
if 'meals_df' not in st.session_state:
    st.session_state.meals_df = pd.DataFrame()

if 'last_uploaded_file_id' not in st.session_state:
    st.session_state.last_uploaded_file_id = None

current_file_id = getattr(uploaded_file, 'file_id', None)

# Load data only when file changes or on first load
if uploaded_file and current_file_id != st.session_state.last_uploaded_file_id:
    st.session_state.meals_df = load_meals_data(uploaded_file)
    st.session_state.last_uploaded_file_id = current_file_id
elif uploaded_file is None and st.session_state.last_uploaded_file_id is not None:
    # File removed: clear data
    st.session_state.meals_df = pd.DataFrame()
    st.session_state.last_uploaded_file_id = None
elif uploaded_file is None and st.sidebar.checkbox("Load Hardcoded Sample Data (for testing)", key='load_sample_sidebar', value=False):
    st.session_state.meals_df = load_meals_data(None)

# --- Display Filters & Suggestions ---
if not st.session_state.meals_df.empty:
    st.sidebar.success("Data loaded. Apply filters below:")

    # Filter by category
    st.sidebar.markdown("---")
    st.sidebar.header("Filter by Category")
    all_categories = sorted(st.session_state.meals_df['category'].unique())
    selected_categories = st.sidebar.multiselect("Select Categories:", all_categories)

    # Filter by country
    st.sidebar.header("Filter by Country")
    all_countries = sorted(st.session_state.meals_df['country'].unique())
    selected_countries = st.sidebar.multiselect("Select Countries:", all_countries)

    # Best Seller filter
    show_best_sellers = st.sidebar.checkbox("Show Only Best Sellers")

    # Search filter
    search_query = st.sidebar.text_input("Search Meal Name", placeholder="e.g., chicken, soup")

    # --- Apply Filters ---
    filtered_df = st.session_state.meals_df.copy()
    if selected_categories:
        filtered_df = filtered_df[filtered_df['category'].isin(selected_categories)]
    if selected_countries:
        filtered_df = filtered_df[filtered_df['country'].isin(selected_countries)]
    if show_best_sellers:
        filtered_df = filtered_df[filtered_df['best_seller']]
    if search_query:
        filtered_df = filtered_df[filtered_df['meal_name'].str.contains(search_query, case=False, na=False)]

    # --- Surprise Me ---
    col1, col2 = st.columns([1, 3])
    with col1:
        if st.button("✨ Surprise Me!"):
            if not st.session_state.meals_df.empty:
                random_meal = st.session_state.meals_df.sample(1).iloc[0]
                st.info(f"**{random_meal['meal_name']}** ({random_meal['category']}) from {random_meal['country']}")
                if random_meal['best_seller']:
                    st.write("🏆 This is a **Best Seller!**")
            else:
                st.warning("No meals to suggest. Load data first.")
    with col2:
        st.write("Get a random meal suggestion from your data.")

    # --- Display Filtered Results ---
    st.markdown("---")
    if not filtered_df.empty:
        st.subheader("Meal Suggestions")
        cols = st.columns(3)
        for idx, (_, row) in enumerate(filtered_df.iterrows()):
            with cols[idx % 3]:
                st.info(f"**{row['meal_name']}**")
                st.markdown(f"Category: `{row['category']}`  \nCountry: `{row['country']}`")
                if row['best_seller']:
                    st.markdown("🏆 **Best Seller!**")
                st.markdown("---")
    else:
        st.info("No meals found. Adjust filters or search criteria.")
else:
    # No data block
    st.warning("No data loaded yet. Please upload a file or enable sample data.")

st.markdown("---")
st.write("Built with ❤️ using Streamlit")
