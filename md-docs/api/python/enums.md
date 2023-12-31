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


## DatasetType
```python 
DatasetType()
```


---
**Fields:**

- TABULAR

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


## MonitoringTarget
```python 
MonitoringTarget()
```


---
**Fields:**

- MODEL
- INPUT
- CONCEPT

----


## StoragePolicy
```python 
StoragePolicy()
```


---
Enumeration that specify the storage policy for the data sent to
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
- CLASSIFICATION

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
