from llama_index import GPTVectorStoreIndex
from llama_hub.youtube_transcript import YoutubeTranscriptReader

loader = YoutubeTranscriptReader()
documents = loader.load_data(ytlinks=['https://www.youtube.com/watch?v=i3OYlaoj-BM'])

index = GPTVectorStoreIndex.from_documents(documents)
query_engine = index.as_query_engine()

response = query_engine.query('Did he talk about OpenAI?')
print(response)