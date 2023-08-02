# chat-assistant

A question-answering chatbot powered by Langchain and OpenAI's GPT-3.5, designed to provide answers based on a collection of documents.

## Overview

This chatbot leverages Langchain's text processing capabilities and OpenAI's GPT-3.5 model to provide answers to user queries. It utilizes Pinecone for efficient vector storage and retrieval.

## Features

- Retrieve answers from a collection of documents using OpenAI's GPT-3.5 model.
- Efficiently store and retrieve document vectors using Pinecone.
- Seamless integration with Langchain's components for text processing.

## Setup

1. Clone this repository:

   ```bash
   git clone https://github.com/your-username/your-chatbot-repo.git
   cd your-chatbot-repo
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Configure your environment variables:

   Create a `.env` file in the root directory and add the following:

   ```plaintext
   OPENAI_API_KEY=your_openai_api_key
   Pinecone_API_Key=your_pinecone_api_key
   Pinecone_Environment=your_pinecone_environment
   ```

4. Load your documents:

   Modify the `directory` variable in `main.py` to point to your document directory.

5. Run the chatbot:

   ```bash
   python main.py
   ```

## Usage

1. Run the chatbot by following the setup instructions.
2. Enter your query when prompted.
3. The chatbot will provide an answer based on the documents and GPT-3.5 model.

## Contributing

Contributions are welcome! If you encounter any issues or have suggestions, please open an issue or submit a pull request.

---

Feel free to customize this template to match your chatbot's specific details and functionalities. Make sure to provide clear and concise instructions for setting up and using your chatbot. Good luck with your project!