import streamlit as st
import pandas as pd
import random

# --- App Setup ---
st.set_page_config(page_title="Personalized Meal Suggestions", layout="centered")
st.title("🍽️ Personalized Meal Suggestions")

st.sidebar.header("Options")
uploaded_file = st.sidebar.file_uploader("Upload Meal List (CSV or Excel)", type=['csv', 'xlsx', 'xls'])

# Initialize session_state if not present
if 'meals_df' not in st.session_state:
    st.session_state['meals_df'] = pd.DataFrame()

# Dummy data loading for demonstration (replace with your real load_meals_data function)
if uploaded_file is not None:
    st.session_state['meals_df'] = pd.DataFrame({
        'meal_name': ["Pizza", "Burger", "Pasta"],
        'category': ["Fast Food", "Fast Food", "Italian"],
        'country': ["USA", "USA", "Italy"],
        'best_seller': [True, False, True]
    })

# --- Display Filters as Checkboxes ---
if not st.session_state['meals_df'].empty:
    st.sidebar.markdown("---")
    st.sidebar.header("Filter by Category")
    all_categories = sorted(st.session_state['meals_df']['category'].unique())
    selected_categories = [cat for cat in all_categories if st.sidebar.checkbox(cat)]

    st.sidebar.header("Filter by Country")
    all_countries = sorted(st.session_state['meals_df']['country'].unique())
    selected_countries = [country for country in all_countries if st.sidebar.checkbox(country)]

    show_best_sellers = st.sidebar.checkbox("Show Only Best Sellers")
    search_query = st.sidebar.text_input("Search Meal Name")

    # Apply Filters
    filtered_df = st.session_state['meals_df']
    if selected_categories:
        filtered_df = filtered_df[filtered_df['category'].isin(selected_categories)]
    if selected_countries:
        filtered_df = filtered_df[filtered_df['country'].isin(selected_countries)]
    if show_best_sellers:
        filtered_df = filtered_df[filtered_df['best_seller']]
    if search_query:
        filtered_df = filtered_df[filtered_df['meal_name'].str.contains(search_query, case=False, na=False)]

    # Only display if any filter is active
    filters_active = bool(selected_categories or selected_countries or show_best_sellers or search_query)

    # Surprise Me feature
    if st.button("✨ Surprise Me!"):
        random_meal = st.session_state['meals_df'].sample(1).iloc[0]
        st.info(f"**{random_meal['meal_name']}** ({random_meal['category']}) from {random_meal['country']}")
        if random_meal['best_seller']:
            st.write("🏆 This is a **Best Seller!**")
        filters_active = True

    if filters_active:
        if not filtered_df.empty:
            st.markdown("---")
            st.subheader("Meal Suggestions")
            for idx, (_, row) in enumerate(filtered_df.iterrows()):
                st.info(f"**{row['meal_name']}**")
                st.markdown(f"Category: `{row['category']}`")
                st.markdown(f"Country: `{row['country']}`")
                if row['best_seller']:
                    st.markdown("🏆 **Best Seller!**")
                st.markdown("---")
        else:
            st.info("No meals found matching your selection.")
    else:
        st.info("Please select filters or use 'Surprise Me!' to see suggestions.")
else:
    st.warning("No data loaded yet. Please upload a file or enable sample data.")

st.markdown("---")
st.write("Built with ❤️ using Streamlit")
