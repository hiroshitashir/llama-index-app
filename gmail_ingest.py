from llama_index import download_loader

GmailReader = download_loader('GmailReader')
loader = GmailReader(query="from:me after:2023-01-01", service=None, results_per_page=10)
documents = loader.load_data()

# 2. Parse the docs into nodes
from llama_index.node_parser import SimpleNodeParser

parser = SimpleNodeParser.from_defaults()
nodes = parser.get_nodes_from_documents(documents)

# 3. Build an index
from llama_index import GPTVectorStoreIndex
index = GPTVectorStoreIndex(nodes)

# 4. Store the index
index.storage_context.persist(persist_dir="index-gmail")