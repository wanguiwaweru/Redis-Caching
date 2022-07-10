import redis
import requests
import sys

def redis_connect():
    try:
        client = redis.Redis(
            host="localhost",
            port=6379,
            db=0,
        )
        ping = client.ping()
        if ping is True:
            print("connection established")
            return client
    except redis.AuthenticationError:
        print("AuthenticationError")
        sys.exit(1)

def get_data_from_api(url):
    data = requests.get(url).json()
    return data

def set_data_to_cache(data):
    id = data['id']
    title = data['title']
    timeout = 30
    return client.setex(id,title,timeout)

def get_data_from_cache(id):
    title = client.get(id)
    return title

def display_data(id):
    title = get_data_from_cache(id)
    if title is not None:
        return title
    else:
        data = get_data_from_api(url)
        print(data['title'])
        title = data['title']
        return title
    
client = redis_connect()
url = "https://jsonplaceholder.typicode.com/posts/1"
display_data("1")

