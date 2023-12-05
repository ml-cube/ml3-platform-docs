#


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


## AWSEventBridgeRetrainTrigger
```python 
AWSEventBridgeRetrainTrigger()
```


---
Base model to define an AWS EventBridge retrain trigger

Fields:
type
credentials_id
credentials_name
aws_region_name
event_bus_name

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


## AzureBlobDataSource
```python 
AzureBlobDataSource()
```


---
A source that identifies a blob in Azure Storage.


**Attributes**

* **object_path**  : str


----


## AzureCredentials
```python 
AzureCredentials()
```


---
Azure integration credentials.


**Attributes**

* **app_id**  : The id of the service principal


----


## ClassificationTaskCostInfo
```python 
ClassificationTaskCostInfo()
```


---
Regression cost info is expressed in two terms:
- cost due to overestimation
- cost due to underestimation

Both terms have tolerance threshold that allows to ignore the costs
if the overestimation is lower than that specific value

Fields:
currency
false_positive_cost
false_negative_cost
false_positive_threshold:
    maximum value for which the cost of a false positive is
    negligible
false_negative_threshold:
    maximum value for which the cost of a false negative is
    negligible

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


## DataSchema
```python 
DataSchema()
```


---
Data schema base model


**Attributes**

* **columns**  : List[ColumnInfo]


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


## DetectionEventAction
```python 
DetectionEventAction()
```


---
Generic action that can be performed


**Attributes**

* **type**  : DetectionEventActionType


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
* **model_name**  : Optional[str]
* **severity**  : DetectionEventSeverity
* **detection_event_type**  : DetectionEventType
* **monitoring_target**  : MonitoringTarget
* **actions**  : List[DetectionEventAction]


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


## EmailNotificationAction
```python 
EmailNotificationAction()
```


---
Base Model for Email Notification Action


**Attributes**

* **address**  : str
type = DetectionEventActionType.EMAIL_NOTIFICATION

----


## GCPCredentials
```python 
GCPCredentials()
```


---
GCP integration credentials.


**Attributes**

* **credentials_id**  : str
* **name**  : str
* **default**  : bool
* **type**  : ExternalIntegration
* **gcp_project_id**  : The id of the project on GCP
* **client_email**  : The email that identifies the service account
* **client_id**  : The client id


----


## GCSDataSource
```python 
GCSDataSource()
```


---
A source that identifies a file in a GCS bucket.


**Attributes**

* **object_path**  : str


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


## KPI
```python 
KPI()
```


---
KPI base model


**Attributes**

* **kpi_id**  : str
* **name**  : str
* **status**  : ModelStatus
* **status_kpi_start_timestamp**  : Optional[datetime]
* **status_insert_datetime**  : datetime


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
* **status_data_start_timestamp**  : Optional[str]
* **status_insert_datetime**  : datetime
* **metric_name**  : performance or error metric associated with
    the model
* **creation_datetime**  : Optional[datetime]
* **retrain_trigger**  : Optional[RetrainTrigger]


----


## PredictionDataSourceInfo
```python 
PredictionDataSourceInfo()
```


---
Base model to define the relationship
between a model and its prediction file

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


## RegressionTaskCostInfo
```python 
RegressionTaskCostInfo()
```


---
Regression cost info is expressed in two terms:
- cost due to overestimation
- cost due to underestimation

Both terms have tolerance threshold that allows to ignore the costs
if the overestimation is lower than that specific value.

Fields:
currency
overestimation_cost
underestimation_cost
overestimation_threshold:
    maximum value for which the cost of a overestimation is
    negligible
underestimation_threshold:
    maximum value for which the cost of a underestimation is
    negligible

----


## RemoteDataSource
```python 
RemoteDataSource()
```


---
A source that identifies where data is stored.


**Attributes**

* **credentials_id**  : The id of the credentials to use to authenticate
to the remote data source. If None, the default will be used

----


## RetrainAction
```python 
RetrainAction()
```


---
Base Model for Retrain Action


**Attributes**

* **type**  : DetectionEventActionType.RETRAIN
* **model_name**  : str


----


## RetrainTrigger
```python 
RetrainTrigger()
```


---
Base model to define a retrain trigger

Fields:
type
credentials_id

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


## S3DataSource
```python 
S3DataSource()
```


---
A source that identifies a file in an S3 bucket.


**Attributes**

* **object_path**  : str


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


## TaskCostInfo
```python 
TaskCostInfo()
```


---
Base class for task cost info.
It depends on TaskType because classification is different from
regression in terms of business costs due to errors

----


## TeamsNotificationAction
```python 
TeamsNotificationAction()
```


---
Base Model for Teams Notification Action


**Attributes**

* **type**  : DetectionEventActionType.TEAMS_NOTIFICATION
* **webhook**  : str

