# Rag Evaluation

## What is RAG Evaluation?

RAG (Retrieval-Augmented Generation) is a way of building AI models that enhances their ability to generate accurate and contextually relevant responses by combining two main steps: **retrieval** and **generation**.

1. **Retrieval**: The model first searches through a large set of documents or pieces of information to "retrieve" the most relevant ones based on the user query.
2. **Generation**: It then uses these retrieved documents as context to generate a response, which is typically more accurate and aligned with the question than if it had generated text from scratch without specific guidance.

Evaluating RAG involves assessing how well the model does in both retrieval and generation.

Our RAG evaluation module analyzes the three main components of a RAG framework:

- **User Input**: The query or question posed by the user.
- **Context**: The retrieved documents or information that the model uses to generate a response. A context can consist of one or more chunks of text.
- **Response**: The generated answer or output provided by the model.

In particular, the analysis is performed on the relationships between these components:

- **User Input - Context**: Retrieval Evaluation
- **Context - Response**: Context Factual Correctness
- **User Input - Response**: Response Evaluation

<figure markdown>
  ![ML cube Platform RAG Evaluation](../../imgs/rag_evaluation.png){ width="600"}
  <figcaption>ML cube Platform RAG Evaluation</figcaption>
</figure>

The evaluation is performed through an LLM-as-a-Judge approach, where a Language Model (LM) acts as a judge to evaluate the quality of a RAG model.

## What are the computed metrics?

Below are the metrics computed by the RAG evaluation module, divided into the three relationships mentioned above.

### User Input - Context

- **Relevance**: Measures how much the retrieved context is relevant to the user input. The score ranges from 1 to 5, with 5 being the highest relevance.
- **Usefulness**: Evaluates how useful the retrieved context is in generating the response. For example, if a context talks about the topic of the user query but it does not contain the information needed to answer the question, it is relevant but not useful. The score ranges from 1 to 5, with 5 being the highest usefulness.
- **Utilization**: Measures the percentage of the retrieved context that contains information that can be used to generate the response. A higher utilization score indicates that more of the retrieved context is useful for generating the response. The score ranges from 0 to 100.
- **Attribution**: Indicates which of the chunks of the retrieved context can be used to generate the response. It is a list of the indices of the chunks that are used, with the first chunk having index 1.

### Context - Response
- **Faithfulness**: Measures how much the response contradicts the retrieved context. A higher faithfulness score indicates that the response is more aligned with the context. The score ranges from 1 to 5, with 5 being the highest faithfulness.

### User Input - Response
- **Satisfaction**: Evaluates how satisfied the user would be with the generated response. The score ranges from 1 to 5, with 1 a response that does not address the user query and 5 a response that fully addresses and answers the user query.

## What is the required data?

The RAG evaluation module computes the metrics based on the data availability for each sample. 
If a sample lacks one of the three components (User Input, Context or Response), only the applicable metrics are computed. 
For instance, if a sample does not have a response, only the **User Input - Context** metrics are computed.

If data added to a [Task] contains contexts with multiple chunks of text, a [context separator](../task.md#retrieval-augmented-generation) must be provided.

[Task]: ../task.md