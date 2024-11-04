# Model

In the ML Cube Platform, a Model is a representation of the actual machine learning model used for making predictions. The data used
for its training usually represent the reference data distribution, while production data comprises the data on which the model 
performs inference.

A Model is uniquely associated with a [Task] and it can be created both through the WebApp and the Python SDK. Currently, we only support one model
per Task.

A Model is defined by a name and a version. The version is updated whenever the model is retrained, allowing to 
track the latest version of the model and the data used for its training. When predictions are uploaded to the platform,
the model version needs to be appropriately specified, following the guidelines in the [Data Schema] page, to ensure that the
predictions are associated to the correct model version.

!!! note
    You don't need to upload the **real** model on the Platform. We only require its training data and predictions.
    The entity you create on the Platform serves more as a placeholder for the model. For this reason,
    the ML cube Platform is considered *model agnostic*.


### RAG Model

RAG Tasks represent an exception to the model framework presented before. In this type of Tasks, the model
is a Large Language Model (LLM), that is used to generate responses to user queries. The model is not trained on a specific dataset
but is rather a pre-trained model that is fine-tuned on the user's data, which means that the classic process of training and
retraining does not apply. 

To maintain a coherent Model definition across task types, the RAG model is also represented as a Model, 
but an update of its version represents an update of the reference data distribution and not necessarily
an update of the model itself. Moreover, most of the attributes which will be described in the following sections
are not applicable, as they are related to the retraining module, which is not usable in RAG tasks.

### Probabilistic output

When creating a model, you can specify if you want to provide also the probabilistic output of the model along with the predictions. 
The probabilistic output represents the probability or confidence score associated with the model's predictions. If provided, 
the ML cube Platform will use this information to compute additional metrics and insights.

It is optional and currently supported only for Classification and RAG tasks. If specified, the probabilistic output must be provided 
as a new column in the predictions file, following the guidelines in the [Data Schema] page.

### Metric

A Model Metric represents the evaluation metric used to assess the performance of the model. 
It can both represent a performance or an error. The chosen metric will be used in the various views of the platform to
provide insights on the model's performance. The available options are:

- `Accuracy`, for classification tasks
- `RMSE`, for regression tasks
- `R2`, for regression tasks
- `Average Precision`, for Object Detection tasks

RAG tasks have no metric, as in that case the model is an LLM for which classic definitions of metrics are not applicable.

### Suggestion Type

The Suggestion Type represents the type of suggestion that the ML cube Platform should provide when computing the 
[retraining dataset](modules/retraining.md#retraining-dataset). The available options are:

- `Sample Weights`: each sample uploaded in ML cube Platform is assigned a weight that can be used as sample weight in a weighted loss function.
    The higher the weight, the greater the importance of the sample for the new retraining.
- `Resampled Dataset`: a list of sample ids (using data schema column object with role ID) is provided indicating which data form the retraining dataset.
    This format can be used when the training procedure does not support weighted loss or when a fixed size retraining dataset is preferred.
    Note that samples ids can appear more than once: this happens when a sample is particularly important for the new retraining.

[Task]: task.md
[Data Schema]: data_schema.md

[//]: # ()
[//]: # ()
[//]: # (What is additional probabilistic output?)

[//]: # ()
[//]: # (What is metric?)

[//]: # ()
[//]: # (What is suggestion type?)

[//]: # ()
[//]: # (What is retraining cost?)

[//]: # ()
[//]: # (What is retraining trigger?)