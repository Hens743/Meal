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

df = pd.DataFrame(meal_list)

# --- Language Configuration ---
# Define all text strings in English and Spanish
TEXT_CONTENT = {
    "en": {
        "page_title": "Meal Idea Generator",
        "app_title": "🍽️ What's For Dinner? 🍽️",
        "app_description": "Feeling stuck for meal ideas? Use this app to explore a variety of delicious dishes!",
        "filter_header": "Filter Your Meal Search",
        "broad_type_select": "Choose a meal type:",
        "all_option": "All",
        "other_type": "Other Type", # Placeholder prefix for additional categories
        "best_seller_checkbox": "Show only Best Sellers",
        "results_header_prefix": "Discover",
        "results_header_suffix": "Meal Ideas!",
        "suggest_button": "Suggest a Random Meal",
        "best_seller_tag": "⭐ Best Seller",
        "all_matching_meals": "All Matching Meals:",
        "broad_type_label": "Broad Type:",
        "category_label": "Category:",
        "no_meals_warning": "No meals found matching your criteria. Try adjusting your filters!",
        "footer": "Happy cooking! 🍳",
        "language_select_label": "Select Language",
        # Translations for broad_type categories
        "broad_type_translations": {
            "Roasted & Baked Dishes": "Roasted & Baked Dishes",
            "Specialty & Street Foods": "Specialty & Street Foods",
            "Soups & Stews": "Soups & Stews",
            "Rice & Grain Bowls": "Rice & Grain Bowls",
            "Grilled & Pan-Seared": "Grilled & Pan-Seared",
            "Salads & Light Meals": "Salads & Light Meals",
            "Noodles & Pasta": "Noodles & Pasta",
            "Sandwiches & Wraps": "Sandwiches & Wraps",
        }
    },
    "es": {
        "page_title": "Generador de Ideas de Comidas",
        "app_title": "🍽️ ¿Qué hay de Cenar? 🍽️",
        "app_description": "¿No se te ocurren ideas para la comida? ¡Usa esta aplicación para explorar una variedad de deliciosos platos!",
        "filter_header": "Filtra Tu Búsqueda de Comida",
        "broad_type_select": "Elige un tipo de comida:",
        "all_option": "Todos",
        "other_type": "Otro Tipo", # Placeholder prefix for additional categories
        "best_seller_checkbox": "Mostrar solo los más vendidos",
        "results_header_prefix": "¡Descubre",
        "results_header_suffix": "Ideas de Comida!",
        "suggest_button": "Sugerir una Comida Aleatoria",
        "best_seller_tag": "⭐ Más Vendido",
        "all_matching_meals": "Todas las Comidas Coincidentes:",
        "broad_type_label": "Tipo Amplio:",
        "category_label": "Categoría:",
        "no_meals_warning": "No se encontraron comidas que coincidan con tus criterios. ¡Intenta ajustar tus filtros!",
        "footer": "¡Feliz cocina! 🍳",
        "language_select_label": "Seleccionar Idioma",
        # Translations for broad_type categories
        "broad_type_translations": {
            "Roasted & Baked Dishes": "Platos Asados y Horno",
            "Specialty & Street Foods": "Comidas Especiales y Callejeras",
            "Soups & Stews": "Sopas y Guisos",
            "Rice & Grain Bowls": "Platos de Arroz y Granos",
            "Grilled & Pan-Seared": "A la Plancha y Asados",
            "Salads & Light Meals": "Ensaladas y Comidas Ligeras",
            "Noodles & Pasta": "Fideos y Pastas",
            "Sandwiches & Wraps": "Sándwiches y Wraps",
        }
    }
}

# Initialize session state for language if not already set
if 'language' not in st.session_state:
    st.session_state.language = "en" # Default language is English

# Get the current text content based on selected language
current_text = TEXT_CONTENT[st.session_state.language]

# --- Streamlit App Configuration ---
st.set_page_config(
    page_title=current_text["page_title"],
    layout="centered",
    initial_sidebar_state="collapsed"
)

# --- Custom CSS for Mobile Optimization ---
st.markdown("""
<style>
    /* General body styling for better mobile readability */
    body {
        font-family: 'Helvetica Neue', sans-serif;
        color: #333;
        line-height: 1.6;
    }
    .stApp {
        padding: 1rem; /* Adjust padding for mobile screens */
    }
    /* Header styling */
    h1 {
        color: #4CAF50;
        text-align: center;
        margin-bottom: 1.5rem;
        font-size: 1.8em; /* Smaller on mobile */
    }
    h2 {
        color: #2E8B57;
        font-size: 1.4em; /* Smaller on mobile */
        margin-top: 1.5rem;
        margin-bottom: 1rem;
    }
    /* Selectbox and Multiselect styling */
    .stSelectbox, .stMultiSelect {
        margin-bottom: 1rem;
    }
    .stSelectbox > div > div > div {
        font-size: 0.95em;
    }
    /* Button styling */
    .stButton > button {
        background-color: #4CAF50;
        color: white;
        padding: 0.75rem 1.5rem;
        border-radius: 0.5rem;
        border: none;
        font-size: 1.1em;
        width: 100%; /* Full width button for mobile */
        margin-top: 1rem;
    }
    .stButton > button:hover {
        background-color: #45a049;
    }
    /* Card-like display for meal ideas */
    .meal-card {
        background-color: #f9f9f9;
        border-left: 5px solid #4CAF50;
        padding: 1rem;
        margin-bottom: 1rem;
        border-radius: 0.5rem;
        box-shadow: 0 2px 5px rgba(0,0,0,0.1);
    }
    .meal-card h3 {
        color: #333;
        font-size: 1.2em;
        margin-top: 0;
        margin-bottom: 0.5rem;
    }
    .meal-card p {
        font-size: 0.9em;
        color: #555;
        margin-bottom: 0.2rem;
    }
    .best-seller-tag {
        background-color: #FFD700; /* Gold color */
        color: #333;
        font-weight: bold;
        padding: 0.2em 0.5em;
        border-radius: 0.3em;
        font-size: 0.7em;
        margin-left: 0.5em;
    }
    /* Center the markdown text */
    .center-text {
        text-align: center;
    }
</style>
""", unsafe_allow_html=True)

