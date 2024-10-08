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


## ColumnRole
```python 
ColumnRole()
```


---
Column role enum
Describe the role of a column

----


## ColumnSubRole
```python 
ColumnSubRole()
```


---
Column subrole enum
Describe the subrole of a column

----


## Currency
```python 
Currency()
```


---
Currency of to use for the Task

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

- DRIFT

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

Fields
------
RGB: Red, Green, Blue
RGBA: Red, Green, Blue, Alpha
GRAYSCALE: Grayscale

----


## JobStatus
```python 
JobStatus()
```


---
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

----


## MonitoringMetric
```python 
MonitoringMetric()
```


---
**Fields:**

- FEATURE
- TEXT_TOXICITY
- TEXT_EMOTION
- TEXT_SENTIMENT
- MODEL_PERPLEXITY

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
- USER_INPUT
- USER_INPUT_RETRIEVED_CONTEXT
- RETRIEVED_CONTEXT
- USER_INPUT_MODEL_OUTPUT
- MODEL_OUTPUT_RETRIEVED_CONTEXT

----


## ProductKeyStatus
```python 
ProductKeyStatus()
```


---
Status of a product key

Fields
------
NEW = generated but not yet used product key
VALIDATING = validation requested from client
IN_USE = validated product key, client activated

----


## RetrainTriggerType
```python 
RetrainTriggerType()
```


---
Enumeration of the possible retrain triggers

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

----


## SubscriptionType
```python 
SubscriptionType()
```


---
Type of subscription plan of a company

Fields
------
CLOUD: subscription plan for web app or sdk access
EDGE: subscription plan for edge deployment

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

----


## TextLanguage
```python 
TextLanguage()
```


---
Enumeration of text language used in nlp tasks.

Fields
------

ITALIAN
ENGLISH
MULTILANGUAGE

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
