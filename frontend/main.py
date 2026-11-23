from typing import TypedDict

from langgraph.graph import START, StateGraph


class State(TypedDict):
    name: str
    greeting: str


def greet(state: State) -> dict:
    return {"greeting": f"Hello, {state['name']}!"}


graph = StateGraph(State)
graph.add_node("greet", greet)
graph.add_edge(START, "greet")
app = graph.compile()

result = app.invoke({"name": "Saurabh"})
print(result["greeting"])
