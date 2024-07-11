import openai
import streamlit as st

# Load API key from Streamlit secrets
openai.api_key = st.secrets["OPENAI_API_KEY"]

def clarification_agent(question):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": f"A student asked: '{question}'\n\nIs the question clear? If not, ask for more details:"}
        ]
    )
    return response.choices[0].message['content'].strip()

def solution_agent(question):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": f"Provide a detailed solution to the following homework question:\n\n{question}\n\nSolution:"}
        ]
    )
    return response.choices[0].message['content'].strip()

def quality_assurance_agent(solution):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": f"Review the following solution for accuracy and completeness. Suggest improvements if necessary:\n\n{solution}\n\nReview:"}
        ]
    )
    return response.choices[0].message['content'].strip()

def concise_answer_agent(solution):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": f"Provide a concise summary of the following detailed solution:\n\n{solution}\n\nConcise Summary:"}
        ]
    )
    return response.choices[0].message['content'].strip()
