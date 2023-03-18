Patent Search Engine
====================

### This is a "[CS242] Information Retrival and Web Search" Project

### University of California, Riverside

### Winter 2023

-----------

Description
-----------

This is a patent search engine that uses machine learning models and Elasticsearch to retrieve relevant patent documents based on user queries. The search engine retrieves documents using two methods: semantic search using a BERT-based model and keyword search using Elasticsearch.

Requirements
------------

- Python 3.6 or higher
- Elasticsearch
- Flask
- SentenceTransformers
- Faiss
- Pandas
- Flask-Paginate
- pip (for requirements installation)

Installation
------------

1. Install Python 3.6 or higher on your machine.[optional]
2. Install Elasticsearch by following the instructions in the official documentation: <https://www.elastic.co/guide/en/elasticsearch/reference/current/install-elasticsearch.html>.[optional]
3. Run Elasticsearch by navigating to the Elasticsearch directory and running .\bin\elasticsearch.bat on Windows or ./bin/elasticsearch on Unix/Linux.[optional]
4. Clone this repository using $`git clone https://github.com/AnishmMore/patent_search.git`.
5. Navigate to the cloned repository by running $`cd patent_search` .
6. Install the required Python packages by running $`pip install --ignore-installed -r requirements.txt` OR simply run the `run.sh` script [windows]: $`bash .\run.sh` OR [unix/linux]: $`.\run.sh`.

Usage
-----

1. Run the Python Flask application by running `python3 app.py`.
2. Open a web browser and go to `http://127.0.0.1:8080` to access the search engine.
3. Enter a query in the search box and click "Search" to retrieve relevant patent documents.

License
-------

This project is licensed under the MIT License - see the LICENSE file for details.

Credits
-------

- The machine learning models used in this project were developed by the SentenceTransformers and Faiss libraries.
- The Flask web framework was used to develop the web application.
- The Elasticsearch library was used to index and search patent documents.
- The Flask-Paginate library was used to implement pagination in the search results.

Team Members and Contributors
------

- Akash Bilgi   [netID - abilg003  SID – 862395080 ]
- Kaushik Daiv  [netID - kdaiv001 SID – 862393181 ]
- Mrunali Lachake [netID - mlach008 SID – 862394872 ]
- Amrutha Alewoor [netID - aalew002 SID – 862395063 ]
- Anish More   [netID - amore159 SID – 862324523 ]
