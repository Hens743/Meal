import streamlit as st
import pandas as pd
import random

# --- Data Loading Function ---
def load_meals_data(uploaded_file=None):
            # Original small list
            original_meals = [
                {'meal_name': "Sample Noodles", 'category': "Warm Meal", 'best_seller': True},
                {'meal_name': "Sample Soup", 'category': "Soup", 'best_seller': False},
                {'meal_name': "Sample Sandwich", 'category': "Sandwich", 'best_seller': False},
                {'meal_name': "Sample Salad", 'category': "Salad", 'best_seller': False},
                {'meal_name': "Sample Chili", 'category': "Warm Meal", 'best_seller': True},
                {'meal_name': "Sample Pasta", 'category': "Warm Meal", 'best_seller': True},
                {'meal_name': "Sample Tacos", 'category': "Warm Meal", 'best_seller': False}
            ]

            extended_meal_list = [
                # Chilean Inspired
                {'meal_name': "Pastel de Choclo Bake", 'category': "Savory Bake", 'best_seller': random.choice([True, False])},
                {'meal_name': "Empanadas Pino (Beef)", 'category': "Savory Bake", 'best_seller': random.choice([True, False])},
                {'meal_name': "Hearty Cazuela Chilena", 'category': "Stew", 'best_seller': random.choice([True, False])},
                {'meal_name': "Humitas Corn Parcels", 'category': "Warm Meal", 'best_seller': random.choice([True, False])},
                {'meal_name': "Porotos Granados Stew", 'category': "Stew", 'best_seller': random.choice([True, False])},
                {'meal_name': "Lomo Saltado Style Beef", 'category': "Warm Meal", 'best_seller': random.choice([True, False])}, # Peruvian, but often liked
                {'meal_name': "Congrio Frito (Fried Conger Eel)", 'category': "Seafood Special", 'best_seller': random.choice([True, False])},
                {'meal_name': "Machas a la Parmesana", 'category': "Seafood Special", 'best_seller': random.choice([True, False])},
                {'meal_name': "Charquican Beef Stew", 'category': "Stew", 'best_seller': random.choice([True, False])},
                {'meal_name': "Pebre Chicken Bowl", 'category': "Rice Bowl", 'best_seller': random.choice([True, False])},
                {'meal_name': "Curanto Inspired Seafood Pot", 'category': "Seafood Special", 'best_seller': random.choice([True, False])},
                {'meal_name': "Sopaipillas Pasadas (savory version context)", 'category': "Warm Meal", 'best_seller': random.choice([True, False])}, # Ensure savory context
                {'meal_name': "Valdiviano Soup", 'category': "Soup", 'best_seller': random.choice([True, False])},
                {'meal_name': "Costillar de Chancho Ahumado", 'category': "Roast", 'best_seller': random.choice([True, False])}, # Smoked Pork Ribs
                {'meal_name': "Pastel de Jaiba (Crab Pie)", 'category': "Savory Bake", 'best_seller': random.choice([True, False])},


                # General Meals - Warm Meals
                {'meal_name': "Classic Chicken Roast", 'category': "Roast", 'best_seller': random.choice([True, False])},
                {'meal_name': "Beef & Ale Stew", 'category': "Stew", 'best_seller': True},
                {'meal_name': "Spicy Lamb Curry", 'category': "Warm Meal", 'best_seller': random.choice([True, False])},
                {'meal_name': "Pork Belly Ramen", 'category': "Soup", 'best_seller': random.choice([True, False])},
                {'meal_name': "Vegetable Paella", 'category': "Rice Bowl", 'best_seller': False},
                {'meal_name': "Mushroom Risotto", 'category': "Pasta Dish", 'best_seller': True}, # Technically rice, but often with pasta
                {'meal_name': "Shepherd's Pie", 'category': "Savory Bake", 'best_seller': random.choice([True, False])},
                {'meal_name': "Chicken Tikka Masala", 'category': "Warm Meal", 'best_seller': True},
                {'meal_name': "Hearty Beef Goulash", 'category': "Stew", 'best_seller': random.choice([True, False])},
                {'meal_name': "Lemon Herb Roasted Chicken", 'category': "Roast", 'best_seller': random.choice([True, False])},
                {'meal_name': "Spicy Chorizo and Bean Casserole", 'category': "Savory Bake", 'best_seller': random.choice([True, False])},
                {'meal_name': "Thai Green Curry with Tofu", 'category': "Warm Meal", 'best_seller': random.choice([True, False])},
                {'meal_name': "Slow-Cooked Pulled Pork", 'category': "Warm Meal", 'best_seller': True},
                {'meal_name': "Stuffed Bell Peppers with Quinoa", 'category': "Vegetarian Delight", 'best_seller': random.choice([True, False])},
                {'meal_name': "Beef Stroganoff with Noodles", 'category': "Pasta Dish", 'best_seller': random.choice([True, False])},
                {'meal_name': "Baked Salmon with Asparagus", 'category': "Seafood Special", 'best_seller': random.choice([True, False])},
                {'meal_name': "Chicken and Mushroom Pie", 'category': "Savory Bake", 'best_seller': random.choice([True, False])},
                {'meal_name': "Lentil Shepherd's Pie", 'category': "Vegetarian Delight", 'best_seller': random.choice([True, False])},
                {'meal_name': "Pork Chops with Apple Sauce", 'category': "Warm Meal", 'best_seller': random.choice([True, False])},
                {'meal_name': "Vegetable Stir-fry with Noodles", 'category': "Warm Meal", 'best_seller': False},
                {'meal_name': "Classic Meatloaf", 'category': "Roast", 'best_seller': random.choice([True, False])},
                {'meal_name': "Chicken Fajitas Platter", 'category': "Warm Meal", 'best_seller': random.choice([True, False])},
                {'meal_name': "BBQ Ribs", 'category': "Grilled Dish", 'best_seller': True},
                {'meal_name': "Spinach and Ricotta Stuffed Shells", 'category': "Pasta Dish", 'best_seller': random.choice([True, False])},
                {'meal_name': "Beef Burrito Bowl", 'category': "Rice Bowl", 'best_seller': random.choice([True, False])},

                # Soups
                {'meal_name': "Creamy Tomato Soup", 'category': "Soup", 'best_seller': random.choice([True, False])},
                {'meal_name': "Chicken Noodle Soup", 'category': "Soup", 'best_seller': True},
                {'meal_name': "Minestrone Soup", 'category': "Soup", 'best_seller': random.choice([True, False])},
                {'meal_name': "French Onion Soup", 'category': "Soup", 'best_seller': random.choice([True, False])},
                {'meal_name': "Butternut Squash Soup", 'category': "Soup", 'best_seller': random.choice([True, False])},
                {'meal_name': "Lentil and Vegetable Soup", 'category': "Soup", 'best_seller': random.choice([True, False])},
                {'meal_name': "Spicy Black Bean Soup", 'category': "Soup", 'best_seller': False},
                {'meal_name': "Potato Leek Soup", 'category': "Soup", 'best_seller': random.choice([True, False])},
                {'meal_name': "Gazpacho Andaluz", 'category': "Soup", 'best_seller': random.choice([True, False])}, # Cold soup
                {'meal_name': "Miso Soup with Tofu", 'category': "Soup", 'best_seller': random.choice([True, False])},

                # Sandwiches
                {'meal_name': "Classic BLT Sandwich", 'category': "Sandwich", 'best_seller': True},
                {'meal_name': "Grilled Cheese Sandwich", 'category': "Sandwich", 'best_seller': random.choice([True, False])},
                {'meal_name': "Turkey Club Sandwich", 'category': "Sandwich", 'best_seller': random.choice([True, False])},
                {'meal_name': "Roast Beef Sandwich", 'category': "Sandwich", 'best_seller': random.choice([True, False])},
                {'meal_name': "Veggie Delight Sandwich", 'category': "Sandwich", 'best_seller': False},
                {'meal_name': "Pulled Pork Sandwich", 'category': "Sandwich", 'best_seller': random.choice([True, False])},
                {'meal_name': "Chicken Salad Sandwich", 'category': "Sandwich", 'best_seller': random.choice([True, False])},
                {'meal_name': "Tuna Melt Sandwich", 'category': "Sandwich", 'best_seller': random.choice([True, False])},
                {'meal_name': "Falafel Pita Sandwich", 'category': "Sandwich", 'best_seller': random.choice([True, False])},
                {'meal_name': "Caprese Panini", 'category': "Sandwich", 'best_seller': random.choice([True, False])},

                # Salads (as main courses)
                {'meal_name': "Chicken Caesar Salad", 'category': "Salad", 'best_seller': True},
                {'meal_name': "Greek Salad with Feta", 'category': "Salad", 'best_seller': random.choice([True, False])},
                {'meal_name': "Cobb Salad", 'category': "Salad", 'best_seller': random.choice([True, False])},
                {'meal_name': "Quinoa Salad with Roasted Vegetables", 'category': "Salad", 'best_seller': random.choice([True, False])},
                {'meal_name': "Nicoise Salad with Tuna", 'category': "Salad", 'best_seller': random.choice([True, False])},
                {'meal_name': "Taco Salad with Beef", 'category': "Salad", 'best_seller': random.choice([True, False])},
                {'meal_name': "Warm Goat Cheese Salad", 'category': "Salad", 'best_seller': False},
                {'meal_name': "Pasta Salad with Pesto", 'category': "Salad", 'best_seller': random.choice([True, False])},
                {'meal_name': "Asian Chicken Salad", 'category': "Salad", 'best_seller': random.choice([True, False])},
                {'meal_name': "Lentil Salad with Herbs", 'category': "Salad", 'best_seller': random.choice([True, False])},

                # Stews
                {'meal_name': "Irish Lamb Stew", 'category': "Stew", 'best_seller': random.choice([True, False])},
                {'meal_name': "Hungarian Goulash", 'category': "Stew", 'best_seller': random.choice([True, False])},
                {'meal_name': "Seafood Cioppino", 'category': "Stew", 'best_seller': random.choice([True, False])},
                {'meal_name': "Chickpea and Spinach Stew", 'category': "Stew", 'best_seller': random.choice([True, False])},
                {'meal_name': "Brazilian Feijoada", 'category': "Stew", 'best_seller': random.choice([True, False])},
                {'meal_name': "Spicy Sausage and Kale Stew", 'category': "Stew", 'best_seller': random.choice([True, False])},
                {'meal_name': "Root Vegetable Stew", 'category': "Vegetarian Delight", 'best_seller': False},
                {'meal_name': "Moroccan Chicken Tagine", 'category': "Stew", 'best_seller': random.choice([True, False])},
                {'meal_name': "Beef and Guinness Stew", 'category': "Stew", 'best_seller': random.choice([True, False])},
                {'meal_name': "White Bean and Escarole Stew", 'category': "Stew", 'best_seller': random.choice([True, False])},

                # Roasts
                {'meal_name': "Roast Duck with Orange Glaze", 'category': "Roast", 'best_seller': random.choice([True, False])},
                {'meal_name': "Honey Glazed Ham", 'category': "Roast", 'best_seller': random.choice([True, False])},
                {'meal_name': "Roast Turkey Breast", 'category': "Roast", 'best_seller': random.choice([True, False])},
                {'meal_name': "Garlic and Herb Crusted Lamb Roast", 'category': "Roast", 'best_seller': random.choice([True, False])},
                {'meal_name': "Pot Roast with Vegetables", 'category': "Roast", 'best_seller': True},
                {'meal_name': "Whole Roasted Cauliflower", 'category': "Vegetarian Delight", 'best_seller': random.choice([True, False])},
                {'meal_name': "Roast Pork Shoulder (Pernil)", 'category': "Roast", 'best_seller': random.choice([True, False])},
                {'meal_name': "Mediterranean Roasted Vegetables", 'category': "Roast", 'best_seller': False},
                {'meal_name': "Prime Rib Roast", 'category': "Roast", 'best_seller': random.choice([True, False])},
                {'meal_name': "Maple Glazed Roasted Salmon", 'category': "Seafood Special", 'best_seller': random.choice([True, False])},

                # Grilled Dishes
                {'meal_name': "Grilled Salmon with Lemon Dill Sauce", 'category': "Grilled Dish", 'best_seller': True},
                {'meal_name': "BBQ Chicken Skewers", 'category': "Grilled Dish", 'best_seller': random.choice([True, False])},
                {'meal_name': "Grilled Steak with Chimichurri", 'category': "Grilled Dish", 'best_seller': random.choice([True, False])},
                {'meal_name': "Grilled Halloumi and Vegetable Skewers", 'category': "Grilled Dish", 'best_seller': random.choice([True, False])},
                {'meal_name': "Jerk Chicken Wings", 'category': "Grilled Dish", 'best_seller': random.choice([True, False])},
                {'meal_name': "Grilled Swordfish Steaks", 'category': "Seafood Special", 'best_seller': random.choice([True, False])},
                {'meal_name': "Korean BBQ Short Ribs (Galbi)", 'category': "Grilled Dish", 'best_seller': random.choice([True, False])},
                {'meal_name': "Grilled Portobello Mushrooms", 'category': "Vegetarian Delight", 'best_seller': False},
                {'meal_name': "Lamb Kofta Kebabs", 'category': "Grilled Dish", 'best_seller': random.choice([True, False])},
                {'meal_name': "Pineapple Glazed Grilled Pork Tenderloin", 'category': "Grilled Dish", 'best_seller': random.choice([True, False])},

                # Savory Bakes
                {'meal_name': "Chicken Pot Pie", 'category': "Savory Bake", 'best_seller': True},
                {'meal_name': "Lasagna Bolognese", 'category': "Savory Bake", 'best_seller': True},
                {'meal_name': "Vegetable Lasagna", 'category': "Savory Bake", 'best_seller': random.choice([True, False])},
                {'meal_name': "Macaroni and Cheese Bake", 'category': "Savory Bake", 'best_seller': random.choice([True, False])},
                {'meal_name': "Quiche Lorraine", 'category': "Savory Bake", 'best_seller': random.choice([True, False])},
                {'meal_name': "Spinach and Feta Pie (Spanakopita)", 'category': "Savory Bake", 'best_seller': random.choice([True, False])},
                {'meal_name': "Sausage and Bean Bake", 'category': "Savory Bake", 'best_seller': random.choice([True, False])},
                {'meal_name': "Tuna Noodle Casserole", 'category': "Savory Bake", 'best_seller': False},
                {'meal_name': "Moussaka", 'category': "Savory Bake", 'best_seller': random.choice([True, False])},
                {'meal_name': "Cornbread Topped Chili Bake", 'category': "Savory Bake", 'best_seller': random.choice([True, False])},

                # Pasta Dishes
                {'meal_name': "Spaghetti Carbonara", 'category': "Pasta Dish", 'best_seller': True},
                {'meal_name': "Penne alla Vodka", 'category': "Pasta Dish", 'best_seller': random.choice([True, False])},
                {'meal_name': "Fettuccine Alfredo", 'category': "Pasta Dish", 'best_seller': random.choice([True, False])},
                {'meal_name': "Pesto Pasta with Cherry Tomatoes", 'category': "Pasta Dish", 'best_seller': random.choice([True, False])},
                {'meal_name': "Shrimp Scampi with Linguine", 'category': "Pasta Dish", 'best_seller': random.choice([True, False])},
                {'meal_name': "Aglio e Olio Peperoncino", 'category': "Pasta Dish", 'best_seller': False},
                {'meal_name': "Baked Ziti", 'category': "Pasta Dish", 'best_seller': random.choice([True, False])},
                {'meal_name': "Sausage and Broccoli Rabe Pasta", 'category': "Pasta Dish", 'best_seller': random.choice([True, False])},
                {'meal_name': "Pad Thai Noodles", 'category': "Pasta Dish", 'best_seller': random.choice([True, False])}, # Noodle dish
                {'meal_name': "Gnocchi with Sage Butter Sauce", 'category': "Pasta Dish", 'best_seller': random.choice([True, False])},

                # Rice Bowls
                {'meal_name': "Teriyaki Chicken Rice Bowl", 'category': "Rice Bowl", 'best_seller': True},
                {'meal_name': "Korean Bibimbap", 'category': "Rice Bowl", 'best_seller': random.choice([True, False])},
                {'meal_name': "Spicy Tuna Poke Bowl", 'category': "Rice Bowl", 'best_seller': random.choice([True, False])},
                {'meal_name': "Mediterranean Chickpea Rice Bowl", 'category': "Rice Bowl", 'best_seller': random.choice([True, False])},
                {'meal_name': "Jambalaya Rice", 'category': "Rice Bowl", 'best_seller': random.choice([True, False])},
                {'meal_name': "Arroz con Pollo", 'category': "Rice Bowl", 'best_seller': False},
                {'meal_name': "Sushi Bowl (Chirashi-style)", 'category': "Rice Bowl", 'best_seller': random.choice([True, False])},
                {'meal_name': "Black Bean and Corn Salsa Rice Bowl", 'category': "Rice Bowl", 'best_seller': random.choice([True, False])},
                {'meal_name': "Coconut Curry Lentil Rice Bowl", 'category': "Rice Bowl", 'best_seller': random.choice([True, False])},
                {'meal_name': "Salmon and Avocado Rice Bowl", 'category': "Rice Bowl", 'best_seller': random.choice([True, False])},
                
                # Seafood Specials
                {'meal_name': "Fish and Chips", 'category': "Seafood Special", 'best_seller': True},
                {'meal_name': "Grilled Swordfish with Mango Salsa", 'category': "Seafood Special", 'best_seller': random.choice([True, False])},
                {'meal_name': "Pan-Seared Scallops", 'category': "Seafood Special", 'best_seller': random.choice([True, False])},
                {'meal_name': "Lobster Bisque", 'category': "Soup", 'best_seller': random.choice([True, False])}, # Also a soup
                {'meal_name': "Crab Cakes with Remoulade", 'category': "Seafood Special", 'best_seller': random.choice([True, False])},
                {'meal_name': "Steamed Mussels in White Wine", 'category': "Seafood Special", 'best_seller': False},
                {'meal_name': "Tuna Steak Au Poivre", 'category': "Seafood Special", 'best_seller': random.choice([True, False])},
                {'meal_name': "Ceviche Clasico", 'category': "Seafood Special", 'best_seller': random.choice([True, False])},
                {'meal_name': "Baked Cod with Lemon and Herbs", 'category': "Seafood Special", 'best_seller': random.choice([True, False])},
                {'meal_name': "Shrimp and Grits", 'category': "Seafood Special", 'best_seller': random.choice([True, False])},

                # Vegetarian Delights (can overlap with other categories)
                {'meal_name': "Eggplant Parmesan", 'category': "Vegetarian Delight", 'best_seller': True},
                {'meal_name': "Tofu Scramble Breakfast Bowl", 'category': "Vegetarian Delight", 'best_seller': random.choice([True, False])},
                {'meal_name': "Mushroom Bourguignon", 'category': "Vegetarian Delight", 'best_seller': random.choice([True, False])},
                {'meal_name': "Vegetable Samosas", 'category': "Vegetarian Delight", 'best_seller': random.choice([True, False])}, # Appetizer/Warm Meal
                {'meal_name': "Sweet Potato and Black Bean Tacos", 'category': "Vegetarian Delight", 'best_seller': random.choice([True, False])},
                {'meal_name': "Ratatouille", 'category': "Vegetarian Delight", 'best_seller': False},
                {'meal_name': "Chana Masala", 'category': "Vegetarian Delight", 'best_seller': random.choice([True, False])},
                {'meal_name': "Falafel Platter with Hummus", 'category': "Vegetarian Delight", 'best_seller': random.choice([True, False])},
                {'meal_name': "Stuffed Artichokes", 'category': "Vegetarian Delight", 'best_seller': random.choice([True, False])},
                {'meal_name': "Dal Makhani", 'category': "Vegetarian Delight", 'best_seller': random.choice([True, False])},
            ]

            all_meals_data = original_meals + extended_meal_list
            
            df = pd.DataFrame(all_meals_data)

