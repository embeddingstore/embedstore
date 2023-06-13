

<div align="center">
  <a href="https://github.com/othneildrew/Best-README-Template">
    <img src="https://i.ibb.co/tP6WX0j/default-2.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">embedstore</h3>

  <p align="center">
    Context retrieval apis to power your LLMs!
    <br />
    <a href="#quick-start"><strong>Get started »</strong></a>
    <br />
    <br />
    <a href="https://playground.embedding.store/podcasts?__theme=light">Play with Embeddings</a>
    ·
    <a href="https://discord.gg/hAnE4e5T6M">Discord</a>
  </p>
</div>


## Quick start
### Installation
`pip install embedstore`

### Get API Key [here](https://api.embedding.store/register)
```python
# Set the API Key
import os
os.environ["EMBEDSTORE_API_KEY"] = <YOUR API KEY> 
```
### Retrieve contexts
In a few lines of code, you can now start retrieving relevant contexts to get better answers from your LLM. We have already embedded Podcast Transcripts and Arxiv Research Papers, with new dataset drops every week ([full list here](#datasets))
```python
from embedstore.rag.retrievers import EmbedStoreRetriever

# Initialize the retriever
arxiv_retriever = EmbedStoreRetriever(dataset_id = "arxiv_01", num_docs=3)

# Query the retriever
contexts = arxiv_retriever.query("What is the state of the art in Autonomous Driving security and safety?")

# Examine the retrieved contexts and then append it to the prompt before you call your LLM
print(contexts[0])
```

Read more [here]() for detailed usage guidelines. 

## What is this?
TBD
<img src="https://i.ibb.co/jgQc4z9/Mindmap.png" alt="Logo">

## Usage
### More about `EmbedStoreRetriever` class
`EmbedStoreRetriever` serves as the single point of entrance to interact with the embedstore.

Parameters to initialize the class :
- `dataset_id (str)` : Dataset to query and retrieve contexts from (eg: `arxiv_01`, `podcasts_01`)
- `num_docs (int)` : Number of contexts to retrieve from the embeddings


### Advanced filtering while querying
You can use `EmbedStoreRetriever.query()` to get contexts based on the user prompt and also perform filtering.

The `query()` function takes two inputs:
- `prompt (str)`: The user prompt that you are querying for 
- `post_processing_config (dict)`: A dictionary of dataset specific filters ([check here](#datasets) for available options)

#### Example : Temporal filter on Arxiv research papers

```python
from embedstore.rag.retrievers import EmbedStoreRetriever

# Initialize the retriever
arxiv_retriever = EmbedStoreRetriever(dataset_id = "arxiv_01", num_docs=3)

# Query the retriever
user_query = "What are some recent papers about CRISPR? Give me a brief summary of major trends."

# Filter to do semantic search on papers published in the last 6 months
post_processing_config = {"filters":{"publish_date_start":"2022-12-01T0:0:0Z"}}

# Calling the `query()` function
contexts = arxiv_retriever.query(user_query,post_processing_config)
```

#### Example : Categorical filter on Podcast Transcripts

```python
# Initialize the retriever
podcast_retriever = EmbedStoreRetriever(dataset_id = "podcasts_01", num_docs=3)

# Query the retriever
user_query = "What are people saying about the new Twitter CEO?"

# Filter to search on Business and Technology podcast episodes
post_processing_config = {"filters":{"category":["Business","Technology"]}}

# Calling the `query()` function
contexts = podcast_retriever.query(user_query,post_processing_config)
```
### Download raw embeddings
You can download raw vector embeddings along with the metadata. 
```python
from embedstore.rag.datadownloaders import download_embeddings

path_to_folder = "" #local path where you want to download the embeddings
download_embeddings('podcasts_01', path_to_folder)
```
`download_embeddings()` downloads the embeddings in `.pkl` format. You can load the file using the following code. The embeddings are stored in a list of tuples `(vector[], metadata{})`

```python
with open(path_to_pickle_file, 'rb') as f:
    import pickle
    data = pickle.load(f)
```

## Datasets

| Dataset             | dataset_id | Description                                                     | Status      | Filters Available                                                                                                                                                                                                                                                                                    | More Details                                                                                                 |
| ------------------- | ----------------------------- | --------------------------------------------------------------- | ----------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------ |
| Podcast Transcripts | podcasts_01                   | 30 most recent podcasts across Finance, Business and Technology | Live        | - `category` : ["Finance","Business","Technology"]                                                                                                                                                                                                                                                 | [Link](https://docs.google.com/spreadsheets/d/1F-MRI7Cqi0YXTsHxbdLEsq_qeXmhSx1qzPoqvW3MOQI/edit?usp=sharing) |
| arXiv               | arxiv_01                      | 2.2M arxiv papers                                               | Live        | - `category` : ['Computer Science', 'Quantitative Biology', 'Economics', 'Quantitative Finance', 'Statistics', 'Electrical Engineering and Systems Science', 'Mathematics', 'Physics']<br><br>- `publish_date_start` : To filter papers published after this date (string in `%Y-%m-%dT%H:%M:%SZ`) | -                                                                                                            |
| Wikipedia                | wikipedia_01                       | -                                                               | Launching Soon |                                                                                                                                                                                                                                                                                                      |       
| News                | news_01                       | -                                                               | Launching Soon |                                                                                                                                                                                                                                                                                                      |                 


## Get involved
We are early, and we want to know how you use this library and what else would you want to make the most out of it.

Join us on our [discord](https://discord.gg/hAnE4e5T6M), or feel free to email us at hello@embedding.store! 
