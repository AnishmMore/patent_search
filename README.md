Patent Search Engine
====================

Description
-----------

This is a patent search engine that uses machine learning models and Elasticsearch to retrieve relevant patent documents based on user queries.

Requirements
------------

-   Python 3.6 or higher
-   Elasticsearch
-   Flask
-   SentenceTransformers
-   Faiss
-   Pandas
-   Flask-Paginate

Installation
------------

1.  Install Python 3.6 or higher on your machine.
2.  Install Elasticsearch by following the instructions in the official documentation: <https://www.elastic.co/guide/en/elasticsearch/reference/current/install-elasticsearch.html>.
3.  Clone this repository using `git clone https://github.com/username/repo.git`.
4.  Navigate to the cloned repository by running `cd repo`.
5.  Install the required Python packages by running `pip install -r requirements.txt`.

Usage
-----

1.  Start Elasticsearch by running `./bin/elasticsearch` in your Elasticsearch installation directory.
2.  Run the Python Flask application by running `python app.py`.
3.  Open a web browser and go to `http://localhost:5000` to access the search engine.
4.  Enter a query in the search box and click "Search" to retrieve relevant patent documents.

License
-------

This project is licensed under the MIT License - see the LICENSE file for details.

Credits
-------

-   The machine learning models used in this project were developed by the SentenceTransformers and Faiss libraries.
-   The Flask web framework was used to develop the web application.
-   The Elasticsearch library was used to index and search patent documents.
-   The Flask-Paginate library was used to implement pagination in the search results.