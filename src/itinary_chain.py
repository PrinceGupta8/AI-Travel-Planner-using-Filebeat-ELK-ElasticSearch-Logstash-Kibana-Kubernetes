from langchain_groq import ChatGroq
from src import config
from langchain_core.prompts import ChatPromptTemplate

llm = ChatGroq(model=config.GROQ_MODEL, api_key=config.QROQ_API_KEY, temperature=0.3)

def generate_itinary(city, interests):
    prompt = ChatPromptTemplate.from_template(
        "You are a travel planner. Create a detailed itinerary for visiting {city} "
        "based on these interests: {interests}. The itinerary should be for 5 days "
        "and include activities, places to eat, and unique experiences."
    )
    
    messages = prompt.format_messages(city=city, interests=", ".join(interests))
    ai_response = llm.invoke(messages)  # get AI's reply
    
    return ai_response.content  # return plain string
