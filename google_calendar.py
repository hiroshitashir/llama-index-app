### Reference https://llamahub.ai/l/google_calendar

from llama_index import GPTVectorStoreIndex, download_loader

GoogleCalendarReader = download_loader('GoogleCalendarReader')

loader = GoogleCalendarReader()
documents = loader.load_data()

index = GPTVectorStoreIndex.from_documents(documents)
query_engine = index.as_query_engine()

response = query_engine.query('What is my schedule today?')
print(response)