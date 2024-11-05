# Data Schema

Data schema contains all the information about the data in the [Task], it is created at the beginning and is immutable.

!!! tip
    Data Schema can be easily created starting from a template from the Web App. Go in Data Schema page after you created a Task and see the precompiled version of Data Schema, update and insert new Columns to create your custom version.

A Data schema is composed of a list of objects named _Column_ that represent each data entity in the Task.
The number and type of Column objects depend on the task type and task data structure.

A Column object has some mandatory attributes and others that depends on its role or data type:

| Attribute  | Description | Mandatory | 
| --------- | ------- | ------ |
| Name      | Name of the entity used to read it from raw data. For instance, in Tabular tasks, it represents the name of the column of the CSV file. | Mandatory |
| Data type | Data format of the entity. Possible values are <br><ul><li>Float: numeric value</li><li>Categorical: entity that can assume a only specified values. A Categorical Column requires the attribute _possible_values_ to be specified.</li><li>String: generic textual data like text input or customer id. To not be used for categorical columns.</li><li>Array 1: one-dimensional array. Requires _dims_ attribute to be defined like a list of 1 element \[n\] that specifies the number of elements of the array.</li><li>Array 2: two-dimensional array. Requires _dims_ attribute to be defined like a list of 2 elements \[n, m\] that specifies the number elements of the each dimension of the array.</li><li>Array 3: three-dimensional array. Requires _dims_ attribute to be defined like a list of 3 elements \[n, m, k\] that specifies the number elements of the each dimension of the array.</li></ul> | Mandatory |
| Role | Defines the role the Column object has in the Task. According to the Task type some roles are required or not allowed. More information in the following sections. | Mandatory |
| Subrole | Additional specification of the role in the Task. Some entities belong to the same Role but have different meanings, the Subroles allows to distinguish between them. More information in the following sections. | Depends on Task Type |
| Is Nullable | If the entity allows missing values. | Mandatory |
| Dims | List with the number of elements each dimension of the array has. The value -1 indicates that that dimension can have an arbitrary number of elements. | Required when Data Type is Array |
| Possible values | List of values the categorical variable can assume. They can be either strings or numbers. When Task Type is Classification Multilabel and Role is Target, possibile values must be \[0, 1\] indicating the presence or not of that class. | Mandatory when Column Data Type is Categorical |
| Classes Names | Names of the classes in the Task. The length of this list must match the length of the Dims of the array. | Required when Column Role is Target and Task Type is Classification Multilabel.|
|Image Mode| Type of image, it can be RGB, RGBA, GRAYSCALE. It also determines the Data Type, which is Array 3 for RBG and RGBA and Array 2 for GRAYSCALE. | Required when Column Role is Input and Data Structure is Image.|


## Role

The Role defines what the Column object represents for the Task.
Roles are used by ML cube Platform to correctly use provided data.
Some Roles are needed to uniquely identify a sample, other to retrieve the correct information.
Moreover, some Roles must be inserted by you when creating the Data Schema the first time, while others, like the model predictions, are created automatically by ML cube Platform.

User defined roles are:

|Role|Data Type| Description | Mandatory
|--|--|--|--|
|ID|String| Unique identifier of the sample. It is used during data validation to avoid duplicates of data and to communicate information about data with you without sending the actual data| It must be always present when sending data to ML cube Platform. |
| Time ID | Float | Timestamp of the sample expressed in seconds (for that reason it is a Float). It is used to temporally order samples maintaining coherence in the analysis of ML cube Platform.|It must be always present when sending data to ML cube Platform. |
| Input | Any available Data Type | Represents input data like a single feature for Tabular tasks or image in Image tasks or text in Text tasks | According to Task Type the number of Input Column object varies from 1 to illimitate. See Section [Data schema templates](data_schema.md#data-schema-templates)|
| Target | Any available Data Type. It must be coherent with Task Type | Represents the true value of the sample in supervised tasks.| It is mandatory for supervised tasks. |
| Input additional embedding | Array 1 | Embedding vector of the Input Column. It is allowed only then Data Structure of Task is Image or Text. When this Column object is present, ML cube Platform uses it as numerical representation of the data, otherwise, it uses an internal embedding algorithm. | It is optional since it depends on your choice to share with ML cube Platform this type of data.|
| Target additional embedding | Array 1 | Embedding vector of the Target Column. It is allowed only then Task Type is RAG. When this Column object is present, ML cube Platform uses it as numerical representation of the data, otherwise, it uses an internal embedding algorithm. | It is optional since it depends on your choice to share with ML cube Platform this type of data.|

ML cube Platform defined roles are:

|Role| Data Type | Description |
| --| --| --|
| Prediction | Same Data Type of Target Column | Prediction Column object automatically created when the Task [Model] is created. The name has the fixed template: <MODEL_NAME\>\@<MODEL_VERSION\>|
| Prediction additional embedding | Array 1 | Embedding vector of the Prediction Column. It is allowed only then Task Type is RAG. When this Column object is present, ML cube Platform uses it as numerical representation of the data, otherwise, it uses an internal embedding algorithm. | It is created automatically by ML cube Platform if Column Object with Role Target additional embedding is present. The name has fixed template: <MODEL_NAME\>_embeddings\@<MODEL_VERSION\>|

## Subrole

Some tasks can have different data entities for the same Role, the Column object's attribute Subrole helps to specify the correct type of data.

| Subrole | Associated Role | Data Type | Description |
| --|--|--|--|
| RAG User Input | INPUT | String | In RAG Tasks it is the user query submitted to the system. |
| RAG Retrieved Context | INPUT | String | In RAG Tasks it is the retrieved contexts (separated with the Task attribute *context separator*) that the retrieval system has selected to answer the query.|
| Model probability | PREDICTION | Depends on Task Type:<br><ul><li>RAG: Array 1</li><li>Classification Binary: Float</li><li>Classification Multiclass: Array 1</li><li>Classification Multilabel: Array 1</li></ul> | It is automatically created by ML cube Platform when the created Model has the flag additional probabilistic output set as True. The name has fixed template: <MODEL_NAME\>_probability\@<MODEL_VERSION\>.| 
| Object detection prediction label| PREDICTION | Array 1 | It is automatically created when Task Type is Object detection. It is an array with length equal to the number of predicted bounding boxes where each element contains the class label assigned to the bounding box. The name has a fixed template: <MODEL_NAME\>_predicted_labels\@<MODEL_VERSION\>.|
| Object detection target label| TARGET | Array 1 | It is mandatory when Task Type is Object detection. It is an array with length equal to the number of actual bounding boxes where each element contains the class label assigned to the bounding box. |

## Data schema constraints

Each combination of Task Type and Data Structure leads to different Data Schema requirements that must be satisfied when it is created for the Task.
For instance, image binary classification tasks requires only one input column object with image data type and target column object must be categorical with only two possible values.

Here the list of constraints about quantities for each Role:

{{ read_excel('../tables/data schema validation.xlsx', engine='openpyxl', sheet_name='qts') }}

Here the list of constraints about Data Types for each Role:

{{ read_excel('../tables/data schema validation.xlsx', engine='openpyxl', sheet_name='types') }}


[Task]: task.md
[Model]: model.md