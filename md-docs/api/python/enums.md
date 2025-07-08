#


## ApiKeyExpirationTime
```python 
ApiKeyExpirationTime()
```


---
**Fields:**

- ONE_MONTH
- THREE_MONTHS
- SIX_MONTHS
- ONE_YEAR
- NEVER

----


## BaseML3Enum
```python 
BaseML3Enum()
```


---
Base class for all enums in the ML3 Platform SDK

----


## BooleanLicenceFeature
```python 
BooleanLicenceFeature()
```


---
Boolean licence feature

**Fields:**
- EXPLAINABILITY
    Whether the company has access to explainability reports
- MONITORING
    Whether the company has monitoring feature enabled
- MONITORING_METRICS
    Whether the company has monitoring metrics feature enabled
- SEGMENTED_MONITORING
    Whether the company has segmented monitoring feature enabled
- RETRAINING
    Whether the company has retraining feature enabled
- TOPIC_ANALYSIS
    Whether the company has topic analysis feature enabled
- RAG_EVALUATION
    Whether the company has RAG evaluation feature enabled
- LLM_SECURITY
    Whether the company has LLM security feature enabled
- BUSINESS
    Whether the company has business feature enabled

----


## ColumnRole
```python 
ColumnRole()
```


---
Column role enum
Describe the role of a column

**Fields:**
- INPUT
- INPUT_MASK
- METADATA
- PREDICTION
- TARGET
- ERROR
- ID
- TIME_ID
- INPUT_ADDITIONAL_EMBEDDING
- TARGET_ADDITIONAL_EMBEDDING
- PREDICTION_ADDITIONAL_EMBEDDING
- USER_INPUT
- RETRIEVED_CONTEXT

----


## ColumnSubRole
```python 
ColumnSubRole()
```


---
Column subrole enum
Describe the subrole of a column

Subroles for ColumnRole.INPUT in RAG settings:

- RAG_USER_INPUT
- RAG_RETRIEVED_CONTEXT
- RAG_SYS_PROMPT

Subroles for ColumnRole.PREDICTION:

- MODEL_PROBABILITY
- OBJECT_LABEL_PREDICTION

Subroles for ColumnRole.TARGET:

- OBJECT_LABEL_TARGET

----


## Currency
```python 
Currency()
```


---
Currency of to use for the Task

**Fields:**
- EURO
- DOLLAR

----


## DataStructure
```python 
DataStructure()
```


---
Represents the typology of the data to send

**Fields:**

- TABULAR
- IMAGE
- TEXT
- EMBEDDING

----


## DataType
```python 
DataType()
```


---
Data type enum
Describe data type of input

**Fields:**
- FLOAT
- STRING
- CATEGORICAL
- ARRAY_1
- ARRAY_2
- ARRAY_3

----


## DetectionEventActionType
```python 
DetectionEventActionType()
```


---
**Fields:**

- DISCORD_NOTIFICATION
- SLACK_NOTIFICATION
- EMAIL_NOTIFICATION
- TEAMS_NOTIFICATION
- MQTT_NOTIFICATION
- RETRAIN
- NEW_PLOT_CONFIGURATION

----


## DetectionEventSeverity
```python 
DetectionEventSeverity()
```


---
**Fields:**

- LOW
- MEDIUM
- HIGH

----


## DetectionEventType
```python 
DetectionEventType()
```


---
**Fields:**

- WARNING_OFF
- WARNING_ON
- DRIFT_ON
- DRIFT_OFF

----


## ExternalIntegration
```python 
ExternalIntegration()
```


---
An integration with a 3rd party service provider

**Fields:**
- AWS
- GCP
- AZURE
- AWS_COMPATIBLE

----


## FileType
```python 
FileType()
```


---
**Fields:**

- CSV
- JSON
- PARQUET
- PNG
- JPG
- NPY

----


## FolderType
```python 
FolderType()
```


---
Type of folder

**Fields**

- UNCOMPRESSED
- TAR
- ZIP

----


## ImageMode
```python 
ImageMode()
```


---
Image mode enumeration

**Fields:**
- RGB
- RGBA
- GRAYSCALE

----


## JobStatus
```python 
JobStatus()
```


---
Enum containing all the job's status that a client can see

 **Fields:**

- IDLE
- STARTING
- RUNNING
- COMPLETED
- ERROR

----


## KPIStatus
```python 
KPIStatus()
```


---
**Fields:**

- NOT_INITIALIZED
- OK
- WARNING
- DRIFT

----


