#


## AWSCompatibleCredentials
```python 
AWSCompatibleCredentials()
```


---
AWS-compatible integration credentials.


**Attributes**

* **credentials_id**  : str
* **name**  : str
* **default**  : bool
* **type**  : ExternalIntegration
* **access_key_id**  : The access key id
* **endpoint_url**  : The endpoint url (if any)


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


## AWSEventBridgeRetrainTrigger
```python 
AWSEventBridgeRetrainTrigger()
```


---
Base model to define an AWS EventBridge retrain trigger

Fields:
type
credentials_id
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
* **name**  : str
* **expiration_time**  : str | None


----


## AzureBlobDataSource
```python 
AzureBlobDataSource()
```


---
A source that identifies a blob in Azure Storage.


**Attributes**

* **file_type**  : FileType
* **is_folder**  : bool
* **folder_type**  : FolderType | None
* **credentials_id**  : The id of the credentials to use to authenticate
    to the remote data source. If None, the default will be used
* **object_path**  : str



**Methods:**


### .get_path
```python
.get_path()
```


### .get_source_type
```python
.get_source_type()
```


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


## AzureEventGridRetrainTrigger
```python 
AzureEventGridRetrainTrigger()
```


---
Base model to define an Azure EventGrid retrain trigger

Fields:
type
credentials_id
topic_endpoint

----


## BinaryClassificationTaskCostInfo
```python 
BinaryClassificationTaskCostInfo()
```


---
Binary classification cost info is expressed in two terms:
- cost of false positive
- cost of false negative

----


## ColumnInfo
```python 
ColumnInfo()
```


---
Column base model


**Attributes**

* **name**  : str
* **role**  : ColumnRole
* **is_nullable**  : bool
* **data_type**  : DataType
* **predicted_target**  : Optional[str] = None
* **possible_values**  : Optional[list[str | int | bool]] = None
* **model_id**  : Optional[str] = None
* **dims**  : Optional[tuple[int]] = None
    it is mandatory when data_type is Array
* **classes_names**  : Optional[list[str]] = None
    it is mandatory when the column is the target
    in multilabel classification tasks
* **subrole**  : Optional[ColumnSubRole] = None
    Indicates the subrole of the column. It's used in
    RAG tasks to define the role of the input columns
    (e.g. user input or retrieved context)
* **image_mode**  : Optional[ImageMode] = None
    Indicates the mode of the image. It must be provided
    when the data type is an image


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


## Data
```python 
Data()
```


---
Generic data model that contains all information about a data


**Attributes**

* **data_structure**  : DataStructure
* **source**  : DataSource


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

* **file_type**  : FileType
* **is_folder**  : bool
* **folder_type**  : FolderType | None


----


## DetectionEvent
```python 
DetectionEvent()
```


---
An event created during the detection process.


**Attributes**

* **event_id**  : str
* **event_type**  : DetectionEventType
* **monitoring_target**  : MonitoringTarget
* **monitoring_metric**  : MonitoringMetric | None
* **severity_type**  : Optional[DetectionEventSeverity]
* **insert_datetime**  : str
* **sample_timestamp**  : float
* **sample_customer_id**  : str
* **model_id**  : Optional[str]
* **model_name**  : Optional[str]
* **model_version**  : Optional[str]
* **user_feedback**  : Optional[bool]
* **specification**  : Optional[str]


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


## EmbeddingData
```python 
EmbeddingData()
```


---
Embedding data model i.e., a data that can be represented via
DataFrame and is stored in formats like: csv, parquet, json.
There is only one input that has type array_1


**Attributes**

* **data_structure**  : DataStructure = DataStructure.EMBEDDING
* **source**  : DataSource


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


## GCPPubSubRetrainTrigger
```python 
GCPPubSubRetrainTrigger()
```


---
Base model to define a GCP PubSub retrain trigger

Fields:
type
credentials_id
topic_name

----


## GCSDataSource
```python 
GCSDataSource()
```


