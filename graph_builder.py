from langgraph.graph import StateGraph, END

from state import State

from nodes import (
    categorize,
    analyze_sentiment,
    handle_technical,
    handle_billing,
    handle_general,
    escalate,
    route_query
)


def build_graph():

    workflow = StateGraph(State)

    workflow.add_node(
        "categorize",
        categorize
    )

    workflow.add_node(
        "analyze_sentiment",
        analyze_sentiment
    )

    workflow.add_node(
        "handle_technical",
        handle_technical
    )

    workflow.add_node(
        "handle_billing",
        handle_billing
    )

    workflow.add_node(
        "handle_general",
        handle_general
    )

    workflow.add_node(
        "escalate",
        escalate
    )

    workflow.set_entry_point(
        "categorize"
    )

    workflow.add_edge(
        "categorize",
        "analyze_sentiment"
    )

    workflow.add_conditional_edges(
        "analyze_sentiment",
        route_query,
        {
            "handle_technical": "handle_technical",
            "handle_billing": "handle_billing",
            "handle_general": "handle_general",
            "escalate": "escalate"
        }
    )

    workflow.add_edge(
        "handle_technical",
        END
    )

    workflow.add_edge(
        "handle_billing",
        END
    )

    workflow.add_edge(
        "handle_general",
        END
    )

    workflow.add_edge(
        "escalate",
        END
    )

    return workflow.compile()