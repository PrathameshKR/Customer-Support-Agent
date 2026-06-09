from utils.config import *
from graph_builder import build_graph

app = build_graph()


def run_customer_support(query):

    result = app.invoke(
        {"query": query}
    )

    return result


if __name__ == "__main__":

    query = input(
        "Enter customer query: "
    )

    result = run_customer_support(
        query
    )

    print("\nCategory :", result["category"])
    print("Sentiment:", result["sentiment"])
    print("Response :", result["response"])