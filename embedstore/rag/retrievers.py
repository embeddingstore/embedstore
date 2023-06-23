from embedstore.helpers.api import call_embed_store
from embedstore.helpers.exceptions import InvalidInput


class EmbedStoreRetriever:
    """
    Base class for retreiver
    """
    def _validate_dataset_id(self,dataset_id):
        available_dataset_id = ['podcasts_01','arxiv_01','wikipedia_01']
        if dataset_id not in available_dataset_id:
            raise InvalidInput(f'Invalid dataset_id : Has to be one of the following - {available_dataset_id}')
    
    def __init__(self, dataset_id, num_docs, retrieving_method="similarity_score") -> None:
        """Init params."""
        self._validate_dataset_id(dataset_id)
        self.dataset_id = dataset_id
        self.num_docs = num_docs
        self.retrieving_method = retrieving_method
    
    
        
    def query(self,prompt,post_processing_config={}) -> list:
        """Get contexts based on given prompt and post processing config"""
                
        request_params = {
            "dataset_id":self.dataset_id,
            "filters":post_processing_config.get("filters",{}),
            "num_docs": self.num_docs
        }
        
        embed_store_response = call_embed_store(prompt,request_params)
        
        if embed_store_response.get('success'):
            contexts = embed_store_response.get('contexts')
            return contexts
        