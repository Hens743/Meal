import streamlit as st
import pandas as pd
import random

# Meal list (remains the same - data content, not UI text)
meal_list = [
    # Chilean Meals - Broad Type Categorization
    {'meal_name': "Pastel de Choclo Bake", 'category': "Savory Bake", 'best_seller': random.choice([True, False]), 'broad_type': "Roasted & Baked Dishes"},
    {'meal_name': "Empanadas Pino (Beef)", 'category': "Savory Bake", 'best_seller': random.choice([True, False]), 'broad_type': "Specialty & Street Foods"}, # Can be baked, but often street food
    {'meal_name': "Hearty Cazuela Chilena", 'category': "Stew", 'best_seller': random.choice([True, False]), 'broad_type': "Soups & Stews"},
    {'meal_name': "Humitas Corn Parcels", 'category': "Warm Meal", 'best_seller': random.choice([True, False]), 'broad_type': "Rice & Grain Bowls"}, # Corn is a grain/staple
    {'meal_name': "Porotos Granados Stew", 'category': "Stew", 'best_seller': random.choice([True, False]), 'broad_type': "Soups & Stews"},
    {'meal_name': "Congrio Frito (Fried Conger Eel)", 'category': "Seafood Special", 'best_seller': random.choice([True, False]), 'broad_type': "Grilled & Pan-Seared"}, # Fried is a form of pan-searing
    {'meal_name': "Machas a la Parmesana", 'category': "Seafood Special", 'best_seller': random.choice([True, False]), 'broad_type': "Specialty & Street Foods"}, # Unique seafood prep
    {'meal_name': "Charquican Beef Stew", 'category': "Stew", 'best_seller': random.choice([True, False]), 'broad_type': "Soups & Stews"},
    {'meal_name': "Pebre Chicken Bowl", 'category': "Rice Bowl", 'best_seller': random.choice([True, False]), 'broad_type': "Rice & Grain Bowls"},
    {'meal_name': "Curanto Inspired Seafood Pot", 'category': "Seafood Special", 'best_seller': random.choice([True, False]), 'broad_type': "Soups & Stews"}, # Pot/Stew
    {'meal_name': "Sopaipillas Pasadas (savory version context)", 'category': "Warm Meal", 'best_seller': random.choice([True, False]), 'broad_type': "Specialty & Street Foods"}, # Fried pastry
    {'meal_name': "Valdiviano Soup", 'category': "Soup", 'best_seller': random.choice([True, False]), 'broad_type': "Soups & Stews"},
    {'meal_name': "Costillar de Chancho Ahumado", 'category': "Roast", 'best_seller': random.choice([True, False]), 'broad_type': "Roasted & Baked Dishes"},
    {'meal_name': "Pastel de Jaiba (Crab Pie)", 'category': "Savory Bake", 'best_seller': random.choice([True, False]), 'broad_type': "Roasted & Baked Dishes"},

    # Peruvian Meals - Broad Type Categorization
    {'meal_name': "Lomo Saltado Style Beef", 'category': "Warm Meal", 'best_seller': random.choice([True, False]), 'broad_type': "Grilled & Pan-Seared"}, # Stir-fried, so direct heat
    {'meal_name': "Ceviche Clasico", 'category': "Seafood Special", 'best_seller': random.choice([True, False]), 'broad_type': "Salads & Light Meals"}, # Cold, light, raw

    # French Meals - Broad Type Categorization
    {'meal_name': "Classic French Onion Soup", 'category': "Soup", 'best_seller': random.choice([True, False]), 'broad_type': "Soups & Stews"},
    {'meal_name': "Quiche Lorraine", 'category': "Savory Bake", 'best_seller': random.choice([True, False]), 'broad_type': "Roasted & Baked Dishes"},
    {'meal_name': "Ratatouille", 'category': "Vegetarian Delight", 'best_seller': False, 'broad_type': "Roasted & Baked Dishes"}, # Often baked or slow-cooked
    {'meal_name': "Mushroom Bourguignon", 'category': "Vegetarian Delight", 'best_seller': random.choice([True, False]), 'broad_type': "Soups & Stews"}, # Stew
    {'meal_name': "Steak au Poivre with Red Wine Pan Sauce", 'category': "Warm Meal", 'best_seller': random.choice([True, False]), 'broad_type': "Grilled & Pan-Seared"},
    {'meal_name': "Duck à l'Orange", 'category': "Roast", 'best_seller': random.choice([True, False]), 'broad_type': "Roasted & Baked Dishes"},
    {'meal_name': "Julia Child's Favorite Roast Chicken", 'category': "Roast", 'best_seller': random.choice([True, False]), 'broad_type': "Roasted & Baked Dishes"},
    {'meal_name': "Lyon-Style Chicken with Vinegar Sauce", 'category': "Warm Meal", 'best_seller': random.choice([True, False]), 'broad_type': "Grilled & Pan-Seared"}, # Pan-seared then sauced
    {'meal_name': "Crispy Monkfish with Capers", 'category': "Seafood Special", 'best_seller': random.choice([True, False]), 'broad_type': "Grilled & Pan-Seared"},
    {'meal_name': "Beef Stew in Red Wine Sauce (Boeuf Bourguignon)", 'category': "Stew", 'best_seller': random.choice([True, False]), 'broad_type': "Soups & Stews"},
    {'meal_name': "Chicken Legs Coq au Vin", 'category': "Stew", 'best_seller': random.choice([True, False]), 'broad_type': "Soups & Stews"},
    {'meal_name': "Stuffed Pork Tenderloins with Bacon and Apple-Riesling Sauce", 'category': "Roast", 'best_seller': random.choice([True, False]), 'broad_type': "Roasted & Baked Dishes"},
    {'meal_name': "French Egg Salad", 'category': "Salad", 'best_seller': random.choice([True, False]), 'broad_type': "Salads & Light Meals"},
    {'meal_name': "Chicken Cordon Bleu", 'category': "Warm Meal", 'best_seller': random.choice([True, False]), 'broad_type': "Specialty & Street Foods"}, # Breaded and often fried/baked
    {'meal_name': "Lyonnaise Potatoes (Pommes de terre à la Lyonnaise)", 'category': "Side Dish", 'best_seller': random.choice([True, False]), 'broad_type': "Roasted & Baked Dishes"}, # Often baked/roasted to crisp
    {'meal_name': "Lamb Navarin (Navarin d'agneau)", 'category': "Stew", 'best_seller': random.choice([True, False]), 'broad_type': "Soups & Stews"},
    {'meal_name': "French-Style Potato and Green Bean Salad", 'category': "Salad", 'best_seller': random.choice([True, False]), 'broad_type': "Salads & Light Meals"},
    {'meal_name': "White Asparagus à la Grenobloise", 'category': "Vegetarian Delight", 'best_seller': random.choice([True, False]), 'broad_type': "Salads & Light Meals"}, # Light meal, cooked asparagus
    {'meal_name': "French Beef Daube (Traditional Provençal Stew)", 'category': "Stew", 'best_seller': random.choice([True, False]), 'broad_type': "Soups & Stews"},
    {'meal_name': "Braised Pork Loin with Prunes (Porc aux pruneaux)", 'category': "Roast", 'best_seller': random.choice([True, False]), 'broad_type': "Roasted & Baked Dishes"},
    {'meal_name': "Beer-Braised Spiced Pork Shanks", 'category': "Warm Meal", 'best_seller': random.choice([True, False]), 'broad_type': "Soups & Stews"}, # Braised is close to stewing
    {'meal_name': "Classic French Coq Au Vin Rouge", 'category': "Stew", 'best_seller': random.choice([True, False]), 'broad_type': "Soups & Stews"},
    {'meal_name': "Chicken Fricassée with Shallots and Bacon", 'category': "Warm Meal", 'best_seller': random.choice([True, False]), 'broad_type': "Soups & Stews"}, # Creamy stew-like
    {'meal_name': "Creamy French Chicken Tarragon (Poulet à l'Estragon)", 'category': "Warm Meal", 'best_seller': random.choice([True, False]), 'broad_type': "Soups & Stews"}, # Creamy stew-like
    {'meal_name': "Clementine Roast Chicken with Fennel and Honey", 'category': "Roast", 'best_seller': random.choice([True, False]), 'broad_type': "Roasted & Baked Dishes"},
    {'meal_name': "French Chicken Marengo", 'category': "Warm Meal", 'best_seller': random.choice([True, False]), 'broad_type': "Soups & Stews"}, # Stew-like
    {'meal_name': "Sardine White Bean Cakes (Croquettes de Sardine)", 'category': "Seafood Special", 'best_seller': random.choice([True, False]), 'broad_type': "Specialty & Street Foods"}, # Cakes/fritters
    {'meal_name': "French Chicken And Mushroom Pie (Tourte)", 'category': "Savory Bake", 'best_seller': random.choice([True, False]), 'broad_type': "Roasted & Baked Dishes"},
    {'meal_name': "French Warm Goat Cheese Salad (Salade de Chèvre Chaud)", 'category': "Salad", 'best_seller': False, 'broad_type': "Salads & Light Meals"},
    {'meal_name': "French Antillean Cod Fritters (Accras de Morue)", 'category': "Seafood Special", 'best_seller': random.choice([True, False]), 'broad_type': "Specialty & Street Foods"}, # Fritters
    {'meal_name': "Tourtière (French Canadian Meat Pie)", 'category': "Savory Bake", 'best_seller': random.choice([True, False]), 'broad_type': "Roasted & Baked Dishes"},
    {'meal_name': "Caramelized Onion Tart (Tarte à l'Oignon Alsacienne)", 'category': "Savory Bake", 'best_seller': random.choice([True, False]), 'broad_type': "Roasted & Baked Dishes"},

    # Spanish Meals - Broad Type Categorization
    {'meal_name': "Vegetable Paella", 'category': "Rice Bowl", 'best_seller': False, 'broad_type': "Rice & Grain Bowls"},
    {'meal_name': "Gazpacho Andaluz", 'category': "Soup", 'best_seller': random.choice([True, False]), 'broad_type': "Soups & Stews"},
    {'meal_name': "Arroz con Pollo", 'category': "Rice Bowl", 'best_seller': False, 'broad_type': "Rice & Grain Bowls"},
    {'meal_name': "Tortilla Española (potato, egg, and onion omelet)", 'category': "Warm Meal", 'best_seller': random.choice([True, False]), 'broad_type': "Specialty & Street Foods"}, # Omelet/frittata style
    {'meal_name': "Albóndigas (meatballs in sauce)", 'category': "Warm Meal", 'best_seller': random.choice([True, False]), 'broad_type': "Specialty & Street Foods"}, # Meatballs are a distinct type
    {'meal_name': "Fabada (white bean stew with meats)", 'category': "Stew", 'best_seller': random.choice([True, False]), 'broad_type': "Soups & Stews"},
    {'meal_name': "Zarzuela (fish and shellfish stew)", 'category': "Seafood Special", 'best_seller': random.choice([True, False]), 'broad_type': "Soups & Stews"},
    {'meal_name': "Fideuá (vermicelli with shellfish)", 'category': "Seafood Special", 'best_seller': random.choice([True, False]), 'broad_type': "Noodles & Pasta"}, # Vermicelli is a type of noodle/pasta
    {'meal_name': "Cocido (a garbanzo dish with meats)", 'category': "Stew", 'best_seller': random.choice([True, False]), 'broad_type': "Soups & Stews"},
    {'meal_name': "Patatas aliñadás from Cadiz (potato salad)", 'category': "Salad", 'best_seller': random.choice([True, False]), 'broad_type': "Salads & Light Meals"},
    {'meal_name': "Pisto (fried vegetables)", 'category': "Vegetarian Delight", 'best_seller': random.choice([True, False]), 'broad_type': "Specialty & Street Foods"}, # Fried vegetables, can be a side or light meal
    {'meal_name': "Marmitako (tuna and potato stew)", 'category': "Stew", 'best_seller': random.choice([True, False]), 'broad_type': "Soups & Stews"},
    {'meal_name': "Revuelto de patatas (scrambled potatoes)", 'category': "Warm Meal", 'best_seller': random.choice([True, False]), 'broad_type': "Specialty & Street Foods"}, # Scrambled dishes
    {'meal_name': "Tortilla campera (vegetable and egg omelet)", 'category': "Warm Meal", 'best_seller': random.choice([True, False]), 'broad_type': "Specialty & Street Foods"}, # Omelet
    {'meal_name': "Ensaladilla Rusa (a rich potato salad)", 'category': "Salad", 'best_seller': random.choice([True, False]), 'broad_type': "Salads & Light Meals"},
    {'meal_name': "Authentic Spanish Cocido Stew Croquettes", 'category': "Warm Meal", 'best_seller': random.choice([True, False]), 'broad_type': "Specialty & Street Foods"}, # Croquettes are a type of fried/baked specialty
    {'meal_name': "Spanish Green Beans and Chicken", 'category': "Warm Meal", 'best_seller': random.choice([True, False]), 'broad_type': "Grilled & Pan-Seared"}, # Often pan-fried or sautéed
    {'meal_name': "Spanish Lentil Soup", 'category': "Soup", 'best_seller': random.choice([True, False]), 'broad_type': "Soups & Stews"},

    # Japanese Meals - Broad Type Categorization
    {'meal_name': "Pork Belly Ramen", 'category': "Soup", 'best_seller': random.choice([True, False]), 'broad_type': "Soups & Stews"},
    {'meal_name': "Miso Soup with Tofu", 'category': "Soup", 'best_seller': random.choice([True, False]), 'broad_type': "Soups & Stews"},
    {'meal_name': "Sushi Bowl (Chirashi-style)", 'category': "Rice Bowl", 'best_seller': random.choice([True, False]), 'broad_type': "Rice & Grain Bowls"},
    {'meal_name': "Sushi", 'category': "Seafood Special", 'best_seller': random.choice([True, False]), 'broad_type': "Specialty & Street Foods"}, # Unique preparation, often light meal
    {'meal_name': "Udon", 'category': "Pasta Dish", 'best_seller': random.choice([True, False]), 'broad_type': "Noodles & Pasta"},
    {'meal_name': "Tempura", 'category': "Fried Dish", 'best_seller': random.choice([True, False]), 'broad_type': "Specialty & Street Foods"}, # Fried specialty
    {'meal_name': "Yakitori", 'category': "Grilled Dish", 'best_seller': random.choice([True, False]), 'broad_type': "Grilled & Pan-Seared"},
    {'meal_name': "Sashimi", 'category': "Seafood Special", 'best_seller': random.choice([True, False]), 'broad_type': "Salads & Light Meals"}, # Raw fish, light meal
    {'meal_name': "Donburi", 'category': "Rice Bowl", 'best_seller': random.choice([True, False]), 'broad_type': "Rice & Grain Bowls"},
    {'meal_name': "Oden", 'category': "Stew", 'best_seller': random.choice([True, False]), 'broad_type': "Soups & Stews"},
    {'meal_name': "Tamagoyaki", 'category': "Warm Meal", 'best_seller': random.choice([True, False]), 'broad_type': "Specialty & Street Foods"}, # Omelet/egg dish
    {'meal_name': "Soba", 'category': "Pasta Dish", 'best_seller': random.choice([True, False]), 'broad_type': "Noodles & Pasta"},
    {'meal_name': "Tonkatsu", 'category': "Fried Dish", 'best_seller': random.choice([True, False]), 'broad_type': "Specialty & Street Foods"}, # Fried cutlet
    {'meal_name': "Sukiyaki", 'category': "Hot Pot", 'best_seller': random.choice([True, False]), 'broad_type': "Soups & Stews"}, # Hot pot is a form of stew/soup
    {'meal_name': "Okonomiyaki", 'category': "Warm Meal", 'best_seller': random.choice([True, False]), 'broad_type': "Specialty & Street Foods"}, # Savory pancake
    {'meal_name': "Nikujaga", 'category': "Stew", 'best_seller': random.choice([True, False]), 'broad_type': "Soups & Stews"},
    {'meal_name': "Curry Rice", 'category': "Rice Bowl", 'best_seller': random.choice([True, False]), 'broad_type': "Rice & Grain Bowls"},
    {'meal_name': "Unagi no Kabayaki", 'category': "Seafood Special", 'best_seller': random.choice([True, False]), 'broad_type': "Grilled & Pan-Seared"}, # Grilled eel
    {'meal_name': "Shabu Shabu Hot Pot", 'category': "Hot Pot", 'best_seller': random.choice([True, False]), 'broad_type': "Soups & Stews"},

    # Mexican Meals - Broad Type Categorization
    {'meal_name': "Sweet Potato and Black Bean Tacos", 'category': "Vegetarian Delight", 'best_seller': random.choice([True, False]), 'broad_type': "Specialty & Street Foods"}, # Tacos are street food
    {'meal_name': "Beef Burrito Bowl", 'category': "Rice Bowl", 'best_seller': random.choice([True, False]), 'broad_type': "Rice & Grain Bowls"},
    {'meal_name': "Chicken Fajitas Platter", 'category': "Warm Meal", 'best_seller': random.choice([True, False]), 'broad_type': "Grilled & Pan-Seared"}, # Grilled/Sautéed
    {'meal_name': "Salsa Chicken", 'category': "Warm Meal", 'best_seller': random.choice([True, False]), 'broad_type': "Grilled & Pan-Seared"}, # Can be pan-seared/baked
    {'meal_name': "Easy Chorizo Street Tacos", 'category': "Warm Meal", 'best_seller': random.choice([True, False]), 'broad_type': "Specialty & Street Foods"},
    {'meal_name': "Mexican Casserole", 'category': "Savory Bake", 'best_seller': random.choice([True, False]), 'broad_type': "Roasted & Baked Dishes"},
    {'meal_name': "Easy Spicy Mexican-American Chicken", 'category': "Warm Meal", 'best_seller': random.choice([True, False]), 'broad_type': "Grilled & Pan-Seared"}, # Often pan-seared or baked
    {'meal_name': "Suegra's Tomatillo Chicken", 'category': "Warm Meal", 'best_seller': random.choice([True, False]), 'broad_type': "Soups & Stews"}, # Cooked in sauce, stew-like
    {'meal_name': "Salsa Verde Pork", 'category': "Warm Meal", 'best_seller': random.choice([True, False]), 'broad_type': "Soups & Stews"}, # Cooked in sauce, stew-like
    {'meal_name': "Papas con Chorizo (Mexican Chorizo and Potatoes)", 'category': "Warm Meal", 'best_seller': random.choice([True, False]), 'broad_type': "Grilled & Pan-Seared"}, # Sautéed
    {'meal_name': "Flaming Slow Cooker Pork", 'category': "Warm Meal", 'best_seller': random.choice([True, False]), 'broad_type': "Soups & Stews"}, # Slow cooked often results in stew-like consistency
    {'meal_name': "Delia's Grilled Shrimp Sonora", 'category': "Grilled Dish", 'best_seller': random.choice([True, False]), 'broad_type': "Grilled & Pan-Seared"},
    {'meal_name': "Mexican Mostaccioli", 'category': "Pasta Dish", 'best_seller': random.choice([True, False]), 'broad_type': "Noodles & Pasta"},
    {'meal_name': "Taco-Seasoned Salmon", 'category': "Seafood Special", 'best_seller': random.choice([True, False]), 'broad_type': "Grilled & Pan-Seared"}, # Often grilled or pan-seared
    {'meal_name': "Quesadillas de Flor de Calabaza (Zucchini Blossom Quesadillas)", 'category': "Vegetarian Delight", 'best_seller': random.choice([True, False]), 'broad_type': "Specialty & Street Foods"}, # Quesadillas are specialty/street food

    # Thai Meals - Broad Type Categorization
    {'meal_name': "Thai Green Curry with Tofu", 'category': "Warm Meal", 'best_seller': random.choice([True, False]), 'broad_type': "Soups & Stews"}, # Curry is a type of stew
    {'meal_name': "Pad Thai Noodles", 'category': "Pasta Dish", 'best_seller': random.choice([True, False]), 'broad_type': "Noodles & Pasta"},
    {'meal_name': "Khao Soi (Thai Coconut Noodle Soup)", 'category': "Soup", 'best_seller': random.choice([True, False]), 'broad_type': "Soups & Stews"},
    {'meal_name': "Thai Larb Salad", 'category': "Salad", 'best_seller': random.choice([True, False]), 'broad_type': "Salads & Light Meals"},
    {'meal_name': "Thai Massaman Curry", 'category': "Warm Meal", 'best_seller': random.choice([True, False]), 'broad_type': "Soups & Stews"},
    {'meal_name': "Thai Fish Curry", 'category': "Warm Meal", 'best_seller': random.choice([True, False]), 'broad_type': "Soups & Stews"},
    {'meal_name': "Thai Noodle Salad with Peanut Sauce", 'category': "Salad", 'best_seller': random.choice([True, False]), 'broad_type': "Salads & Light Meals"},
    {'meal_name': "Pad See Ew", 'category': "Pasta Dish", 'best_seller': random.choice([True, False]), 'broad_type': "Noodles & Pasta"},
    {'meal_name': "Thai Red Curry", 'category': "Warm Meal", 'best_seller': random.choice([True, False]), 'broad_type': "Soups & Stews"},
    {'meal_name': "Tom Kha Gai (Thai Coconut Chicken Soup)", 'category': "Soup", 'best_seller': random.choice([True, False]), 'broad_type': "Soups & Stews"},
    {'meal_name': "Thai Basil Chicken", 'category': "Warm Meal", 'best_seller': random.choice([True, False]), 'broad_type': "Grilled & Pan-Seared"}, # Stir-fried
    {'meal_name': "Thai Eggplant Stir-Fry", 'category': "Vegetarian Delight", 'best_seller': random.choice([True, False]), 'broad_type': "Grilled & Pan-Seared"}, # Stir-fried
    {'meal_name': "Thai Pineapple Fried Rice", 'category': "Rice Bowl", 'best_seller': random.choice([True, False]), 'broad_type': "Rice & Grain Bowls"},
    {'meal_name': "Thai Grilled Eggplant Salad", 'category': "Salad", 'best_seller': random.choice([True, False]), 'broad_type': "Salads & Light Meals"},
    {'meal_name': "Thai Coconut Chicken Salad", 'category': "Salad", 'best_seller': random.choice([True, False]), 'broad_type': "Salads & Light Meals"},
    {'meal_name': "Thai Chicken Satay with Peanut Dipping Sauce", 'category': "Grilled Dish", 'best_seller': random.choice([True, False]), 'broad_type': "Grilled & Pan-Seared"},
    {'meal_name': "Thai Baked Chicken and Rice", 'category': "Savory Bake", 'best_seller': random.choice([True, False]), 'broad_type': "Roasted & Baked Dishes"},
    {'meal_name': "Thai Turkey Burgers", 'category': "Grilled Dish", 'best_seller': random.choice([True, False]), 'broad_type': "Specialty & Street Foods"}, # Burgers
    {'meal_name': "Thai Curry Meatballs", 'category': "Warm Meal", 'best_seller': random.choice([True, False]), 'broad_type': "Specialty & Street Foods"}, # Meatballs
    {'meal_name': "Thai Burritos with Peanut Sauce", 'category': "Warm Meal", 'best_seller': random.choice([True, False]), 'broad_type': "Sandwiches & Wraps"}, # Burritos are wraps

    # Vietnamese Meals - Broad Type Categorization
    {'meal_name': "Phở (Beef Noodle Soup)", 'category': "Soup", 'best_seller': random.choice([True, False]), 'broad_type': "Soups & Stews"},
    {'meal_name': "Bánh Mì (Vietnamese Sandwich)", 'category': "Sandwich", 'best_seller': random.choice([True, False]), 'broad_type': "Sandwiches & Wraps"},
    {'meal_name': "Cơm Tấm (Broken Rice)", 'category': "Rice Bowl", 'best_seller': random.choice([True, False]), 'broad_type': "Rice & Grain Bowls"},
    {'meal_name': "Bún Bò Huế (Hue Style Beef Noodle Soup)", 'category': "Soup", 'best_seller': random.choice([True, False]), 'broad_type': "Soups & Stews"},
    {'meal_name': "Gỏi cuốn (Fresh Spring Rolls)", 'category': "Appetizer/Light Meal", 'best_seller': random.choice([True, False]), 'broad_type': "Salads & Light Meals"}, # Cold rolls, light meal
    {'meal_name': "Canh (Vietnamese Soups)", 'category': "Soup", 'best_seller': random.choice([True, False]), 'broad_type': "Soups & Stews"},
    {'meal_name': "Bánh cuốn (Steamed Rice Rolls)", 'category': "Warm Meal", 'best_seller': random.choice([True, False]), 'broad_type': "Specialty & Street Foods"}, # Steamed rolls
    {'meal_name': "Cháo (Rice Porridge)", 'category': "Soup", 'best_seller': random.choice([True, False]), 'broad_type': "Soups & Stews"},
    {'meal_name': "Cha Ca Ha Noi (Hanoi Grilled Fish)", 'category': "Grilled Dish", 'best_seller': random.choice([True, False]), 'broad_type': "Grilled & Pan-Seared"},
    {'meal_name': "Cá Kho Tộ (Caramelized Fish in Clay Pot)", 'category': "Warm Meal", 'best_seller': random.choice([True, False]), 'broad_type': "Soups & Stews"}, # Pot cooked, stew-like
    {'meal_name': "Bánh xèo (Crispy Pancakes)", 'category': "Warm Meal", 'best_seller': random.choice([True, False]), 'broad_type': "Specialty & Street Foods"}, # Pancakes
    {'meal_name': "Bun bo nam bo (Beef Noodle Salad)", 'category': "Salad", 'best_seller': random.choice([True, False]), 'broad_type': "Salads & Light Meals"},
    {'meal_name': "Bo luc lac (Shaking Beef)", 'category': "Warm Meal", 'best_seller': random.choice([True, False]), 'broad_type': "Grilled & Pan-Seared"}, # Shaking beef is quick seared
    {'meal_name': "Banh goi (Fried Pastry)", 'category': "Warm Meal", 'best_seller': random.choice([True, False]), 'broad_type': "Specialty & Street Foods"}, # Fried pastry

    # Indonesian Meals - Broad Type Categorization
    {'meal_name': "Nasi goreng (Fried Rice)", 'category': "Rice Bowl", 'best_seller': random.choice([True, False]), 'broad_type': "Rice & Grain Bowls"},
    {'meal_name': "Mie goreng (Fried Noodles)", 'category': "Pasta Dish", 'best_seller': random.choice([True, False]), 'broad_type': "Noodles & Pasta"},
    {'meal_name': "Sate (Grilled Skewers)", 'category': "Grilled Dish", 'best_seller': random.choice([True, False]), 'broad_type': "Grilled & Pan-Seared"},
    {'meal_name': "Rendang (Beef Curry)", 'category': "Warm Meal", 'best_seller': random.choice([True, False]), 'broad_type': "Soups & Stews"}, # Curry is a type of stew
    {'meal_name': "Rawon (Beef Soup)", 'category': "Soup", 'best_seller': random.choice([True, False]), 'broad_type': "Soups & Stews"},
    {'meal_name': "Soto (Soup)", 'category': "Soup", 'best_seller': random.choice([True, False]), 'broad_type': "Soups & Stews"},
    {'meal_name': "Perkedel (Potato Patties)", 'category': "Side Dish/Light Meal", 'best_seller': random.choice([True, False]), 'broad_type': "Specialty & Street Foods"}, # Patties/Fritters
    {'meal_name': "Bebek goreng (Fried Duck)", 'category': "Fried Dish", 'best_seller': random.choice([True, False]), 'broad_type': "Grilled & Pan-Seared"}, # Fried is a form of pan-searing
    {'meal_name': "Kare (Curry)", 'category': "Warm Meal", 'best_seller': random.choice([True, False]), 'broad_type': "Soups & Stews"},
    {'meal_name': "Ayam bakar Taliwang (Grilled Chicken)", 'category': "Grilled Dish", 'best_seller': random.choice([True, False]), 'broad_type': "Grilled & Pan-Seared"},
    {'meal_name': "Bakso (Meatball Soup)", 'category': "Soup", 'best_seller': random.choice([True, False]), 'broad_type': "Soups & Stews"},
    {'meal_name': "Gado-gado (Vegetable Salad with Peanut Sauce)", 'category': "Salad", 'best_seller': random.choice([True, False]), 'broad_type': "Salads & Light Meals"},
    {'meal_name': "Batagor (Fried Tofu with Meatball)", 'category': "Fried Dish", 'best_seller': random.choice([True, False]), 'broad_type': "Specialty & Street Foods"}, # Fried specialty
    {'meal_name': "Babi guling (Roasted Suckling Pig)", 'category': "Roast", 'best_seller': random.choice([True, False]), 'broad_type': "Roasted & Baked Dishes"},
    {'meal_name': "Pepes (Herbal Packet)", 'category': "Steamed Dish", 'best_seller': random.choice([True, False]), 'broad_type': "Specialty & Street Foods"}, # Steamed specialty

    # Filipino Meals - Broad Type Categorization
    {'meal_name': "Adobo (Pork or Chicken Stewed in Soy Sauce and Vinegar)", 'category': "Stew", 'best_seller': random.choice([True, False]), 'broad_type': "Soups & Stews"},
    {'meal_name': "Afritada (Chicken or Pork Stewed in Tomato Sauce)", 'category': "Stew", 'best_seller': random.choice([True, False]), 'broad_type': "Soups & Stews"},
    {'meal_name': "Barbecue (Inihaw, Inasal, Satti) (Grilled Meat Skewers)", 'category': "Grilled Dish", 'best_seller': random.choice([True, False]), 'broad_type': "Grilled & Pan-Seared"},
    {'meal_name': "Bopis (Spicy Pork Lungs and Heart)", 'category': "Warm Meal", 'best_seller': random.choice([True, False]), 'broad_type': "Specialty & Street Foods"}, # Unique organ meat dish
    {'meal_name': "Camaron rebosado (Deep Fried Battered Shrimps)", 'category': "Fried Dish", 'best_seller': random.choice([True, False]), 'broad_type': "Specialty & Street Foods"}, # Fried specialty
    {'meal_name': "Chicken pastel (Chicken Stew in Cream Sauce)", 'category': "Stew", 'best_seller': random.choice([True, False]), 'broad_type': "Soups & Stews"},
    {'meal_name': "Crispy pata (Deep Fried Pork Leg)", 'category': "Fried Dish", 'best_seller': random.choice([True, False]), 'broad_type': "Roasted & Baked Dishes"}, # Deep fried then roasted for crisp
    {'meal_name': "Crispy tadyang ng baka (Crispy Beef Ribs)", 'category': "Fried Dish", 'best_seller': random.choice([True, False]), 'broad_type': "Specialty & Street Foods"}, # Fried specialty
    {'meal_name': "Curacha (Boiled or Steamed Sea Crab)", 'category': "Seafood Special", 'best_seller': random.choice([True, False]), 'broad_type': "Grilled & Pan-Seared"}, # Steamed or boiled, but often served as a main dish with other preparations
    {'meal_name': "Daing (Fried Dried Fish)", 'category': "Seafood Special", 'best_seller': random.choice([True, False]), 'broad_type': "Grilled & Pan-Seared"}, # Fried
    {'meal_name': "Embutido (Meatloaf)", 'category': "Warm Meal", 'best_seller': random.choice([True, False]), 'broad_type': "Roasted & Baked Dishes"}, # Meatloaf is baked
    {'meal_name': "Escabeche (Sweet and Sour Fish)", 'category': "Seafood Special", 'best_seller': random.choice([True, False]), 'broad_type': "Grilled & Pan-Seared"}, # Fish is fried then sauced
    {'meal_name': "Giniling (Picadillo) (Ground Pork or Beef)", 'category': "Warm Meal", 'best_seller': random.choice([True, False]), 'broad_type': "Specialty & Street Foods"}, # Ground meat dish
    {'meal_name': "Halabos na hipon (Steamed Shrimps)", 'category': "Seafood Special", 'best_seller': random.choice([True, False]), 'broad_type': "Salads & Light Meals"}, # Steamed, often light
    {'meal_name': "Hamonado (Sweet Glazed Pork)", 'category': "Warm Meal", 'best_seller': random.choice([True, False]), 'broad_type': "Roasted & Baked Dishes"}, # Often roasted
    {'meal_name': "Humba (Sweet Pork Stew)", 'category': "Stew", 'best_seller': random.choice([True, False]), 'broad_type': "Soups & Stews"},
    {'meal_name': "Inasal na manok (Grilled Chicken)", 'category': "Grilled Dish", 'best_seller': random.choice([True, False]), 'broad_type': "Grilled & Pan-Seared"},
    {'meal_name': "Inihaw na liempo (Grilled Pork Belly)", 'category': "Grilled Dish", 'best_seller': random.choice([True, False]), 'broad_type': "Grilled & Pan-Seared"},
    {'meal_name': "Inun-unan (Fish Stewed in Vinegar)", 'category': "Stew", 'best_seller': random.choice([True, False]), 'broad_type': "Soups & Stews"},
    {'meal_name': "Kadyos-Baboy-Langka (Pigeon Peas, Pork, and Jackfruit Stew)", 'category': "Stew", 'best_seller': random.choice([True, False]), 'broad_type': "Soups & Stews"},
    {'meal_name': "Kadyos Manok Ubad (Pigeon Peas, Chicken, and Banana Stalk Stew)", 'category': "Stew", 'best_seller': random.choice([True, False]), 'broad_type': "Soups & Stews"},
    {'meal_name': "Kaldereta (Meat Stew in Tomato Sauce)", 'category': "Stew", 'best_seller': random.choice([True, False]), 'broad_type': "Soups & Stews"},
    {'meal_name': "Kinunot (Shredded Stingray or Shark in Coconut Milk)", 'category': "Seafood Special", 'best_seller': random.choice([True, False]), 'broad_type': "Soups & Stews"}, # Stew-like
    {'meal_name': "Bicol Express (Pork Cooked in Coconut Milk and Chili)", 'category': "Warm Meal", 'best_seller': random.choice([True, False]), 'broad_type': "Soups & Stews"}, # Stew-like
    {'meal_name': "Filipino Spaghetti (Sweet and Meaty Spaghetti)", 'category': "Pasta Dish", 'best_seller': random.choice([True, False]), 'broad_type': "Noodles & Pasta"},
    {'meal_name': "Pork Menudo (Pork Stew with Tomatoes and Potatoes)", 'category': "Stew", 'best_seller': random.choice([True, False]), 'broad_type': "Soups & Stews"},
    {'meal_name': "Chicken Tinola (Chicken Soup with Ginger and Papaya)", 'category': "Soup", 'best_seller': random.choice([True, False]), 'broad_type': "Soups & Stews"},
    {'meal_name': "Arroz Caldo (Chicken Rice Porridge)", 'category': "Soup", 'best_seller': random.choice([True, False]), 'broad_type': "Soups & Stews"},
    {'meal_name': "Pinakbet (Vegetable Stew with Shrimp Paste)", 'category': "Vegetarian Delight", 'best_seller': random.choice([True, False]), 'broad_type': "Soups & Stews"}, # Stew
    {'meal_name': "Kare-Kare (Stew with Peanut Sauce)", 'category': "Stew", 'best_seller': random.choice([True, False]), 'broad_type': "Soups & Stews"},
    {'meal_name': "Lumpia (Spring Rolls)", 'category': "Appetizer/Light Meal", 'best_seller': random.choice([True, False]), 'broad_type': "Specialty & Street Foods"}, # Spring rolls
    {'meal_name': "Filipino Chicken Curry", 'category': "Warm Meal", 'best_seller': random.choice([True, False]), 'broad_type': "Soups & Stews"}, # Curry
    {'meal_name': "Sinigang na Hipon (Sour Shrimp Soup)", 'category': "Soup", 'best_seller': random.choice([True, False]), 'broad_type': "Soups & Stews"},
    {'meal_name': "Beef Caldereta (Beef Stew in Tomato Sauce)", 'category': "Stew", 'best_seller': random.choice([True, False]), 'broad_type': "Soups & Stews"},
    {'meal_name': "Bistek Tagalog (Beef Braised in Soy Sauce and Citrus)", 'category': "Warm Meal", 'best_seller': random.choice([True, False]), 'broad_type': "Grilled & Pan-Seared"}, # Often pan-seared or braised
    {'meal_name': "Adobong Pusit (Squid Adobo)", 'category': "Seafood Special", 'best_seller': random.choice([True, False]), 'broad_type': "Soups & Stews"}, # Stewed
    {'meal_name': "Tortang Talong (Eggplant Omelette)", 'category': "Vegetarian Delight", 'best_seller': random.choice([True, False]), 'broad_type': "Specialty & Street Foods"}, # Omelet
    {'meal_name': "Lechon (Roasted Pig)", 'category': "Roast", 'best_seller': random.choice([True, False]), 'broad_type': "Roasted & Baked Dishes"}
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

# Initialize session state for language if not already set
if 'language' not in st.session_state:
    st.session_state.language = "en" # Default language is English

# Callback function for the toggle
def toggle_language():
    if st.session_state.language_toggle: # If toggle is True (checked)
        st.session_state.language = "es"
    else: # If toggle is False (unchecked)
        st.session_state.language = "en"
    st.experimental_rerun() # Rerun the app to apply language changes

# Get the current text content based on selected language
current_text = TEXT_CONTENT[st.session_state.language]


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
