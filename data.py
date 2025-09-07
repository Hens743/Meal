import streamlit as st
import pandas as pd
import random

# --- LOAD DATA FROM EXTERNAL CSV FILE ---
try:
    df = pd.read_json("meals.json")
except FileNotFoundError:
    st.error("Error: meals.json not found. Please create this file in the same directory as your app.")
    st.stop()

# --- LANGUAGE CONFIGURATION ---
TEXT_CONTENT = {
    "en": {
        "page_title": "Meal Idea Generator", "app_title": "🍽️ What's For Dinner? 🍽️",
        "app_description": "Feeling stuck for meal ideas? Use this app to explore a variety of delicious dishes!",
        "filter_header": "Filter Your Meal Search", "broad_type_select": "Choose a meal type:",
        "all_option": "All", "favorite_checkbox": "Show only My Favorites",
        "results_header_prefix": "Discover", "results_header_suffix": "Meal Ideas!",
        "suggest_button": "Suggest a Random Meal", "all_matching_meals": "All Matching Meals:",
        "broad_type_label": "Broad Type:", "category_label": "Category:",
        "no_meals_warning": "No meals found matching your criteria. Try adjusting your filters!",
        "footer": "Happy cooking! 🍳", "language_toggle_label": "Switch to Spanish",
        "favorite_button": "🤍 Favorite", "unfavorite_button": "❤️ Unfavorite",
        "broad_type_translations": {
            "Roasted & Baked Dishes": "Roasted & Baked Dishes", "Specialty & Street Foods": "Specialty & Street Foods",
            "Soups & Stews": "Soups & Stews", "Rice & Grain Bowls": "Rice & Grain Bowls",
            "Grilled & Pan-Seared": "Grilled & Pan-Seared", "Salads & Light Meals": "Salads & Light Meals",
            "Noodles & Pasta": "Noodles & Pasta", "Sandwiches & Wraps": "Sandwiches & Wraps",
        }
    },
    "es": {
        "page_title": "Generador de Ideas de Comidas", "app_title": "🍽️ ¿Qué hay de Cenar? 🍽️",
        "app_description": "¿No se te ocurren ideas para la comida? ¡Usa esta aplicación para explorar una variedad de deliciosos platos!",
        "filter_header": "Filtra Tu Búsqueda de Comida", "broad_type_select": "Elige un tipo de comida:",
        "all_option": "Todos", "favorite_checkbox": "Mostrar solo Mis Favoritos",
        "results_header_prefix": "¡Descubre", "results_header_suffix": "Ideas de Comida!",
        "suggest_button": "Sugerir una Comida Aleatoria", "all_matching_meals": "Todas las Comidas Coincidentes:",
        "broad_type_label": "Tipo Amplio:", "category_label": "Categoría:",
        "no_meals_warning": "No se encontraron comidas que coincidan con tus criterios. ¡Intenta ajustar tus filtros!",
        "footer": "¡Feliz cocina! 🍳", "language_toggle_label": "Cambiar a Inglés",
        "favorite_button": "🤍 Favorito", "unfavorite_button": "❤️ Quitar Favorito",
        "broad_type_translations": {
            "Roasted & Baked Dishes": "Platos Asados y Horno", "Specialty & Street Foods": "Comidas Especiales y Callejeras",
            "Soups & Stews": "Sopas y Guisos", "Rice & Grain Bowls": "Platos de Arroz y Granos",
            "Grilled & Pan-Seared": "A la Plancha y Asados", "Salads & Light Meals": "Ensaladas y Comidas Ligeras",
            "Noodles & Pasta": "Fideos y Pastas", "Sandwiches & Wraps": "Sándwiches y Wraps",
        }
    }
}

# --- SESSION STATE INITIALIZATION ---
if 'language' not in st.session_state:
    st.session_state.language = "en"
if 'user_favorites' not in st.session_state:
    st.session_state.user_favorites = []

# --- CALLBACK FUNCTIONS ---
def toggle_language():
    st.session_state.language = "es" if st.session_state.language_toggle else "en"

def toggle_favorite(meal_name):
    if meal_name in st.session_state.user_favorites:
        st.session_state.user_favorites.remove(meal_name)
    else:
        st.session_state.user_favorites.append(meal_name)

