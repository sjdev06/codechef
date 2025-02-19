# Step 1: Install required libraries
# Run this in your terminal
# pip install langchain ollama fastapi uvicorn

# --- main.py ---
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from langchain_ollama import OllamaLLM
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
from langchain.prompts import PromptTemplate

# Initialize FastAPI app
app = FastAPI()

# Initialize Ollama with a model
llm = OllamaLLM(model="mistral")

# Setup conversation memory
memory = ConversationBufferMemory()

# Define prompt template for Langchain
prompt = PromptTemplate(
    input_variables=["history", "input"],
    template="You are a helpful chatbot. {history}\nUser: {input}\nChatbot:"
)

# Initialize conversation chain
chat_chain = ConversationChain(llm=llm, memory=memory, prompt=prompt)

# Define request and response models
class ChatRequest(BaseModel):
    user_input: str

class ChatResponse(BaseModel):
    response: str

# API endpoint to receive and respond to user input
@app.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):
    try:
        response = chat_chain.run(request.user_input)
        return ChatResponse(response=response)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# To run: uvicorn main:app --reload

# Now you have a FastAPI endpoint for your chatbot using Langchain and Ollama!
# Deploy on local machine or cloud with ease.