---
A source that identifies a file in a GCS bucket.


**Attributes**

* **file_type**  : FileType
* **is_folder**  : bool
* **folder_type**  : FolderType | None
* **credentials_id**  : The id of the credentials to use to authenticate
    to the remote data source. If None, the default will be used
* **object_path**  : str



**Methods:**


### .get_path
```python
.get_path()
```


### .get_source_type
```python
.get_source_type()
```


----


## ImageData
```python 
ImageData()
```


---
Image data model i.e., images, text or other. Since it is
composed of multiple files, it needs a mapping between customer ids
and those files


**Attributes**

* **data_structure**  : DataStructure = DataStructure.IMAGE
* **source**  : DataSource
* **mapping_source**  : DataSource
* **embedding_source**  : DataSource | None


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


## LLMPrompt
```python 
LLMPrompt()
```


---
Base model to define llm prompts


**Attributes**

* **role**  : str
* **task**  : str
* **behavior_guidelines**  : str
* **security_guidelines**  : str


----


## LLMSpecs
```python 
LLMSpecs()
```


---
Base model to define llm specs


**Attributes**

* **llm**  : str
* **temperature**  : float
* **prompt**  : LLMPrompt


----


## LocalDataSource
```python 
LocalDataSource()
```


---
Use this data source if you want to upload a file from your
local disk to the ML cube platform cloud.


**Attributes**

* **file_type**  : FileType
* **is_folder**  : bool
* **folder_type**  : FolderType | None
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
* **metric_name**  : performance or error metric associated with
    the model
* **creation_datetime**  : Optional[datetime]
* **retrain_trigger**  : Optional[RetrainTrigger]
* **retraining_cost**  : float
* **llm_specs**  : Optional[LLMSpecs]


----


## MonitoringQuantityStatus
```python 
MonitoringQuantityStatus()
```


---
Base model to store the monitoring status
of a monitoring quantity (target or metric)


**Attributes**

* **monitoring_target**  : MonitoringTarget
* **status**  : MonitoringStatus
* **monitoring_metric**  : MonitoringMetric | None


----


## MqttNotificationAction
```python 
MqttNotificationAction()
```


---
Base Model for Mqtt Notification Action


**Attributes**

* **type**  : DetectionEventActionType.MQTT_NOTIFICATION
* **connection_string**  : str
* **topic**  : str
* **payload**  : str


----


## MulticlassClassificationTaskCostInfo
```python 
MulticlassClassificationTaskCostInfo()
```


---
Multiclass classification cost info is expressed in terms of
the misclassification costs for each class

----


## MultilabelClassificationTaskCostInfo
```python 
MultilabelClassificationTaskCostInfo()
```


---
Multilabel classification cost info is expressed in terms of
false positive and false negative costs for each class

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

Fields:
currency
overestimation_cost
underestimation_cost

----


## RemoteDataSource
```python 
RemoteDataSource()
```


---
A source that identifies where data is stored.


**Attributes**

* **file_type**  : FileType
* **is_folder**  : bool
* **folder_type**  : FolderType | None
* **credentials_id**  : The id of the credentials to use to authenticate
    to the remote data source. If None, the default will be used



**Methods:**


### .get_path
```python
.get_path()
```

---
Return the path of the object

### .get_source_type
```python
.get_source_type()
```

---
Returns raw data source type

----


## ResampledDatasetSuggestion
```python 
ResampledDatasetSuggestion()
```


---
ResampledDatasetSuggestion base model


**Attributes**

* **suggestion_id**  : str
* **suggestion_type**  : SuggestionType
* **sample_ids**  : List[str]
* **sample_counts**  : List[int]


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
* **suggestion**  : Suggestion
* **effective_sample_size**  : float
* **model_metric_name**  : str
* **performance_upper_bound**  : float
* **performance_lower_bound**  : float
* **cost_upper_bound**  : float
* **cost_lower_bound**  : float


----


## S3DataSource
```python 
S3DataSource()
```


