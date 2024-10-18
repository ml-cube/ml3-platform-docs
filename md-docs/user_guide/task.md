# Task

A Task is the third and last organizational entity in ML cube Platform.
A Task represents an ordinary artificial intelligence task like regression, classification, text generation or object detection.

A Task is associated with a [Model] that provides an output from input data and a [Data schema] that describes all the information about the data.

A Task is described by a set of attributes that vary according to its type.
Common attributes for every Task are:

| Attribute | Description |
|--|--|
| Name | Name of the Task, unique for the Project. |
| Tags | Optional customizable list of tags. It is used to better describe the Task and to improve search. |
| Task type | Artificial intelligence type of Task. Possible values are:<br><ul><li>[Regression](task.md#regression)</li><li>[Binary classification](task.md#classification)</li><li>[Multiclass classification](task.md#classification)</li><li>[Multilabel classification](task.md#classification)</li><li>[Retrieval Augmented Generation](task.md#retrieval-augmented-generation)</li><li>[Object Detection](task.md#object-detection)</li></ul>|
| Data structure | Type of input data the Task uses. Possible values are:<br><ul><li>Tabular</li><li>Image</li><li>Text: when data structure is Text, attribute *Text Language* is required.</li><li>Embeddings: input data are arrays that could represent embedding either image or text data. This data structure is used when raw data are not shared with ML cube Platform.</li></ul> |
|Optional target| Boolean value that specifies if the ground truth is always available or not. In some Tasks, the actual value is not present until explicit labeling is done. In this cases, the Task is marked as with optional target so that ML cube Platform works accordingly. |
| Cost info | Optional information about costs that depend on Task Type. |


## Data structure support
|Task type| Tabular | Image | Text | Embedding|
| -- | -- | -- | -- | -- |
| Regression | :material-check: | :material-check: | :material-check: | :material-check: |
| Classification | :material-check: | :material-check: | :material-check: | :material-check: |
| RAG | :material-close: | :material-close: | :material-check: | :material-check: |
| Object Detection | :material-close: | :material-check: | :material-close: | :material-check: |


## Regression

Supervised regression Task with continuous target.

### Cost information
Cost information is expressed by two proportional coefficients $c_{o}$ and $c_{u}$:

- $c_{o}$ is the cost of overestimating the target value, i.e., when $\hat{y} > y$
- $c_{u}$ is the cost of underestimating the target value. i.e., when $\hat{y} < y$

Given a data batch, the mean cost $\bar{C}$ is expressed as 
$$
\bar{C} = \frac{\sum_{i | \delta_i < 0} \delta_i \times c_{o} + \sum_{i | \delta_i > 0} \delta_i \times c_{u}}{N}
$$
where $\delta_i = y_i - \hat{y}_i$ is the different between the target and the estimated value.


## Classification

Supervised classification Task with discrete target.
Classification Tasks divides in:

- **Binary:** when then target is a binary variable. For binary classification tasks additional *positive class* attribute must be specified indicating which value is considered as the positive one. For instance, in fraud detection classification task "1" can represent that the sample is a fraud, while "0" when it is not. In that case positive class attribute is "1".
- **Multiclass:** when the target is a categorical variable with more than two possible values but only one value can be assigned.
- **Multilabel:** when the target is an array indicating which of the possible categories are present. In this case, each element can be either 0 or 1, and more than one element of the array can be 1.

### Cost information
Cost information differs from each of the three classification types, however, the concept is similar.
A cost is associated to every misclassification possibility:

- **Binary:**
    - $c_{FP}$ is the cost of classifying a negative sample as positive
    - $c_{FN}$ is the cost of classifying a positive sample as negative

    Given a data batch, the mean cost $\bar{C}$ is expressed as 
$$
\bar{C} = \frac{N_{FP} \times c_{FP} + N_{FN} \times c_{FN}}{N}
$$
where $N_{FP}$ and $N_{FN}$ are the number of false positives and false negatives respectively.

- **Multiclass:**
    - $c_{k}$ is the cost of misclassifying a sample which actual class is $k$ with another class

    Given a data batch, the mean cost $\bar{C}$ is expressed as 
$$
\bar{C} = \frac{\sum_{k} N_{k} \times c_{k} }{N}
$$
where $N_{k}$ is the number of misclassified samples of class $k$.


- **Multilabel:**
    - $c_{FP}^{k}$ is the cost of classifying a sample as class $k$ when the actual class $k$ is not present
    - $c_{FN}^{k}$ is the cost of not classifying a sample as class $k$ when the actual class $k$ is present

    Given a data batch, the mean cost $\bar{C}$ is expressed as 
$$
\bar{C} = \frac{\sum_{k} N_{FP}^{k} \times c_{FP}^{k} + N_{FN}^{k} \times c_{FN}^{k}}{N}
$$
where $N_{FP}^{k}$ and $N_{FN}^{k}$ are the number of false positives and false negatives of class $k$ respectively


## Retrieval Augmented Generation

Retrieval Augmented Generation is a particular AI task for Text data based on Large Language Models to generate responses of user query using a set of retrieved documents as context to generate a precise and more focused response.

RAG Tasks, do not have a Target therefore, the attribute *optional target* is always set to True.
Moreover, in this Task, the Target is a text as well and the input is composed of two entities:

- User Input: the user query that the model needs to answer
- Retrieved Context: the set of documents the retrieval engine selected to help the model

RAG tasks has additional attribute *context separator* which is string used to separate different retrieved contexts into chunks. Context data is sent as a single string, however, in RAG settings multiple documents can be retrieved. In this case, context separator is used to distinguish them. It is optional since a single context can be provided.

## Object Detection

Object Detection task processes images and provides as output a list of bounding boxes with associated label indicating the type of identified entity.
Therefore, target is a list of four elements tuples indicating the vertex of the box and a string label for the entity type.

[Model]: model.md
[Data schema]: data_schema.md