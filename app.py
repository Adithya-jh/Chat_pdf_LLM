import streamlit as st

from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import HuggingFaceInstructEmbeddings
from langchain.vectorstores import FAISS


def get_pdf_text(pdf_docs):
    text = ""
    for pdf in pdf_docs:
        reader = PdfReader(pdf)
        for page in reader.pages:
            text += page.extract_text()
    return text

def get_text_chunks(raw_text):
    splitter = CharacterTextSplitter(separator='\n', chunk_size=1000 , chunk_overlap = 200, length_function = len)
    text_chunks = splitter.split_text(raw_text)
    return text_chunks


def get_vectors_store(text_chunks):
    embeddings = HuggingFaceInstructEmbeddings(model_name="hkunlp/instructor-xl")
    vectorstore = FAISS.from_texts(texts = text_chunks , embeddings = embeddings)
    return vectorstore

def main():
    # load_dotenv()
    st.set_page_config(page_title="Chat with the PDFs" , page_icon = ":books:")
    st.header("Chat with the PDFs :books:")
    st.text_input("Ask a qustion about your document: ")

    with st.sidebar:
        st.subheader("Your Docs")
        pdf_docs = st.file_uploader("Upload your PDFs Here and click on process",accept_multiple_files=True)
        if st.button("Process"):
            with st.spinner("Processing"):
                # get pdf texts
                raw_text = get_pdf_text(pdf_docs)
               
                # get the text chunks
                text_chunks = get_text_chunks(raw_text)
                # st.write(text_chunks)

                # create a vctor store
                vectors_store = get_vectors_store(text_chunks)


if __name__ == "__main__":
    main()