# --- Language Selector ---
# Place the language selector at the top for easy access
language_options = {"English": "en", "Español": "es"}
selected_lang_display = st.selectbox(
    current_text["language_select_label"],
    options=list(language_options.keys()),
    index=list(language_options.values()).index(st.session_state.language),
    key="language_selector"
)
# Check if the language actually changed to trigger a rerun
if st.session_state.language != language_options[selected_lang_display]:
    st.session_state.language = language_options[selected_lang_display]
    st.experimental_rerun()

# --- App Title and Description ---
st.markdown(f"<h1 class='center-text'>{current_text['app_title']}</h1>", unsafe_allow_html=True)
st.write(current_text["app_description"])



## Filter Your Meal Search

st.subheader(current_text["filter_header"])

# Get unique 'broad_type' categories from the DataFrame for *internal* filtering
unique_broad_types_from_data = sorted(df['broad_type'].unique().tolist())

# Prepare the display options for the selectbox, using translations
# We'll create a mapping from displayed_name -> original_broad_type_from_data
broad_type_display_options_map = {}
for bt_original in unique_broad_types_from_data:
    # Use the translated name if available, otherwise fallback to original
    translated_name = current_text["broad_type_translations"].get(bt_original, bt_original)
    broad_type_display_options_map[translated_name] = bt_original

# Add placeholder categories if needed to ensure 8 options
# Ensure we always have exactly 8 options in the dropdown, by adding dummy translated types
# Only add dummy types if the actual broad types are less than 8
if len(broad_type_display_options_map) < 8:
    current_count = len(broad_type_display_options_map)
    for i in range(8 - current_count):
        dummy_name = f"{current_text['other_type']} {i+1}"
        broad_type_display_options_map[dummy_name] = f"DUMMY_TYPE_{i+1}" # Assign a unique internal key

# Convert the map keys to a list for the selectbox options, sorted
displayed_broad_types = [current_text["all_option"]] + sorted(list(broad_type_display_options_map.keys()))

# Broad Type selection
selected_broad_type_display_name = st.selectbox(
    current_text["broad_type_select"],
    displayed_broad_types,
    index=0
)

# Convert the selected display name back to its original broad_type for filtering
if selected_broad_type_display_name == current_text["all_option"]:
    selected_broad_type_for_filter = None # Use None to indicate "All"
else:
    selected_broad_type_for_filter = broad_type_display_options_map.get(selected_broad_type_display_name)


# Best Seller checkbox
filter_best_seller = st.checkbox(current_text["best_seller_checkbox"])



## Meal Ideas

# Filter logic
filtered_df = df.copy()

if selected_broad_type_for_filter is not None:
    # Filter only if the internal broad_type exists in the actual DataFrame
    if selected_broad_type_for_filter in df['broad_type'].unique():
        filtered_df = filtered_df[filtered_df['broad_type'] == selected_broad_type_for_filter]
    else:
        filtered_df = pd.DataFrame() # No meals for a dummy/non-existent broad type

if filter_best_seller:
    filtered_df = filtered_df[filtered_df['best_seller'] == True]

# Display results
if not filtered_df.empty:
    st.markdown(f"<h2>{current_text['results_header_prefix']} {len(filtered_df)} {current_text['results_header_suffix']}</h2>", unsafe_allow_html=True)

    # Random meal suggestion
    if st.button(current_text["suggest_button"]):
        random_meal = filtered_df.sample(1).iloc[0]
        st.markdown(
            f"""
            <div class='meal-card'>
                <h3>{random_meal['meal_name']} {
                    f"<span class='best-seller-tag'>{current_text['best_seller_tag']}</span>" if random_meal['best_seller'] else ""
                }</h3>
                <p><strong>{current_text['broad_type_label']}</strong> {current_text['broad_type_translations'].get(random_meal['broad_type'], random_meal['broad_type'])}</p>
                <p><strong>{current_text['category_label']}</strong> {random_meal['category']}</p>
            </div>
            """, unsafe_allow_html=True
        )
        st.markdown("---")

    st.markdown(f"<h2>{current_text['all_matching_meals']}</h2>", unsafe_allow_html=True)

    # Display all filtered meals in a mobile-friendly card format
    for index, row in filtered_df.iterrows():
        st.markdown(
            f"""
            <div class='meal-card'>
                <h3>{row['meal_name']} {
                    f"<span class='best-seller-tag'>{current_text['best_seller_tag']}</span>" if row['best_seller'] else ""
                }</h3>
                <p><strong>{current_text['broad_type_label']}</strong> {current_text['broad_type_translations'].get(row['broad_type'], row['broad_type'])}</p>
                <p><strong>{current_text['category_label']}</strong> {row['category']}</p>
            </div>
            """, unsafe_allow_html=True
        )
else:
    st.warning(current_text["no_meals_warning"])



st.markdown(f"<p class='center-text'>{current_text['footer']}</p>", unsafe_allow_html=True)
