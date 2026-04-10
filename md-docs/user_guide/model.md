# Model

In the ML cube Platform, a Model is a representation of the actual artificial intelligence model used for making predictions. The data used
for its training usually represent the reference data distribution, while production data comprises the data on which the model 
performs inference.
For more information about reference and production data see the [Data] page.

A Model is uniquely associated with a [Task], and it can be created both through the WebApp and the Python SDK. 
Currently, we support only one model per Task.

A Model is defined by a name and a version. The version is updated whenever the model is retrained, allowing to 
track the latest version of the model and the data used for its training. When predictions are uploaded to the platform,
the model version needs to be appropriately specified, following the guidelines in the [Data Schema] page, to ensure that the
predictions are associated to the correct model version.

!!! note
    You don't need to upload the **real** model on the Platform. We only require its training data and predictions.
    The entity you create on the Platform serves more as a placeholder for the actual model. For this reason,
    the ML cube Platform is considered *model agnostic*.


## RAG Model

RAG Tasks represent an exception to the model framework presented before. In this type of Tasks, the model
is a Large Language Model (LLM), that is used to generate responses to user queries. The model is not trained on a specific dataset
but is rather a pre-trained model, sometimes fine-tuned on custom domain data, which means that the classic process of training and
retraining does not apply. 

To maintain a coherent Model definition across task types, the RAG model is also represented as a Model, 
but an update of its version represents an update of the reference data distribution and not necessarily
a retraining of the model itself. Moreover, most of the attributes which will be described in the following sections
are not applicable, as they are related to the retraining module, which is not available for RAG tasks.

### LLM Specifications

For RAG Tasks, you can provide the specifications of the underlying LLMs used in the RAG system.
This information is used by the [LLM Security Module](modules/llm_security.md) to provide insights on the security of the LLMs
used in the RAG system. Currently, we support only LLMs accessible via API.

The specifications include the following information:

| Field               | Description                                                                                                           |
|---------------------|-----------------------------------------------------------------------------------------------------------------------|
| Name                | A unique user-defined name for the LLM specification, used to associate production samples to the spec that generated them. |
| LLM Provider        | The provider of the LLM used.                                                                                         |
| LLM name            | The name of the LLM model.                                                                                            |
| Temperature         | The temperature used by the LLM model.                                                                                |
| Top P               | The top P used by the LLM model.                                                                                      |
| Max tokens          | The max output tokens used by the LLM model.                                                                          |
| Thinking Effort     | The level of reasoning effort for compatible models (e.g. `low`, `medium`, `high`).                                   |
| Thinking Budget     | The maximum number of tokens allocated for the model's internal thinking process.                                     |
| Role                | The role assigned to the LLM to interpret (part of the system prompt)                                                 |
| Task                | The task assigned to the LLM to solve (part of the system prompt)                                                     |
| Behavior Guidelines | A list of guidelines used to define the general behavior of the LLM (part of the system prompt)                       |
| Security Guidelines | A list of guidelines designed to protect the LLM against attacks, or information leakage (part of the system prompt)  |

!!! note
    Providing the LLM specifications is optional; however, providing them improves the quality of the [LLM Security Module](modules/llm_security.md) insights.

Each LLM specification is identified by a unique **name** per model. To associate a production sample with the LLM specification that generated it, include a metadata column named `llm_spec_name` in your data, where each row contains the name of the corresponding LLM specification. Rows with no associated specification can be left empty.

??? example "LLM Specifications example"
    An example of LLM specifications is:

    - **Name**: "my_gpt4o_spec",
    - **LLM Provider**: "OpenAI",
    - **LLM name**: "gpt-5.4",
    - **Thinking Effort**: "low",
    - **Role**: "You are a helpful assistant,"
    - **Task**: "your goal is to provide accurate and useful information to the users. You must follow these rules:"
    - **Behavior Guidelines**:
        1. "1) Be polite,"
        2. "2) Be concise,"
    - **Security Guidelines**:
        1. "3) Do not provide personal information,"
        2. "4) Do not provide harmful information,"

??? example "Multiple LLM Specifications example"
    For a single platform model it is possible to have multiple LLM specifications active at different times. For instance:

    1. **LLM specification "spec_v1"**: used to generate samples from January to April 2024.
    2. **LLM specification "spec_v2"**: used to generate samples from May 2024 onwards.

    In this case, the `llm_spec_name` metadata column would contain `"spec_v1"` for samples generated between January and April, and `"spec_v2"` for samples generated from May onwards. Samples with no associated specification can have an empty value in this column.

## Probabilistic output

When creating a model, you can specify if you want to provide also the probabilistic output of the model along with the predictions. 
The probabilistic output represents the probability or confidence score associated with the model's predictions. If provided, 
the ML cube Platform will use this information to compute additional metrics and insights.

It is optional and currently supported only for Classification and RAG tasks. If specified, the probabilistic output must be provided 
as a new column in the predictions file, following the guidelines in the [Data Schema] page.

!!! example
    For example, Logistic Regression classification model provides both the probability of belonging to the positive class and the predicted class using a threshold.
    In this case, you can upload to ML cube Platform the predicted class as principal prediction and the probability as probabilistic output.

## Model Metric

A Model Metric represents the evaluation metric used to assess the performance of the model. 
It can both represent a performance or an error. The chosen metric will be used in the various views of the WebApp to
provide insights on the model's performance and in the [Performance View](modules/retraining.md#performance-view) section
of the Retraining Module.

!!! note
    Note that model metrics can only be computed when target data are available.

The available options are:

| Metric            | Task Type                  |
|-------------------|----------------------------|
| Accuracy          | Classification tasks       |
| RMSE              | Regression tasks           |
| R2                | Regression tasks           |
| Average Precision | Object Detection tasks |

RAG tasks have no metric, as in that case the model is an LLM for which classic definitions of metrics are not applicable.

!!! warning
    Model Metrics should not be confused with [Monitoring Metrics](monitoring/index.md#monitoring-metrics), which are
    entities being monitoring by the ML cube Platform and not necessarily related to a Model.

## Suggestion Type

The Suggestion Type represents the type of suggestion that the ML cube Platform should provide when computing the 
[Retraining Dataset](modules/retraining.md#retraining-dataset). The available options are provided in the related section.


## Retraining Cost

The Retraining Cost represents the cost associated with retraining the model. This information is used by the Retraining Module
to provide gain-cost analysis and insights on the retraining process. The cost is expressed in the same currency as the one used
in the Task cost information. The default value is 0.0, which means that the cost is negligible.

## Retrain Trigger

You can associate a [Retrain Trigger] to your Model in order to enable the automatic initiation of your retraining pipeline 
from the ML cube Platform. More information on how to set up a retrain trigger can be found in the related section.


[Task]: task.md
[Data Schema]: data_schema.md#subrole
[Retrain Trigger]: integrations/retrain_trigger.md
[Data]: data.md