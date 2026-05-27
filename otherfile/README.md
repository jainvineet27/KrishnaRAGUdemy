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


PDF → Text → Chunks → Embeddings → Vector Store → ANN Index → Query → Cosine Similarity → Top‑K Chunks → LLM Answer


| Component | Purpose | Input | Output | Internal Mechanism | When It Runs |
| --- | --- | --- | --- | --- | --- |
| **Chunking** | Break text into small pieces | Raw text | List of chunks | Recursive splitting | After PDF load |
| **Embeddings** | Convert text → vector | Chunk text | Vector (float list) | Transformer model | Before storing |
| **Vector Store** | Store vectors + metadata | Vectors | Indexed DB | ANN index | After embeddings |
| **Cosine Similarity** | Compare query vs chunks | Query vector | Similarity score | Dot product math | During search |
| **ANN Search** | Fast retrieval | Query vector | Top‑K chunks | HNSW / IVF | During query |
| **LLM** | Generate answer | Query + chunks | Final answer | Attention mechanism | Last step |


🧭 11. End‑to‑End Flow (Simple)
Load PDF
Extract text
Split into chunks
Generate embeddings
Store in vector DB
Build ANN index
User asks question
Query embedding generated
ANN search finds top chunks
LLM uses chunks to answer

| Concept | Meaning |
| --- | --- |
| Sentence | Too small, no context |
| Chunk | Big enough to capture meaning |
| Embedding | Vector of chunk meaning |
| Cosine similarity | Query vs chunk match |
| Retrieval | Top chunks return |


| Model kitna information compress karega | 
| vector kitna detailed hoga | 
speed vs accuracy ka balance kya hoga | 
384 dimensions ka matlab: | 
Model har sentence ko 384 numbers me compress karta hai. | 
Ye numbers sentence ke meaning ko represent karte hain.  | 


"He is a cat" → [0.11, -0.22, 0.33, ...]  (384 numbers)

| Concept | Meaning |
| --- | --- |
| **384 dimensions** | Model ka fixed vector size |
| **1 sentence → 1 embedding** | Always one vector |
| **Chunk ≠ sentence** | Chunk = multiple sentences |
| **Chunking needed** | Better meaning, better retrieval |
| **384 chosen** | Speed + accuracy ka perfect balance |