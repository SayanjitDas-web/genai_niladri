from unittest import result

from langgraph.graph import START , END, StateGraph
from pydantic import BaseModel
from langchain_google_genai import GoogleGenerativeAI

llm = GoogleGenerativeAI(
    api_key = "",
    model = "gemini-2.5-flash"
)

class AgentState(BaseModel):
    query: str
    tool: str = ""
    result: str = ""

def codegen_node(state: AgentState):
    query = state.query
    result = llm.invoke(query+"you are an software engineer expert. Write the code only.")
    state.result = result
    return state

def codereview_node(state: AgentState):
    query = state.query
    result = llm.invoke(query+"you are a QA engineer expert . Review the code and give only the review detailes.")
    state.result = result
    return state

def tool_selector(state: AgentState):
    query = state.query
    result = llm.invoke(query+"""
    understand the given query and classify that if the query is for generating review or generating code.
    if it is all about generating review just only return the word 'review' or if it is all aboyt generating code only return the word 'code'.please don't include any other text.
""")
    if(result == "review"):
        state.tool = "review"
    elif(result == "code"):
        state.tool = "code"
    return state

def decider_function(state: AgentState):
    return state.tool

agent = StateGraph(AgentState)

agent.add_node("codegen_node",codegen_node)
agent.add_node("codereview_node",codereview_node)
agent.add_node("tool_selector",tool_selector)

agent.add_edge(START,"tool_selector")

agent.add_conditional_edges(
    "tool_selector",
    decider_function,
    {
        "code":"codegen_node",
        "review":"codereview_node"
    }
)

agent.add_edge("codegen_node",END)
agent.add_edge("codereview_node",END)

app = agent.compile()

result = app.invoke({"query":"write a function in python to perform a string reverse"})

print(result["result"])