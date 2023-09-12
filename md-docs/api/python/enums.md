#


## TaskType
```python 
TaskType()
```


---
**Fields:**

- REGRESSION
- CLASSIFICATION

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


## DatasetType
```python 
DatasetType()
```


---
**Fields:**

- TABULAR

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


## DetectionEventActionType
```python 
DetectionEventActionType()
```


---
**Fields:**

- DISCORD_NOTIFICATION
- SLACK_NOTIFICATION

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
