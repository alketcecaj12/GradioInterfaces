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

# Function to send output to API
def send_output_to_api(output):
    # Replace 'YOUR_PUT_API_ENDPOINT' with your actual API endpoint
    api_endpoint = "YOUR_PUT_API_ENDPOINT"
    headers = {
        "Content-Type": "application/json"
    }
    payload = {
        "output": output
    }
    
    # Make the PUT request
    response = requests.put(api_endpoint, headers=headers, json=payload)
    
    # Check if the request was successful
    if response.status_code == 200:
        return "Output successfully sent to API"
    else:
        return f"Error sending output to API: {response.status_code} - {response.text}"

# Gradio function to process the input
def process_file_and_question(file, question):
    # Read the content of the file
    context = file.read().decode("utf-8")
    
    # Call the LLM API with the context and question
    answer = query_llm_api(context, question)
    
    return answer

# Create the Gradio interface
with gr.Blocks() as iface:
    gr.Markdown("# Text File Q&A with LLM")
    gr.Markdown("Upload a text file and ask a question about its content.")
    
    with gr.Row():
        file_input = gr.File(label="Upload Text File")
        question_input = gr.Textbox(label="Ask a Question")
    
    submit_button = gr.Button("Submit")
    
    output = gr.Textbox(label="Answer")
    
    send_button = gr.Button("Send Output to API")
    api_response = gr.Textbox(label="API Response")
    
    submit_button.click(
        fn=process_file_and_question,
        inputs=[file_input, question_input],
        outputs=output
    )
    
    send_button.click(
        fn=send_output_to_api,
        inputs=output,
        outputs=api_response
    )

# Launch the interface
iface.launch()