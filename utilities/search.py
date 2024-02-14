import pickle
import os
final_ratings_app = pickle.load(open(os.path.join(os.getcwd(), 'data', 'similarity_score.pkl'), 'rb'))

def search(search_term):
  mask = final_ratings_app.apply(lambda col: col.astype(str).str.contains(search_term, case=False, regex=True)).any(axis=1)
  return final_ratings_app.loc[mask]