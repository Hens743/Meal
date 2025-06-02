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
            
            st.info(f"Columns found in the file: {df.columns.tolist()}") # Debug: show columns found
            
            missing_cols = [col for col in required_columns if col not in df.columns]
            if missing_cols:
                st.error(f"Critical Error: Your uploaded file is missing required columns. Please ensure it has: {', '.join(required_columns)}. Missing: {', '.join(missing_cols)}")
                return pd.DataFrame() # Returns empty DataFrame on missing columns
            
            if not df.empty:
                st.info(f"First 3 rows of loaded data:\n{df.head(3).to_string()}") # Debug: show first few rows
            else:
                st.warning("Warning: The file was read, but the DataFrame is empty. Please check your file content.")

            if 'best_seller' in df.columns:
                df['best_seller'] = df['best_seller'].astype(str).str.lower().isin(['yes', 'true', '1'])
            
            st.success("File successfully processed into DataFrame.")
            return df
        except Exception as e:
            st.error(f"Error reading file: {e}. Please check your file content and format.")
            st.info("Ensure your CSV/Excel file is not open in another program and is correctly formatted.")
            return pd.DataFrame()
    else:
        if st.sidebar.checkbox("Load Hardcoded Sample Data (for testing)", value=False, key='load_hardcoded_checkbox'): 
            data = {
                'meal_name': ["Sample Noodles", "Sample Soup", "Sample Sandwich", "Sample Salad", "Sample Chili", "Sample Pasta", "Sample Tacos"],
                'category': ["Warm Meal", "Soup", "Sandwich", "Salad", "Warm Meal", "Warm Meal", "Warm Meal"],
                'best_seller': [True, False, False, False, True, True, False],
                'country': ["China", "Italy", "USA", "Greece", "Mexico", "Italy", "Mexico"]
            }
            df = pd.DataFrame(data)
            st.sidebar.info("Loaded hardcoded sample data.")
            return df
        
        st.sidebar.warning("No meal data loaded. Please upload a file or select 'Load Hardcoded Sample Data' above.")
        return pd.DataFrame()

# --- Streamlit App Setup ---
st.set_page_config(page_title="Personalized Meal Suggestions", layout="centered")

st.title("🍽️ Your Personal Meal Suggestion App")
st.markdown("Welcome! Upload your meal list or use the sample data to get personalized meal suggestions.")

# --- Sidebar for Data Upload and Filters ---
st.sidebar.header("Options")
uploaded_file = st.sidebar.file_uploader("Upload your Meal List (CSV or Excel)", type=['csv', 'xlsx', 'xls'])

if 'last_uploaded_file_id' not in st.session_state:
    st.session_state.last_uploaded_file_id = None

current_file_id = uploaded_file.file_id if uploaded_file else None

if uploaded_file is not None and current_file_id != st.session_state.last_uploaded_file_id:
    st.session_state.meals_df = load_meals_data(uploaded_file)
    st.session_state.last_uploaded_file_id = current_file_id
    # Reset filters when a new file is uploaded
    st.session_state.selected_categories = []
    st.session_state.selected_countries = []
elif 'meals_df' not in st.session_state:
    st.session_state.meals_df = load_meals_data(None)
    st.session_state.last_uploaded_file_id = None

if uploaded_file is None and \
   not st.session_state.get('load_hardcoded_checkbox', False) and \
   'meals_df' in st.session_state and \
   not st.session_state.meals_df.empty and \
   st.session_state.get('last_uploaded_file_id') is None : # Ensure this only triggers if hardcoded was source
    st.session_state.meals_df = pd.DataFrame()


