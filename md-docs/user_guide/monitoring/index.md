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

## How does the ML cube Platform perform Monitoring?

The ML cube platform performs monitoring by employing statistical techniques to compare a certain reference (for instance, data used for training or the 
performance of a model
on the test set) to incoming production data. 

These statistical techniques, also known as _monitoring algorithms_, are tailored to the type of data
being observed; for instance, univariate data requires different monitoring techniques than multivariate data. However, you don't need to worry about
the specifics of these algorithms, as the ML cube Platform takes care of selecting the most appropriate ones for your task.

If a significant difference between reference and production data is detected, an alarm is raised, signaling that the monitored entity
is drifting away from the expected behavior and that corrective actions should be taken.

In practical terms, you can use the SDK to specify the time period where the reference of a given model should be placed.
As a consequence, all algorithms associated with the specified model (not just those monitoring the performance, but also those operating 
on the data used by the model) will
be initialized on the specified reference. Of course, you should provide to the 
Platform the data you want to use as a reference before setting the reference itself. This can be done through the SDK as well.

After setting the reference, you can send production data to the platform, still using the SDK. This data will be analyzed by the monitoring algorithms
and, if a significant difference is detected, an alarm will be raised, in the form of a [Detection Event]. 
You can explore more about detection events and how you can set up automatic actions upon their reception in the [Detection Event] 
and the [Detection Event Rule] sections respectively.

### Targets and Metrics

After explaining why monitoring is so important in modern AI systems and detailing how it is performed in the ML cube Platform, 
we can introduce the concepts of Monitoring Targets and Monitoring Metrics. They both represent quantities that the ML cube Platform monitors, 
but they differ in their nature.

Targets and Metrics are defined by the ML cube platform based on the [Task] attributes, such as the Task type and the data structure, and their monitoring
is automatically enabled upon the task creation. The idea underlying defining many entities to monitor, rather than monitoring
only the model error, is to provide a comprehensive view of the model's
performance and the data distribution, easing the identification of the root causes of a drift and thus facilitating the corrective actions.

#### Monitoring Targets

A Monitoring Target is a relevant entity involved in a [Task]. They represent the main quantities monitored by the platform, those whose
variation can have a significant impact on the AI task success. 

The ML cube platform supports the following monitoring targets:

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
aspects of an entity, which might help in identifying the root cause of a drift, as well as defining the corrective actions to be taken.

The following table displays the monitoring metrics supported, along with their monitoring target and the conditions
under which they are actually monitored. The possible values that each metric can assume are also provided.
Notice that also this table is subject to changes, as new metrics will be added.

| **Monitoring Metric** | Description                                              |              **Monitoring Target**               |             **Conditions**             | **Possible values**                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|:---------------------:|----------------------------------------------------------|:------------------------------------------------:|:--------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|     TEXT_TOXICITY     | The toxicity of the text                                 |          INPUT, USER_INPUT, PREDICTION           |    When the data structure is text     | Either _neutral_ or _toxic_.                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|     TEXT_EMOTION      | The emotion of the text                                  |                INPUT, USER_INPUT                 |    When the data structure is text     | If the Task text language is Italian, one between these: _anger_, _joy_, _sadness_, _fear_. <br/> <br/> Otherwise, _one_ between these: _admiration_, _amusement_, _anger_, _annoyance_, _approval_, _caring_, _confusion_, _curiosity_, _desire_, _disappointment_, _disapproval_, _disgust_, _embarrassment_, _excitement_, _fear_, _gratitude_, _grief_, _joy_, _love_, _nervousness_, _optimism_, _pride_, _realization_, _relief_, _remorse_, _sadness_, _surprise_, _neutral_. |
|    TEXT_SENTIMENT     | The sentiment of the text                                |                INPUT, USER_INPUT                 |    When the data structure is text     | If the Task text language is Italian, one between these: _POSITIVE_, _NEGATIVE_. Otherwise, one between these: _negative_, _neutral_, _positive_                                                                                                                                                                                                                                                                                                                                     |
|      TEXT_LENGTH      | The length of the text                                   | INPUT, USER_INPUT, RETRIEVED_CONTEXT, PREDICTION |    When the data structure is text     | An integer value.                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|   MODEL_PERPLEXITY    | A measure of how well the LLM predicts the next words    |                    PREDICTION                    |       When the task type is RAG        | A floating point value.                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|   IMAGE_BRIGHTNESS    | The brightness of the image                              |                      INPUT                       |    When the data structure is image    | A floating point value.                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|    IMAGE_CONTRAST     | The contrast of the image                                |                      INPUT                       |    When the data structure is image    | A floating point value.                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|      BBOXES_AREA      | The average area of the predicted bounding boxes         |                    PREDICTION                    | When the task type is Object Detection | A floating point value.                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|    BBOXES_QUANTITY    | The average number of predicted bounding boxes per image |                    PREDICTION                    | When the task type is Object Detection | An integer value.                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |


### Monitoring Status

All the entities being monitored are associated with a status, which can be one of the following:

- `OK`: the entity is behaving as expected.
- `WARNING`: the entity has shown signs of drifts, but it is still within the acceptable range.
- `DRIFT`: the entity has experienced a significant change and corrective actions should be taken.

The following diagram illustrates the possible transitions between the statuses.
Each transition is triggered by a [Detection Event] and the status of the entity is updated accordingly.

<div class="mermaid-container">

```mermaid
stateDiagram-v2
    direction LR
    
    [*] --> OK : Initial State
    
    OK --> WARNING : Warning On
    WARNING --> OK : Warning Off
    
    WARNING --> DRIFT : Drift On
    DRIFT --> WARNING : Drift Off
    
    DRIFT --> OK : Drift Off
```
</div>

Notice that a drift off event can either bring the entity back to the `OK` status or to the `WARNING` status, 
depending on the velocity of the change and the monitoring algorithm's sensitivity.

You can check the status of the monitored entities in two ways:

- **WebApp**: The homepage of the task displays the status of both monitoring targets and metrics.
- **SDK**: there are a couple of methods to retrieve the status of the monitored entities programmatically. You can either get the status of a specific entity
            or retrieve the status of all the entities associated with a task.


[Task]: ../task.md
[Detection Event Rule]: detection_event_rules.md
[Detection Event]: detection_event.md
[get_task]: ../../api/python/client.md#get_task