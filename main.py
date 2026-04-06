from recipes import recipes
from difflib import get_close_matches

def correct_spelling(word, valid_words):
    matches = get_close_matches(word, valid_words, n=1, cutoff=0.7)
    return matches[0] if matches else word

def clean_groceries_input(user_input):
    groceries = [item.strip().lower() for item in user_input.split(",") if item.strip()]
    all_possible_items = {ing for rcp in recipes.values() for ing in rcp}
    return [correct_spelling(item, all_possible_items) for item in groceries]

def get_available_recipes(groceries):
    available = []
    for recipe, ingredients in recipes.items():
        matched = sum(1 for ing in ingredients if ing in groceries)
        total = len(ingredients)
        main_ingredient = ingredients[0]
        # Main ingredient must be present + logic for matched ingredients
        if main_ingredient in groceries and (matched >= total - 1 or matched / total >= 0.5):
            available.append((recipe, matched, total))
    return sorted(available, key=lambda x: x[1] / x[2], reverse=True)

def plan_meals(days, groceries):
    plan = {}
    used_items = set()
    day = 1
    while groceries and day <= days:
        all_recipes = get_available_recipes(groceries)
        if not all_recipes:
            break
        
        meals_today = all_recipes[:3] if len(all_recipes) >= 3 else all_recipes
        plan[f"Day {day}"] = [r[0] for r in meals_today]
        
        for recipe_name, _, _ in meals_today:
            for ing in recipes[recipe_name]:
                if ing in groceries:
                    used_items.add(ing)
        
        # Update groceries to remove items used today
        groceries = [item for item in groceries if item not in used_items]
        day += 1
        
    leftovers = [item for item in groceries if item not in used_items]
    return plan, leftovers

def main():
    print("Welcome to the Meal Planner")
    try:
        days = int(input("Enter number of days you want to plan for: "))
    except ValueError:
        print("Please enter a valid number for days.")
        return

    groceries_input = input("Enter all available groceries (comma separated): ")
    groceries = clean_groceries_input(groceries_input)
    
    meal_plan, leftovers = plan_meals(days, groceries)
    
    print("\nYour Meal Plan:")
    for day, meals in meal_plan.items():
        print(f"\n{day}:")
        for i, recipe in enumerate(meals, start=1):
            print(f"  {i}. {recipe}")
        
        if len(meals) < 3:
            print(f"  Only {len(meals)} meal(s) could be planned for this day due to limited ingredients.")
    
    if len(meal_plan) < days:
        print(f"\nOnly {len(meal_plan)} out of {days} days could be planned due to limited groceries.")
        
    print("\nLeftover Groceries:")
    if leftovers:
        print(", ".join(leftovers))
    else:
        print("None – all groceries were used!")

if __name__ == "__main__":
    main()