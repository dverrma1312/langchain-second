from langchain_openai import OpenAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder


chat_template = ChatPromptTemplate([
    ('system','You are a helpful customer support agent'),
    MessagesPlaceholder(variable_name='chat_history'),
    ('human','{query}')
])

chat_history = []

with open('chat_history') as f:
    chat_history.extend(f.readlines())
    
result = chat_template.invoke({'chat_history': chat_history, 'human':'how are you doing'})