# --- REUSABLE DISPLAY FUNCTION (UPGRADED) ---
# This single function now draws every meal card, including the new details.
def display_meal_card(meal_row, text_labels):
    """Displays a meal card with its image, details, and a favorite button."""
    is_favorite = meal_row['meal_name'] in st.session_state.user_favorites
    button_label = text_labels['unfavorite_button'] if is_favorite else text_labels['favorite_button']
    
    # Display the meal name and favorite button
    col1, col2 = st.columns([4, 1])
    with col1:
        st.subheader(meal_row['meal_name'])
    with col2:
        st.button(
            button_label, 
            key=f"fav_{meal_row['meal_name']}", 
            on_click=toggle_favorite, 
            args=(meal_row['meal_name'],)
        )

    st.image(meal_row['image_url'], caption=meal_row['meal_name'])
    st.markdown(f"**{text_labels['broad_type_label']}** {text_labels['broad_type_translations'].get(meal_row['broad_type'], meal_row['broad_type'])}")
    st.markdown(f"**{text_labels['category_label']}** {meal_row['category']}")
    
    # --- NEW: Display additional recipe details ---
    # We'll use columns to keep it tidy.
    col1, col2, col3 = st.columns(3)
    col1.metric("Prep Time", f"{int(meal_row['prep_time_mins'])} min")
    col2.metric("Cook Time", f"{int(meal_row['cook_time_mins'])} min")
    col3.metric("Servings", f"{int(meal_row['servings'])} 👤")
    
    # --- NEW: Create a collapsible section for ingredients ---
    with st.expander("Show Ingredients"):
        # Split the ingredients string from the CSV into a list
        ingredients_list = meal_row['ingredients'].split(';')
        # Display each ingredient as a bullet point
        for ingredient in ingredients_list:
            st.markdown(f"- {ingredient.strip()}")
            
    # --- NEW: Add a button to link to the full recipe ---
    # This button will only appear if a URL is provided in the CSV
    if pd.notna(meal_row['recipe_url']) and meal_row['recipe_url'].startswith('http'):
        st.link_button("View Full Recipe ➞", meal_row['recipe_url'])

    st.markdown("---")

# --- APP SETUP ---
current_text = TEXT_CONTENT[st.session_state.language]
st.set_page_config(
    page_title=current_text["page_title"],
    layout="centered",
    # initial_sidebar_state="collapsed" # You can choose 'expanded' or 'auto' as well
)

# --- SIDEBAR CONTROLS ---
# All filters are now neatly tucked away in the sidebar.
st.sidebar.header(current_text["filter_header"])

# Language toggle is also moved to the sidebar for consistency
is_spanish = (st.session_state.language == "es")
st.sidebar.toggle(label=current_text["language_toggle_label"], value=is_spanish, key="language_toggle", on_change=toggle_language)
st.sidebar.markdown("---") # Add a separator

unique_broad_types = sorted(df['broad_type'].unique().tolist())
broad_type_map = { current_text["broad_type_translations"].get(bt, bt): bt for bt in unique_broad_types }
display_options = [current_text["all_option"]] + list(broad_type_map.keys())
selected_display_name = st.sidebar.selectbox(current_text["broad_type_select"], display_options)

filter_favorite = st.sidebar.checkbox(current_text["favorite_checkbox"])

# --- MAIN PAGE CONTENT ---
st.title(current_text['app_title'])
st.write(current_text["app_description"])

# --- APPLY FILTERS ---
filtered_df = df.copy()
if selected_display_name != current_text["all_option"]:
    internal_name = broad_type_map[selected_display_name]
    filtered_df = filtered_df[filtered_df['broad_type'] == internal_name]
if filter_favorite:
    filtered_df = filtered_df[filtered_df['meal_name'].isin(st.session_state.user_favorites)]

# --- DISPLAY RESULTS on the main page ---
if not filtered_df.empty:
    st.header(f"{current_text['results_header_prefix']} {len(filtered_df)} {current_text['results_header_suffix']}")
    
    if st.button(current_text["suggest_button"]):
        random_meal = filtered_df.sample(1).iloc[0]
        display_meal_card(random_meal, current_text)
    else:
        st.markdown(f"### {current_text['all_matching_meals']}")
        for _, row in filtered_df.iterrows():
            display_meal_card(row, current_text)
else:
    st.warning(current_text["no_meals_warning"])

st.markdown(f"<p style='text-align: center;'>{current_text['footer']}</p>", unsafe_allow_html=True)
