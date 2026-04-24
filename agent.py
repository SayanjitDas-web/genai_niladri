from langgraph.graph import START , END, StateGraph
from pydantic import BaseModel
from langchain_google_genai import GoogleGenerativeAI

llm = GoogleGenerativeAI(
    api_key = "AIzaSyBsp1z4jPid1IWztmD286VtbiF5lJ9djdM",
    model = "gemini-2.5-flash"
)

class AgentState(BaseModel):
    query: str
    tool: str = ""
    result: str = ""

def sum_node(state: AgentState):
    query = state.query
    result = llm.invoke(query+"do sum")
    state.result = result
    return state

def subs_node(state: AgentState):
    query = state.query
    result = llm.invoke(query+"do substraction")
    state.result = result
    return state

def tool_selector(state: AgentState):
    if("+" in state.query):
        state.tool = "sum"
    else:
        state.tool = "subs"
    return state
    
def decider_function(state: AgentState):
    return state.tool
    
agent = StateGraph(AgentState)

agent.add_node("sum_node",sum_node)
agent.add_node("subs_node",subs_node)
agent.add_node("tool_selector",tool_selector)

agent.add_edge(START,"tool_selector")

agent.add_conditional_edges(
    "tool_selector",
    decider_function,
    {
        "sum":"sum_node",
        "subs":"subs_node"
    }
)

agent.add_edge("sum_node",END)
agent.add_edge("subs_node",END)

app = agent.compile()

result = app.invoke({"query":"99+258+30"})

print(result["result"])