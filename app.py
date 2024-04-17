import streamlit as st
from transformers import pipeline

# Initialize the pipeline for text-generation with the GPT-2 model
generator = pipeline('text-generation', model='gpt2')

# Set the title of the app
st.title('My Hugging Face Chatbot')

# User input text box
user_input = st.text_input("Say something to the chatbot:")

# Function to process the model response
def process_response(input_text, generated_text):
    # Add conversational context to the prompt
    prompt = f"Human: {input_text}\nAI:"
    
    # Check if the prompt is in the generated text and remove it
    if prompt in generated_text:
        return generated_text.replace(prompt, '').strip()
    
    # Remove only the exact user input if found at the start
    if generated_text.startswith(input_text):
        return generated_text[len(input_text):].strip()
    
    # Return the original generated text if no repetition is found
    return generated_text

# Generate and process the response when there is user input
if user_input:
    # We increase max_length to have more content to work with
    raw_response = generator(user_input, max_length=100, Truncation = True)[0]['generated_text']
    response = process_response(user_input, raw_response)
    
    # Display the processed response
    st.text(response)
