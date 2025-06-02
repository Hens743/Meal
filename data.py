import streamlit as st
import pandas as pd
import random

# Meal list (remains the same - data content, not UI text)
meal_list = [
    # Chilean Meals - Broad Type Categorization
    {'meal_name': "Pastel de Choclo Bake", 'category': "Savory Bake", 'favorite': random.choice([True, False]), 'broad_type': "Roasted & Baked Dishes", 'image_url': "https://placehold.co/300x200/FFD700/000000?text=Pastel+de+Choclo+Bake"},
    {'meal_name': "Empanadas Pino (Beef)", 'category': "Savory Bake", 'favorite': random.choice([True, False]), 'broad_type': "Specialty & Street Foods", 'image_url': "https://placehold.co/300x200/FFD700/000000?text=Empanadas+Pino"},
    {'meal_name': "Hearty Cazuela Chilena", 'category': "Stew", 'favorite': random.choice([True, False]), 'broad_type': "Soups & Stews", 'image_url': "https://placehold.co/300x200/FFD700/000000?text=Cazuela+Chilena"},
    {'meal_name': "Humitas Corn Parcels", 'category': "Warm Meal", 'favorite': random.choice([True, False]), 'broad_type': "Rice & Grain Bowls", 'image_url': "https://placehold.co/300x200/FFD700/000000?text=Humitas+Corn+Parcels"},
    {'meal_name': "Porotos Granados Stew", 'category': "Stew", 'favorite': random.choice([True, False]), 'broad_type': "Soups & Stews", 'image_url': "https://placehold.co/300x200/FFD700/000000?text=Porotos+Granados+Stew"},
    {'meal_name': "Congrio Frito (Fried Conger Eel)", 'category': "Seafood Special", 'favorite': random.choice([True, False]), 'broad_type': "Grilled & Pan-Seared", 'image_url': "https://placehold.co/300x200/FFD700/000000?text=Congrio+Frito"},
    {'meal_name': "Machas a la Parmesana", 'category': "Seafood Special", 'favorite': random.choice([True, False]), 'broad_type': "Specialty & Street Foods", 'image_url': "https://placehold.co/300x200/FFD700/000000?text=Machas+a+la+Parmesana"},
    {'meal_name': "Charquican Beef Stew", 'category': "Stew", 'favorite': random.choice([True, False]), 'broad_type': "Soups & Stews", 'image_url': "https://placehold.co/300x200/FFD700/000000?text=Charquican+Beef+Stew"},
    {'meal_name': "Pebre Chicken Bowl", 'category': "Rice Bowl", 'favorite': random.choice([True, False]), 'broad_type': "Rice & Grain Bowls", 'image_url': "https://placehold.co/300x200/FFD700/000000?text=Pebre+Chicken+Bowl"},
    {'meal_name': "Curanto Inspired Seafood Pot", 'category': "Seafood Special", 'favorite': random.choice([True, False]), 'broad_type': "Soups & Stews", 'image_url': "https://placehold.co/300x200/FFD700/000000?text=Curanto+Seafood+Pot"},
    {'meal_name': "Sopaipillas Pasadas (savory version context)", 'category': "Warm Meal", 'favorite': random.choice([True, False]), 'broad_type': "Specialty & Street Foods", 'image_url': "https://placehold.co/300x200/FFD700/000000?text=Sopaipillas+Pasadas"},
    {'meal_name': "Valdiviano Soup", 'category': "Soup", 'favorite': random.choice([True, False]), 'broad_type': "Soups & Stews", 'image_url': "https://placehold.co/300x200/FFD700/000000?text=Valdiviano+Soup"},
    {'meal_name': "Costillar de Chancho Ahumado", 'category': "Roast", 'favorite': random.choice([True, False]), 'broad_type': "Roasted & Baked Dishes", 'image_url': "https://placehold.co/300x200/FFD700/000000?text=Costillar+de+Chancho"},
    {'meal_name': "Pastel de Jaiba (Crab Pie)", 'category': "Savory Bake", 'favorite': random.choice([True, False]), 'broad_type': "Roasted & Baked Dishes", 'image_url': "https://placehold.co/300x200/FFD700/000000?text=Pastel+de+Jaiba"},

    # Peruvian Meals - Broad Type Categorization
    {'meal_name': "Lomo Saltado Style Beef", 'category': "Warm Meal", 'favorite': random.choice([True, False]), 'broad_type': "Grilled & Pan-Seared", 'image_url': "https://placehold.co/300x200/87CEEB/000000?text=Lomo+Saltado"},
    {'meal_name': "Ceviche Clasico", 'category': "Seafood Special", 'favorite': random.choice([True, False]), 'broad_type': "Salads & Light Meals", 'image_url': "https://placehold.co/300x200/87CEEB/000000?text=Ceviche+Clasico"},

    # French Meals - Broad Type Categorization
    {'meal_name': "Classic French Onion Soup", 'category': "Soup", 'favorite': random.choice([True, False]), 'broad_type': "Soups & Stews", 'image_url': "https://placehold.co/300x200/ADD8E6/000000?text=French+Onion+Soup"},
    {'meal_name': "Quiche Lorraine", 'category': "Savory Bake", 'favorite': random.choice([True, False]), 'broad_type': "Roasted & Baked Dishes", 'image_url': "https://placehold.co/300x200/ADD8E6/000000?text=Quiche+Lorraine"},
    {'meal_name': "Ratatouille", 'category': "Vegetarian Delight", 'favorite': False, 'broad_type': "Roasted & Baked Dishes", 'image_url': "https://placehold.co/300x200/ADD8E6/000000?text=Ratatouille"},
    {'meal_name': "Mushroom Bourguignon", 'category': "Vegetarian Delight", 'favorite': random.choice([True, False]), 'broad_type': "Soups & Stews", 'image_url': "https://placehold.co/300x200/ADD8E6/000000?text=Mushroom+Bourguignon"},
    {'meal_name': "Steak au Poivre with Red Wine Pan Sauce", 'category': "Warm Meal", 'favorite': random.choice([True, False]), 'broad_type': "Grilled & Pan-Seared", 'image_url': "https://placehold.co/300x200/ADD8E6/000000?text=Steak+au+Poivre"},
    {'meal_name': "Duck à l'Orange", 'category': "Roast", 'favorite': random.choice([True, False]), 'broad_type': "Roasted & Baked Dishes", 'image_url': "https://placehold.co/300x200/ADD8E6/000000?text=Duck+a+l+Orange"},
    {'meal_name': "Julia Child's Favorite Roast Chicken", 'category': "Roast", 'favorite': random.choice([True, False]), 'broad_type': "Roasted & Baked Dishes", 'image_url': "https://placehold.co/300x200/ADD8E6/000000?text=Roast+Chicken"},
    {'meal_name': "Lyon-Style Chicken with Vinegar Sauce", 'category': "Warm Meal", 'favorite': random.choice([True, False]), 'broad_type': "Grilled & Pan-Seared", 'image_url': "https://placehold.co/300x200/ADD8E6/000000?text=Lyon-Style+Chicken"},
    {'meal_name': "Crispy Monkfish with Capers", 'category': "Seafood Special", 'favorite': random.choice([True, False]), 'broad_type': "Grilled & Pan-Seared", 'image_url': "https://placehold.co/300x200/ADD8E6/000000?text=Crispy+Monkfish"},
    {'meal_name': "Beef Stew in Red Wine Sauce (Boeuf Bourguignon)", 'category': "Stew", 'favorite': random.choice([True, False]), 'broad_type': "Soups & Stews", 'image_url': "https://placehold.co/300x200/ADD8E6/000000?text=Boeuf+Bourguignon"},
    {'meal_name': "Chicken Legs Coq au Vin", 'category': "Stew", 'favorite': random.choice([True, False]), 'broad_type': "Soups & Stews", 'image_url': "https://placehold.co/300x200/ADD8E6/000000?text=Coq+au+Vin"},
    {'meal_name': "Stuffed Pork Tenderloins with Bacon and Apple-Riesling Sauce", 'category': "Roast", 'favorite': random.choice([True, False]), 'broad_type': "Roasted & Baked Dishes", 'image_url': "https://placehold.co/300x200/ADD8E6/000000?text=Stuffed+Pork"},
    {'meal_name': "French Egg Salad", 'category': "Salad", 'favorite': random.choice([True, False]), 'broad_type': "Salads & Light Meals", 'image_url': "https://placehold.co/300x200/ADD8E6/000000?text=French+Egg+Salad"},
    {'meal_name': "Chicken Cordon Bleu", 'category': "Warm Meal", 'favorite': random.choice([True, False]), 'broad_type': "Specialty & Street Foods", 'image_url': "https://placehold.co/300x200/ADD8E6/000000?text=Chicken+Cordon+Bleu"},
    {'meal_name': "Lyonnaise Potatoes (Pommes de terre à la Lyonnaise)", 'category': "Side Dish", 'favorite': random.choice([True, False]), 'broad_type': "Roasted & Baked Dishes", 'image_url': "https://placehold.co/300x200/ADD8E6/000000?text=Lyonnaise+Potatoes"},
    {'meal_name': "Lamb Navarin (Navarin d'agneau)", 'category': "Stew", 'favorite': random.choice([True, False]), 'broad_type': "Soups & Stews", 'image_url': "https://placehold.co/300x200/ADD8E6/000000?text=Lamb+Navarin"},
    {'meal_name': "French-Style Potato and Green Bean Salad", 'category': "Salad", 'favorite': random.choice([True, False]), 'broad_type': "Salads & Light Meals", 'image_url': "https://placehold.co/300x200/ADD8E6/000000?text=Potato+Green+Bean+Salad"},
    {'meal_name': "White Asparagus à la Grenobloise", 'category': "Vegetarian Delight", 'favorite': random.choice([True, False]), 'broad_type': "Salads & Light Meals", 'image_url': "https://placehold.co/300x200/ADD8E6/000000?text=White+Asparagus"},
    {'meal_name': "French Beef Daube (Traditional Provençal Stew)", 'category': "Stew", 'favorite': random.choice([True, False]), 'broad_type': "Soups & Stews", 'image_url': "https://placehold.co/300x200/ADD8E6/000000?text=French+Beef+Daube"},
    {'meal_name': "Braised Pork Loin with Prunes (Porc aux pruneaux)", 'category': "Roast", 'favorite': random.choice([True, False]), 'broad_type': "Roasted & Baked Dishes", 'image_url': "https://placehold.co/300x200/ADD8E6/000000?text=Braised+Pork+Loin"},
    {'meal_name': "Beer-Braised Spiced Pork Shanks", 'category': "Warm Meal", 'favorite': random.choice([True, False]), 'broad_type': "Soups & Stews", 'image_url': "https://placehold.co/300x200/ADD8E6/000000?text=Beer-Braised+Pork"},
    {'meal_name': "Classic French Coq Au Vin Rouge", 'category': "Stew", 'favorite': random.choice([True, False]), 'broad_type': "Soups & Stews", 'image_url': "https://placehold.co/300x200/ADD8E6/000000?text=Coq+Au+Vin+Rouge"},
    {'meal_name': "Chicken Fricassée with Shallots and Bacon", 'category': "Warm Meal", 'favorite': random.choice([True, False]), 'broad_type': "Soups & Stews", 'image_url': "https://placehold.co/300x200/ADD8E6/000000?text=Chicken+Fricassee"},
    {'meal_name': "Creamy French Chicken Tarragon (Poulet à l'Estragon)", 'category': "Warm Meal", 'favorite': random.choice([True, False]), 'broad_type': "Soups & Stews", 'image_url': "https://placehold.co/300x200/ADD8E6/000000?text=Chicken+Tarragon"},
    {'meal_name': "Clementine Roast Chicken with Fennel and Honey", 'category': "Roast", 'favorite': random.choice([True, False]), 'broad_type': "Roasted & Baked Dishes", 'image_url': "https://placehold.co/300x200/ADD8E6/000000?text=Clementine+Roast+Chicken"},
    {'meal_name': "French Chicken Marengo", 'category': "Warm Meal", 'favorite': random.choice([True, False]), 'broad_type': "Soups & Stews", 'image_url': "https://placehold.co/300x200/ADD8E6/000000?text=Chicken+Marengo"},
    {'meal_name': "Sardine White Bean Cakes (Croquettes de Sardine)", 'category': "Seafood Special", 'favorite': random.choice([True, False]), 'broad_type': "Specialty & Street Foods", 'image_url': "https://placehold.co/300x200/ADD8E6/000000?text=Sardine+Cakes"},
    {'meal_name': "French Chicken And Mushroom Pie (Tourte)", 'category': "Savory Bake", 'favorite': random.choice([True, False]), 'broad_type': "Roasted & Baked Dishes", 'image_url': "https://placehold.co/300x200/ADD8E6/000000?text=Chicken+Mushroom+Pie"},
    {'meal_name': "French Warm Goat Cheese Salad (Salade de Chèvre Chaud)", 'category': "Salad", 'favorite': False, 'broad_type': "Salads & Light Meals", 'image_url': "https://placehold.co/300x200/ADD8E6/000000?text=Goat+Cheese+Salad"},
    {'meal_name': "French Antillean Cod Fritters (Accras de Morue)", 'category': "Seafood Special", 'favorite': random.choice([True, False]), 'broad_type': "Specialty & Street Foods", 'image_url': "https://placehold.co/300x200/ADD8E6/000000?text=Cod+Fritters"},
    {'meal_name': "Tourtière (French Canadian Meat Pie)", 'category': "Savory Bake", 'favorite': random.choice([True, False]), 'broad_type': "Roasted & Baked Dishes", 'image_url': "https://placehold.co/300x200/ADD8E6/000000?text=Tourtiere"},
    {'meal_name': "Caramelized Onion Tart (Tarte à l'Oignon Alsacienne)", 'category': "Savory Bake", 'favorite': random.choice([True, False]), 'broad_type': "Roasted & Baked Dishes", 'image_url': "https://placehold.co/300x200/ADD8E6/000000?text=Caramelized+Onion+Tart"},

    # Spanish Meals - Broad Type Categorization
    {'meal_name': "Vegetable Paella", 'category': "Rice Bowl", 'favorite': False, 'broad_type': "Rice & Grain Bowls", 'image_url': "https://placehold.co/300x200/FFC0CB/000000?text=Vegetable+Paella"},
    {'meal_name': "Gazpacho Andaluz", 'category': "Soup", 'favorite': random.choice([True, False]), 'broad_type': "Soups & Stews", 'image_url': "https://placehold.co/300x200/FFC0CB/000000?text=Gazpacho+Andaluz"},
    {'meal_name': "Arroz con Pollo", 'category': "Rice Bowl", 'favorite': False, 'broad_type': "Rice & Grain Bowls", 'image_url': "https://placehold.co/300x200/FFC0CB/000000?text=Arroz+con+Pollo"},
    {'meal_name': "Tortilla Española (potato, egg, and onion omelet)", 'category': "Warm Meal", 'favorite': random.choice([True, False]), 'broad_type': "Specialty & Street Foods", 'image_url': "https://placehold.co/300x200/FFC0CB/000000?text=Tortilla+Espanola"},
    {'meal_name': "Albóndigas (meatballs in sauce)", 'category': "Warm Meal", 'favorite': random.choice([True, False]), 'broad_type': "Specialty & Street Foods", 'image_url': "https://placehold.co/300x200/FFC0CB/000000?text=Albondigas"},
    {'meal_name': "Fabada (white bean stew with meats)", 'category': "Stew", 'favorite': random.choice([True, False]), 'broad_type': "Soups & Stews", 'image_url': "https://placehold.co/300x200/FFC0CB/000000?text=Fabada"},
    {'meal_name': "Zarzuela (fish and shellfish stew)", 'category': "Seafood Special", 'favorite': random.choice([True, False]), 'broad_type': "Soups & Stews", 'image_url': "https://placehold.co/300x200/FFC0CB/000000?text=Zarzuela"},
    {'meal_name': "Fideuá (vermicelli with shellfish)", 'category': "Seafood Special", 'favorite': random.choice([True, False]), 'broad_type': "Noodles & Pasta", 'image_url': "https://placehold.co/300x200/FFC0CB/000000?text=Fideua"},
    {'meal_name': "Cocido (a garbanzo dish with meats)", 'category': "Stew", 'favorite': random.choice([True, False]), 'broad_type': "Soups & Stews", 'image_url': "https://placehold.co/300x200/FFC0CB/000000?text=Cocido"},
    {'meal_name': "Patatas aliñadás from Cadiz (potato salad)", 'category': "Salad", 'favorite': random.choice([True, False]), 'broad_type': "Salads & Light Meals", 'image_url': "https://placehold.co/300x200/FFC0CB/000000?text=Patatas+alinadas"},
    {'meal_name': "Pisto (fried vegetables)", 'category': "Vegetarian Delight", 'favorite': random.choice([True, False]), 'broad_type': "Specialty & Street Foods", 'image_url': "https://placehold.co/300x200/FFC0CB/000000?text=Pisto"},
    {'meal_name': "Marmitako (tuna and potato stew)", 'category': "Stew", 'favorite': random.choice([True, False]), 'broad_type': "Soups & Stews", 'image_url': "https://placehold.co/300x200/FFC0CB/000000?text=Marmitako"},
    {'meal_name': "Revuelto de patatas (scrambled potatoes)", 'category': "Warm Meal", 'favorite': random.choice([True, False]), 'broad_type': "Specialty & Street Foods", 'image_url': "https://placehold.co/300x200/FFC0CB/000000?text=Revuelto+de+patatas"},
    {'meal_name': "Tortilla campera (vegetable and egg omelet)", 'category': "Warm Meal", 'favorite': random.choice([True, False]), 'broad_type': "Specialty & Street Foods", 'image_url': "https://placehold.co/300x200/FFC0CB/000000?text=Tortilla+campera"},
    {'meal_name': "Ensaladilla Rusa (a rich potato salad)", 'category': "Salad", 'favorite': random.choice([True, False]), 'broad_type': "Salads & Light Meals", 'image_url': "https://placehold.co/300x200/FFC0CB/000000?text=Ensaladilla+Rusa"},
    {'meal_name': "Authentic Spanish Cocido Stew Croquettes", 'category': "Warm Meal", 'favorite': random.choice([True, False]), 'broad_type': "Specialty & Street Foods", 'image_url': "https://placehold.co/300x200/FFC0CB/000000?text=Cocido+Croquettes"},
    {'meal_name': "Spanish Green Beans and Chicken", 'category': "Warm Meal", 'favorite': random.choice([True, False]), 'broad_type': "Grilled & Pan-Seared", 'image_url': "https://placehold.co/300x200/FFC0CB/000000?text=Spanish+Green+Beans"},
    {'meal_name': "Spanish Lentil Soup", 'category': "Soup", 'favorite': random.choice([True, False]), 'broad_type': "Soups & Stews", 'image_url': "https://placehold.co/300x200/FFC0CB/000000?text=Spanish+Lentil+Soup"},

    # Japanese Meals - Broad Type Categorization
    {'meal_name': "Pork Belly Ramen", 'category': "Soup", 'favorite': random.choice([True, False]), 'broad_type': "Soups & Stews", 'image_url': "https://placehold.co/300x200/90EE90/000000?text=Pork+Belly+Ramen"},
    {'meal_name': "Miso Soup with Tofu", 'category': "Soup", 'favorite': random.choice([True, False]), 'broad_type': "Soups & Stews", 'image_url': "https://placehold.co/300x200/90EE90/000000?text=Miso+Soup+with+Tofu"},
    {'meal_name': "Sushi Bowl (Chirashi-style)", 'category': "Rice Bowl", 'favorite': random.choice([True, False]), 'broad_type': "Rice & Grain Bowls", 'image_url': "https://placehold.co/300x200/90EE90/000000?text=Sushi+Bowl"},
    {'meal_name': "Sushi", 'category': "Seafood Special", 'favorite': random.choice([True, False]), 'broad_type': "Specialty & Street Foods", 'image_url': "https://placehold.co/300x200/90EE90/000000?text=Sushi"},
    {'meal_name': "Udon", 'category': "Pasta Dish", 'favorite': random.choice([True, False]), 'broad_type': "Noodles & Pasta", 'image_url': "https://placehold.co/300x200/90EE90/000000?text=Udon"},
    {'meal_name': "Tempura", 'category': "Fried Dish", 'favorite': random.choice([True, False]), 'broad_type': "Specialty & Street Foods", 'image_url': "https://placehold.co/300x200/90EE90/000000?text=Tempura"},
    {'meal_name': "Yakitori", 'category': "Grilled Dish", 'favorite': random.choice([True, False]), 'broad_type': "Grilled & Pan-Seared", 'image_url': "https://placehold.co/300x200/90EE90/000000?text=Yakitori"},
    {'meal_name': "Sashimi", 'category': "Seafood Special", 'favorite': random.choice([True, False]), 'broad_type': "Salads & Light Meals", 'image_url': "https://placehold.co/300x200/90EE90/000000?text=Sashimi"},
    {'meal_name': "Donburi", 'category': "Rice Bowl", 'favorite': random.choice([True, False]), 'broad_type': "Rice & Grain Bowls", 'image_url': "https://placehold.co/300x200/90EE90/000000?text=Donburi"},
    {'meal_name': "Oden", 'category': "Stew", 'favorite': random.choice([True, False]), 'broad_type': "Soups & Stews", 'image_url': "https://placehold.co/300x200/90EE90/000000?text=Oden"},
    {'meal_name': "Tamagoyaki", 'category': "Warm Meal", 'favorite': random.choice([True, False]), 'broad_type': "Specialty & Street Foods", 'image_url': "https://placehold.co/300x200/90EE90/000000?text=Tamagoyaki"},
    {'meal_name': "Soba", 'category': "Pasta Dish", 'favorite': random.choice([True, False]), 'broad_type': "Noodles & Pasta", 'image_url': "https://placehold.co/300x200/90EE90/000000?text=Soba"},
    {'meal_name': "Tonkatsu", 'category': "Fried Dish", 'favorite': random.choice([True, False]), 'broad_type': "Specialty & Street Foods", 'image_url': "https://placehold.co/300x200/90EE90/000000?text=Tonkatsu"},
    {'meal_name': "Sukiyaki", 'category': "Hot Pot", 'favorite': random.choice([True, False]), 'broad_type': "Soups & Stews", 'image_url': "https://placehold.co/300x200/90EE90/000000?text=Sukiyaki"},
    {'meal_name': "Okonomiyaki", 'category': "Warm Meal", 'favorite': random.choice([True, False]), 'broad_type': "Specialty & Street Foods", 'image_url': "https://placehold.co/300x200/90EE90/000000?text=Okonomiyaki"},
    {'meal_name': "Nikujaga", 'category': "Stew", 'favorite': random.choice([True, False]), 'broad_type': "Soups & Stews", 'image_url': "https://placehold.co/300x200/90EE90/000000?text=Nikujaga"},
    {'meal_name': "Curry Rice", 'category': "Rice Bowl", 'favorite': random.choice([True, False]), 'broad_type': "Rice & Grain Bowls", 'image_url': "https://placehold.co/300x200/90EE90/000000?text=Curry+Rice"},
    {'meal_name': "Unagi no Kabayaki", 'category': "Seafood Special", 'favorite': random.choice([True, False]), 'broad_type': "Grilled & Pan-Seared", 'image_url': "https://placehold.co/300x200/90EE90/000000?text=Unagi+no+Kabayaki"},
    {'meal_name': "Shabu Shabu Hot Pot", 'category': "Hot Pot", 'favorite': random.choice([True, False]), 'broad_type': "Soups & Stews", 'image_url': "https://placehold.co/300x200/90EE90/000000?text=Shabu+Shabu+Hot+Pot"},

    # Mexican Meals - Broad Type Categorization
    {'meal_name': "Sweet Potato and Black Bean Tacos", 'category': "Vegetarian Delight", 'favorite': random.choice([True, False]), 'broad_type': "Specialty & Street Foods", 'image_url': "https://placehold.co/300x200/FFA07A/000000?text=Sweet+Potato+Tacos"},
    {'meal_name': "Beef Burrito Bowl", 'category': "Rice Bowl", 'favorite': random.choice([True, False]), 'broad_type': "Rice & Grain Bowls", 'image_url': "https://placehold.co/300x200/FFA07A/000000?text=Beef+Burrito+Bowl"},
    {'meal_name': "Chicken Fajitas Platter", 'category': "Warm Meal", 'favorite': random.choice([True, False]), 'broad_type': "Grilled & Pan-Seared", 'image_url': "https://placehold.co/300x200/FFA07A/000000?text=Chicken+Fajitas"},
    {'meal_name': "Salsa Chicken", 'category': "Warm Meal", 'favorite': random.choice([True, False]), 'broad_type': "Grilled & Pan-Seared", 'image_url': "https://placehold.co/300x200/FFA07A/000000?text=Salsa+Chicken"},
    {'meal_name': "Easy Chorizo Street Tacos", 'category': "Warm Meal", 'favorite': random.choice([True, False]), 'broad_type': "Specialty & Street Foods", 'image_url': "https://placehold.co/300x200/FFA07A/000000?text=Chorizo+Street+Tacos"},
    {'meal_name': "Mexican Casserole", 'category': "Savory Bake", 'favorite': random.choice([True, False]), 'broad_type': "Roasted & Baked Dishes", 'image_url': "https://placehold.co/300x200/FFA07A/000000?text=Mexican+Casserole"},
    {'meal_name': "Easy Spicy Mexican-American Chicken", 'category': "Warm Meal", 'favorite': random.choice([True, False]), 'broad_type': "Grilled & Pan-Seared", 'image_url': "https://placehold.co/300x200/FFA07A/000000?text=Spicy+Mexican+Chicken"},
    {'meal_name': "Suegra's Tomatillo Chicken", 'category': "Warm Meal", 'favorite': random.choice([True, False]), 'broad_type': "Soups & Stews", 'image_url': "https://placehold.co/300x200/FFA07A/000000?text=Tomatillo+Chicken"},
    {'meal_name': "Salsa Verde Pork", 'category': "Warm Meal", 'favorite': random.choice([True, False]), 'broad_type': "Soups & Stews", 'image_url': "https://placehold.co/300x200/FFA07A/000000?text=Salsa+Verde+Pork"},
    {'meal_name': "Papas con Chorizo (Mexican Chorizo and Potatoes)", 'category': "Warm Meal", 'favorite': random.choice([True, False]), 'broad_type': "Grilled & Pan-Seared", 'image_url': "https://placehold.co/300x200/FFA07A/000000?text=Papas+con+Chorizo"},
    {'meal_name': "Flaming Slow Cooker Pork", 'category': "Warm Meal", 'favorite': random.choice([True, False]), 'broad_type': "Soups & Stews", 'image_url': "https://placehold.co/300x200/FFA07A/000000?text=Slow+Cooker+Pork"},
    {'meal_name': "Delia's Grilled Shrimp Sonora", 'category': "Grilled Dish", 'favorite': random.choice([True, False]), 'broad_type': "Grilled & Pan-Seared", 'image_url': "https://placehold.co/300x200/FFA07A/000000?text=Grilled+Shrimp+Sonora"},
    {'meal_name': "Mexican Mostaccioli", 'category': "Pasta Dish", 'favorite': random.choice([True, False]), 'broad_type': "Noodles & Pasta", 'image_url': "https://placehold.co/300x200/FFA07A/000000?text=Mexican+Mostaccioli"},
    {'meal_name': "Taco-Seasoned Salmon", 'category': "Seafood Special", 'favorite': random.choice([True, False]), 'broad_type': "Grilled & Pan-Seared", 'image_url': "https://placehold.co/300x200/FFA07A/000000?text=Taco-Seasoned+Salmon"},
    {'meal_name': "Quesadillas de Flor de Calabaza (Zucchini Blossom Quesadillas)", 'category': "Vegetarian Delight", 'favorite': random.choice([True, False]), 'broad_type': "Specialty & Street Foods", 'image_url': "https://placehold.co/300x200/FFA07A/000000?text=Zucchini+Blossom+Quesadillas"},

    # Thai Meals - Broad Type Categorization
    {'meal_name': "Thai Green Curry with Tofu", 'category': "Warm Meal", 'favorite': random.choice([True, False]), 'broad_type': "Soups & Stews", 'image_url': "https://placehold.co/300x200/DDA0DD/000000?text=Thai+Green+Curry"},
    {'meal_name': "Pad Thai Noodles", 'category': "Pasta Dish", 'favorite': random.choice([True, False]), 'broad_type': "Noodles & Pasta", 'image_url': "https://placehold.co/300x200/DDA0DD/000000?text=Pad+Thai+Noodles"},
    {'meal_name': "Khao Soi (Thai Coconut Noodle Soup)", 'category': "Soup", 'favorite': random.choice([True, False]), 'broad_type': "Soups & Stews", 'image_url': "https://placehold.co/300x200/DDA0DD/000000?text=Khao+Soi"},
    {'meal_name': "Thai Larb Salad", 'category': "Salad", 'favorite': random.choice([True, False]), 'broad_type': "Salads & Light Meals", 'image_url': "https://placehold.co/300x200/DDA0DD/000000?text=Thai+Larb+Salad"},
    {'meal_name': "Thai Massaman Curry", 'category': "Warm Meal", 'favorite': random.choice([True, False]), 'broad_type': "Soups & Stews", 'image_url': "https://placehold.co/300x200/DDA0DD/000000?text=Thai+Massaman+Curry"},
    {'meal_name': "Thai Fish Curry", 'category': "Warm Meal", 'favorite': random.choice([True, False]), 'broad_type': "Soups & Stews", 'image_url': "https://placehold.co/300x200/DDA0DD/000000?text=Thai+Fish+Curry"},
    {'meal_name': "Thai Noodle Salad with Peanut Sauce", 'category': "Salad", 'favorite': random.choice([True, False]), 'broad_type': "Salads & Light Meals", 'image_url': "https://placehold.co/300x200/DDA0DD/000000?text=Thai+Noodle+Salad"},
    {'meal_name': "Pad See Ew", 'category': "Pasta Dish", 'favorite': random.choice([True, False]), 'broad_type': "Noodles & Pasta", 'image_url': "https://placehold.co/300x200/DDA0DD/000000?text=Pad+See+Ew"},
    {'meal_name': "Thai Red Curry", 'category': "Warm Meal", 'favorite': random.choice([True, False]), 'broad_type': "Soups & Stews", 'image_url': "https://placehold.co/300x200/DDA0DD/000000?text=Thai+Red+Curry"},
    {'meal_name': "Tom Kha Gai (Thai Coconut Chicken Soup)", 'category': "Soup", 'favorite': random.choice([True, False]), 'broad_type': "Soups & Stews", 'image_url': "https://placehold.co/300x200/DDA0DD/000000?text=Tom+Kha+Gai"},
    {'meal_name': "Thai Basil Chicken", 'category': "Warm Meal", 'favorite': random.choice([True, False]), 'broad_type': "Grilled & Pan-Seared", 'image_url': "https://placehold.co/300x200/DDA0DD/000000?text=Thai+Basil+Chicken"},
    {'meal_name': "Thai Eggplant Stir-Fry", 'category': "Vegetarian Delight", 'favorite': random.choice([True, False]), 'broad_type': "Grilled & Pan-Seared", 'image_url': "https://placehold.co/300x200/DDA0DD/000000?text=Thai+Eggplant+Stir-Fry"},
    {'meal_name': "Thai Pineapple Fried Rice", 'category': "Rice Bowl", 'favorite': random.choice([True, False]), 'broad_type': "Rice & Grain Bowls", 'image_url': "https://placehold.co/300x200/DDA0DD/000000?text=Thai+Pineapple+Fried+Rice"},
    {'meal_name': "Thai Grilled Eggplant Salad", 'category': "Salad", 'favorite': random.choice([True, False]), 'broad_type': "Salads & Light Meals", 'image_url': "https://placehold.co/300x200/DDA0DD/000000?text=Thai+Grilled+Eggplant+Salad"},
    {'meal_name': "Thai Coconut Chicken Salad", 'category': "Salad", 'favorite': random.choice([True, False]), 'broad_type': "Salads & Light Meals", 'image_url': "https://placehold.co/300x200/DDA0DD/000000?text=Thai+Coconut+Chicken+Salad"},
    {'meal_name': "Thai Chicken Satay with Peanut Dipping Sauce", 'category': "Grilled Dish", 'favorite': random.choice([True, False]), 'broad_type': "Grilled & Pan-Seared", 'image_url': "https://placehold.co/300x200/DDA0DD/000000?text=Thai+Chicken+Satay"},
    {'meal_name': "Thai Baked Chicken and Rice", 'category': "Savory Bake", 'favorite': random.choice([True, False]), 'broad_type': "Roasted & Baked Dishes", 'image_url': "https://placehold.co/300x200/DDA0DD/000000?text=Thai+Baked+Chicken+and+Rice"},
    {'meal_name': "Thai Turkey Burgers", 'category': "Grilled Dish", 'favorite': random.choice([True, False]), 'broad_type': "Specialty & Street Foods", 'image_url': "https://placehold.co/300x200/DDA0DD/000000?text=Thai+Turkey+Burgers"},
    {'meal_name': "Thai Curry Meatballs", 'category': "Warm Meal", 'favorite': random.choice([True, False]), 'broad_type': "Specialty & Street Foods", 'image_url': "https://placehold.co/300x200/DDA0DD/000000?text=Thai+Curry+Meatballs"},
    {'meal_name': "Thai Burritos with Peanut Sauce", 'category': "Warm Meal", 'favorite': random.choice([True, False]), 'broad_type': "Sandwiches & Wraps", 'image_url': "https://placehold.co/300x200/DDA0DD/000000?text=Thai+Burritos"},

    # Vietnamese Meals - Broad Type Categorization
    {'meal_name': "Phở (Beef Noodle Soup)", 'category': "Soup", 'favorite': random.choice([True, False]), 'broad_type': "Soups & Stews", 'image_url': "https://placehold.co/300x200/FFB6C1/000000?text=Pho"},
    {'meal_name': "Bánh Mì (Vietnamese Sandwich)", 'category': "Sandwich", 'favorite': random.choice([True, False]), 'broad_type': "Sandwiches & Wraps", 'image_url': "https://placehold.co/300x200/FFB6C1/000000?text=Banh+Mi"},
    {'meal_name': "Cơm Tấm (Broken Rice)", 'category': "Rice Bowl", 'favorite': random.choice([True, False]), 'broad_type': "Rice & Grain Bowls", 'image_url': "https://placehold.co/300x200/FFB6C1/000000?text=Com+Tam"},
    {'meal_name': "Bún Bò Huế (Hue Style Beef Noodle Soup)", 'category': "Soup", 'favorite': random.choice([True, False]), 'broad_type': "Soups & Stews", 'image_url': "https://placehold.co/300x200/FFB6C1/000000?text=Bun+Bo+Hue"},
    {'meal_name': "Gỏi cuốn (Fresh Spring Rolls)", 'category': "Appetizer/Light Meal", 'favorite': random.choice([True, False]), 'broad_type': "Salads & Light Meals", 'image_url': "https://placehold.co/300x200/FFB6C1/000000?text=Fresh+Spring+Rolls"},
    {'meal_name': "Canh (Vietnamese Soups)", 'category': "Soup", 'favorite': random.choice([True, False]), 'broad_type': "Soups & Stews", 'image_url': "https://placehold.co/300x200/FFB6C1/000000?text=Canh"},
    {'meal_name': "Bánh cuốn (Steamed Rice Rolls)", 'category': "Warm Meal", 'favorite': random.choice([True, False]), 'broad_type': "Specialty & Street Foods", 'image_url': "https://placehold.co/300x200/FFB6C1/000000?text=Steamed+Rice+Rolls"},
    {'meal_name': "Cháo (Rice Porridge)", 'category': "Soup", 'favorite': random.choice([True, False]), 'broad_type': "Soups & Stews", 'image_url': "https://placehold.co/300x200/FFB6C1/000000?text=Chao"},
    {'meal_name': "Cha Ca Ha Noi (Hanoi Grilled Fish)", 'category': "Grilled Dish", 'favorite': random.choice([True, False]), 'broad_type': "Grilled & Pan-Seared", 'image_url': "https://placehold.co/300x200/FFB6C1/000000?text=Hanoi+Grilled+Fish"},
    {'meal_name': "Cá Kho Tộ (Caramelized Fish in Clay Pot)", 'category': "Warm Meal", 'favorite': random.choice([True, False]), 'broad_type': "Soups & Stews", 'image_url': "https://placehold.co/300x200/FFB6C1/000000?text=Caramelized+Fish"},
    {'meal_name': "Bánh xèo (Crispy Pancakes)", 'category': "Warm Meal", 'favorite': random.choice([True, False]), 'broad_type': "Specialty & Street Foods", 'image_url': "https://placehold.co/300x200/FFB6C1/000000?text=Crispy+Pancakes"},
    {'meal_name': "Bun bo nam bo (Beef Noodle Salad)", 'category': "Salad", 'favorite': random.choice([True, False]), 'broad_type': "Salads & Light Meals", 'image_url': "https://placehold.co/300x200/FFB6C1/000000?text=Beef+Noodle+Salad"},
    {'meal_name': "Bo luc lac (Shaking Beef)", 'category': "Warm Meal", 'favorite': random.choice([True, False]), 'broad_type': "Grilled & Pan-Seared", 'image_url': "https://placehold.co/300x200/FFB6C1/000000?text=Shaking+Beef"},
    {'meal_name': "Banh goi (Fried Pastry)", 'category': "Warm Meal", 'favorite': random.choice([True, False]), 'broad_type': "Specialty & Street Foods", 'image_url': "https://placehold.co/300x200/FFB6C1/000000?text=Fried+Pastry"},

    # Indonesian Meals - Broad Type Categorization
    {'meal_name': "Nasi goreng (Fried Rice)", 'category': "Rice Bowl", 'favorite': random.choice([True, False]), 'broad_type': "Rice & Grain Bowls", 'image_url': "https://placehold.co/300x200/FFDAB9/000000?text=Nasi+Goreng"},
    {'meal_name': "Mie goreng (Fried Noodles)", 'category': "Pasta Dish", 'favorite': random.choice([True, False]), 'broad_type': "Noodles & Pasta", 'image_url': "https://placehold.co/300x200/FFDAB9/000000?text=Mie+Goreng"},
    {'meal_name': "Sate (Grilled Skewers)", 'category': "Grilled Dish", 'favorite': random.choice([True, False]), 'broad_type': "Grilled & Pan-Seared", 'image_url': "https://placehold.co/300x200/FFDAB9/000000?text=Sate"},
    {'meal_name': "Rendang (Beef Curry)", 'category': "Warm Meal", 'favorite': random.choice([True, False]), 'broad_type': "Soups & Stews", 'image_url': "https://placehold.co/300x200/FFDAB9/000000?text=Rendang"},
    {'meal_name': "Rawon (Beef Soup)", 'category': "Soup", 'favorite': random.choice([True, False]), 'broad_type': "Soups & Stews", 'image_url': "https://placehold.co/300x200/FFDAB9/000000?text=Rawon"},
    {'meal_name': "Soto (Soup)", 'category': "Soup", 'favorite': random.choice([True, False]), 'broad_type': "Soups & Stews", 'image_url': "https://placehold.co/300x200/FFDAB9/000000?text=Soto"},
    {'meal_name': "Perkedel (Potato Patties)", 'category': "Side Dish/Light Meal", 'favorite': random.choice([True, False]), 'broad_type': "Specialty & Street Foods", 'image_url': "https://placehold.co/300x200/FFDAB9/000000?text=Perkedel"},
    {'meal_name': "Bebek goreng (Fried Duck)", 'category': "Fried Dish", 'favorite': random.choice([True, False]), 'broad_type': "Grilled & Pan-Seared", 'image_url': "https://placehold.co/300x200/FFDAB9/000000?text=Bebek+Goreng"},
    {'meal_name': "Kare (Curry)", 'category': "Warm Meal", 'favorite': random.choice([True, False]), 'broad_type': "Soups & Stews", 'image_url': "https://placehold.co/300x200/FFDAB9/000000?text=Kare"},
    {'meal_name': "Ayam bakar Taliwang (Grilled Chicken)", 'category': "Grilled Dish", 'favorite': random.choice([True, False]), 'broad_type': "Grilled & Pan-Seared", 'image_url': "https://placehold.co/300x200/FFDAB9/000000?text=Ayam+Bakar+Taliwang"},
    {'meal_name': "Bakso (Meatball Soup)", 'category': "Soup", 'favorite': random.choice([True, False]), 'broad_type': "Soups & Stews", 'image_url': "https://placehold.co/300x200/FFDAB9/000000?text=Bakso"},
    {'meal_name': "Gado-gado (Vegetable Salad with Peanut Sauce)", 'category': "Salad", 'favorite': random.choice([True, False]), 'broad_type': "Salads & Light Meals", 'image_url': "https://placehold.co/300x200/FFDAB9/000000?text=Gado-gado"},
    {'meal_name': "Batagor (Fried Tofu with Meatball)", 'category': "Fried Dish", 'favorite': random.choice([True, False]), 'broad_type': "Specialty & Street Foods", 'image_url': "https://placehold.co/300x200/FFDAB9/000000?text=Batagor"},
    {'meal_name': "Babi guling (Roasted Suckling Pig)", 'category': "Roast", 'favorite': random.choice([True, False]), 'broad_type': "Roasted & Baked Dishes", 'image_url': "https://placehold.co/300x200/FFDAB9/000000?text=Babi+Guling"},
    {'meal_name': "Pepes (Herbal Packet)", 'category': "Steamed Dish", 'favorite': random.choice([True, False]), 'broad_type': "Specialty & Street Foods", 'image_url': "https://placehold.co/300x200/FFDAB9/000000?text=Pepes"},

    # Filipino Meals - Broad Type Categorization
    {'meal_name': "Adobo (Pork or Chicken Stewed in Soy Sauce and Vinegar)", 'category': "Stew", 'favorite': random.choice([True, False]), 'broad_type': "Soups & Stews", 'image_url': "https://placehold.co/300x200/E6E6FA/000000?text=Adobo"},
    {'meal_name': "Afritada (Chicken or Pork Stewed in Tomato Sauce)", 'category': "Stew", 'favorite': random.choice([True, False]), 'broad_type': "Soups & Stews", 'image_url': "https://placehold.co/300x200/E6E6FA/000000?text=Afritada"},
    {'meal_name': "Barbecue (Inihaw, Inasal, Satti) (Grilled Meat Skewers)", 'category': "Grilled Dish", 'favorite': random.choice([True, False]), 'broad_type': "Grilled & Pan-Seared", 'image_url': "https://placehold.co/300x200/E6E6FA/000000?text=Filipino+BBQ"},
    {'meal_name': "Bopis (Spicy Pork Lungs and Heart)", 'category': "Warm Meal", 'favorite': random.choice([True, False]), 'broad_type': "Specialty & Street Foods", 'image_url': "https://placehold.co/300x200/E6E6FA/000000?text=Bopis"},
    {'meal_name': "Camaron rebosado (Deep Fried Battered Shrimps)", 'category': "Fried Dish", 'favorite': random.choice([True, False]), 'broad_type': "Specialty & Street Foods", 'image_url': "https://placehold.co/300x200/E6E6FA/000000?text=Camaron+Rebosado"},
    {'meal_name': "Chicken pastel (Chicken Stew in Cream Sauce)", 'category': "Stew", 'favorite': random.choice([True, False]), 'broad_type': "Soups & Stews", 'image_url': "https://placehold.co/300x200/E6E6FA/000000?text=Chicken+Pastel"},
    {'meal_name': "Crispy pata (Deep Fried Pork Leg)", 'category': "Fried Dish", 'favorite': random.choice([True, False]), 'broad_type': "Roasted & Baked Dishes", 'image_url': "https://placehold.co/300x200/E6E6FA/000000?text=Crispy+Pata"},
    {'meal_name': "Crispy tadyang ng baka (Crispy Beef Ribs)", 'category': "Fried Dish", 'favorite': random.choice([True, False]), 'broad_type': "Specialty & Street Foods", 'image_url': "https://placehold.co/300x200/E6E6FA/000000?text=Crispy+Beef+Ribs"},
    {'meal_name': "Curacha (Boiled or Steamed Sea Crab)", 'category': "Seafood Special", 'favorite': random.choice([True, False]), 'broad_type': "Grilled & Pan-Seared", 'image_url': "https://placehold.co/300x200/E6E6FA/000000?text=Curacha"},
    {'meal_name': "Daing (Fried Dried Fish)", 'category': "Seafood Special", 'favorite': random.choice([True, False]), 'broad_type': "Grilled & Pan-Seared", 'image_url': "https://placehold.co/300x200/E6E6FA/000000?text=Daing"},
    {'meal_name': "Embutido (Meatloaf)", 'category': "Warm Meal", 'favorite': random.choice([True, False]), 'broad_type': "Roasted & Baked Dishes", 'image_url': "https://placehold.co/300x200/E6E6FA/000000?text=Embutido"},
    {'meal_name': "Escabeche (Sweet and Sour Fish)", 'category': "Seafood Special", 'favorite': random.choice([True, False]), 'broad_type': "Grilled & Pan-Seared", 'image_url': "https://placehold.co/300x200/E6E6FA/000000?text=Escabeche"},
    {'meal_name': "Giniling (Picadillo) (Ground Pork or Beef)", 'category': "Warm Meal", 'favorite': random.choice([True, False]), 'broad_type': "Specialty & Street Foods", 'image_url': "https://placehold.co/300x200/E6E6FA/000000?text=Giniling"},
    {'meal_name': "Halabos na hipon (Steamed Shrimps)", 'category': "Seafood Special", 'favorite': random.choice([True, False]), 'broad_type': "Salads & Light Meals", 'image_url': "https://placehold.co/300x200/E6E6FA/000000?text=Halabos+na+Hipon"},
    {'meal_name': "Hamonado (Sweet Glazed Pork)", 'category': "Warm Meal", 'favorite': random.choice([True, False]), 'broad_type': "Roasted & Baked Dishes", 'image_url': "https://placehold.co/300x200/E6E6FA/000000?text=Hamonado"},
    {'meal_name': "Humba (Sweet Pork Stew)", 'category': "Stew", 'favorite': random.choice([True, False]), 'broad_type': "Soups & Stews", 'image_url': "https://placehold.co/300x200/E6E6FA/000000?text=Humba"},
    {'meal_name': "Inasal na manok (Grilled Chicken)", 'category': "Grilled Dish", 'favorite': random.choice([True, False]), 'broad_type': "Grilled & Pan-Seared", 'image_url': "https://placehold.co/300x200/E6E6FA/000000?text=Inasal+na+Manok"},
    {'meal_name': "Inihaw na liempo (Grilled Pork Belly)", 'category': "Grilled Dish", 'favorite': random.choice([True, False]), 'broad_type': "Grilled & Pan-Seared", 'image_url': "https://placehold.co/300x200/E6E6FA/000000?text=Inihaw+na+Liempo"},
    {'meal_name': "Inun-unan (Fish Stewed in Vinegar)", 'category': "Stew", 'favorite': random.choice([True, False]), 'broad_type': "Soups & Stews", 'image_url': "https://placehold.co/300x200/E6E6FA/000000?text=Inun-unan"},
    {'meal_name': "Kadyos-Baboy-Langka (Pigeon Peas, Pork, and Jackfruit Stew)", 'category': "Stew", 'favorite': random.choice([True, False]), 'broad_type': "Soups & Stews", 'image_url': "https://placehold.co/300x200/E6E6FA/000000?text=Kadyos-Baboy-Langka"},
    {'meal_name': "Kadyos Manok Ubad (Pigeon Peas, Chicken, and Banana Stalk Stew)", 'category': "Stew", 'favorite': random.choice([True, False]), 'broad_type': "Soups & Stews", 'image_url': "https://placehold.co/300x200/E6E6FA/000000?text=Kadyos+Manok+Ubad"},
    {'meal_name': "Kaldereta (Meat Stew in Tomato Sauce)", 'category': "Stew", 'favorite': random.choice([True, False]), 'broad_type': "Soups & Stews", 'image_url': "https://placehold.co/300x200/E6E6FA/000000?text=Kaldereta"},
    {'meal_name': "Kinunot (Shredded Stingray or Shark in Coconut Milk)", 'category': "Seafood Special", 'favorite': random.choice([True, False]), 'broad_type': "Soups & Stews", 'image_url': "https://placehold.co/300x200/E6E6FA/000000?text=Kinunot"},
    {'meal_name': "Bicol Express (Pork Cooked in Coconut Milk and Chili)", 'category': "Warm Meal", 'favorite': random.choice([True, False]), 'broad_type': "Soups & Stews", 'image_url': "https://placehold.co/300x200/E6E6FA/000000?text=Bicol+Express"},
    {'meal_name': "Filipino Spaghetti (Sweet and Meaty Spaghetti)", 'category': "Pasta Dish", 'favorite': random.choice([True, False]), 'broad_type': "Noodles & Pasta", 'image_url': "https://placehold.co/300x200/E6E6FA/000000?text=Filipino+Spaghetti"},
    {'meal_name': "Pork Menudo (Pork Stew with Tomatoes and Potatoes)", 'category': "Stew", 'favorite': random.choice([True, False]), 'broad_type': "Soups & Stews", 'image_url': "https://placehold.co/300x200/E6E6FA/000000?text=Pork+Menudo"},
    {'meal_name': "Chicken Tinola (Chicken Soup with Ginger and Papaya)", 'category': "Soup", 'favorite': random.choice([True, False]), 'broad_type': "Soups & Stews", 'image_url': "https://placehold.co/300x200/E6E6FA/000000?text=Chicken+Tinola"},
    {'meal_name': "Arroz Caldo (Chicken Rice Porridge)", 'category': "Soup", 'favorite': random.choice([True, False]), 'broad_type': "Soups & Stews", 'image_url': "https://placehold.co/300x200/E6E6FA/000000?text=Arroz+Caldo"},
    {'meal_name': "Pinakbet (Vegetable Stew with Shrimp Paste)", 'category': "Vegetarian Delight", 'favorite': random.choice([True, False]), 'broad_type': "Soups & Stews", 'image_url': "https://placehold.co/300x200/E6E6FA/000000?text=Pinakbet"},
    {'meal_name': "Kare-Kare (Stew with Peanut Sauce)", 'category': "Stew", 'favorite': random.choice([True, False]), 'broad_type': "Soups & Stews", 'image_url': "https://placehold.co/300x200/E6E6FA/000000?text=Kare-Kare"},
    {'meal_name': "Lumpia (Spring Rolls)", 'category': "Appetizer/Light Meal", 'favorite': random.choice([True, False]), 'broad_type': "Specialty & Street Foods", 'image_url': "https://placehold.co/300x200/E6E6FA/000000?text=Lumpia"},
    {'meal_name': "Filipino Chicken Curry", 'category': "Warm Meal", 'favorite': random.choice([True, False]), 'broad_type': "Soups & Stews", 'image_url': "https://placehold.co/300x200/E6E6FA/000000?text=Filipino+Chicken+Curry"},
    {'meal_name': "Sinigang na Hipon (Sour Shrimp Soup)", 'category': "Soup", 'favorite': random.choice([True, False]), 'broad_type': "Soups & Stews", 'image_url': "https://placehold.co/300x200/E6E6FA/000000?text=Sinigang+na+Hipon"},
    {'meal_name': "Beef Caldereta (Beef Stew in Tomato Sauce)", 'category': "Stew", 'favorite': random.choice([True, False]), 'broad_type': "Soups & Stews", 'image_url': "https://placehold.co/300x200/E6E6FA/000000?text=Beef+Caldereta"},
    {'meal_name': "Bistek Tagalog (Beef Braised in Soy Sauce and Citrus)", 'category': "Warm Meal", 'favorite': random.choice([True, False]), 'broad_type': "Grilled & Pan-Seared", 'image_url': "https://placehold.co/300x200/E6E6FA/000000?text=Bistek+Tagalog"},
    {'meal_name': "Adobong Pusit (Squid Adobo)", 'category': "Seafood Special", 'favorite': random.choice([True, False]), 'broad_type': "Soups & Stews", 'image_url': "https://placehold.co/300x200/E6E6FA/000000?text=Adobong+Pusit"},
    {'meal_name': "Tortang Talong (Eggplant Omelette)", 'category': "Vegetarian Delight", 'favorite': random.choice([True, False]), 'broad_type': "Specialty & Street Foods", 'image_url': "https://placehold.co/300x200/E6E6FA/000000?text=Tortang+Talong"},
    {'meal_name': "Lechon (Roasted Pig)", 'category': "Roast", 'favorite': random.choice([True, False]), 'broad_type': "Roasted & Baked Dishes", 'image_url': "https://placehold.co/300x200/E6E6FA/000000?text=Lechon"},
    {'meal_name': "Pancit Palabok (Noodle Dish with Shrimp Sauce)", 'category': "Pasta Dish", 'favorite': random.choice([True, False]), 'broad_type': "Noodles & Pasta", 'image_url': "https://placehold.co/300x200/E6E6FA/000000?text=Pancit+Palabok"},
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
        "favorite_checkbox": "Show only Favorite",
        "results_header_prefix": "Discover",
        "results_header_suffix": "Meal Ideas!",
        "suggest_button": "Suggest a Random Meal",
        "favorite_tag": "⭐ Favorite",
        "all_matching_meals": "All Matching Meals:",
        "broad_type_label": "Broad Type:",
        "category_label": "Category:",
        "no_meals_warning": "No meals found matching your criteria. Try adjusting your filters!",
        "footer": "Happy cooking! 🍳",
        "language_toggle_label": "Switch to Spanish", # Label for the toggle
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
        "favorite_checkbox": "Mostrar solo los favoritos",
        "results_header_prefix": "¡Descubre",
        "results_header_suffix": "Ideas de Comida!",
        "suggest_button": "Sugerir una Comida Aleatoria",
        "favorite_tag": "⭐ Más Vendido",
        "all_matching_meals": "Todas las Comidas Coincidentes:",
        "broad_type_label": "Tipo Amplio:",
        "category_label": "Categoría:",
        "no_meals_warning": "No se encontraron comidas que coincidan con tus criterios. ¡Intenta ajustar tus filtros!",
        "footer": "¡Feliz cocina! 🍳",
        "language_toggle_label": "Cambiar a Inglés", # Label for the toggle
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

# Callback function for the toggle
def toggle_language():
    if st.session_state.language_toggle: # If toggle is True (checked)
        st.session_state.language = "es"
    else: # If toggle is False (unchecked)
        st.session_state.language = "en"
    st.rerun() # Rerun the app to apply language changes

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

# --- Language Toggle ---
# Determine initial state of the toggle based on current language
is_spanish = (st.session_state.language == "es")

st.toggle(
    label=current_text["language_toggle_label"],
    value=is_spanish,
    key="language_toggle",
    on_change=toggle_language,
    help="Toggle to switch between English and Spanish" # This help text will not change with language
)

# --- App Title and Description ---
st.markdown(f"<h1 class='center-text'>{current_text['app_title']}</h1>", unsafe_allow_html=True)
st.write(current_text["app_description"])

# --- Filter Your Meal Search
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


# Favorite checkbox
filter_favorite = st.checkbox(current_text["favorite_checkbox"])

# --- Meal Ideas

# Filter logic
filtered_df = df.copy()

if selected_broad_type_for_filter is not None:
    # Filter only if the internal broad_type exists in the actual DataFrame
    if selected_broad_type_for_filter in df['broad_type'].unique():
        filtered_df = filtered_df[filtered_df['broad_type'] == selected_broad_type_for_filter]
    else:
        filtered_df = pd.DataFrame() # No meals for a dummy/non-existent broad type

if filter_favorite:
    filtered_df = filtered_df[filtered_df['favorite'] == True]

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
                    f"<span class='best-seller-tag'>{current_text['favorite_tag']}</span>" if random_meal['favorite'] else ""
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
                    f"<span class='best-seller-tag'>{current_text['favorite_tag']}</span>" if row['favorite'] else ""
                }</h3>
                <p><strong>{current_text['broad_type_label']}</strong> {current_text['broad_type_translations'].get(row['broad_type'], row['broad_type'])}</p>
                <p><strong>{current_text['category_label']}</strong> {row['category']}</p>
            </div>
            """, unsafe_allow_html=True
        )
else:
    st.warning(current_text["no_meals_warning"])

st.markdown(f"<p class='center-text'>{current_text['footer']}</p>", unsafe_allow_html=True)