## ModelMetricName
```python 
ModelMetricName()
```


---
Name of the model metrics that is associated with the model

**Fields:**
- RMSE
- RSQUARE
- ACCURACY
- AVERAGE_PRECISION

----


## MonitoringMetric
```python 
MonitoringMetric()
```


---
Tabular:
- FEATURE

---
Text:
    - TEXT_TOXICITY
    - TEXT_EMOTION
    - TEXT_SENTIMENT
    - TEXT_LENGTH

Model probabilistic output:
    - MODEL_PERPLEXITY
    - MODEL_ENTROPY

Image:
    - IMAGE_BRIGHTNESS
    - IMAGE_CONTRAST
    - IMAGE_FOCUS
    - IMAGE_BLUR
    - IMAGE_COLOR_VARIATION
    - IMAGE_COLOR_CONTRAST

Object detection and semantic segmentation:
        (position wrt Cartesian axis with origin in the center of the image)

----


## MonitoringStatus
```python 
MonitoringStatus()
```


---
**Fields:**

- OK
- WARNING
- DRIFT

----


## MonitoringTarget
```python 
MonitoringTarget()
```


---
**Fields:**

- ERROR
- INPUT
- CONCEPT
- PREDICTION
- INPUT_PREDICTION
- USER_INPUT
- RETRIEVED_CONTEXT
- USER_INPUT_RETRIEVED_CONTEXT
- USER_INPUT_MODEL_OUTPUT
- MODEL_OUTPUT_RETRIEVED_CONTEXT

----


## NumericLicenceFeature
```python 
NumericLicenceFeature()
```


---
Numeric licence feature

**Fields:**
- MAX_TASKS
    Maximum number of tasks that the company can have
- MAX_USERS
    Maximum number of users that the company can have
- DAILY_DATA_BATCH_UPLOAD
    Maximum number of data batches that the company can upload
    in a day. Only considers production data batches.

----


## ProductKeyStatus
```python 
ProductKeyStatus()
```


---
Status of a product key

**Fields:**:
- NEW = generated but not yet used product key
- VALIDATING = validation requested from client
- IN_USE = validated product key, client activated

----


## RetrainTriggerType
```python 
RetrainTriggerType()
```


---
Enumeration of the possible retrain triggers

**Fields:**:
- AWS_EVENT_BRIDGE
- GCP_PUBSUB
- AZURE_EVENT_GRID

----


## SegmentOperator
```python 
SegmentOperator()
```


---
Segment operator for segmentation rules.
**Fields:**
- IN: the given rule is verified if the field is in the list of values
- OUT: the given rule is verified if the field is not in the list of values

----


## SemanticSegTargetType
```python 
SemanticSegTargetType()
```


---
Format of the target and prediction for the semantic segmentation
task.

POLYGON: each identified object is represented by the vertices of
the polygon

----


## StoragePolicy
```python 
StoragePolicy()
```


---
Enumeration that specifies the storage policy for the data sent to
ML cube Platform

**Fields:**
    cloud
    it needs to read data

----


## StoringDataType
```python 
StoringDataType()
```


---
**Fields:**

- HISTORICAL
- REFERENCE
- PRODUCTION
- KPI

----


## SubscriptionType
```python 
SubscriptionType()
```


---
Type of subscription plan of a company

**Fields:**:
- CLOUD: subscription plan for web app or sdk access
- EDGE: subscription plan for edge deployment

----


## SuggestionType
```python 
SuggestionType()
```


---
Enum to specify the preferred
type of suggestion

**Fields:**
- SAMPLE_WEIGHTS
- RESAMPLED_DATASET

----


## TaskType
```python 
TaskType()
```


---
**Fields:**

- REGRESSION
- CLASSIFICATION_BINARY
- CLASSIFICATION_MULTICLASS
- CLASSIFICATION_MULTILABEL
- RAG
- OBJECT_DETECTION
- SEMANTIC_SEGMENTATION

----


## TextLanguage
```python 
TextLanguage()
```


---
Enumeration of text language used in nlp tasks.

**Fields:**
- ITALIAN
- ENGLISH
- MULTILANGUAGE

----


## UserCompanyRole
```python 
UserCompanyRole()
```


---
**Fields:**

- COMPANY_OWNER
- COMPANY_ADMIN
- COMPANY_USER
- COMPANY_NONE

----


## UserProjectRole
```python 
UserProjectRole()
```


---
**Fields:**

- PROJECT_ADMIN
- PROJECT_USER
- PROJECT_VIEW