# The rest of your Streamlit application code remains the same
# Make sure to copy this updated load_meals_data function into your existing script.
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
    st.session_state.selected_categories = []
elif 'meals_df' not in st.session_state:
    st.session_state.meals_df = load_meals_data(None)
    st.session_state.last_uploaded_file_id = None

if uploaded_file is None and \
   not st.session_state.get('load_hardcoded_checkbox', False) and \
   'meals_df' in st.session_state and \
   not st.session_state.meals_df.empty and \
   st.session_state.get('last_uploaded_file_id') is None : 
    st.session_state.meals_df = pd.DataFrame()


# --- Display Filters and Suggestions (ONLY if data is loaded) ---
if 'meals_df' in st.session_state and not st.session_state.meals_df.empty:
    st.sidebar.success("Meal data loaded successfully! Filters are available.")
    st.sidebar.markdown("---")
    st.sidebar.header("Filter Suggestions")

    if 'selected_categories' not in st.session_state:
        st.session_state.selected_categories = []

    st.sidebar.subheader("Filter by Category")
    temp_selected_categories = []
    if 'category' in st.session_state.meals_df.columns:
        all_categories = sorted(st.session_state.meals_df['category'].unique().tolist())
        for category in all_categories:
            if st.sidebar.checkbox(category, key=f"category_checkbox_{category}", value=(category in st.session_state.selected_categories)):
                temp_selected_categories.append(category)
        if temp_selected_categories != st.session_state.selected_categories: 
            st.session_state.selected_categories = temp_selected_categories
    else:
        st.sidebar.warning("Category information is not available in the current dataset.")
    
    show_best_sellers = st.sidebar.checkbox("Show Only Best Sellers")
    search_query = st.sidebar.text_input("Search by Meal Name", placeholder="e.g., chicken, soup")

    # --- Apply Filters ---
    filtered_df = st.session_state.meals_df.copy()
    if st.session_state.selected_categories and 'category' in filtered_df.columns:
        filtered_df = filtered_df[filtered_df['category'].isin(st.session_state.selected_categories)]
    
    if show_best_sellers:
        if 'best_seller' in filtered_df.columns:
             filtered_df = filtered_df[filtered_df['best_seller'] == True]
        else:
            st.sidebar.warning("Best seller information is not available for filtering.") 
    if search_query and 'meal_name' in filtered_df.columns:
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
                st.warning("Your meal database is empty! Cannot provide a surprise.")
    with col_desc:
        st.caption("Get a random meal from your entire collection.")

    if surprise_meal_details is not None:
        st.subheader("🎉 Today's Surprise Meal!")
        meal_name_display = surprise_meal_details.get('meal_name', 'N/A')
        category_display = surprise_meal_details.get('category', 'N/A')
        is_best_seller = surprise_meal_details.get('best_seller', False)

        card_md = f"""
        <div style="border: 1px solid #ddd; border-radius: 5px; padding: 15px; margin-bottom: 10px; background-color: #f9f9f9;">
            <h4>{meal_name_display}</h4>
            <p><strong>Category:</strong> {category_display}<br>
            </p>
            { "<h5>🏆 Best Seller!</h5>" if is_best_seller else "" }
        </div>
        """
        st.markdown(card_md, unsafe_allow_html=True)

    st.markdown("---")

    any_filter_active = (
        bool(st.session_state.selected_categories) or
        show_best_sellers or
        bool(search_query)
    )

    if any_filter_active:
        st.subheader("Your Meal Suggestions (based on filters):")
        if not filtered_df.empty:
            num_cols = 3 
            cols = st.columns(num_cols)
            for index, row in filtered_df.iterrows():
                with cols[index % num_cols]:
                    meal_name_display = row.get('meal_name', 'N/A')
                    category_display = row.get('category', 'N/A')
                    is_best_seller = row.get('best_seller', False)
                    
                    st.markdown(f"""
                    <div style="border: 1px solid #ddd; border-radius: 5px; padding: 10px; margin: 5px 0;">
                        <strong>{meal_name_display}</strong><br>
                        <small>Category: {category_display}</small><br>
                        { "🏆 <small><strong>Best Seller!</strong></small>" if is_best_seller else "" }
                    </div>
                    """, unsafe_allow_html=True)
        else:
            st.info("No meals found matching your current filters. Try adjusting your search criteria!")
    elif surprise_meal_details is None: 
        st.info("Apply filters to see suggestions, or click 'Surprise Me!' for a random pick.")

else:
    if 'meals_df' not in st.session_state or st.session_state.meals_df.empty:
         st.info("Upload a meal list or select 'Load Hardcoded Sample Data' in the sidebar to get started.")


st.markdown("---")
st.write("Built with ❤️ using Streamlit")
