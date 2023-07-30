# QuestionAnswer
Answer questions from uploaded PDF's
# Chat with Multiple PDFs - Streamlit Web Application

This is a Streamlit web application that enables users to upload multiple PDF documents, process the text from those documents, create a conversation chain model, and interactively ask questions about the uploaded documents. The application utilizes various libraries, including Streamlit, dotenv, PyPDF2, and the langchain library for natural language processing.

# Features
Upload and process multiple PDF documents simultaneously.
Extract text from the uploaded PDFs and create chunks for efficient processing.
Generate an AI-based conversation chain model for answering user questions.
Interactively ask questions about the uploaded documents and receive model responses.

# Prerequisites
Before running the application, ensure you have the following installed:

Python

Streamlit

PyPDF2

langchain

# How to Run
Clone or download this repository to your local machine.
Install the required dependencies (Streamlit, PyPDF2, langchain) using pip.
Open a terminal or command prompt and navigate to the project's root directory.
Run the Streamlit application with the following command:

streamlit run app.py

The application will open in your default web browser.

# Usage
Upon opening the application, you will see a header "Chat with multiple PDFs" along with an icon of books.
In the sidebar, click on the "Upload your PDFs here and click on 'Process'" section to upload your desired PDF documents. You can upload multiple PDFs at once.
After uploading the PDFs, click on the "Process" button. The application will extract the text from the uploaded PDFs and create a conversation chain model based on the text.
Once the processing is complete, you can ask questions related to the uploaded documents in the text input box below. Type your question and press Enter.
The model will provide responses to your questions based on the information extracted from the PDFs.

# Resetting the Application
If you wish to start over or change the uploaded PDFs, you can click the "Reset" button in the sidebar. This will clear the uploaded PDFs, conversation chain model, and the chat history.

