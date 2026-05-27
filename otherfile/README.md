pip install uv 

uv venv rag
source rag/Scripts/activate
uv add -r requirements.txt

| Step                   | Kya hota hai |
| --- |                   --- |
| Chunking              | PDF ko small pieces me todna |
 Embedding              Har chunk ko vector me convert karna 
 Vector Store           Vectors + metadata store karna    
 Index                  Fast search structure    
 Query                  Query vector banta hai   
 Cosine Similarity      Query vector vs chunk vectors    
 Retrieval              Top 3–5 best chunks  
 LLM                    Answer generate karta hai  