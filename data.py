import streamlit as st
import pandas as pd
import random

# --- Data Loading Function ---
def load_meals_data(uploaded_file=None):
    if uploaded_file:
        try:
            # Determine file type and read accordingly
            if uploaded_file.name.endswith('.csv'):
                df = pd.read_csv(uploaded_file)
            elif uploaded_file.name.endswith(('.xls', '.xlsx')):
                df = pd.read_excel(uploaded_file)
            else:
                st.error("Unsupported file type. Please upload a CSV or Excel file.")
                return pd.DataFrame() # Return empty DataFrame on error

            # Ensure expected columns are present, including 'country'
            required_columns = ['meal_name', 'category', 'best_seller', 'country']
            if not all(col in df.columns for col in required_columns):
                st.error(f"Missing required columns in your file. Please ensure it has: {', '.join(required_columns)}")
                return pd.DataFrame()

            # Convert 'best_seller' to boolean for easier filtering
            df['best_seller'] = df['best_seller'].astype(str).str.lower().isin(['yes', 'true'])
            return df
        except Exception as e:
            st.error(f"Error reading file: {e}")
            return pd.DataFrame()
    else:
        # --- Hardcoded Data Option (Uncomment to use instead of file upload) ---
        # If you prefer hardcoding, uncomment the lines below and comment out the file upload logic
        # data = {
        #     'meal_name': ["Spicy Noodles", "Creamy Tomato Soup", "Grilled Cheese", "Garden Salad", "Chili Con Carne", "Fish and Chips", "Chocolate Cake"],
        #     'category': ["Warm Meal", "Soup", "Sandwich", "Salad", "Warm Meal", "Fried", "Dessert"],
        #     'best_seller': [True, False, False, False, True, False, True],
        #     'country': ["China", "Italy", "USA", "USA", "Mexico", "UK", "France"]
        # }
        # df = pd.DataFrame(data)
        # return df
        # --- End Hardcoded Data Option ---

        return pd.DataFrame() # Return empty if no file uploaded and no hardcoded data

# --- Streamlit App Setup ---
st.set_page_config(page_title="Personalized Meal Suggestions", layout="centered")

st.title("🍽️ Your Personal Meal Suggestion App")

st.markdown("""
Welcome! Upload your meal list or use the pre-loaded data to get personalized meal suggestions.
""")

# --- Sidebar for Data Upload and Filters ---
st.sidebar.header("Options")

uploaded_file = st.sidebar.file_uploader("Upload your Meal List (CSV or Excel)", type=['csv', 'xlsx', 'xls'])

# Load data when app starts or file is uploaded
if 'meals_df' not in st.session_state or uploaded_file is not None:
    st.session_state.meals_df = load_meals_data(uploaded_file)
    if uploaded_file:
        st.sidebar.success("Meal list uploaded successfully!")
    elif st.session_state.meals_df.empty and uploaded_file is None:
        st.sidebar.warning("No meal data loaded. Please upload a file or uncomment the hardcoded data in `app.py`.")


if not st.session_state.meals_df.empty:
    st.sidebar.markdown("---")
    st.sidebar.header("Filter Suggestions")

    # Get unique categories from the current DataFrame
    all_categories = st.session_state.meals_df['category'].unique().tolist()
    selected_categories = st.sidebar.multiselect("Select Category", sorted(all_categories))

    # Get unique countries from the current DataFrame
    all_countries = sorted(st.session_state.meals_df['country'].unique().tolist())
    st.sidebar.markdown("---") # Add a separator for country filter
    st.sidebar.subheader("Filter by Country")
    
    # Initialize selected_countries in session_state if not present
    if 'selected_countries' not in st.session_state:
        st.session_state.selected_countries = []

    # Create checkboxes for each country
    temp_selected_countries = []
    for country in all_countries:
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

else:
    st.warning("Please upload a meal list using the sidebar to get started!")

st.markdown("---")
st.write("Built with ❤️ using Streamlit")
