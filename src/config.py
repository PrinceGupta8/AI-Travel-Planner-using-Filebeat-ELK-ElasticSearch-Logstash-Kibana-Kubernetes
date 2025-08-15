from dotenv import load_dotenv
import os
load_dotenv()

QROQ_API_KEY=os.getenv("QROQ_API_KEY")
GROQ_MODEL="llama-3.3-70b-versatile"