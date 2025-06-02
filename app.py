import streamlit as st
import pandas as pd
import random

# --- App Setup ---
st.set_page_config(page_title="Personalized Meal Suggestions", layout="centered")
st.title("🍽️ Personalized Meal Suggestions")

# --- Hardcoded meal data (replacing the CSV file) ---
data = {
    "meal_name": [
        "Pasta Primavera", "Sushi Platter", "Chicken Biryani",
        "Veggie Burger", "Caesar Salad", "Miso Soup",
        "Beef Tacos", "Greek Salad", "Pad Thai",
        "Chicken Soup", "Steak Frites", "Margherita Pizza"
    ],
    "category": [
        "Pasta", "Seafood", "Rice",
        "Burger", "Salad", "Soup",
        "Tacos", "Salad", "Noodles",
        "Soup", "Meat", "Pizza"
    ],
    "best_seller": [
        "yes", "no", "yes",
        "no", "yes", "no",
        "yes", "no", "yes",
        "no", "yes", "yes"
    ],
    "country": [
        "Italy", "Japan", "India",
        "USA", "Italy", "Japan",
        "Mexico", "Greece", "Thailand",
        "USA", "France", "Italy"
    ]
}
df = pd.DataFrame(data)

# --- Filters ---
types = sorted(df['category'].dropna().unique())
selected_categories = [cat for cat in types if st.checkbox(cat)]

countries = sorted(df['country'].dropna().unique())
selected_countries = [c for c in countries if st.checkbox(c)]

show_best_sellers = st.checkbox("Show Only Best Sellers")
search_query = st.text_input("Search Meal Name")

# --- Apply filters ---
filtered_df = df.copy()
if selected_categories:
    filtered_df = filtered_df[filtered_df['category'].isin(selected_categories)]
if selected_countries:
    filtered_df = filtered_df[filtered_df['country'].isin(selected_countries)]
if show_best_sellers:
    filtered_df = filtered_df[filtered_df['best_seller'].astype(str).str.lower() == 'yes']
if search_query:
    filtered_df = filtered_df[filtered_df['meal_name'].str.contains(search_query, case=False, na=False)]

# --- Determine if any filter is active ---
filters_active = bool(selected_categories or selected_countries or show_best_sellers or search_query)

# --- Surprise Me! ---
if st.button("✨ Surprise Me!"):
    random_meal = df.sample(1).iloc[0]
    st.info(f"**{random_meal['meal_name']}** ({random_meal['category']}) from {random_meal['country']}")
    if random_meal['best_seller'].lower() == 'yes':
        st.write("🏆 This is a **Best Seller!**")
    filters_active = True

# --- Show Results ---
if filters_active:
    if not filtered_df.empty:
        st.markdown("---")
        st.subheader("Meal Suggestions")
        for _, row in filtered_df.iterrows():
            st.info(f"**{row['meal_name']}**")
            st.markdown(f"Category: `{row['category']}`")
            st.markdown(f"Country: `{row['country']}`")
            if row['best_seller'].lower() == 'yes':
                st.markdown("🏆 **Best Seller!**")
            st.markdown("---")
    else:
        st.info("No meals found matching your selection.")
else:
    st.info("Please select filters or use 'Surprise Me!' to see suggestions.")

st.markdown("---")
st.write("Built with ❤️ using Streamlit")