---
A source that identifies a file in an S3 bucket.


**Attributes**

* **file_type**  : FileType
* **is_folder**  : bool
* **folder_type**  : FolderType | None
* **credentials_id**  : The id of the credentials to use to authenticate
    to the remote data source. If None, the default will be used
* **object_path**  : str



**Methods:**


### .get_path
```python
.get_path()
```


### .get_source_type
```python
.get_source_type()
```


----


## SampleWeightsSuggestion
```python 
SampleWeightsSuggestion()
```


---
SampleWeightsSuggestion base model


**Attributes**

* **suggestion_id**  : str
* **suggestion_type**  : SuggestionType
* **sample_ids**  : List[str]
* **sample_weights**  : List[float]


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


## SubscriptionPlanInfo
```python 
SubscriptionPlanInfo()
```


---
Data model for a subscription plan
Permission limit set to None means no limit is set
Expiration date set to None means no expiration is set
Product key data are set only if a product key is associated to the
subscription plan


**Attributes**

* **subscription_id**  : str
* **type**  : SubscriptionType
* **max_tasks**  : int | None
* **max_users**  : int | None
* **monitoring**  : bool
* **explainability**  : bool
* **retraining**  : bool
* **is_active**  : bool
* **start_date**  : date
* **expiration_date**  : date | None
* **product_key**  : str | None
* **product_key_status**  : ProductKeyStatus | None


----


## Suggestion
```python 
Suggestion()
```


---
Suggestion base model


**Attributes**

* **suggestion_id**  : str
* **suggestion_type**  : SuggestionType
* **sample_ids**  : List[str]


----


## SuggestionInfo
```python 
SuggestionInfo()
```


---
SuggestionInfo base model


**Attributes**

* **id**  : str
* **executed**  : bool
* **timestamp**  : float


----


## TabularData
```python 
TabularData()
```


---
Tabular data model i.e., a data that can be represented via
DataFrame and is stored in formats like: csv, parquet, json


**Attributes**

* **data_structure**  : DataStructure = DataStructure.TABULAR
* **source**  : DataSource


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
* **cost_info**  : TaskCostInfoUnion | None = None
* **optional_target**  : bool
* **monitoring_targets**  : list[MonitoringTarget]
* **monitoring_metrics**  : (
    None
    | dict[MonitoringTarget, list[tuple[MonitoringMetric, str | None]]]
* **monitoring_status**  : list[MonitoringQuantityStatus]
) = None

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


## TaskLlmSecReportItem
```python 
TaskLlmSecReportItem()
```


---
Task LLM security report item model.
It contains the most important information of
a LLM security report.


**Attributes**

* **id**  : str
* **creation_date**  : datetime
* **name**  : str
* **status**  : JobStatus
* **from_datetime**  : datetime
* **to_datetime**  : datetime


----


## TaskRagEvalReportItem
```python 
TaskRagEvalReportItem()
```


---
base model for Rag Evaluation Report


**Attributes**

* **id**  : str
* **creation_datetime**  : datetime
* **name**  : str
* **status**  : JobStatus
* **from_datetime**  : datetime
* **to_datetime**  : datetime


----


## TaskTopicModelingReportDetails
```python 
TaskTopicModelingReportDetails()
```


---
Task Topic Modeling Report Details base model


**Attributes**

* **sample_ids**  : list[str]
* **topics**  : list[str]


----


## TaskTopicModelingReportItem
```python 
TaskTopicModelingReportItem()
```


---
Task Topic Modeling Report Item base model


**Attributes**

* **id**  : str
* **creation_datetime**  : datetime
* **name**  : str
* **status**  : JobStatus
* **from_date**  : datetime
* **to_date**  : datetime


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


----


## TextData
```python 
TextData()
```


---
Text data model for nlp tasks.


**Attributes**

* **data_structure**  : DataStructure = DataStructure.TEXT
* **source**  : DataSource
* **embedding_source**  : DataSource | None

