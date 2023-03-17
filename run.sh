#!/bin/bash

# Check if dependencies are already installed
if python3 -c "import sentence_transformers, faiss, Flask, pandas, elasticsearch, flask_paginate, transformers; from bert import *; bert_client = BertClient();":
then
    # Dependencies are already installed
    echo "All dependencies are already installed."
else
    # Dependencies are not installed, so install them
    echo "Installing dependencies..."
    pip install sentence-transformers==1.0.4
    pip install faiss-cpu==1.7.0
    pip install Flask==2.1.2
    pip install pandas==1.3.3
    pip install elasticsearch==7.14.1
    pip install flask-paginate==0.9.0
    pip install transformers==4.11.3

    # Download pre-trained BERT model
    python3 -c "from bert import *; bert_client = BertClient();"

    echo "Dependencies installed."
fi

# Run app
python3 app.py
