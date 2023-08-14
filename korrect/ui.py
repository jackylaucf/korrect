import streamlit as st
import random

class KorrectUI:
    def __init__(self):
        self.random_number = None

    def run(self):
        st.title("Korrect")
        
        if st.button("Generate Random Number"):
            self.random_number = random.randint(1, 100)
        
        if self.random_number is not None:
            st.write(f"Generated Random Number: {self.random_number}")

if __name__ == "__main__":
    KorrectUI().run()