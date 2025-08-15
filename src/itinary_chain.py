from langchain_groq import ChatGroq
from src import config
from langchain_core.prompts import ChatPromptTemplate

llm=ChatGroq(model=config.GROQ_MODEL,api_key=config.QROQ_API_KEY,temperature=0.3)

itinary_prompt=ChatPromptTemplate(
    ("system","You are a helpful travel assistant. Create a day trip itinary for the {city} based of user interest {interests}. Create a brief bullet itinary"),
    ("human","Create a itinary for my day trip")
)

def generate_itinary(city:str, interests:list[str]):
    response=llm.invoke(itinary_prompt.from_template(city=city,interests=', '.join(interests)))
    return response.content
