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


## ColumnRole
```python 
ColumnRole()
```


---
Column role enum
Describe the role of a column

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
Describe data type of an input

----


## DetectionEventActionType
```python 
DetectionEventActionType()
```


---
**Fields:**

- DISCORD_NOTIFICATION
- SLACK_NOTIFICATION

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


## ModelStatus
```python 
ModelStatus()
```


---
**Fields:**

- NOT_INITIALIZED
- OK
- WARNING
- DRIFT

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


## TaskStatus
```python 
TaskStatus()
```


---
**Fields:**

- OK
- WARNING
- DRIFT

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
