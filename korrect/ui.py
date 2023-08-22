import streamlit as st
from urllib.parse import quote, unquote
import pyperclip
from korrect.backend import fact_checking
import os
from korrect.core import BASE_PATH
import json

class KorrectUI():
    def __init__(self):
        self.MODES = ["Fact-checking"]
        self.MODEL_TYPES = [
            "OpenAI Chat", "OpenAI Completion", "Anthropic", 
            "Google PaLM", "LlamaCpp Chat", "LlamaCpp Completion", 
            "HuggingFace Hub"
        ]
        self.OPENAI_CHAT_MODELS = [
            "gpt-3.5-turbo", "gpt-4", "gpt-4-32k"
        ]
        self.OPENAI_COMPLETION_MODELS = [
            "gpt-3.5-turbo", "gpt-4", "gpt-4-32k"
        ]
        self.api_key = None
        self.model_type = None
        self.model = None
        self.mode = None
        self.prompts = []
        self.dfs = []
        self.var_names = []

    def run(self):
        # with open(os.path.join(BASE_PATH, "style.css")) as f:
        #     st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

        st.header("Korrect QA")

        self.mode = st.sidebar.radio("Choose a mode", self.MODES)
        self.handle_mode()

        st.write("Show your support by \U00002B50ing us on [GitHub](https://github.com/kortex-labs/korrect)")

    def handle_mode(self):
        if self.mode == "Fact-checking":
            self.handle_model_selection()
            self.handle_fact_checking_mode_ui()

    def handle_model_selection(self):
        self.model_type = st.sidebar.selectbox("Model Type", self.MODEL_TYPES)
        if self.model_type in {"LlamaCpp Chat", "LlamaCpp Completion"}:
            self.model = st.sidebar.text_input("Local Model Path")
        elif self.model_type == "HuggingFace Hub":
            self.model = st.sidebar.text_input("Repo ID")
            self.api_key = st.sidebar.text_input("HuggingFace Hub API Key")
        elif self.model_type == "Google PaLM":
            self.model = st.sidebar.text_input("Model")
            self.api_key = st.sidebar.text_input("Google PaLM API Key")
        elif self.model_type == "Anthropic":
            self.model = st.sidebar.selectbox("Model", ("claude-2", "claude-instant-1"))
            self.api_key = st.sidebar.text_input("Anthropic API Key")
        elif self.model_type == "OpenAI Chat":
            self.model = st.sidebar.selectbox("Model", self.OPENAI_CHAT_MODELS)
            self.api_key = st.sidebar.text_input("OpenAI API Key", type="password")
        elif self.model_type == "OpenAI Completion":
            self.model = st.sidebar.selectbox("Model", self.OPENAI_COMPLETION_MODELS)
            self.api_key = st.sidebar.text_input("OpenAI API Key", type="password")
        self.serper_key = st.sidebar.text_input("SERPER API Key", type="password")
    
    def _set_env_vars(self):
        if self.model_type == "OpenAI Completion" or self.model_type == "OpenAI Chat":
            os.environ["OPENAI_API_KEY"] = self.api_key
        if self.serper_key:
            os.environ["SERPER_API_KEY"] = self.serper_key

    def handle_fact_checking_mode_ui(self):
        self._set_env_vars()
        prompt_to_check = st.text_area("Enter a prompt:", key="prompt_to_check")
        submit_button = st.button("Submit")

        if submit_button and prompt_to_check:
            # Implement fact-checking logic here
            if "OPENAI_API_KEY" not in os.environ:
                st.warning("Please set the OPENAI_API_KEY first.")
            else:
                _, response, claims, validation = fact_checking(BASE_PATH, prompt_to_check, self.model_type)
                st.subheader("Response:")
                st.markdown(response)

                # CSS to inject contained in a string
                hide_table_row_index = """
                            <style>
                            thead tr th:first-child {display:none}
                            tbody th {display:none}
                            </style>
                            """

                # Inject CSS with Markdown
                st.markdown(hide_table_row_index, unsafe_allow_html=True)

                # Display Claims as a table
                st.subheader("Claims:")
                claims_table = [claim for claim in claims]
                st.table(claims_table)

                # Display Validation as a table
                st.subheader("Validation:")
                validation_table = validation  # assuming validation is a list of dictionaries
                st.table(validation_table)



    def share_button_logic(self, link):
        share_button = st.columns([1])[0]
        with share_button:
            share = st.button("Share")
            if share:
                try:
                    pyperclip.copy(link)
                except pyperclip.PyperclipException:
                    st.write("Please copy the following link:")
                    st.code(link)

if __name__ == "__main__":
    korrect_ui = KorrectUI()
    korrect_ui.run()
