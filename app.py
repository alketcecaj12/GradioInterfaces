import gradio as gr
import requests

# Function to call the LLM API
def query_llm_api(context, question):
    # Replace 'YOUR_API_ENDPOINT' and 'YOUR_API_KEY' with your actual LLM API endpoint and key
    api_endpoint = "YOUR_API_ENDPOINT"
    headers = {
        "Authorization": f"Bearer YOUR_API_KEY",
        "Content-Type": "application/json"
    }
    payload = {
        "context": context,
        "question": question
    }
    
    # Make the API request
    response = requests.post(api_endpoint, headers=headers, json=payload)
    
    # Check if the request was successful
    if response.status_code == 200:
        return response.json().get("answer", "No answer found.")
    else:
        return f"Error: {response.status_code} - {response.text}"

# Gradio function to process the input
def process_file_and_question(file, question):
    # Read the content of the file
    context = file.read().decode("utf-8")
    
    # Call the LLM API with the context and question
    answer = query_llm_api(context, question)
    
    return answer

# Create the Gradio interface
iface = gr.Interface(
    fn=process_file_and_question,
    inputs=[
        gr.File(label="Upload Text File"),
        gr.Textbox(label="Ask a Question")
    ],
    outputs=gr.Textbox(label="Answer"),
    title="Text File Q&A with LLM",
    description="Upload a text file and ask a question about its content."
)

# Launch the interface
iface.launch()