import streamlit as st
import pandas as pd
import random

# Meal list (remains the same - data content, not UI text)
meal_list = [
    # Chilean Meals - Broad Type Categorization
    {'meal_name': "Pastel de Choclo Bake", 'category': "Savory Bake", 'favorite': random.choice([True, False]), 'broad_type': "Roasted & Baked Dishes", 'image_url': "data:image/jpeg;base64,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"},
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
        "favorite_tag": "⭐ Favoritos",
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
