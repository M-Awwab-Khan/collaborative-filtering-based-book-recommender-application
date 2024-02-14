import numpy as np
import pickle
import os

similarity_score = pickle.load(open(os.path.join(os.getcwd(), 'data', 'similarity_score.pkl'), 'rb'))
pt = pickle.load(open(os.path.join(os.getcwd(), 'data', 'pt.pkl'), 'rb'))
final_ratings_app = pickle.load(open(os.path.join(os.getcwd(), 'data', 'final_ratings_app.pkl'), 'rb'))

def recommend(book_name):
    index = np.where(pt.index == book_name)[0][0]
    similar_items = sorted(list(enumerate(similarity_score[index])), key=lambda x: x[1], reverse=True)[1:6]
    data = []
    for item in similar_items:
        temp = final_ratings_app[final_ratings_app['Book-Title'] == pt.index[item[0]]]
        temp_data = {}
        temp_data['isbn'] = temp['ISBN'].values[0]
        temp_data['title'] = temp['Book-Title'].values[0]
        temp_data['author'] = temp['Book-Author'].values[0]
        temp_data['yop'] = temp['Year-Of-Publication'].values[0]
        temp_data['num_ratings'] = temp['num_ratings'].values[0]
        temp_data['avg_rating'] = temp['avg_rating'].values[0]
        data.append(temp_data)
    return data