# --- Display Filters and Suggestions (ONLY if data is loaded) ---
if 'meals_df' in st.session_state and not st.session_state.meals_df.empty:
    st.sidebar.success("Meal data loaded successfully! Filters are available.")
    st.sidebar.markdown("---")
    st.sidebar.header("Filter Suggestions")

    if 'selected_categories' not in st.session_state:
        st.session_state.selected_categories = []
    if 'selected_countries' not in st.session_state:
        st.session_state.selected_countries = []

    st.sidebar.subheader("Filter by Category")
    temp_selected_categories = []
    all_categories = sorted(st.session_state.meals_df['category'].unique().tolist())
    for category in all_categories:
        if st.sidebar.checkbox(category, key=f"category_checkbox_{category}", value=(category in st.session_state.selected_categories)):
            temp_selected_categories.append(category)
    if temp_selected_categories != st.session_state.selected_categories: # Only update if changed
        st.session_state.selected_categories = temp_selected_categories

    st.sidebar.markdown("---")
    st.sidebar.subheader("Filter by Country")
    temp_selected_countries = []
    all_countries = sorted(st.session_state.meals_df['country'].unique().tolist())
    for country in all_countries:
        if st.sidebar.checkbox(country, key=f"country_checkbox_{country}", value=(country in st.session_state.selected_countries)):
            temp_selected_countries.append(country)
    if temp_selected_countries != st.session_state.selected_countries: # Only update if changed
        st.session_state.selected_countries = temp_selected_countries
    
    show_best_sellers = st.sidebar.checkbox("Show Only Best Sellers")
    search_query = st.sidebar.text_input("Search by Meal Name", placeholder="e.g., chicken, soup")

    # --- Apply Filters ---
    filtered_df = st.session_state.meals_df.copy()
    if st.session_state.selected_categories:
        filtered_df = filtered_df[filtered_df['category'].isin(st.session_state.selected_categories)]
    if st.session_state.selected_countries:
        filtered_df = filtered_df[filtered_df['country'].isin(st.session_state.selected_countries)]
    if show_best_sellers:
        if 'best_seller' in filtered_df.columns: # Ensure column exists
             filtered_df = filtered_df[filtered_df['best_seller'] == True]
        else:
            st.warning("Best seller information is not available in the current dataset.")
    if search_query:
        filtered_df = filtered_df[filtered_df['meal_name'].str.contains(search_query, case=False, na=False)]

    # --- "Surprise Me!" Button ---
    st.markdown("---") 
    col_button, col_desc = st.columns([1, 3]) 
    surprise_meal_details = None 

    with col_button:
        if st.button("✨ Surprise Me!"):
            if not st.session_state.meals_df.empty:
                random_meal = st.session_state.meals_df.sample(1).iloc[0]
                surprise_meal_details = random_meal 
            else:
                # This should ideally not be reached if the parent check `if not st.session_state.meals_df.empty:` is active
                st.warning("Your meal database is empty! Cannot provide a surprise.")
    with col_desc:
        st.caption("Get a random meal from your entire collection.") # Using caption for a softer look

    # Display surprise meal output if one was selected in this run
    if surprise_meal_details is not None:
        st.subheader("🎉 Today's Surprise Meal!")
        card_md = f"""
        <div style="border: 1px solid #ddd; border-radius: 5px; padding: 15px; margin-bottom: 10px; background-color: #f9f9f9;">
            <h4>{surprise_meal_details['meal_name']}</h4>
            <p><strong>Category:</strong> {surprise_meal_details['category']}<br>
               <strong>Country:</strong> {surprise_meal_details['country']}</p>
            { "<h5>🏆 Best Seller!</h5>" if surprise_meal_details['best_seller'] else "" }
        </div>
        """
        st.markdown(card_md, unsafe_allow_html=True)
        # st.info(f"**{surprise_meal_details['meal_name']}** ({surprise_meal_details['category']}) from {surprise_meal_details['country']}")
        # if surprise_meal_details['best_seller']:
        #     st.write("🏆 This is a **Best Seller!**")

    st.markdown("---")

    # --- Determine if filtered results should be shown ---
    any_filter_active = (
        bool(st.session_state.selected_categories) or
        bool(st.session_state.selected_countries) or
        show_best_sellers or
        bool(search_query)
    )

    if any_filter_active:
        st.subheader("Your Meal Suggestions (based on filters):")
        if not filtered_df.empty:
            num_cols = 3 # Desired number of columns for the grid
            cols = st.columns(num_cols)
            for index, row in filtered_df.iterrows():
                with cols[index % num_cols]:
                    st.markdown(f"""
                    <div style="border: 1px solid #ddd; border-radius: 5px; padding: 10px; margin: 5px 0;">
                        <strong>{row['meal_name']}</strong><br>
                        <small>Category: {row['category']}</small><br>
                        <small>Country: {row['country']}</small><br>
                        { "🏆 <small><strong>Best Seller!</strong></small>" if row['best_seller'] else "" }
                    </div>
                    """, unsafe_allow_html=True)
                    # st.info(f"**{row['meal_name']}**") # Previous style
                    # st.markdown(f"Category: `{row['category']}`")
                    # st.markdown(f"Country: `{row['country']}`")
                    # if row['best_seller']:
                    #     st.markdown("🏆 **Best Seller!**")
                    # st.markdown("---") # Separator for each meal card (within column)
        else:
            st.info("No meals found matching your current filters. Try adjusting your search criteria!")
    elif surprise_meal_details is None: 
        # Show this message if data is loaded, no filters active, AND surprise wasn't just shown
        st.info("Apply filters to see suggestions, or click 'Surprise Me!' for a random pick.")

else:
    # Feedback for no data loaded is primarily handled by the `load_meals_data` function (sidebar warning).
    # If the main area needs a message when df is empty and no upload/hardcoded selected yet:
    if 'meals_df' not in st.session_state or st.session_state.meals_df.empty:
         st.info("Upload a meal list or select 'Load Hardcoded Sample Data' in the sidebar to get started.")


st.markdown("---")
st.write("Built with ❤️ using Streamlit")
