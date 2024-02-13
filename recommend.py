import numpy as np
import pickle

similarity_score = pickle.load(open('similarity_score.pkl', 'rb'))
pt = pickle.load(open('pt.pkl', 'rb'))
final_ratings_app = pickle.load(open('final_ratings_app.pkl', 'rb'))

def recommend(book_name):
    index = np.where(pt.index == book_name)[0][0]
    similar_items = sorted(list(enumerate(similarity_score[index])), key=lambda x: x[1], reverse=True)[1:6]
    data = []
    for item in similar_items:
        temp_data =-{}
        temp = final_ratings_app[final_ratings_app['Book-Title'] == pt.index[item[0]]]
        temp_data['isbn'] = temp['ISBN'].values[0]