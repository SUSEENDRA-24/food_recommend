import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer

# Sample health, food, and nutritional data
data = {
    'User_ID': [1, 2, 3],
    'Health_Record': ['Diabetic', 'Heart Disease', 'Allergies'],
    'Foods': ['Salad', 'Salmon', 'Oatmeal'],
}

nutritional_data = {
    'Foods': ['Salad', 'Salmon', 'Oatmeal'],
    'Calories': [100, 200, 150],
    'Protein (g)': [3, 20, 5],
    'Carbs (g)': [10, 0, 30],
    'Fat (g)': [6, 10, 2],
}

# Create DataFrames for health and food data
df = pd.DataFrame(data)
nutritional_df = pd.DataFrame(nutritional_data)

# Merge the health and nutritional DataFrames on the 'Foods' column
df = pd.merge(df, nutritional_df, on='Foods', how='inner')

# Create a TF-IDF vectorizer
tfidf_vectorizer = TfidfVectorizer()

# Fit and transform the health records
health_matrix = tfidf_vectorizer.fit_transform(df['Health_Record'])

# Calculate the cosine similarity between health records
cosine_sim = cosine_similarity(health_matrix, health_matrix)

# Function to get food recommendations for an individual user
def get_recommendations(user_id, cosine_sim=cosine_sim):
    user_health = df.loc[df['User_ID'] == user_id, 'Health_Record'].values[0]

    sim_scores = list(enumerate(cosine_sim[user_id - 1]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:4]  # Get the top 3 similar users

    food_indices = [i[0] for i in sim_scores]
    
    recommendations = df.loc[df.index.isin(food_indices), ['Foods', 'Calories', 'Protein (g)', 'Carbs (g)', 'Fat (g)']]

    return recommendations

# Example usage: Get food recommendations for User 2
user_id = 3
recommendations = get_recommendations(user_id)
print(recommendations)
