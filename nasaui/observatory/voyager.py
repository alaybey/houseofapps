import requests
APOD_URL = "https://api.nasa.gov/planetary/apod"
SEARCH_URL = "https://images-api.nasa.gov/search"
payload = {'api_key': 'dMBh2zkf3tnBLcA1684JvbhafhH2bMcbQ1L9pbMI'}



def get_apod():
    r = requests.get(APOD_URL, params = payload)
    return r.json()
#print(r.json()['title'])

def search_images(keyword):
    payload_search = {'q': keyword}
    r = requests.get(SEARCH_URL, params= payload_search )
    return r.json()
def search_next_page(url):
    r = requests.get(url)
    return r.json()