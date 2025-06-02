import streamlit as st
import pandas as pd
import random

# --- App Setup ---
st.set_page_config(page_title="Personalized Meal Suggestions", layout="centered")
st.title("🍽️ Personalized Meal Suggestions")

st.sidebar.header("Options")
uploaded_file = st.sidebar.file_uploader("Upload Meal List (CSV or Excel)", type=['csv', 'xlsx', 'xls'])

# Load data if uploaded
if uploaded_file is not None:
    if uploaded_file.name.endswith('.csv'):
        df = pd.read_csv(uploaded_file)
    elif uploaded_file.name.endswith(('.xls', '.xlsx')):
        df = pd.read_excel(uploaded_file)
    else:
        st.error("Unsupported file type.")
        df = pd.DataFrame()
else:
    df = pd.DataFrame()

if not df.empty:
    st.sidebar.markdown("---")
    st.sidebar.header("Filter by Category")
    categories = sorted(df['category'].dropna().unique())
    selected_categories = [cat for cat in categories if st.sidebar.checkbox(cat)]

    st.sidebar.header("Filter by Country")
    countries = sorted(df['country'].dropna().unique())
    selected_countries = [c for c in countries if st.sidebar.checkbox(c)]

    show_best_sellers = st.sidebar.checkbox("Show Only Best Sellers")
    search_query = st.sidebar.text_input("Search Meal Name")

    # Apply filters
    filtered_df = df.copy()
    if selected_categories:
        filtered_df = filtered_df[filtered_df['category'].isin(selected_categories)]
    if selected_countries:
        filtered_df = filtered_df[filtered_df['country'].isin(selected_countries)]
    if show_best_sellers:
        filtered_df = filtered_df[filtered_df['best_seller']]
    if search_query:
        filtered_df = filtered_df[filtered_df['meal_name'].str.contains(search_query, case=False, na=False)]

    # Determine if any filter is active
    filters_active = bool(selected_categories or selected_countries or show_best_sellers or search_query)

    # Surprise Me feature
    if st.button("✨ Surprise Me!"):
        random_meal = df.sample(1).iloc[0]
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
    st.warning("No data loaded yet. Please upload a file.")

st.markdown("---")
st.write("Built with ❤️ using Streamlit")
