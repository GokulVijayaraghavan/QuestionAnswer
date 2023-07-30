# Import necessary libraries
import streamlit as st
from dotenv import load_dotenv
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain

# Function to extract text from PDF documents
def get_pdf_text(pdf_docs):
    text = ""
    for pdf in pdf_docs:
        pdf_reader = PdfReader(pdf)
        for page in pdf_reader.pages:
            text += page.extract_text()
    return text

# Function to split text into chunks for efficient processing
def get_text_chunks(text):
    text_splitter = CharacterTextSplitter(
        separator="\n",
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len
    )
    chunks = text_splitter.split_text(text)
    return chunks

# Function to create a vector store for the text chunks
def get_vectorstore(text_chunks):
    embeddings = OpenAIEmbeddings()
    vectorstore = FAISS.from_texts(texts=text_chunks, embedding=embeddings)
    return vectorstore

# Function to create a conversation chain model
def get_conversation_chain(vectorstore):
    language_model = ChatOpenAI()
    memory = ConversationBufferMemory(memory_key='chat_history', return_messages=True)
    conversation_chain = ConversationalRetrievalChain.from_llm(
        llm=language_model,
        retriever=vectorstore.as_retriever(),
        memory=memory
    )
    return conversation_chain

# Function to handle user input and get model responses
def handle_user_input(user_question):
    response = st.session_state.conversation({'question': user_question})
    st.session_state.chat_history = response['chat_history']
    message = response['chat_history'][-1]
    message.content

# Function to reset session state
def reset_session_state():
    st.session_state.conversation = None
    st.session_state.chat_history = None
    st.session_state.pdf_text = ""

# Main function to run the Streamlit web application
def main():
    load_dotenv()
    st.set_page_config(page_title="Chat with multiple PDFs", page_icon=":books:")

    # Check if conversation and chat history are present in session state
    if "conversation" not in st.session_state:
        st.session_state.conversation = None
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = None

    st.header("Answering the questions from PDF")

    # Check if PDFs have been uploaded
    files_uploaded = "pdf_text" in st.session_state and st.session_state.pdf_text != ""

    # Sidebar section to upload PDFs and process them
    with st.sidebar:
        # Check if the user has uploaded PDF documents or not
        pdf_docs = st.file_uploader(
            "Upload your documents here",
            accept_multiple_files=True,
            type=["pdf"]
        )
        st.subheader("Your documents")

        # Disable the Process button if no files are uploaded
        process_button_disabled = (pdf_docs == [])

        if st.button("Process", disabled=process_button_disabled):
            with st.spinner("Processing"):
                # Get pdf text
                raw_text = get_pdf_text(pdf_docs)
                st.session_state.pdf_text = raw_text

                # Get the text chunks
                text_chunks = get_text_chunks(raw_text)

                # Create vector store
                vectorstore = get_vectorstore(text_chunks)

                # Create conversation chain
                st.session_state.conversation = get_conversation_chain(vectorstore)

        if st.button("Reset"):
            reset_session_state()

    # Main section for user interaction and displaying model responses
    if files_uploaded:
        user_question = st.text_input("Ask questions about your documents:")
        if user_question:
            handle_user_input(user_question)

if __name__ == '__main__':
    main()
