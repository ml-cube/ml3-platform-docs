# Topic Modeling

The Topic Modeling module allows you to categorize documents based on their content. The goal is to represent each document as a set of topics, where a topic is made up of a list of words that commonly appear together. The percentage of topics in a document varies, suggesting the concepts it covers and in what proportion.

For example, a company could use Topic Modeling to analyze customer reviews and identify areas for improvement. Imagine that an e-commerce company uses Topic Modeling to analyze customer reviews of its products. The Topic Modeling module could identify topics such as “price,” “quality,” “shipping,” and “customer service.” The company could then use this information to improve its products and services in areas where customers have expressed concerns or dissatisfaction.

Topic Modeling in ML cube Platform is based on unsupervised machine learning algorithms that analyze a corpus of documents and identify the latent topics.
### Key Concepts

| Term | Description |
|---|---|
| Topic | A subject represented by a set of words that commonly appear together.|
| Document Distribution | Each document shows a spread of topics, indicating the concepts it covers and in what proportion.|

## Topic Modeling Report
The Topic Modeling report provides a comprehensive overview of the topics identified in the corpus of documents. The report includes the following sections:

*   **Topic Summary:** This section provides a list of the identified topics, along with their coherence and perplexity. Coherence is a measure of how related the words in a topic are to each other. Perplexity is a measure of how well the model is able to predict the documents in the corpus.
*   **Topic Visualization:** This section includes various types of visualizations that help to understand the identified topics. The available visualizations include:
    *   **Bar Charts:** Shows the distribution of topics in the corpus of documents.
    *   **Heatmaps:** Shows the relationship between topics and words.
    *   **Word Clouds:** Shows the most frequent words in each topic.
*   **Document Analysis:** This section allows you to examine the topic distribution in individual documents.
??? code-block "SDK Example"
    The following code shows how to create a topic modeling report
    When triggered, it first sends a notification to the `ml3-platform-notifications` channel on your Slack workspace, using the 
    provided webhook URL, and then starts the retraining of the model.

    ```py
    #In the following example, it is used
    # a Polars DataFrame for production data,
    #  but you can use any other data structure.

    prod_data_df = pl.read_csv("production_data.csv")
    topic_modeling_job_id = client.compute_topic_modeling_report(
        task_id=task_id,
        report_name="topic_modeling_report_name",
        from_timestamp=prod_data_df["timestamp"].min(), # The initial timestamp from which to start the analysis
        to_timestamp=prod_data_df["timestamp"].max(), # The final timestamp to end the analysis
    )
    ```

## Supported Tasks and Data Structures
ML cube Platform supports the following tasks and data structures for Topic Modeling:

|Task Type| Tabular | Image | Text | Embedding|
| -- | -- | -- | -- | -- |
| Regression |  |  | :material-check: |  |
| Classification |  |  | :material-check: |  |
| RAG |  |  | :material-check: :material-information-outline:{title="Only for User Input"} |  |

Topic Modeling is only supported for text data structures because it is based on the analysis of words in documents. Topic Modeling for RAG tasks is only supported for user input because the retrieved context is not always available.
<figure markdown="span" style="display: inline-block; text-align: center; width: 100%;">
  ![Topic Modeling Timeseries](../../imgs/topic_modeling_demo_rag.png)
  <figcaption style="white-space: nowrap;">Topic Modeling Timeseries: visualization of topic distribution over time.</figcaption>
</figure>
