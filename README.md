# 🥗 Smart Meal Planner

A Python-based CLI application that generates a multi-day meal plan based on available groceries and a recipe database.

## ✅ Core Features
- **Dictionary-Based Lookup:** Efficiently maps recipes to their required ingredients using Python dictionaries.
- **Fuzzy Spelling Correction:** Uses the `difflib` library to handle user typos (e.g., "pner" is corrected to "paneer") by calculating string similarity ratios.
- **Main Ingredient Logic:** A recipe is only suggested if the user possesses the "Main Ingredient" (the first item in the recipe list).
- **Match Threshold:** Filters recipes based on a 50% ingredient match or if only one ingredient is missing.
- **Dynamic Inventory:** Automatically "removes" used ingredients from your list as it plans each day's meals.

## 🛠️ Built With
- **Python 3**
- **difflib**: For the Gestalt Pattern Matching algorithm used in spelling correction.
- **random**: To ensure variety in the meal suggestions.

## 📋 How to Use
1. **Run the script:**
   ```bash
   python3 main.py
