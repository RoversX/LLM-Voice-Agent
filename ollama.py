import gradio as gr
import requests
import json
import tempfile
import os
from threading import Event

OLLAMA_API_URL = "<OllamaAPI>:11434/api/generate"
GPT_SOVITS_API_URL = "<GPTSOVITSAPI>:9880/"

stop_event = Event()

def ollama_to_gpt_sovits(user_message, history):
    global stop_event
    stop_event.clear()

    # Prepare the prompt with conversation history
    full_prompt = ""
    if history:
        full_prompt += "\nsystem\nYou are an AI assistant."
    for h in history:
        full_prompt += f"\nuser\n{h[0]}\nassistant\n{h[1]}"
    full_prompt += f"\nuser\n{user_message}\nassistant\n"

    try:
        # Step 1: Send user input to Ollama API with streaming
        ollama_response = requests.post(OLLAMA_API_URL, json={
            "model": "closex/neuraldaredevil-8b-abliterated",
            "prompt": full_prompt,
            "stream": True
        }, stream=True)
        ollama_response.raise_for_status()

        ollama_output = ""
        for line in ollama_response.iter_lines():
            if stop_event.is_set():
                break
            if line:
                json_response = json.loads(line)
                chunk = json_response.get("response", "")
                ollama_output += chunk
                history[-1][1] = ollama_output
                yield history, "Generating response...", None, history

        if stop_event.is_set():
            yield history, "Generation stopped", None, history
            return

        # Step 2: Send complete Ollama output to GPT-SoVITS API
        gpt_sovits_response = requests.post(GPT_SOVITS_API_URL, json={
            "text": ollama_output,
            "text_language": "auto"
        })
        gpt_sovits_response.raise_for_status()
        audio_data = gpt_sovits_response.content

        # Step 3: Save audio data to a temporary file
        with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as temp_audio_file:
            temp_audio_file.write(audio_data)
            temp_audio_path = temp_audio_file.name

        # Update conversation history
        history[-1][1] = ollama_output
        yield history, "Audio generated successfully ✅", temp_audio_path, history

    except Exception as e:
        yield history, f"Error: {str(e)}", None, history

def clear_chat_history():
    return [], "", None, []

def stop_generation():
    global stop_event
    stop_event.set()
    return "Generation stopped"

def retry_last_message(history):
    if history:
        last_user_message = history[-1][0]
        history[-1][1] = None  # Clear the previous response
        return last_user_message, history
    return "", history

css = """
@media (min-width: 768px) {
    .chatbox { height: 500px; font-size: 16px; }
}
@media (max-width: 767px) {
    .chatbox { height: 450px; font-size: 16px; }
}
textarea, input { font-size: 16px; }
"""

with gr.Blocks(css=css) as demo:
    gr.Markdown("# Streaming Dialogue with Ollama and GPT-SoVITS")
    gr.Markdown("Enter your query, get a streaming response from Ollama, and generate audio using GPT-SoVITS. The conversation history is maintained for context.")

    with gr.Row():
        with gr.Column(scale=2):
            chatbot = gr.Chatbot(label="Chat History", elem_id="chatbot", height=500)
            msg = gr.Textbox(placeholder="Enter your message...", show_label=False)
            with gr.Row():
                send_btn = gr.Button("Send")
            with gr.Row():
                stop_btn = gr.Button("Stop ✋")
                retry_btn = gr.Button("Retry 🔄")
                clear_btn = gr.Button("Clear Chat 🗑️")
        with gr.Column(scale=1):
            status_text = gr.Textbox(label="Status")
            audio_output = gr.Audio(type="filepath", label="Generated Audio", autoplay=True)

    state = gr.State([])

    def user_message_submission(user_message, history):
        history.append([user_message, None])
        return "", history

    send_btn.click(
        user_message_submission, [msg, state], [msg, chatbot], queue=False
    ).then(
        ollama_to_gpt_sovits, [msg, state], [chatbot, status_text, audio_output, state]
    )

    msg.submit(
        user_message_submission, [msg, state], [msg, chatbot], queue=False
    ).then(
        ollama_to_gpt_sovits, [msg, state], [chatbot, status_text, audio_output, state]
    )

    stop_btn.click(stop_generation, outputs=[status_text])

    retry_btn.click(
        retry_last_message, [state], [msg, chatbot], queue=False
    ).then(
        ollama_to_gpt_sovits, [msg, state], [chatbot, status_text, audio_output, state]
    )

    clear_btn.click(clear_chat_history, outputs=[chatbot, status_text, audio_output, state])

demo.queue()
demo.launch(server_name="0.0.0.0", server_port=7860)
