import streamlit as st
import pandas as pd
import random

# Meal list with 'broad_type' categories (data, so it remains the same)
meal_list = [
    {'meal_name': "Pastel de Choclo Bake", 'category': "Savory Bake", 'best_seller': random.choice([True, False]), 'broad_type': "Roasted & Baked Dishes"},
    {'meal_name': "Empanadas Pino (Beef)", 'category': "Savory Bake", 'best_seller': random.choice([True, False]), 'broad_type': "Specialty & Street Foods"},
    {'meal_name': "Hearty Cazuela Chilena", 'category': "Stew", 'best_seller': random.choice([True, False]), 'broad_type': "Soups & Stews"},
    {'meal_name': "Humitas Corn Parcels", 'category': "Warm Meal", 'best_seller': random.choice([True, False]), 'broad_type': "Rice & Grain Bowls"},
    {'meal_name': "Porotos Granados Stew", 'category': "Stew", 'best_seller': random.choice([True, False]), 'broad_type': "Soups & Stews"},
    {'meal_name': "Congrio Frito (Fried Conger Eel)", 'category': "Seafood Special", 'best_seller': random.choice([True, False]), 'broad_type': "Grilled & Pan-Seared"},
    {'meal_name': "Machas a la Parmesana", 'category': "Seafood Special", 'best_seller': random.choice([True, False]), 'broad_type': "Specialty & Street Foods"},
    {'meal_name': "Charquican Beef Stew", 'category': "Stew", 'best_seller': random.choice([True, False]), 'broad_type': "Soups & Stews"},
    {'meal_name': "Pebre Chicken Bowl", 'category': "Rice Bowl", 'best_seller': random.choice([True, False]), 'broad_type': "Rice & Grain Bowls"},
    {'meal_name': "Curanto Inspired Seafood Pot", 'category': "Seafood Special", 'best_seller': random.choice([True, False]), 'broad_type': "Soups & Stews"},
    {'meal_name': "Sopaipillas Pasadas (savory version context)", 'category': "Warm Meal", 'best_seller': random.choice([True, False]), 'broad_type': "Specialty & Street Foods"},
    {'meal_name': "Valdiviano Soup", 'category': "Soup", 'best_seller': random.choice([True, False]), 'broad_type': "Soups & Stews"},
    {'meal_name': "Costillar de Chancho Ahumado", 'category': "Roast", 'best_seller': random.choice([True, False]), 'broad_type': "Roasted & Baked Dishes"},
    {'meal_name': "Pastel de Jaiba (Crab Pie)", 'category': "Savory Bake", 'best_seller': random.choice([True, False]), 'broad_type': "Roasted & Baked Dishes"},
]

# Create a DataFrame from the meal list
df = pd.DataFrame(meal_list)

# --- Translations Dictionary ---
# All user-facing text is stored here, organized by language.
translations = {
    "en": {
        "page_title": "Meal Idea Generator",
        "app_title": "🍽️ What's For Dinner? 🍽️",
        "app_description": "Feeling stuck for meal ideas? Use this app to explore a variety of delicious dishes!",
        "filter_header": "Filter Your Meal Search",
        "select_meal_type": "Choose a meal type:",
        "all_option": "All",
        "show_best_sellers": "Show only Best Sellers",
        "ideas_header": "Meal Ideas",
        "discover_meals": "Discover {} Meal Ideas!",
        "suggest_random": "Suggest a Random Meal",
        "best_seller_tag": "⭐ Best Seller",
        "broad_type_label": "Broad Type:",
        "category_label": "Category:",
        "all_matching_meals": "All Matching Meals:",
        "no_meals_found": "No meals found matching your criteria. Try adjusting your filters!",
        "footer_text": "Happy cooking! 🍳",
        "other_type": "Other Type", # For placeholder categories
    },
    "es": {
        "page_title": "Generador de Ideas de Comidas",
        "app_title": "🍽️ ¿Qué hay de Cenar? 🍽️",
        "app_description": "¿No se te ocurren ideas para la comida? ¡Usa esta aplicación para explorar una variedad de deliciosos platos!",
        "filter_header": "Filtra Tu Búsqueda de Comida",
        "select_meal_type": "Elige un tipo de comida:",
        "all_option": "Todos",
        "show_best_sellers": "Mostrar solo los más vendidos",
        "ideas_header": "Ideas de Comida",
        "discover_meals": "¡Descubre {} Ideas de Comida!",
        "suggest_random": "Sugerir una Comida Aleatoria",
        "best_seller_tag": "⭐ Más Vendido",
        "broad_type_label": "Tipo Amplio:",
        "category_label": "Categoría:",
        "all_matching_meals": "Todas las Comidas Coincidentes:",
        "no_meals_found": "No se encontraron comidas que coincidan con tus criterios. ¡Intenta ajustar tus filtros!",
        "footer_text": "¡Feliz cocina! 🍳",
        "other_type": "Otro Tipo", # For placeholder categories
    }
}

# --- Session State for Language ---
if 'language' not in st.session_state:
    st.session_state.language = 'en' # Default language is English

# Set the current text dictionary based on the selected language
text = translations[st.session_state.language]

# --- Streamlit App Configuration ---
st.set_page_config(
    page_title=text["page_title"], # Uses translated title
    layout="centered",
    initial_sidebar_state="collapsed"
)

