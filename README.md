# Customer Support Agent using LangGraph & Gemini

An intelligent customer support workflow built with **LangGraph**, **LangChain**, and **Google Gemini**. The application automatically categorizes customer queries, analyzes sentiment, routes requests to the appropriate support department, and escalates negative interactions when necessary.

---

## Features

- Query Categorization
  - Technical Support
  - Billing Support
  - General Support

- Sentiment Analysis
  - Positive
  - Neutral
  - Negative

- Intelligent Routing
  - Automatically directs queries to the correct support workflow

- Escalation System
  - Routes negative customer interactions to a human representative

- Modular LangGraph Architecture
  - Easy to extend and maintain

- Gemini Integration
  - Powered by Google's Gemini models through LangChain

---

## Project Architecture

```text
User Query
     │
     ▼
Categorize Query
     │
     ▼
Analyze Sentiment
     │
     ├── Negative ─────► Escalate to Human Agent
     │
     ├── Technical ────► Technical Support
     │
     ├── Billing ──────► Billing Support
     │
     └── General ──────► General Support
```

---

## Project Structure

```text
customer_support_agent/
│
├── app.py
├── graph_builder.py
├── nodes.py
├── state.py
├── requirements.txt
├── .env
│
└── utils/
    └── config.py
```

---

## Tech Stack

- Python
- LangGraph
- LangChain
- Google Gemini
- python-dotenv

---

## Installation

### Clone Repository

```bash
git clone https://github.com/your-username/customer-support-agent.git

cd customer-support-agent
```

### Create Virtual Environment

```bash
conda create -n customer_support python=3.11

conda activate customer_support
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Configure API Key

Create a `.env` file in the project root:

```env
GOOGLE_API_KEY=YOUR_GEMINI_API_KEY
```

Obtain your API key from Google AI Studio.

---

## Run the Application

```bash
python app.py
```

---

## Example

### Input

```text
I was charged twice for my subscription.
```

### Output

```text
Category : Billing
Sentiment: Neutral

Response :
I apologize for the inconvenience. Please provide your transaction details so we can investigate the duplicate charge.
```

---

## Workflow Description

### Categorization Node

Determines whether the query belongs to:

- Technical
- Billing
- General

### Sentiment Analysis Node

Classifies the customer's tone as:

- Positive
- Neutral
- Negative

### Routing Logic

Based on category and sentiment, the workflow dynamically selects the next node.

### Support Nodes

Generate specialized responses for:

- Technical issues
- Billing issues
- General inquiries

### Escalation Node

Automatically escalates highly negative customer interactions to a human support representative.

---

## Future Enhancements

- Conversation Memory
- Multi-Agent Support Teams
- Retrieval-Augmented Generation (RAG)
- Knowledge Base Integration
- Tool Calling
- Database Logging
- Human-in-the-Loop Review
- Customer Ticket Generation
- Web Interface using Flask or FastAPI
- Deployment on Cloud Platforms

---

## Learning Objectives

This project demonstrates:

- Graph-based AI workflows
- State management in LangGraph
- Conditional routing
- LLM-powered classification
- Sentiment analysis
- Agent orchestration
- Modular project design

---

## Requirements

```txt
langgraph
langchain-core
langchain-google-genai
python-dotenv
ipython
```

---

## License

This project is intended for educational and research purposes.

---

## Author

Prathamesh Ranaware

Machine Learning | Data Science | Generative AI | MLOps