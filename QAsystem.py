import os
from haystack.document_stores import ElasticsearchDocumentStore
from elasticsearch import Elasticsearch
from haystack.utils import launch_es
from haystack.document_stores import ElasticsearchDocumentStore
from haystack import Pipeline
from haystack.nodes import TextConverter, PreProcessor
from haystack.nodes import BM25Retriever
from haystack.nodes import FARMReader
from pprint import pprint
from haystack.utils import print_answers

# Get the host where Elasticsearch is running, default to localhost
host = os.environ.get("ELASTICSEARCH_HOST", "localhost")

document_store = ElasticsearchDocumentStore(
    host=host,
    username="",
    password="",
    index="document"
)

launch_es()

doc_dir = "C:/Users/User/Documents/Study/Degree/Year 3/Sem 1/Natural Language Processing/project/cleaned data"  # Specify the output directory path


indexing_pipeline = Pipeline()
text_converter = TextConverter()
preprocessor = PreProcessor(
    clean_whitespace=True,
    clean_header_footer=True,
    clean_empty_lines=True,
    split_by="word",
    split_length=500,
    split_overlap=20,
    split_respect_sentence_boundary=True,
)

indexing_pipeline.add_node(component=text_converter, name="TextConverter", inputs=["File"])
indexing_pipeline.add_node(component=preprocessor, name="PreProcessor", inputs=["TextConverter"])
indexing_pipeline.add_node(component=document_store, name="DocumentStore", inputs=["PreProcessor"])

files_to_index = [doc_dir + "/" + f for f in os.listdir(doc_dir)]
indexing_pipeline.run_batch(file_paths=files_to_index)

retriever = BM25Retriever(document_store=document_store)

reader = FARMReader(model_name_or_path="C:/Users/User/Documents/Study/Degree/Year 3/Sem 1/Natural Language Processing/project/my_model", use_gpu=True)
querying_pipeline = Pipeline()
querying_pipeline.add_node(component=retriever, name="Retriever", inputs=["Query"])
querying_pipeline.add_node(component=reader, name="Reader", inputs=["Retriever"])


def QAsystem(question):
    
    prediction = querying_pipeline.run(
        query=question,
        params={
            "Retriever": {"top_k": 10},
            "Reader": {"top_k": 1}
        }
    )
    
    answer = prediction['answers'][0].answer
    print(answer)
    
    return answer
