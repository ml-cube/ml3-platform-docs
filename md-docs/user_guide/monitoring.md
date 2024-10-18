# Monitoring

The monitoring module is a key feature of the ML cube Platform. 
It enables continuous tracking of your AI models performance over time, helping to identify potential issues. 
Additionally, it allows the monitoring of production data to preemptively detect distribution changes, ensuring
that the model continues to perform as expected and aligns with business requirements.

## Why do we need Monitoring?

Machine Learning algorithms are based on the assumption that the distribution of the data used for training is the same as the one from which
production data are drawn from. This assumption never holds in practice, as the real world is characterized by dynamic and ever-changing conditions.
These distributional changes, if not addressed properly, can cause a drop in the model's performance, leading to bad estimations or predictions, which
in turn can have a negative impact on the business.

Monitoring, also known as __Drift Detection__ in the literature, refers the process of continuously tracking the performance of a model 
and the distribution of the data it is operating on. 

## How does the MLCube Platform perform Monitoring?

The MLCube platform performs monitoring by employing statistical techniques to compare a certain reference (for instance, data used for training or the performance of a model
on the test set) to incoming production data. If a significant difference is detected, an alarm is raised, signaling that the monitored entity
is drifting away from the expected behavior and that corrective actions should be taken.

In more practical terms, the [set_model_reference] method can be used to specify the time period where the reference of a given model should be placed. As a consequence,
all algorithms associated with the specified model (not just those monitoring the performance, but also those operating on the data used by the model) will
be initialized on the specified reference. Of course, you should send the data you want to use as a reference to the platform before calling this method, for instance using the 
[add_historical_data] method.

After setting the reference, the [add_production_data] method can be used to send production data to the platform. This data will be analyzed by the monitoring algorithms
and, if a significant difference is detected, an alarm will be raised, in the form of a [DetectionEvent]. We will go into more detail about detection events and
how you can set up automatic actions upon their reception in the [Detection Event] section.

The MLCube Platform monitors different entities, which will be explored in the following section.

### Targets and Metrics

After going through the reasons why monitoring is so important in modern AI systems and explaining how monitoring is performed in the ML cube Platform, 
we can introduce the concepts of Monitoring Targets and Monitoring Metrics. They both represent quantities that the MLCube Platform monitors, but they differ in their nature.

#### Monitoring Targets

A Monitoring Target is a relevant entity involved in a [Task]. They represent the main quantities monitored by the platform, those whose
variation can have a significant impact on the AI task success. 

The MLCube platform supports the following monitoring targets:

- `INPUT`: the input distribution, $P(X)$.
- `CONCEPT`: the joint distribution of input and target, $P(X, Y)$.
- `PREDICTION`: the prediction of the model, $P(\hat{Y})$.
- `INPUT_PREDICTION`: the joint distribution of input and prediction, $P(X, \hat{Y})$.
- `ERROR`: the error of the model, whose computation depends on the task type.
- `USER_INPUT`: the input provided by the user, usually in the form of a query. This target is only available in tasks of type RAG.
- `USER_INPUT_RETRIEVED_CONTEXT`: the similarity between the user input and the context retrieved by the RAG system. This target is only available in tasks of type RAG.
- `USER_INPUT_MODEL_OUTPUT`: the similarity between the user input and the response of the Large Language Model. This target is only available in tasks of type RAG.
- `MODEL_OUTPUT_RETRIEVED_CONTEXT`: the similarity between the response of the Large Language Model and the context retrieved by the RAG system. This target is only available in tasks of type RAG.

As mentioned, some targets are available only for specific task types. The following table shows all the available monitoring targets in relation with the task type. 
Notice that while some targets were specifically designed for a certain task type, others are more general and can be used in different contexts. 
Nonetheless, the platform might not support yet all possible combinations. The table will be updated as new targets are added to the product.

| **Monitoring Target**          |   **REGRESSION**   | **CLASSIFICATION_BINARY** | **CLASSIFICATION_MULTICLASS** | **CLASSIFICATION_MULTILABEL** | **OBJECT_DETECTION** |      **RAG**       |
|--------------------------------|:------------------:|:-------------------------:|:-----------------------------:|:-----------------------------:|:--------------------:|:------------------:|
| INPUT                          | :white_check_mark: |    :white_check_mark:     |      :white_check_mark:       |      :white_check_mark:       |  :white_check_mark:  |                    |
| CONCEPT                        | :white_check_mark: |    :white_check_mark:     |      :white_check_mark:       |      :white_check_mark:       |                      |                    |
| PREDICTION                     | :white_check_mark: |    :white_check_mark:     |      :white_check_mark:       |                               |                      |                    |
| INPUT_PREDICTION               | :white_check_mark: |    :white_check_mark:     |      :white_check_mark:       |                               |                      |                    |
| ERROR                          | :white_check_mark: |    :white_check_mark:     |      :white_check_mark:       |      :white_check_mark:       |                      |                    |
| USER_INPUT                     |                    |                           |                               |                               |                      | :white_check_mark: |
| USER_INPUT_RETRIEVED_CONTEXT   |                    |                           |                               |                               |                      | :white_check_mark: |
| USER_INPUT_MODEL_OUTPUT        |                    |                           |                               |                               |                      | :white_check_mark: |
| MODEL_OUTPUT_RETRIEVED_CONTEXT |                    |                           |                               |                               |                      | :white_check_mark: |

#### Monitoring Metrics

A Monitoring Metric is a generic quantity that can be computed on a Monitoring Target. They enable the monitoring of specific
aspects of a target, which might help in identifying the root cause of a drift, as well as defining the corrective actions to be taken.

The following table display the monitoring metrics supported, along with their monitoring target and the conditions
under which they are actually monitored. Notice that also this table is subject to changes, as new metrics are added.

| **Monitoring Metric** | Description                                              |              **Monitoring Target**               |             **Conditions**             |
|:---------------------:|----------------------------------------------------------|:------------------------------------------------:|:--------------------------------------:|
|     TEXT_TOXICITY     | The toxicity of the text                                 |          INPUT, USER_INPUT, PREDICTION           |    When the data structure is text     |
|     TEXT_EMOTION      | The emotion of the text                                  |                INPUT, USER_INPUT                 |    When the data structure is text     |
|    TEXT_SENTIMENT     | The sentiment of the text                                |                INPUT, USER_INPUT                 |    When the data structure is text     |
|      TEXT_LENGTH      | The length of the text                                   | INPUT, USER_INPUT, RETRIEVED_CONTEXT, PREDICTION |    When the data structure is text     |
|   MODEL_PERPLEXITY    | The uncertainty of the LLM                               |                    PREDICTION                    |       When the task type is RAG        |
|   IMAGE_BRIGHTNESS    | The brightness of the image                              |                      INPUT                       |    When the data structure is image    |
|    IMAGE_CONTRAST     | The contrast of the image                                |                      INPUT                       |    When the data structure is image    |
|      BBOXES_AREA      | The average area of the predicted bounding boxes         |                    PREDICTION                    | When the task type is Object Detection |
|    BBOXES_QUANTITY    | The average number of predicted bounding boxes per image |                    PREDICTION                    | When the task type is Object Detection |


[Task]: task.md
[set_model_reference]: ../../api/python/client#set_model_reference
[add_production_data]: ../../api/python/client#add_production_data
[add_historical_data]: ../../api/python/client#add_historical_data
[DetectionEvent]: ../../api/python/models#detectionevent
