from llama_index import StorageContext, load_index_from_storage

storage_context = StorageContext.from_defaults(persist_dir="index-spotify")

index = load_index_from_storage(storage_context)
query_engine = index.as_query_engine()
# response = query_engine.query(
#     "When are some other artists i might like based on what i listen to?"
# )
# print(response)

response = query_engine.query(
    "When are artists i listen to?"
)
print(response)
