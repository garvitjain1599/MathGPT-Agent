# 🧮 MathGPT Agent

MathGPT Agent is an AI-powered mathematical reasoning assistant built using **Streamlit**, **LangChain**, and **Groq LLMs**. The application follows a modern **Agent Architecture**, enabling the model to intelligently decide when to use specialized tools such as a calculator, Wikipedia search, and reasoning helper to solve user queries.

## Features

* Agent-based architecture using LangChain
* Mathematical calculations using a dedicated calculator tool
* Wikipedia integration for factual knowledge retrieval
* Multi-step reasoning support
* Interactive chat interface built with Streamlit
* Powered by Groq's high-speed inference engine
* Modern LangChain implementation without deprecated APIs

## Architecture

```text
User
  │
  ▼
MathGPT Agent
  │
  ├── Calculator Tool
  │      └── Evaluates mathematical expressions
  │
  ├── Wikipedia Search Tool
  │      └── Retrieves factual information
  │
  └── Reasoning Helper Tool
         └── Guides multi-step problem solving
  │
  ▼
Final Response
```

The agent analyzes the user's query, determines whether external tools are required, invokes the appropriate tool(s), and generates a final response.

## Tech Stack

* Python
* Streamlit
* LangChain
* Groq
* Wikipedia API
* NumExpr

## Installation

### Clone the Repository

```bash
git clone https://github.com/your-username/mathgpt-agent.git
cd mathgpt-agent
```

### Create and Activate a Virtual Environment

```bash
conda create -n mathgpt python=3.11
conda activate mathgpt
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

Or install manually:

```bash
pip install streamlit langchain langchain-groq langchain-community wikipedia numexpr
```

## Configuration

Generate a Groq API key from:

https://console.groq.com/keys

Enter the API key in the Streamlit sidebar when launching the application.

## Running the Application

```bash
streamlit run math_llm_agent.py
```

The application will be available at:

```text
http://localhost:8501
```

## Example Queries

### Mathematical Problems

```text
What is 25 × 18?
```

```text
Solve (125 + 75) / 4
```

```text
A train travels 60 km/h for 3 hours. How far does it travel?
```

### Reasoning Problems

```text
I have 5 bananas and 7 grapes. I eat 2 bananas and give away 3 grapes. Then I buy a dozen apples and 2 packs of blueberries containing 25 berries each. How many total pieces of fruit do I have?
```

### Knowledge Questions

```text
Who invented calculus?
```

```text
What is the capital of Japan?
```

## Project Structure

```text
mathgpt-agent/
│
├── app.py
├── requirements.txt
├── README.md
└── assets/
```

## Learning Outcomes

This project demonstrates:

* Agent development with LangChain
* Tool calling and orchestration
* Integration of external knowledge sources
* Mathematical reasoning workflows
* Streamlit-based AI applications
* Modern LangChain agent architecture

## Future Improvements

* Conversational memory
* SymPy integration for symbolic mathematics
* Unit conversion tools
* Geometry solver tools
* Graph plotting support
* Retrieval-Augmented Generation (RAG)
* Multi-agent architecture

## License

This project is licensed under the MIT License.

## Author

Garvit Jain

Aspiring AI/ML Engineer passionate about Generative AI, Agentic AI, and Large Language Models.