# --- Custom CSS (CSS itself remains language-agnostic) ---
st.markdown("""
<style>
    body { font-family: 'Helvetica Neue', sans-serif; color: #333; line-height: 1.6; }
    .stApp { padding: 1rem; }
    h1 { color: #4CAF50; text-align: center; margin-bottom: 1.5rem; font-size: 1.8em; }
    h2 { color: #2E8B57; font-size: 1.4em; margin-top: 1.5rem; margin-bottom: 1rem; }
    .stSelectbox, .stMultiSelect { margin-bottom: 1rem; }
    .stSelectbox > div > div > div { font-size: 0.95em; }
    .stButton > button { background-color: #4CAF50; color: white; padding: 0.75rem 1.5rem; border-radius: 0.5rem; border: none; font-size: 1.1em; width: 100%; margin-top: 1rem; }
    .stButton > button:hover { background-color: #45a049; }
    .meal-card { background-color: #f9f9f9; border-left: 5px solid #4CAF50; padding: 1rem; margin-bottom: 1rem; border-radius: 0.5rem; box-shadow: 0 2px 5px rgba(0,0,0,0.1); }
    .meal-card h3 { color: #333; font-size: 1.2em; margin-top: 0; margin-bottom: 0.5rem; }
    .meal-card p { font-size: 0.9em; color: #555; margin-bottom: 0.2rem; }
    .best-seller-tag { background-color: #FFD700; color: #333; font-weight: bold; padding: 0.2em 0.5em; border-radius: 0.3em; font-size: 0.7em; margin-left: 0.5em; }
    .center-text { text-align: center; }
</style>
""", unsafe_allow_html=True)

# --- Language Selector ---
# Place the language selector at the top or in a prominent position
language_choice = st.selectbox(
    "Select Language / Seleccionar Idioma:",
    options=['English', 'Español'],
    index=0 if st.session_state.language == 'en' else 1,
    key="language_selector"
)

# Update session state based on selection
if language_choice == 'English':
    st.session_state.language = 'en'
else:
    st.session_state.language = 'es'

# Re-set 'text' variable based on potentially changed session state
text = translations[st.session_state.language]

# --- App Title and Description ---
st.markdown(f"<h1 class='center-text'>{text['app_title']}</h1>", unsafe_allow_html=True)
st.write(text["app_description"])



## {text['filter_header']}

# Get unique 'broad_type' categories for the filter
all_broad_types = sorted(df['broad_type'].unique().tolist())

# Ensure we have at least 8 broad types for the selection, adding placeholders if necessary
if len(all_broad_types) < 8:
    current_count = len(all_broad_types)
    for i in range(8 - current_count):
        all_broad_types.append(f"{text['other_type']} {i+1}") # Uses translated 'Other Type'

# Limit to exactly 8 broad types if more are generated by mistake or future data
broad_types_for_filter = [text["all_option"]] + all_broad_types[:8]

# Broad Type selection
selected_broad_type = st.selectbox(
    text["select_meal_type"],
    broad_types_for_filter,
    index=0
)

# Best Seller checkbox
filter_best_seller = st.checkbox(text["show_best_sellers"])



## {text['ideas_header']}

# Filter logic
filtered_df = df.copy()

if selected_broad_type != text["all_option"]:
    if selected_broad_type in df['broad_type'].unique():
        filtered_df = filtered_df[filtered_df['broad_type'] == selected_broad_type]
    else:
        filtered_df = pd.DataFrame() # No meals for placeholder broad types

if filter_best_seller:
    filtered_df = filtered_df[filtered_df['best_seller'] == True]

# Display results
if not filtered_df.empty:
    st.markdown(f"<h2>{text['discover_meals'].format(len(filtered_df))}</h2>", unsafe_allow_html=True)

    # Random meal suggestion
    if st.button(text["suggest_random"]):
        random_meal = filtered_df.sample(1).iloc[0]
        st.markdown(
            f"""
            <div class='meal-card'>
                <h3>{random_meal['meal_name']} {
                    f"<span class='best-seller-tag'>{text['best_seller_tag']}</span>" if random_meal['best_seller'] else ""
                }</h3>
                <p><strong>{text['broad_type_label']}</strong> {random_meal['broad_type']}</p>
                <p><strong>{text['category_label']}</strong> {random_meal['category']}</p>
            </div>
            """, unsafe_allow_html=True
        )
        st.markdown("---") # Separator after random suggestion

    st.markdown(f"<h2>{text['all_matching_meals']}</h2>", unsafe_allow_html=True)

    # Display all filtered meals in a mobile-friendly card format
    for index, row in filtered_df.iterrows():
        st.markdown(
            f"""
            <div class='meal-card'>
                <h3>{row['meal_name']} {
                    f"<span class='best-seller-tag'>{text['best_seller_tag']}</span>" if row['best_seller'] else ""
                }</h3>
                <p><strong>{text['broad_type_label']}</strong> {row['broad_type']}</p>
                <p><strong>{text['category_label']}</strong> {row['category']}</p>
            </div>
            """, unsafe_allow_html=True
        )
else:
    st.warning(text["no_meals_found"])



st.markdown(f"<p class='center-text'>{text['footer_text']}</p>", unsafe_allow_html=True)
