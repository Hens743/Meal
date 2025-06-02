import streamlit as st
import pandas as pd
import random

# Meal list as provided
meal_list = [
    # Chilean Inspired
    {'meal_name': "Pastel de Choclo Bake", 'category': "Savory Bake", 'best_seller': random.choice([True, False])},
    {'meal_name': "Empanadas Pino (Beef)", 'category': "Savory Bake", 'best_seller': random.choice([True, False])},
    {'meal_name': "Hearty Cazuela Chilena", 'category': "Stew", 'best_seller': random.choice([True, False])},
    {'meal_name': "Humitas Corn Parcels", 'category': "Warm Meal", 'best_seller': random.choice([True, False])},
    {'meal_name': "Porotos Granados Stew", 'category': "Stew", 'best_seller': random.choice([True, False])},
    {'meal_name': "Lomo Saltado Style Beef", 'category': "Warm Meal", 'best_seller': random.choice([True, False])},
    {'meal_name': "Congrio Frito (Fried Conger Eel)", 'category': "Seafood Special", 'best_seller': random.choice([True, False])},
    {'meal_name': "Machas a la Parmesana", 'category': "Seafood Special", 'best_seller': random.choice([True, False])},
    {'meal_name': "Charquican Beef Stew", 'category': "Stew", 'best_seller': random.choice([True, False])},
    {'meal_name': "Pebre Chicken Bowl", 'category': "Rice Bowl", 'best_seller': random.choice([True, False])},
    {'meal_name': "Curanto Inspired Seafood Pot", 'category': "Seafood Special", 'best_seller': random.choice([True, False])},
    {'meal_name': "Sopaipillas Pasadas (savory version context)", 'category': "Warm Meal", 'best_seller': random.choice([True, False])},
    {'meal_name': "Valdiviano Soup", 'category': "Soup", 'best_seller': random.choice([True, False])},
    {'meal_name': "Costillar de Chancho Ahumado", 'category': "Roast", 'best_seller': random.choice([True, False])},
    {'meal_name': "Pastel de Jaiba (Crab Pie)", 'category': "Savory Bake", 'best_seller': random.choice([True, False])},

    # General Meals - Warm Meals
    {'meal_name': "Classic Chicken Roast", 'category': "Roast", 'best_seller': random.choice([True, False])},
    {'meal_name': "Beef & Ale Stew", 'category': "Stew", 'best_seller': True},
    {'meal_name': "Spicy Lamb Curry", 'category': "Warm Meal", 'best_seller': random.choice([True, False])},
    {'meal_name': "Pork Belly Ramen", 'category': "Soup", 'best_seller': random.choice([True, False])},
    {'meal_name': "Vegetable Paella", 'category': "Rice Bowl", 'best_seller': False},
    {'meal_name': "Mushroom Risotto", 'category': "Pasta Dish", 'best_seller': True},
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
    {'meal_name': "Gazpacho Andaluz", 'category': "Soup", 'best_seller': random.choice([True, False])},
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
    {'meal_name': "Pad Thai Noodles", 'category': "Pasta Dish", 'best_seller': random.choice([True, False])},
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
    {'meal_name': "Lobster Bisque", 'category': "Soup", 'best_seller': random.choice([True, False])},
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
    {'meal_name': "Vegetable Samosas", 'category': "Vegetarian Delight", 'best_seller': random.choice([True, False])},
    {'meal_name': "Sweet Potato and Black Bean Tacos", 'category': "Vegetarian Delight", 'best_seller': random.choice([True, False])},
    {'meal_name': "Ratatouille", 'category': "Vegetarian Delight", 'best_seller': False},
    {'meal_name': "Chana Masala", 'category': "Vegetarian Delight", 'best_seller': random.choice([True, False])},
    {'meal_name': "Falafel Platter with Hummus", 'category': "Vegetarian Delight", 'best_seller': random.choice([True, False])},
    {'meal_name': "Stuffed Artichokes", 'category': "Vegetarian Delight", 'best_seller': random.choice([True, False])},
    {'meal_name': "Dal Makhani", 'category': "Vegetarian Delight", 'best_seller': random.choice([True, False])},
]

# Create a DataFrame from the meal list
df = pd.DataFrame(meal_list)

# --- Streamlit App Configuration ---
st.set_page_config(
    page_title="Meal Idea Generator",
    layout="centered",
    initial_sidebar_state="expanded"
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

# --- App Title and Description ---
st.markdown("<h1 class='center-text'>🍽️ What's For Dinner? 🍽️</h1>", unsafe_allow_html=True)
st.write("Feeling stuck for meal ideas? Use this app to explore a variety of delicious dishes!")

# --- Sidebar for Filters (Mobile-friendly) ---
st.sidebar.header("Filter Meals")

# Get unique categories for the filter
categories = ["All"] + sorted(df['category'].unique().tolist())

# Category selection
selected_category = st.sidebar.selectbox(
    "Choose a meal category:",
    categories,
    index=0 # Default to "All"
)

# Best Seller checkbox
filter_best_seller = st.sidebar.checkbox("Show only Best Sellers")

# --- Main Content Area ---
st.markdown("---")

# Filter logic
filtered_df = df.copy()

if selected_category != "All":
    filtered_df = filtered_df[filtered_df['category'] == selected_category]

if filter_best_seller:
    filtered_df = filtered_df[filtered_df['best_seller'] == True]

# Display results
if not filtered_df.empty:
    st.markdown(f"<h2>Discover {len(filtered_df)} Meal Ideas!</h2>", unsafe_allow_html=True)

    # Random meal suggestion (for mobile, one at a time is better)
    if st.button("Suggest a Random Meal"):
        random_meal = filtered_df.sample(1).iloc[0]
        st.markdown(
            f"""
            <div class='meal-card'>
                <h3>{random_meal['meal_name']} {
                    "<span class='best-seller-tag'>⭐ Best Seller</span>" if random_meal['best_seller'] else ""
                }</h3>
                <p><strong>Category:</strong> {random_meal['category']}</p>
            </div>
            """, unsafe_allow_html=True
        )
        st.markdown("---") # Separator after random suggestion

    st.markdown("<h2>All Matching Meals:</h2>", unsafe_allow_html=True)

    # Display all filtered meals in a mobile-friendly card format
    for index, row in filtered_df.iterrows():
        st.markdown(
            f"""
            <div class='meal-card'>
                <h3>{row['meal_name']} {
                    "<span class='best-seller-tag'>⭐ Best Seller</span>" if row['best_seller'] else ""
                }</h3>
                <p><strong>Category:</strong> {row['category']}</p>
            </div>
            """, unsafe_allow_html=True
        )
else:
    st.warning("No meals found matching your criteria. Try adjusting your filters!")

st.markdown("---")
st.markdown("<p class='center-text'>Happy cooking! 🍳</p>", unsafe_allow_html=True)
