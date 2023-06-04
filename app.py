import streamlit as st


def main():
    st.set_page_config(page_title="Chat with the PDFs" , page_icon = ":books:")
    st.header("Chat with the PDFs :books:")
    st.text_input("Ask a qustion about your documents: ")

    with st.sidebar:
        st.subheader("Your Docs")
        st.file_uploader("Upload your PDFs Here and click on process")
        st.button("Process")

if __name__ == "__main__":
    main()