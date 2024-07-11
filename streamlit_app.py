import streamlit as st
from agents import clarification_agent, solution_agent, quality_assurance_agent, concise_answer_agent

def main():
    st.set_page_config(page_title="Homework Helper", page_icon=":books:", layout="wide")

    # Custom CSS to style the app
    st.markdown("""
        <style>
            .main {
                background-color: #f0f2f6;
                padding: 20px;
                border-radius: 10px;
            }
            .stButton>button {
                background-color: #4CAF50;
                color: white;
                border-radius: 12px;
                padding: 10px 20px;
                margin: 10px 0;
                font-size: 16px;
            }
            .stTextArea textarea {
                border-radius: 10px;
                border: 1px solid #d1d9e6;
            }
            .stAlert {
                background-color: #fff;
                border-radius: 10px;
                padding: 20px;
                margin-bottom: 20px;
                box-shadow: 0 4px 6px rgba(0,0,0,0.1);
            }
            .stAlert>div {
                font-size: 16px;
            }
            .stExpander {
                background-color: #fff;
                border-radius: 10px;
                padding: 20px;
                margin-top: 20px;
                box-shadow: 0 4px 6px rgba(0,0,0,0.1);
            }
            .stExpander>div>div {
                font-size: 16px;
            }
        </style>
    """, unsafe_allow_html=True)

    # Title and description
    st.title("Homework Helper :books:")
    st.write("""
        Welcome to the Homework Helper! Ask any homework question and get help from multiple AI agents.
        Enter your question in the text box below and press "Get Help" to see the answers.
    """)

    # Input section
    st.header("Enter Your Homework Question")
    question = st.text_area("Type your question here:", height=150)

    if st.button("Get Help"):
        if question.strip():
            # Clarification agent
            with st.spinner("Checking clarity of the question..."):
                clarification = clarification_agent(question)
            
            if "need more details" in clarification.lower():
                st.error("Clarification needed. Please provide more details for the question.")
                st.info(clarification)
            else:
                # Solution agent
                with st.spinner("Generating solution..."):
                    solution = solution_agent(question)

                # Quality assurance agent
                with st.spinner("Reviewing solution for quality..."):
                    review = quality_assurance_agent(solution)

                # Concise answer agent
                with st.spinner("Generating concise answer..."):
                    concise_answer = concise_answer_agent(solution)

                # Display results
                st.header("Results")
                st.subheader("Concise Answer")
                st.success(concise_answer)
                
                st.subheader("Detailed Solution")
                st.info(solution)

                # Add expanders for detailed agent responses
                st.header("Agent Reasoning")
                with st.expander("Clarification Agent Response"):
                    st.write(clarification)

                with st.expander("Solution Agent Response"):
                    st.write(solution)

                with st.expander("Quality Assurance Agent Response"):
                    st.write(review)
        else:
            st.warning("Please enter a question.")

if __name__ == "__main__":
    main()
