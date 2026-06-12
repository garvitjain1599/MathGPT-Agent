import streamlit as st
import numexpr

from langchain_groq import ChatGroq
from langchain.agents import create_agent
from langchain_core.tools import tool
from langchain_community.utilities import WikipediaAPIWrapper

# =====================================================
# Streamlit UI
# =====================================================

st.set_page_config(
    page_title="MathGPT Agent",
    page_icon="🧮"
)

st.title("🧮 MathGPT Agent")

groq_api_key = st.sidebar.text_input(
    "Groq API Key",
    type="password"
)

if not groq_api_key:
    st.info("Please enter your Groq API key.")
    st.stop()

# =====================================================
# LLM
# =====================================================

llm = ChatGroq(
    model="llama-3.3-70b-versatile",  # more reliable than 8b
    groq_api_key=groq_api_key,
    temperature=0
)

# =====================================================
# Tools
# =====================================================

wiki = WikipediaAPIWrapper()

@tool
def wikipedia_search(query: str) -> str:
    """
    Search Wikipedia for factual information.
    """
    return wiki.run(query)


@tool
def calculator(expression: str) -> str:
    """
    Evaluate a mathematical expression.

    Examples:
    2+2
    15*7
    (25+10)/5
    """

    try:
        result = numexpr.evaluate(expression)
        return str(result.item())
    except Exception as e:
        return f"Calculation Error: {str(e)}"


@tool
def reasoning_helper(problem: str) -> str:
    """
    Use when a question requires logical reasoning,
    planning, or breaking a problem into steps.
    """

    return f"""
Follow this reasoning framework:

1. Identify the goal.
2. Extract important facts.
3. Break the problem into smaller parts.
4. Solve each part carefully.
5. Verify the final answer.

Problem:
{problem}
"""


# =====================================================
# Agent
# =====================================================

agent = create_agent(
    model=llm,
    tools=[
        calculator,
        wikipedia_search,
        reasoning_helper
    ],
    system_prompt="""
You are MathGPT.

Available tools:

1. calculator
   - Use for arithmetic and mathematical calculations.

2. wikipedia_search
   - Use for factual and knowledge-based questions.

3. reasoning_helper
   - Use for complex logical reasoning and multi-step problems.

Rules:
- Use tools whenever appropriate.
- Never invent tool names.
- Show step-by-step explanations.
- Verify numerical answers before responding.
"""
)

# =====================================================
# Session State
# =====================================================

if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": "Hi! I'm MathGPT. Ask me math, reasoning, or factual questions."
        }
    ]

# =====================================================
# Display Chat History
# =====================================================

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# =====================================================
# User Input
# =====================================================

question = st.chat_input(
    "Ask a math, reasoning, or knowledge question..."
)

if question:

    st.session_state.messages.append(
        {
            "role": "user",
            "content": question
        }
    )

    with st.chat_message("user"):
        st.write(question)

    with st.chat_message("assistant"):

        with st.spinner("Thinking..."):

            response = agent.invoke(
                {
                    "messages": [
                        {
                            "role": "user",
                            "content": question
                        }
                    ]
                }
            )

            answer = response["messages"][-1].content

            st.write(answer)

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer
        }
    )