#


## Company
```python 
Company()
```


---
Company model


**Attributes**

* **company_id**  : str
* **name**  : str
* **address**  : str
* **vat**  : str


----


## Project
```python 
Project()
```


---
Project model


**Attributes**

* **project_id**  : str
* **name**  : str


----


## Task
```python 
Task()
```


---
Task model


**Attributes**

* **task_id**  : str
* **name**  : str
* **type**  : TaskType
* **status**  : TaskStatus
* **status_start_date**  : str


----


## Model
```python 
Model()
```


---
Base model to define model item


**Attributes**

* **model_id**  : str
* **task_id**  : str
* **name**  : str
* **version**  : str
* **status**  : ModelStatus
* **status_data_start_timestamp**  : Optional[datetime]
* **status_insert_datetime**  : datetime
* **metric_name**  : performance or error metric associated with
    the model


----


## Job
```python 
Job()
```


---
Job information item model


**Attributes**

* **job_id**  : str
* **job_group**  : str
* **project_id**  : str
* **project_name**  : str
* **task_id**  : str
* **task_name**  : str
* **model_id**  : Optional[str]
* **model_name**  : Optional[str]
* **status**  : str
* **error**  : Optional[str]


----


## ColumnInfo
```python 
ColumnInfo()
```


---
Column base model


**Attributes**

* **name**  : str
* **data_type**  : str
* **role**  : str
* **is_nullable**  : bool
* **predicted_target**  : Optional[str] = None
* **possible_values**  : Optional[List] = None
* **model_id**  : Optional[str] = None


----


## DataSchema
```python 
DataSchema()
```


---
Data schema base model


**Attributes**

* **columns**  : List[ColumnInfo]


----


## Suggestion
```python 
Suggestion()
```


---
Suggestion base model


**Attributes**

* **id**  : str
* **executed**  : bool
* **timestamp**  : str


----


## RetrainingReport
```python 
RetrainingReport()
```


---
base model for Retraining Report


**Attributes**

* **report_id**  : str
* **sample_ids**  : List[str]
* **sample_weights**  : List[float]
* **effective_sample_size**  : float
* **model_metric_name**  : str
* **upper_bound**  : float
* **lower_bound**  : float


----


## CompanyUser
```python 
CompanyUser()
```


---
base model for company user


**Attributes**

* **user_id**  : str
* **company_role**  : UserCompanyRole


----


## ApiKey
```python 
ApiKey()
```


---
base model for api key


**Attributes**

* **api_key**  : str


----


## DetectionEventAction
```python 
DetectionEventAction()
```


---
Generic action that can be performed


**Attributes**

* **type**  : DetectionEventActionType


----


## DiscordNotificationAction
```python 
DiscordNotificationAction()
```


---
Action that sends a notification to a Discord server through
a webhook that you configure


**Attributes**

* **webhook**  : str
type = DetectionEventActionType.DISCORD_NOTIFICATION

----


## SlackNotificationAction
```python 
SlackNotificationAction()
```


---
Action that sends a notification to a Slack channel through
a webhook that you configure.


**Attributes**

* **webhook**  : str
* **channel**  : str
type = DetectionEventActionType.SLACK_NOTIFICATION

----


## DetectionEventRule
```python 
DetectionEventRule(
   **kwargs
)
```


---
A rule that can be triggered by a detection event, and executes
a series of actions.


**Attributes**

* **rule_id**  : str
* **name**  : str
* **task_id**  : str
* **model_id**  : Optional[str]
* **severity**  : DetectionEventSeverity
* **detection_event_type**  : DetectionEventType
* **monitoring_target**  : MonitoringTarget
* **actions**  : List[DetectionEventAction]


----


## IntegrationCredentials
```python 
IntegrationCredentials()
```


---
Credentials to authenticate to a 3rd party service provider
via an integration.


**Attributes**

* **credentials_id**  : str
* **name**  : str
* **default**  : bool
* **type**  : ExternalIntegration


----


## AWSCredentials
```python 
AWSCredentials()
```


---
AWS integration credentials.


**Attributes**

* **credentials_id**  : str
* **name**  : str
* **default**  : bool
* **type**  : ExternalIntegration
* **role_arn**  : The ARN of the role that should be assumed via STS


----


## SecretAWSCredentials
```python 
SecretAWSCredentials()
```


---
AWS integration credentials, that also include the external_id
you need to set up the trust policy on AWS.


**Attributes**

* **credentials_id**  : str
* **name**  : str
* **default**  : bool
* **type**  : ExternalIntegration
* **role_arn**  : The ARN of the IAM role that should be assumed
* **external_id**  : Secret key used to assume the IAM role via STS



**Methods:**


### .generate_trust_policy
```python
.generate_trust_policy()
```

---
Generates a JSON trust policy that you can copy into the IAM
role on AWS.

----


## DataSource
```python 
DataSource()
```


---
Generic data source.


**Attributes**

* **dataset_type**  : DatasetType


----


## LocalDataSource
```python 
LocalDataSource()
```


---
Use this data source if you want to upload a file from your
local disk to the ML cube platform cloud.


**Attributes**

* **file_path**  : str


----


## RemoteDataSource
```python 
RemoteDataSource()
```


---
A source that identifies where data is stored.


**Attributes**

* **credentials_id**  : str


----


## S3DataSource
```python 
S3DataSource()
```


---
A source that identifies a file in an S3 bucket.


**Attributes**

* **object_path**  : str

