# Monitoring

The monitoring module is a key feature of the ML cube Platform. 
It enables continuous tracking of AI models performance over time, helping to identify potential issues. 
Additionally, it allows the monitoring of production data to preemptively detect distribution changes, ensuring
that the model continues to perform as expected and aligns with business requirements.

## Why do you need Monitoring?

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
be initialized on the specified reference. Of course, you should provide to the Platform the data you want to use as a reference before calling this method, for instance using the 
[add_historical_data] method.

After setting the reference, the [add_production_data] method can be used to send production data to the platform. This data will be analyzed by the monitoring algorithms
and, if a significant difference is detected, an alarm will be raised, in the form of a [DetectionEvent]. 
You can explore more about detection events and how you can set up automatic actions upon their reception in the [Detection Event] 
and the [Detection Event Rule] sections respectively.

### Targets and Metrics

After explaining why monitoring is so important in modern AI systems and detailing how it is performed in the ML cube Platform, 
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
under which they are actually monitored. Notice that also this table is subject to changes, as new metrics will be added.

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


### Monitoring Status

All the entities being monitored are associated with a status, which is defined according to the enumeration [MonitoringStatus]. 

The status can be one of the following:

- `OK`: the entity is behaving as expected.
- `WARNING`: the entity has shown signs of drifts, but it is still within the acceptable range.
- `DRIFT`: the entity has experienced a significant change and corrective actions should be taken.

You can check the status of the monitored entities in two ways:

- **WebApp**: The homepage of the task displays the status of both monitoring targets and metrics.
- **SDK**: The [get_monitoring_status] method can be used to retrieve the status of the monitored entities programmatically. 
  This method returns a [MonitoringQuantityStatus], a BaseModel holding the status of the monitoring entity requested.
  Otherwise, you can use the [get_task] method, which returns a BaseModel with all the information related to a task, including
    the list of [MonitoringQuantityStatus] for all the entities monitored in the task.


[Task]: ../task.md
[set_model_reference]:  ../../api/python/client.md#set_model_reference
[add_production_data]: ../../api/python/client.md#add_production_data
[add_historical_data]: ../../api/python/client.md#add_historical_data
[DetectionEvent]: ../../api/python/models.md#detectionevent
[Detection Event Rule]: detection_event_rules.md
[Detection Event]: detection_event.md
[MonitoringStatus]: ../../api/python/enums.md#monitoringstatus
[get_monitoring_status]: ../../api/python/client.md#get_monitoring_status
[MonitoringQuantityStatus]: ../../api/python/models.md#monitoringquantitystatus
[get_task]: ../../api/python/client.md#get_task