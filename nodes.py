from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI

from state import State

# Gemini Model

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0
)


def categorize(state: State):

    prompt = ChatPromptTemplate.from_template(
        """
        Categorize the customer query into one of:
        Technical
        Billing
        General

        Return only the category.

        Query: {query}
        """
    )

    chain = prompt | llm

    category = chain.invoke(
        {"query": state["query"]}
    ).content.strip()

    return {"category": category}


def analyze_sentiment(state: State):

    prompt = ChatPromptTemplate.from_template(
        """
        Analyze the sentiment.

        Return only:
        Positive
        Neutral
        Negative

        Query: {query}
        """
    )

    chain = prompt | llm

    sentiment = chain.invoke(
        {"query": state["query"]}
    ).content.strip()

    return {"sentiment": sentiment}


def handle_technical(state: State):

    prompt = ChatPromptTemplate.from_template(
        """
        You are a technical support agent.

        Query: {query}
        """
    )

    chain = prompt | llm

    response = chain.invoke(
        {"query": state["query"]}
    ).content

    return {"response": response}


def handle_billing(state: State):

    prompt = ChatPromptTemplate.from_template(
        """
        You are a billing support agent.

        Query: {query}
        """
    )

    chain = prompt | llm

    response = chain.invoke(
        {"query": state["query"]}
    ).content

    return {"response": response}


def handle_general(state: State):

    prompt = ChatPromptTemplate.from_template(
        """
        You are a customer support agent.

        Query: {query}
        """
    )

    chain = prompt | llm

    response = chain.invoke(
        {"query": state["query"]}
    ).content

    return {"response": response}


def escalate(state: State):

    return {
        "response":
        "Your issue has been escalated to a human support representative."
    }


def route_query(state: State):

    if state["sentiment"] == "Negative":
        return "escalate"

    elif state["category"] == "Technical":
        return "handle_technical"

    elif state["category"] == "Billing":
        return "handle_billing"

    return "handle_general"