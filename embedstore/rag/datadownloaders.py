from embedstore.helpers.api import download_embed_store
from embedstore.helpers.exceptions import InvalidInput,ServerError


def _validate_dataset_id(dataset_id):
        available_dataset_id = ['podcasts_01','arxiv_01']
        if dataset_id not in available_dataset_id:
            raise InvalidInput(f'Invalid dataset_id : Has to be one of the following - {available_dataset_id}')

def download_embeddings(dataset_id,path):
    import urllib.request
    import os
    _validate_dataset_id(dataset_id)
    if os.path.exists(path):         
        download_obj = download_embed_store(dataset_id)
        if download_obj.get('success'):
            url = download_obj.get('url')
            try:
                print('Downloading embeddings...')
                final_file = os.path.join(path,dataset_id+'.pkl')
                urllib.request.urlretrieve("https://embedstore-downloads.s3.amazonaws.com/podcasts_01/embeddings_1.pkl",final_file)
                print('Download successful...')
            except Exception as e:
                raise ServerError(f'Cannot download {dataset_id}  - {str(e)}')
                
    else:
        raise InvalidInput(f"Check {path}, it does not exist")