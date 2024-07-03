## Streaming Dialogue with Ollama and GPT-SoVITS

### Enter your query, get a streaming response from Ollama, and generate audio using GPT-SoVITS. The conversation history is maintained for context, support markdown.

<img width="1653" alt="Screenshot 2024-07-03 at 4 38 10 PM" src="https://github.com/RoversX/LLM-Voice-Agent/assets/85817538/5494729e-3ab3-4227-81d7-7c4d081a9450">


## Table of Contents

- [Background](#background)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)
- [License](#license)

## Background

This project leverages two key technologies:
1. **[Ollama](https://github.com/ollama/ollama)**: A text generation model that generates responses based on user input and conversation history.
2. **[GPT-SoVITS](https://github.com/RVC-Boss/GPT-SoVITS/)**: A text-to-speech system that converts text into audio in real-time, supporting streaming audio output.

The integration of these technologies allows for an interactive, voice-based dialogue system with streaming audio capabilities.

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/yourrepository.git
   cd yourrepository
   ```

2. **Create a Virtual Environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. **Install Dependencies**:
   ```bash
   pip install requests gradio
   ```
   
## Usage

1. **Run the Application**:
   ```bash
   python ollama.py
   ```

2. **Access the Web Interface**:
   Open your web browser and go to `http://localhost:7860`.

3. **Interacting with the System**:
   - Enter your message in the text box and press "Send".
   - The system will generate a response using Ollama and convert the text to audio using GPT-SoVITS.
   - The generated audio will be played in real-time.

## Configuration

- **OLLAMA_API_URL**: The URL for the Ollama API. 
- **GPT_SOVITS_API_URL**: The URL for the GPT-SoVITS API. 

These can be configured in the `ollama.py` script.

### Logs and Debugging

- **View Logs**:
  The application outputs logs to the console. Check the console for any error messages or debugging information.

- **Enable Debugging**:
  Add logging statements in the code to trace the flow and identify issues. For example, use `print` statements or the `logging` module to log messages.

## Contributing

We welcome contributions! Please fork the repository and submit pull requests. For major changes, please open an issue first to discuss what you would like to change.

### Steps to Contribute

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -am 'Add new feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Create a new Pull Request.

## License

This project is licensed under the MIT License.
