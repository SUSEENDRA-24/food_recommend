# Sample health records for multiple users with different health conditions
user_health_records = [
    {
        'name': 'User1',
        'age': 30,
        'gender': 'male',
        'weight_kg': 70,
        'height_cm': 175,
        'activity_level': 'moderate',
        'health_condition': 'diabetes',
    },
    {
        'name': 'User2',
        'age': 40,
        'gender': 'female',
        'weight_kg': 60,
        'height_cm': 160,
        'activity_level': 'sedentary',
        'health_condition': 'high_blood_pressure',
    },
    # Add more user records with different health conditions here
]

# Sample nutritional database (food items with their nutritional values)
nutritional_database = {
    'apple': {'calories': 52, 'carbs_g': 14, 'protein_g': 0.3, 'fat_g': 0.2, 'fiber_g': 2.4},
    'chicken_breast': {'calories': 165, 'carbs_g': 0, 'protein_g': 31, 'fat_g': 3.6, 'fiber_g': 0},
    'mutton_briyani':{'calories':200,'carbs_g':10,'protein_g':20,'fat_g':5,'fiber_g':3},
    # Add more food items here
}


# # Define the user's nutritional goals based on their health record
def calculate_nutritional_goals(user_record):
    # Example: Calculate daily calorie goal for weight maintenance
    calorie_goal = user_record['weight_kg'] * 30

    # Example: Set macronutrient ratios based on dietary needs and health condition
    if user_record['health_condition'] == 'diabetes':
        carb_ratio = 0.40  # 40% of calories from carbs for diabetes
        fat_ratio = 0.30  # 30% of calories from fat
    elif user_record['health_condition'] == 'high_blood_pressure':
        carb_ratio = 0.35  # 35% of calories from carbs for high blood pressure
        fat_ratio = 0.25  # 25% of calories from fat
    else:
        carb_ratio = 0.45  # Default carb ratio
        fat_ratio = 0.30  # Default fat ratio

    protein_ratio = 1.0 - carb_ratio - fat_ratio

    # Calculate macronutrient goals in grams
    carb_goal = (carb_ratio * calorie_goal) / 4
    protein_goal = (protein_ratio * calorie_goal) / 4
    fat_goal = (fat_ratio * calorie_goal) / 9

    return {
        'calories': calorie_goal,
        'carbs_g': carb_goal,
        'protein_g': protein_goal,
        'fat_g': fat_goal,
    }

# # Recommend a meal based on the user's nutritional goals and health condition
# def recommend_meal(user_nutritional_goals, health_condition, nutritional_database):
#     # This is a simplified example. In a real system, you'd use more complex logic.
#     recommended_meal = {}
#     for food, values in nutritional_database.items():
#         # Consider health condition-specific food restrictions here
#         if health_condition == 'diabetes' and 'high_sugar' in values:
#             continue  # Skip high-sugar foods for diabetes
#         if values['calories'] <= user_nutritional_goals['calories']:
#             recommended_meal[food] = values

#     return recommended_meal

# # Create a list of recommended meals for each user
# recommended_meals = []

# # Process user records and recommend meals for each user
# for user_record in user_health_records:
#     # Calculate nutritional goals for the user
#     user_nutritional_goals = calculate_nutritional_goals(user_record)

#     # Recommend a meal based on nutritional goals and the user's health condition
#     recommended_meal = recommend_meal(user_nutritional_goals, user_record['health_condition'], nutritional_database)

#     recommended_meals.append(recommended_meal)

# # Print recommended meals for each user
# for i, recommended_meal in enumerate(recommended_meals):
#     user_record = user_health_records[i]
#     print(f"Recommended Meal for {user_record['name']} with {user_record['health_condition']}:")
#     for food, values in recommended_meal.items():
#         print(f"{food}: Calories - {values['calories']}, Carbs - {values['carbs_g']}g, Protein - {values['protein_g']}g, Fat - {values['fat_g']}g")


# Recommend a meal based on the user's nutritional goals and health condition
def recommend_meal(user_nutritional_goals, health_condition, nutritional_database):
    # This is a simplified example. In a real system, you'd use a more comprehensive database and rules.
    recommended_meal = {}
    for food, values in nutritional_database.items():
        # Check food suitability for the user's health condition
        if health_condition == 'diabetes':
            if 'high_sugar' in values:
                continue  # Skip high-sugar foods for diabetes
        elif health_condition == 'high_blood_pressure':
            if 'high_sodium' in values:
                continue  # Skip high-sodium foods for high blood pressure
        # Add more condition-specific checks here

        # Check if the food fits within the user's nutritional goals
        if values['calories'] <= user_nutritional_goals['calories']:
            recommended_meal[food] = values

    return recommended_meal

# Create a list of recommended meals for each user
recommended_meals = []

# Process user records and recommend meals for each user
for user_record in user_health_records:
    # Calculate nutritional goals for the user
    user_nutritional_goals = calculate_nutritional_goals(user_record)

    # Recommend a meal based on nutritional goals and the user's health condition
    recommended_meal = recommend_meal(user_nutritional_goals, user_record['health_condition'], nutritional_database)

    recommended_meals.append(recommended_meal)

# Print recommended meals for each user
for i, recommended_meal in enumerate(recommended_meals):
    user_record = user_health_records[i]
    print(f"Recommended Meal for {user_record['name']} with {user_record['health_condition']}:")
    for food, values in recommended_meal.items():
        print(f"{food}: Calories - {values['calories']}, Carbs - {values['carbs_g']}g, Protein - {values['protein_g']}g, Fat - {values['fat_g']}g")
