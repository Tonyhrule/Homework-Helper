# Homework Helper :books:

Welcome to Homework Helper! This simple app allows you to ask any homework question and receive help from multiple AI agents. The AI agents collaborate to clarify your question, generate a detailed solution, and review the solution for quality.

## Class Slides: [Link](https://docs.google.com/presentation/d/11xB6sLTHSxSLAH6mMVigutda0oXZgL3TnM_sbh6WYU4/edit?usp=sharing)

This app is made to showcase how students can make a simple Streamlit app demo from Lecture #14 in the [CMU 82-183: AI for Humanities Summer 2024 Course](https://www.cmu.edu/dietrich/lcal/courses/undergraduate-seminars/ai-humanities.html) (I am the invited speaker for this lecture).

## Features

- **Clarification Agent**: Ensures your question is clear and requests additional details if necessary.
- **Solution Agent**: Provides a detailed solution to your homework question.
- **Quality Assurance Agent**: Review the solution for accuracy and suggest improvements.
- **Concise Answer Agent**: Summarizes the solution into a concise answer.

## Installation

### Prerequisites

- Python 3.6 or higher
- Pip (Python package installer)

### Steps

1. **Clone the repository**:

    ```bash
    git clone https://github.com/yourusername/homework-helper.git
    cd homework-helper
    ```

2. **Create a virtual environment** (optional but recommended):

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required packages**:

    ```bash
    pip install -r requirements.txt
    ```

4. **Create a `.env` file** in the project directory and add your OpenAI API key:

    ```plaintext
    OPENAI_API_KEY=your_openai_api_key
    ```

## Usage

1. **Run the Streamlit app**:

    ```bash
    streamlit run streamlit_app.py
    ```

2. **Open your web browser** and navigate to the URL provided by Streamlit (usually `http://localhost:8501`).

3. **Enter your homework question** in the text area and press "Get Help" to see the answers.

## Project Structure

```plaintext
homework-helper/
│
├── .env                # Environment variables
├── requirements.txt    # List of required Python packages
├── agents.py           # AI agent functions
└── streamlit_app.py    # Streamlit app script
```

## License
This project is licensed under the MIT License. See the [LICENSE](https://github.com/Tonyhrule/Simple-Homework-Helper/blob/main/LICENSE) file for details.
