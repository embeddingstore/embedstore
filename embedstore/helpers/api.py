## All functions to call external APIs (Embed store, OpenAI)
import os
from embedstore.helpers.exceptions import APIKeyError, ServerError

def get_embed_store_apikey():
    EMBEDSTORE_API_KEY = os.getenv("EMBEDSTORE_API_KEY")
    if EMBEDSTORE_API_KEY is not None:
        return EMBEDSTORE_API_KEY
    else:
        raise APIKeyError("Couldn't find EMBEDSTORE_API_KEY in env")

def call_embed_store(prompt,dataset_params):
    import requests
    EMBEDSTORE_API_KEY = get_embed_store_apikey()
    url = 'https://api.embedding.store/retrieve'
    headers = {'API-Key': EMBEDSTORE_API_KEY}
    
    payload = {"query": prompt,"dataset_params": dataset_params}
    
    response = requests.post(url, headers=headers, json=payload)
    
    # Parsing the response and handling errors
    if response.status_code == 200:
        response_json = response.json()
        if response_json['success'] == 'true':
            return {'success':True, 'contexts':response_json.get('contexts')}
        else:
            raise ServerError(f'Server error : {response_json["error"]}. If this persists, please create an issue here - https://github.com/embeddingstore/embedstore/issues')        
    elif response.status_code == 400:
        raise ServerError(f'Server error 400 for -- {url}')        
    elif response.status_code == 401:
        raise APIKeyError(f'Invalid API Key, please contact us at hello@embedding.store.')
    else:
        raise ServerError(f'Server error : {response.status_code}')        
    
    

def download_embed_store(dataset_id):
    import requests
    EMBEDSTORE_API_KEY = get_embed_store_apikey()
    url = 'https://api.embedding.store/download_embeddings'
    headers = {'API-Key': EMBEDSTORE_API_KEY}
    
    payload = {"dataset_id": dataset_id}
    
    response = requests.post(url, headers=headers, json=payload)
    
    # Parsing the response and handling errors
    if response.status_code == 200:
        response_json = response.json()
        if response_json['success'] == 'true':
            return {'success':True, 'url':response_json.get('url')}
        else:
            raise ServerError(f'Server error : {response_json["error"]}. If this persists, please create an issue here - ')        
    elif response.status_code == 400:
        raise ServerError(f'Server error 400 for -- {url}')        
    elif response.status_code == 401:
        raise APIKeyError(f'Invalid API Key, please contact us at hello@embedding.store.')
    else:
        raise ServerError(f'Server error : {response.status_code}')      