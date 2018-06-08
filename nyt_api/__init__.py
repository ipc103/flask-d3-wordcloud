import requests
import json
import re
from collections import defaultdict
import nltk
nltk.download('stopwords')
nltk.download('punkt')
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

import os
NYT_API_KEY = os.getenv('NYT_API_KEY')

URL = 'https://api.nytimes.com/svc/topstories/v2/home.json'


def most_popular_topics():
    data = fetch()
    topic_frequencies = defaultdict(lambda: 0)
    stop_words = set(stopwords.words('english'))
    for result in data["results"]:
        headline = result["title"]
        tokens = word_tokenize(headline)
        words = [token for token in tokens if token.isalpha() and token.lower() not in stop_words]
        for word in words:
            topic_frequencies[word] += 1
    most_popular_topics = []
    for topic, frequency in topic_frequencies.items():
        most_popular_topics.append({"text": topic, "size": frequency * 20})
    return most_popular_topics


def fetch():
    headers = {'api-key': NYT_API_KEY}
    response = requests.get(URL, headers=headers)
    data = json.loads( response.text )
    return data
