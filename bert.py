from sentence_transformers import SentenceTransformer
import pickle
import faiss
from flask import Flask, render_template,request
import numpy as np
import pandas as pd

model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')

df=pd.read_csv('indexed/indexed.csv')

with open('indexed/faiss_indexed_updated.pickle', 'rb') as f:
    index = pickle.load(f)

index = faiss.deserialize_index(index)

def indx(df, I):
    I=I.flatten().tolist()
    return [df.loc[df.numeric_value == idx].to_dict(orient='records') for idx in I]

def s_v(query, model, index, num_results=10):
  vector = model.encode(list(query))
  D, I = index.search(np.array(vector).astype("float32"), k=num_results)
  return D, I