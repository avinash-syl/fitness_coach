import numpy as np
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.preprocessing import LabelEncoder
from models import FitUser, WorkoutPlan

# Load the workout plans data
workout_plans_data = pd.read_csv('workout_plans.csv')

# Load the user data
user_data = pd.read_csv('user_data.csv')

# Convert categorical variables to numerical using LabelEncoder
le = LabelEncoder()

workout_plans_data['goal'] = le.fit_transform(workout_plans_data['goal'])
workout_plans_data['difficulty_level'] = le.fit_transform(workout_plans_data['difficulty_level'])
workout_plans_data['training_part'] = le.fit_transform(workout_plans_data['training_part'])
workout_plans_data['equipment'] = le.fit_transform(workout_plans_data['equipment'])

user_data['gender'] = le.fit_transform(user_data['gender'])
user_data['interest'] = le.fit_transform(user_data['interest'])
user_data['goal'] = le.fit_transform(user_data['goal'])
user_data.fillna(0, inplace=True)

# Merge the workout plans and user data
merged_data = pd.merge(workout_plans_data, user_data, on='goal')

# Drop unnecessary columns
merged_data = merged_data.drop(['plan_name', 'description'], axis=1)

merged_data = np.array(merged_data, type(float))

# Compute cosine similarity matrix
cosine_sim_matrix = cosine_similarity(merged_data)


def generate_recommendations_for_user(user_id):
    # Get user's features
    user_features = user_data.loc[user_data['user_id'] == user_id, 'age':'goal'].values.reshape(1, -1)

    # Compute cosine similarity between user and workout plans
    similarity_scores = cosine_similarity(user_features, merged_data[:, :-6])[0]

    # Sort the similarity scores in descending order
    sorted_scores_indices = similarity_scores.argsort()[::-1]

    # Get the top 3 most similar workout plans
    top_1_indices = sorted_scores_indices[:1]

    # Print the recommendations
    print("Recommendations for user %s:" % user_id)

    for index in top_1_indices:
        print("- %s" % workout_plans_data.iloc[index]['plan_name'])


