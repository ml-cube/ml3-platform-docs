#


## ML3PlatformClient
```python 
ML3PlatformClient(
   url: str, api_key: str
)
```


---
Client class is the single point of interaction with ML cube
Platform APIs, it is initialized providing the `url` and the User
`api_key`.
Every operation is performed verifying the API Key and the
permissions associated to the User that own that key.

### Methods categories
There are the following types of methods:

- **entity creation:** create the entity and return its identifier.
It is used in the other methods to indicate the entity.
- **entity update:** modify the entity but do not return anything.
- **entity getters:** return a Pydantic `BaseModel` with the
required entity.
- **entity show:** print to the stdout the entity, but they do not
return anything.
- **entity delete:** delete the entity
- **job submission:** submit a job on ML cube Platform that will
take some time. They return the job identifier that can be used to
monitor its state.
- **job waiters:** given a job id wait the until the job is
completed

### Exceptions
The Client class raises only exceptions that are subclasses of
`SDKClientException`.
The exception has two fields that you can share with ML cube Support
to get help in identifying the problem:

- **error_code:** unique identifier of the error
- **error_message:** message that explain the error

The page is structured in different blocks of methods, one for each
entity.


**Methods:**


### .create_company
```python
.create_company(
   name: str, address: str, vat: str
)
```

---
Create a company for the User, this method works only is the
User has not a company yet.
After the Company is created the User is the Company Owner.


**Args**

* **name**  : the name of the company
* **address**  : the address of the company
* **vat**  : the vat of the company


**Returns**

* **company_id**  : `str`


**Raises**

`CreateCompanyException`

### .get_company
```python
.get_company()
```

---
Returns the company of the User


**Returns**

* **company**  : `Company`


**Raises**

`SDKClientException`

### .update_company
```python
.update_company(
   name: (str|None), address: (str|None), vat: (str|None)
)
```

---
Update company information.

Empty values will not be updated.

**Allowed Roles**

- `COMPANY_OWNER`
- `COMPANY_ADMIN`


**Args**

* **name**  : new the of the company
* **address**  : new billing address for the company
* **vat**  : new vat of the company


**Raises**

`UpdateCompanyException`

### .create_project
```python
.create_project(
   name: str, description: (str|None), default_storage_policy: StoragePolicy
)
```

---
Create a project inside the company. You don't need to specify
the company because a User belongs only to one company and it
is retrieved automatically.

**Allowed Roles**

- `COMPANY_OWNER`
- `COMPANY_ADMIN`

**Args**

* **name**  : the name of the project
* **description**  : optional description of the project
* **default_storage_policy**  : represents the default policy to
    use for storing data in ML cube Platform


**Returns**

* **project_id**  : `str`


**Raises**

`CreateProjectException`

### .get_projects
```python
.get_projects()
```

---
Get the list of all projects in the company the User has
permissions to view.


**Returns**

* **projects_list**  : `List[Project]`


**Raises**

`SDKClientException`

### .get_project
```python
.get_project(
   project_id: str
)
```

---
Get a project with the given id

**Allowed Roles**

- At least `PROJECT_VIEW` for that project
- `COMPANY_OWNER`
- `COMPANY_ADMIN`


**Args**

* **project_id**  : project identifier


**Returns**

* **project**  : `Project`


**Raises**

`SDKClientException`

### .update_project
```python
.update_project(
   project_id: str, name: (str|None), description: (str|None),
   default_storage_policy: (StoragePolicy|None)
)
```

---
Update project details.

Empty values will not be updated.

**Allowed Roles**

- At least `PROJECT_EDIT` for that project
- `COMPANY_OWNER`
- `COMPANY_ADMIN`


**Args**

* **project_id**  : project identifier
* **name**  : new name of the project
* **description**  : new description of the project
* **default_storage_policy**  : represents the default policy to
    use for storing data in ML cube Platform


**Returns**

* **project**  : `Project`


**Raises**

`UpdateProjectException`

### .show_projects
```python
.show_projects()
```

---
Show a list all projects printing to stdout.

**Example output:**
```
Project ID                Name
------------------------  ----------
6475f8c9ebac5081e529s63f  my project
```

### .create_task
```python
.create_task(
   project_id: str, name: str, tags: list[str], task_type: TaskType,
   data_structure: DataStructure, cost_info: (TaskCostInfoUnion|None) = None,
   optional_target: bool = False, text_language: (TextLanguage|None) = None
)
```

---
Create a task inside the project.

**Allowed Roles:**

- At least `PROJECT_EDIT` for that project
- `COMPANY_OWNER`
- `COMPANY_ADMIN`

**Args**

* **project_id**  : the identifier of the project
* **name**  : the name of the task
* **tags**  : a list of tags associated with the task
* **task_type**  : the type of the task. See `TaskType`
    documentation for more information
* **data_structure**  : type of data in the task
* **cost_info**  : optional argument that specify the cost
    information of the task
* **optional_target**  : True if the target value in not always
    available. This changes the behaviour and the detection
    phase of ML cube Platform that will analyse production
    data without considering the actual target
* **text_language**  : required for NLP tasks, it specifies the
    language used in the task.


**Returns**

* **task_id**  : `str`


**Raises**

`CreateTaskException`

### .update_task
```python
.update_task(
   task_id: str, name: (str|None) = None, tags: (list[str]|None) = None,
   cost_info: (TaskCostInfoUnion|None) = None
)
```

---
Update task attributes.

`None` parameters are ignored for the update.

**Allowed Roles:**

- At least `PROJECT_EDIT` for that project
- `COMPANY_OWNER`
- `COMPANY_ADMIN`

**Args**

* **task_id**  : the identifier of the task
* **name**  : the name of the task
* **tags**  : a list of tags associated with the task. To remove
    all the tags then pass an empty list.
* **cost_info**  : optional argument that specify the cost
    information of the task


**Raises**

`UpdateTaskException`

### .get_tasks
```python
.get_tasks(
   project_id: str
)
```

---
Get the list of the Tasks inside the project.


**Args**

* **project_id**  : identifier of the project


**Returns**

* **task_list**  : `List[Task]`


**Raises**

`SDKClientException`

### .get_task
```python
.get_task(
   task_id: str
)
```

---
Get task by id.

**Allowed Roles:**

- At least `PROJECT_VIEW` for that project
- `COMPANY_OWNER`
- `COMPANY_ADMIN`


**Args**

* **task_id**  : identifier of the task


**Returns**

* **task**  : `Task`


**Raises**

`SDKClientException`

### .show_tasks
```python
.show_tasks(
   project_id: str
)
```

---
Show a list of tasks included in a project to stdout.


**Args**

* **project_id**  : the identifier of a project

---
**Example output:**
```
Task ID                   Name     Type            Status     Status start date
------------------------  -------  --------------  --------   -----------------
6476040d583201813ab4539a  my task  classification  OK         03-02-2023 10:14:06
```

### .create_model
```python
.create_model(
   task_id: str, name: str, version: str, metric_name: ModelMetricName,
   preferred_suggestion_type: SuggestionType, retraining_cost: float = 0.0,
   resampled_dataset_size: (int|None) = None
)
```

---
Create a model inside the task.

**Allowed Roles:**

- At least `PROJECT_EDIT` for that project
- `COMPANY_OWNER`
- `COMPANY_ADMIN`


**Args**

* **task_id**  : the identifier of the task
* **name**  : the name of the model
* **version**  : the current version of the model
* **metric_name**  : performance or error metric associated with
    the model
* **retraining_cost**  : estimated costs in the Task currency to
    retrain the model. This information is used by the
    retraining tool to show gain-cost information.
    Default value is 0.0 meaning that the cost is negligible
* **preferred_suggestion_type**  : preferred type of suggestion that
    will be computed to retrain the model
* **resampled_dataset_size**  : size of the resampled dataset that
    will be proposed to retrain the model
    note: this parameter is required if
    `preferred_suggestion_type` is
    `SuggestionType.RESAMPLED_DATASET`


**Returns**

* **model_id**  : `str` identifier of the created model


**Raises**

`CreateModelException`

### .get_models
```python
.get_models(
   task_id: str
)
```

---
Get all models of a task.

**Allowed Roles:**

- At least `PROJECT_VIEW` for that project
- `COMPANY_OWNER`
- `COMPANY_ADMIN`

**Args**

* **task_id**  : identifier of the task


**Returns**

* **models_list**  : `List[Model]`


**Raises**

`SDKClientException`

### .get_model
```python
.get_model(
   model_id: str
)
```

---
Get model by id.

**Allowed Roles:**

- At least `PROJECT_VIEW` for that project
- `COMPANY_OWNER`
- `COMPANY_ADMIN`

**Args**

* **model_id**  : identifier of the model


**Returns**

* **model**  : `Model`


**Raises**

`SDKClientException`

### .get_model_by_name_and_version
```python
.get_model_by_name_and_version(
   task_id: str, model_name: str, model_version: str
)
```

---
Get model by name and version.

A Model can have multiple versions according to the updates and
retraining done.
This method allow to get the Model object by specifying its
name and the version tag.

**Allowed Roles:**

- At least `PROJECT_VIEW` for that project
- `COMPANY_OWNER`
- `COMPANY_ADMIN`

**Args**

* **task_id**  : the identifier of the task
* **model_name**  : the name of the model
* **model_version**  : the version of the model


**Returns**

* **model**  : `Model`


**Raises**

`SDKClientException`

### .show_models
```python
.show_models(
   task_id: str
)
```

---
Show a list of models included in a task to stdout.

**Allowed Roles:**

- At least `PROJECT_VIEW` for that project
- `COMPANY_OWNER`
- `COMPANY_ADMIN`


**Args**

* **task_id**  : the identifier of the task

---
**Example output:**
```
Model Id                  Task Id                   Name                    Version    Status           Status start timestamp    Status insert date          Metric Name
------------------------  ------------------------  ----------------------  ---------  ---------------  ------------------------  --------------------------  --------------------
64fecf7d323311ab78f17280  64fecf7c323311ab78f17262  model_local_experiment  v0.0.1     not_initialized                            2023-09-11 08:27:41.431000  ModelMetricName.RMSE
```

### .get_suggestions_info
```python
.get_suggestions_info(
   model_id: str, model_version: str
)
```

---
Retrieve suggestions associated with a model.

**Allowed Roles:**

- At least `PROJECT_VIEW` for that project
- `COMPANY_OWNER`
- `COMPANY_ADMIN`


**Args**

* **model_id**  : the identifier of the model
* **model_version**  : the version of the model


**Returns**

* **suggestion_info_list**  : `List[SuggestionInfo]`


**Raises**

`SDKClientException`

### .show_suggestions
```python
.show_suggestions(
   model_id: str, model_version: str
)
```

---
Show the list of suggestions associated with a
model printing them to stdout.

**Allowed Roles:**

- At least `PROJECT_VIEW` for that project
- `COMPANY_OWNER`
- `COMPANY_ADMIN`


**Args**

* **model_id**  : the identifier of the model
* **model_version**  : the version of the model

---
**Example output:**
```
Suggestion Id                     Executed    Timestamp
--------------------------------  ----------  --------------------------
79a8710c351c4b6a9ece7322e153f200  True        2023-08-21 10:54:40.386189
```


**Raises**

`SDKClientException`

### .set_model_suggestion_type
```python
.set_model_suggestion_type(
   model_id: str, preferred_suggestion_type: SuggestionType,
   resampled_dataset_size: (int|None) = None
)
```

---
Set model suggestion type.

**Allowed Roles:**

- At least `PROJECT_EDIT` for that project
- `COMPANY_OWNER`
- `COMPANY_ADMIN`


**Args**

* **model_id**  : the identifier of the task
* **preferred_suggestion_type**  : preferred type of suggestion that
    will be computed to retrain the model
* **resampled_dataset_size**  : size of the resampled dataset that
    will be proposed to retrain the model
    note: this parameter is required if
    `preferred_suggestion_type` is
    `SuggestionType.RESAMPLED_DATASET`


**Raises**

`SetModelSuggestionTypeException`

### .update_model_version_by_suggestion_id
```python
.update_model_version_by_suggestion_id(
   model_id: str, new_model_version: str, suggestion_id: str
)
```

---
Update model version by suggestion id.
To retrain the Model, ML cube Platform provides importance
weights through a `SuggestionInfo`.
After the retraining is completed, you use this method to
create the new model version in ML cube Platform.
By specifying the `suggestion_id`, ML cube Platform
automatically knows which is the reference data the model is
trained on.

This request starts an operation pipeline that is
executed by ML cube Platform.
Thus, the method returns the identifier of the job that you can
monitor to know its status and proceed with the other work
using the method `wait_job_completion(job_id)`

**Allowed Roles:**

- At least `PROJECT_EDIT` for that project
- `COMPANY_OWNER`
- `COMPANY_ADMIN`


**Args**

* **model_id**  : the identifier of the model
* **new_model_version**  : the new version of the model
* **suggestion_id**  : the identifier of the suggestion


**Returns**

* **job_id**  : `str` job identifier of the pipeline in execution


**Raises**

`UpdateModelVersionException`

### .update_model_version_from_time_range
```python
.update_model_version_from_time_range(
   model_id: str, new_model_version: str, from_timestamp: float,
   to_timestamp: float
)
```

---
Update model version by specifying the time range of uploaded
data on ML cube Platform.

This request starts an operation pipeline that is
executed by ML cube Platform.
Thus, the method returns the identifier of the job that you can
monitor to know its status and proceed with the other work
using the method `wait_job_completion(job_id)`

**Allowed Roles:**

- At least `PROJECT_EDIT` for that project
- `COMPANY_OWNER`
- `COMPANY_ADMIN`


**Args**

* **model_id**  : the identifier of the model
* **new_model_version**  : the new version of the model
from_timestamp
to_timestamp


**Raises**

`UpdateModelVersionException`

---
Returns the job_id associated to the pipeline

### .add_data_schema
```python
.add_data_schema(
   task_id: str, data_schema: DataSchema
)
```

---
Associate a data schema to a task.

**Allowed Roles:**

- At least `PROJECT_EDIT` for that project
- `COMPANY_OWNER`
- `COMPANY_ADMIN`



**Args**

* **task_id**  : the identifier of the task
* **data_schema**  : the data schema that characterize your task


**Raises**

`AddDataSchemaException`

### .get_data_schema
```python
.get_data_schema(
   task_id: str
)
```

---
Get task data schema

**Allowed Roles:**

- At least `PROJECT_VIEW` for that project
- `COMPANY_OWNER`
- `COMPANY_ADMIN`


**Args**

* **task_id**  : identifier of the task


**Returns**

* **data_schema**  : `DataSchema`


**Raises**

`SDKClientException`

### .show_data_schema
```python
.show_data_schema(
   task_id: str
)
```

---
Show data schema of associated with a task

**Allowed Roles:**

- At least `PROJECT_VIEW` for that project
- `COMPANY_OWNER`
- `COMPANY_ADMIN`


**Args**

* **task_id**  : identifier of the task


**Raises**

`SDKClientException`

---
**Example output:**


    Column name       Role     Type      Nullable
    ----------------  -------  --------  ----------
    sample_id         id       string    False
    timestamp         time_id  string    False
    sepallength       input    float     False
    sepalwidth        input    float     False
    petallength       input    float     False
    petalwidth        input    float     False
    class             target   category  False

### .add_historical_data
```python
.add_historical_data(
   task_id: str, inputs: Data, target: (Data|None) = None
)
```

---
Add a batch of historical data for the Task.

This request starts an operation pipeline that is
executed by ML cube Platform.
Thus, the method returns the identifier of the job that you can
monitor to know its status and proceed with the other work
using the method `wait_job_completion(job_id)`

**Allowed Roles:**

- At least `PROJECT_EDIT` for that project
- `COMPANY_OWNER`
- `COMPANY_ADMIN`


**Args**

* **task_id**  : the identifier of the task
* **inputs**  : data object that contain input data source.
    It can be None if you upload other kinds of data
* **target**  : data object that contains target data.
    It can be None if you upload other kinds of data


**Returns**

* **job_id**  : `str` identifier of the submitted job


**Raises**

`AddHistoricalDataException`

### .add_target_data
```python
.add_target_data(
   task_id: str, target: Data
)
```

---
Add target samples for data already uploaded on the Task.
This operation is used for Tasks with optional target which is
manually labelled. For instance, fter the labelling process
(maybe with our Active Learning module) you have a set of
labelled samples spread over all the uploaded data. Indeed,
they can belong to different data batches (historical or
production consistent uploads) and can be a subset of the
uploaded data.

This request starts an operation pipeline that is
executed by ML cube Platform.
Thus, the method returns the identifier of the job that you can
monitor to know its status and proceed with the other work
using the method `wait_job_completion(job_id)`

**Allowed Roles:**

- At least `PROJECT_EDIT` for that project
- `COMPANY_OWNER`
- `COMPANY_ADMIN`


**Args**

* **task_id**  : the identifier of the task
* **target**  : data object that contains target data


**Returns**

* **job_id**  : `str` identifier of the submitted job


**Raises**

`AddHistoricalDataException`

### .set_model_reference
```python
.set_model_reference(
   model_id: str, from_timestamp: float, to_timestamp: float
)
```

---
Specify data to use as reference for the model with time range.
Data need to be already uploaded on ML cube Platform.

This request starts an operation pipeline that is
executed by ML cube Platform.
Thus, the method returns the identifier of the job that you can
monitor to know its status and proceed with the other work
using the method `wait_job_completion(job_id)`

**Allowed Roles:**

- At least `PROJECT_EDIT` for that project
- `COMPANY_OWNER`
- `COMPANY_ADMIN`


**Args**

* **model_id**  : the identifier of the model
from_timestamp
to_timestamp


**Returns**

* **job_id**  : `str` identifier of the submitted job


**Raises**

`AddModelReferenceException`

### .add_production_data
```python
.add_production_data(
   task_id: str, inputs: (Data|None) = None, target: (Data|None) = None,
   predictions: (list[tuple[str, Data]]|None) = None
)
```

---
Add a batch of production data associated with a given task.

This request starts an operation pipeline that is
executed by ML cube Platform.
Thus, the method returns the identifier of the job that you can
monitor to know its status and proceed with the other work
using the method `wait_job_completion(job_id)`

**Allowed Roles:**

- At least `PROJECT_EDIT` for that project
- `COMPANY_OWNER`
- `COMPANY_ADMIN`


**Args**

* **task_id**  : the identifier of the task
* **inputs**  : data object that contain input data source.
    It can be None if you upload other kinds of data
* **target**  : data object that contains target data.
    It can be None if you upload other kinds of data
* **predictions**  : list of data objects that contain prediction data.
    Each element is a tuple with model_id and data object.
    It can be None if you upload other kinds of data


**Returns**

* **job_id**  : `str` identifier of the submitted job


**Raises**

`AddProductionDataException`

### .create_kpi
```python
.create_kpi(
   project_id: str, name: str
)
```

---
Create a KPI.

**Allowed Roles:**

- At least `PROJECT_EDIT` for that project
- `COMPANY_OWNER`
- `COMPANY_ADMIN`


**Args**

* **project_id**  : the identifier of the project
* **name**  : the name of the kpi


**Returns**

* **kpi_id**  : `str` identifier of the created kpi


**Raises**

`CreateKpiException`

### .get_kpi
```python
.get_kpi(
   kpi_id: str
)
```

---
Get kpi by id.

**Allowed Roles:**

- At least `PROJECT_VIEW` for that project
- `COMPANY_OWNER`
- `COMPANY_ADMIN`

**Args**

* **kpi_id**  : identifier of the kpi


**Returns**

* **kpi**  : `KPI`


**Raises**

`SDKClientException`

### .get_kpis
```python
.get_kpis(
   project_id: str
)
```

---
Get all kpis of a project.

**Allowed Roles:**

- At least `PROJECT_VIEW` for that project
- `COMPANY_OWNER`
- `COMPANY_ADMIN`

**Args**

* **project_id**  : identifier of the project


**Returns**

* **kpis_list**  : `List[KPI]`


**Raises**

`SDKClientException`

### .show_kpis
```python
.show_kpis(
   project_id: str
)
```

---
Show the list of KPIs included in a project to stdout.

**Allowed Roles:**

- At least `PROJECT_VIEW` for that project
- `COMPANY_OWNER`
- `COMPANY_ADMIN`


**Args**

* **project_id**  : the identifier of the project

---
**Example output:**
```
KPI Id                    Project Id                Name                    Status           Status start timestamp    Status insert date
------------------------  ------------------------  ----------------------  ---------------  ------------------------  --------------------------
64fecf7d323311ab78f17280  64fecf7c323311ab78f17262  model_local_experiment  not_initialized                            2023-09-11 08:27:41.431000
```

### .add_kpi_data
```python
.add_kpi_data(
   project_id: str, kpi_id: str, kpi: TabularData
)
```

---
Add a batch of a given kpi with the given project.

This request starts an operation pipeline that is
executed by ML cube Platform.
Thus, the method returns the identifier of the job that you can
monitor to know its status and proceed with the other work
using the method `wait_job_completion(job_id)`

**Allowed Roles:**

- At least `PROJECT_EDIT` for that project
- `COMPANY_OWNER`
- `COMPANY_ADMIN`


**Args**

* **project_id**  : the identifier of the project
* **kpi_id**  : the identifier of the kpi
* **kpi**  : data object that contains data source.


**Returns**

* **job_id**  : `str` identifier of the submitted job


**Raises**

`AddKPIDataException`

### .compute_retraining_report
```python
.compute_retraining_report(
   model_id: str
)
```

---
Compute the retraining report for a given model

This request starts an operation pipeline that is
executed by ML cube Platform.
Thus, the method returns the identifier of the job that you can
monitor to know its status and proceed with the other work
using the method `wait_job_completion(job_id)`

**Allowed Roles:**

- At least `PROJECT_EDIT` for that project
- `COMPANY_OWNER`
- `COMPANY_ADMIN`


**Args**

* **model_id**  : the identifier of the model


**Returns**

* **job_id**  : `str` identifier of the submitted job


**Raises**

`ComputeRetrainingReportException`

### .get_retraining_report
```python
.get_retraining_report(
   model_id: str
)
```

---
For a given model id, get the sample weights computed
and additional information about them included in
the retraining report

**Allowed Roles:**

- At least `PROJECT_VIEW` for that project
- `COMPANY_OWNER`
- `COMPANY_ADMIN`


**Args**

* **model_id**  : the identifier of the model


**Returns**

* **retraining_report**  : `RetrainingReport`


**Raises**

`GetRetrainingReportException`

### .get_jobs
```python
.get_jobs(
   project_id: (str|None) = None, task_id: (str|None) = None,
   model_id: (str|None) = None, status: (JobStatus|None) = None,
   job_id: (str|None) = None
)
```

---
Get current jobs information.
Jobs can be filtered by project_id, task_id, model_id or status.

**Allowed Roles:**

- At least `PROJECT_VIEW` for that project
- `COMPANY_OWNER`
- `COMPANY_ADMIN`


**Args**

* **project_id**  : the project_id to filter job.
    If ``None`` job of every project will be returned
* **task_id**  : the task_id to filter job.
    If ``None`` job of every task will be returned
* **model_id**  : the model_id to filter job.
    If ``None`` job of every model will be returned
* **status**  : the status to filter job.
    If ``None`` job with every status will be retrieved
* **job_id**  : id of the job to filter.
    If ``None`` job with every id will be retrieved


**Returns**

* **jobs_list**  : `List[Job]`


**Raises**

`SDKClientException`

### .get_job
```python
.get_job(
   job_id: str
)
```

---
Get current job information.

**Allowed Roles:**

- At least `PROJECT_VIEW` for that project
- `COMPANY_OWNER`
- `COMPANY_ADMIN`


**Args**

* **job_id**  : id of the job to retrieve


**Returns**

* **job**  : `Job`


**Raises**

`SDKClientException`

### .show_jobs
```python
.show_jobs()
```

---
Show current job information to stdout.

**Allowed Roles:**

- At least `PROJECT_VIEW` for that project
- `COMPANY_OWNER`
- `COMPANY_ADMIN`


**Raises**

`SDKClientException`

### .get_detection_events
```python
.get_detection_events(
   task_id: str
)
```

---
Get all detection event of a given task.

**Allowed Roles:**

- At least `PROJECT_VIEW` for that project
- `COMPANY_OWNER`
- `COMPANY_ADMIN`


**Args**

* **task_id**  : id of the task for which you want to retrieve
the detection event


**Returns**

* **rules_list**  : `List[DetectionEvent]`


**Raises**

`SDKClientException`

### .get_detection_event_rules
```python
.get_detection_event_rules(
   task_id: str
)
```

---
Get all detection event rules of a given task.

**Allowed Roles:**

- At least `PROJECT_VIEW` for that project
- `COMPANY_OWNER`
- `COMPANY_ADMIN`


**Args**

* **task_id**  : id of the task for which you want to retrieve
the detection event rules


**Returns**

* **rules_list**  : `List[DetectionEventRule]`


**Raises**

`SDKClientException`

### .get_detection_event_rule
```python
.get_detection_event_rule(
   rule_id: str
)
```

---
Get a detection event rule by id.

**Allowed Roles:**

- At least `PROJECT_VIEW` for that project
- `COMPANY_OWNER`
- `COMPANY_ADMIN`


**Args**

* **rule_id**  : id of the rule


**Returns**

* **rule**  : `DetectionEventRule`


**Raises**

`SDKClientException`

### .create_detection_event_rule
```python
.create_detection_event_rule(
   name: str, task_id: str, severity: DetectionEventSeverity,
   detection_event_type: DetectionEventType, monitoring_target: MonitoringTarget,
   actions: list[DetectionEventAction],
   monitoring_metric: (MonitoringMetric|None) = None, model_name: (str|None) = None
)
```

---
Create a detection event rule.

**Allowed Roles:**

- At least `PROJECT_EDIT` for that project
- `COMPANY_OWNER`
- `COMPANY_ADMIN`


**Args**

* **name**  : the name of the rule
* **task_id**  : the id of the task to which the rule belongs.
    The rule will only respond to detection events
    generated by this task.
* **model_name**  : the name of the model, only required if
    monitoring_target is set to MODEL.
* **detection_event_type**  : the type of detection event that
    this rule should respond to.
* **monitoring_target**  : the type of monitoring target that
    this rule should respond to.
* **monitoring_metric**  : additional metric extracted from
    monitoring target that is monitored
* **severity**  : the level of severity of the detection event
    that this rule should respond to.
* **actions**  : the list of actions to execute, in order,
    when the conditions of the rule are matched.


**Returns**

* **rule_id**  : `str`


**Raises**

`CreateDetectionEventRuleException`

### .update_detection_event_rule
```python
.update_detection_event_rule(
   rule_id: str, name: (str|None) = None, model_name: (str|None) = None,
   severity: (DetectionEventSeverity|None) = None,
   detection_event_type: (DetectionEventType|None) = None,
   monitoring_target: (MonitoringTarget|None) = None,
   actions: (list[DetectionEventAction]|None) = None
)
```

---
Update a detection event rule.

**Allowed Roles:**

- At least `PROJECT_EDIT` for that project
- `COMPANY_OWNER`
- `COMPANY_ADMIN`


**Args**

* **rule_id**  : the id of the rule to update
* **name**  : the name of the rule. If None, keeps the existing value.
* **model_name**  : the name of the model, only required if
    monitoring_target is set to MODEL.
    If None, keeps the existing value.
* **detection_event_type**  : the type of detection event that this
    rule should respond to. If None, keeps the existing value.
* **monitoring_target**  : the type of monitoring target that this
    rule should respond to. If None, keeps the existing value.
* **severity**  : the level of severity of the detection event that
    this rule should respond to. If None, keeps the
    existing value.
* **actions**  : the list of actions to execute, in order, when the
    conditions of the rule are matched. If None,
     keeps the existing value.


**Raises**

`CreateDetectionEventRuleException`

### .delete_detection_event_rule
```python
.delete_detection_event_rule(
   rule_id: str
)
```

---
Delete a detection event rule by id.

**Allowed Roles:**

- At least `PROJECT_EDIT` for that project
- `COMPANY_OWNER`
- `COMPANY_ADMIN`


**Args**

* **rule_id**  : id of the rule to delete


**Raises**

`SDKClientException`

### .wait_job_completion
```python
.wait_job_completion(
   job_id: str, max_wait_timeout: int = 3000
)
```

---
Wait that the ML cube Platform job terminates successfully its
execution.

Note that this method stops the execution.

**Allowed Roles:**

- At least `PROJECT_VIEW` for that project
- `COMPANY_OWNER`
- `COMPANY_ADMIN`


**Args**

* **job_id**  : identifier of the job
* **max_wait_timeout**  : maximum amount of seconds to wait before
    launching `JobWaitTimeoutException`


**Raises**


- `JobWaitTimeoutException` when the maximum timeout time
    is reached
- `JobNotFoundException` when the requested job does not
    exist
- `JobFailureException` when the requested job is failed

### .create_company_user
```python
.create_company_user(
   name: str, surname: str, username: str, password: str, email: str,
   company_role: UserCompanyRole
)
```

---
Creates a new User in the company.

**Allowed Roles:**

- `COMPANY_OWNER`


**Args**

* **name**  : name of the user
* **surname**  : surname of the user
* **username**  : username of the user
* **password**  : temporary password for the user. It will change
    this at the first login
* **email**  : email of the user
* **company_role**  : role of the user inside the company


**Returns**

* **user_id**  : `str`


**Raises**

`SDKClientException`

### .get_company_users
```python
.get_company_users()
```

---
Returns the list of users in the company.

**Allowed Roles:**

- `COMPANY_OWNER`
- `COMPANY_ADMIN`
- `COMPANY_USER`


**Returns**

* **users_list**  : `List[CompanyUser]`


**Raises**

`SDKClientException`

### .change_user_company_role
```python
.change_user_company_role(
   user_id: str, company_role: UserCompanyRole
)
```

---
Change the company role of a user in the company.

**Allowed Roles:**

- `COMPANY_OWNER`: can change the roles of all the Users
    Users apart from other Admins and the Owner


**Args**

* **user_id**  : the user for which the role is updated
* **company_role**  : the new role to assign


**Raises**

`SDKClientException`

### .show_company_users
```python
.show_company_users()
```

---
Show company users to stdout.

**Allowed Roles:**

- `COMPANY_OWNER`
- `COMPANY_ADMIN`
- `COMPANY_USER`


**Raises**

`SDKClientException`

### .get_user_projects
```python
.get_user_projects(
   user_id: str
)
```

---
Returns a list of projects that the user can view.

**Allowed Roles:**

- `COMPANY_OWNER`
- `COMPANY_ADMIN`
- `COMPANY_USER`


**Args**

* **user_id**  : the user for which you want to see the list


**Returns**

* **projects_list**  : `List[Project]`


**Raises**

`SDKClientException`

### .show_user_projects
```python
.show_user_projects(
   user_id: str
)
```

---
Shows the projects that the user can view to stdout.

**Allowed Roles:**

- `COMPANY_OWNER`
- `COMPANY_ADMIN`
- `COMPANY_USER`


**Args**

* **user_id**  : the user for which you want to see the list


**Raises**

`SDKClientException`

### .add_user_project_role
```python
.add_user_project_role(
   user_id: str, project_id: str, project_role: UserProjectRole
)
```

---
Add a project role to the user for the given project.

The User Project role can be assigned only to `COMPANY_USER`
because Admin and Owner already have all the permission over
projects.

**Allowed Roles:**

- `COMPANY_OWNER`
- `COMPANY_ADMIN`


**Args**

* **user_id**  : the user for which you want to see the list
* **project_id**  : identifies the project
* **project_role**  : the project role to assign


**Raises**

`SDKClientException`

### .delete_project_role
```python
.delete_project_role(
   user_id: str, project_id: str
)
```

---
Delete the role of the user for the given project.

The User Project role can be deleted only for `COMPANY_USER`
because Admin and Owner have all the permission over projects.

**Allowed Roles:**

- `COMPANY_OWNER`
- `COMPANY_ADMIN`


**Args**

* **user_id**  : the user for which you want to see the list
* **project_id**  : identifies the project


**Raises**

`SDKClientException`

### .get_api_keys
```python
.get_api_keys()
```

---
Returns a list of api keys the user has.

**Allowed Roles:**

- `COMPANY_USER`


**Returns**

* **api_keys_list**  : `List[ApiKey]`


**Raises**

`SDKClientException`

### .show_api_keys
```python
.show_api_keys()
```

---
Shows the list of api keys the user has to stdout.

**Allowed Roles:**

- `COMPANY_USER`


**Raises**

`SDKClientException`

### .create_api_key
```python
.create_api_key(
   name: str, expiration_time: ApiKeyExpirationTime
)
```

---
Create a new api key for the user

**Allowed Roles:**

- `COMPANY_USER`


**Returns**

* **name**  : the name of the api key
* **expiration_time**  : the expiration time of the api key


**Raises**

`SDKClientException`

### .delete_api_key
```python
.delete_api_key(
   api_key: str
)
```

---
Delete the api key of the user

**Allowed Roles:**

- `COMPANY_USER`


**Args**

* **api_key**  : api key to delete


**Raises**

`SDKClientException`

### .get_user_api_keys
```python
.get_user_api_keys(
   user_id: str
)
```

---
Get the list of api keys a user has.

**Allowed Roles:**

- `COMPANY_OWNER`
- `COMPANY_ADMIN`


**Args**

* **user_id**  : the user to get his api keys


**Raises**

`SDKClientException`

### .show_user_api_keys
```python
.show_user_api_keys(
   user_id: str
)
```

---
Shows the list of api keys a user has to stdout.

**Allowed Roles:**

- `COMPANY_OWNER`
- `COMPANY_ADMIN`


**Args**

* **user_id**  : the user to get his api keys


**Raises**

`SDKClientException`

### .create_user_api_key
```python
.create_user_api_key(
   user_id: str, name: str, expiration_time: ApiKeyExpirationTime
)
```

---
Create a new api key for the user.

**Allowed Roles:**

- `COMPANY_OWNER`
- `COMPANY_ADMIN`


**Args**

* **user_id**  : the user to create a new api key
* **name**  : the name of the api key
* **expiration_time**  : the expiration time of the api key


**Returns**

* **api_key**  : the new created api key for the user


**Raises**

`SDKClientException`

### .delete_user_api_key
```python
.delete_user_api_key(
   user_id: str, api_key: str
)
```

---
Delete the api key of the user

**Allowed Roles:**

- `COMPANY_OWNER`
    Admin


**Args**

* **user_id**  : the user to delete an api key
* **api_key**  : the api key to delete


**Raises**

`SDKClientException`

### .change_company_owner
```python
.change_company_owner(
   user_id: str
)
```

---
Change the company owner role from the requesting user to the
other user.

**Allowed Roles:**

- `COMPANY_OWNER`


**Args**

* **user_id**  : the user that become Company Owner


**Raises**

`SDKClientException`

### .delete_company_user
```python
.delete_company_user(
   user_id: str
)
```

---
 Delete a user from the company.

**Allowed Roles:**

- `COMPANY_OWNER`
- `COMPANY_ADMIN`: cannot delete other company admins


**Args**

* **user_id**  : the user to delete


**Raises**

`SDKClientException`

### .get_integration_credentials
```python
.get_integration_credentials(
   credentials_id: str
)
```

---
Get the credentials with the given id for 3rd party service
provider integration.

**Allowed Roles:**

- At least `WORK_ON_PROJECT` for the project where the
credentials have been configured
- `COMPANY_OWNER`
- `COMPANY_ADMIN`


**Args**

* **credentials_id**  : id of the integration credentials to
retrieve.


**Returns**

* **credentials**  : `IntegrationCredentials`


**Raises**

`SDKClientException`

### .get_all_project_integration_credentials
```python
.get_all_project_integration_credentials(
   project_id: str
)
```

---
Get the list of credentials for 3rd party service provider
integrations that are currently configured in a project.

**Allowed Roles:**

- At least `WORK_ON_PROJECT` for that project
- `COMPANY_OWNER`
- `COMPANY_ADMIN`


**Args**

* **project_id**  : id of the project for which all configured
credentials should be retrieved.


**Returns**

* **credentials_list**  : `List[IntegrationCredentials]`


**Raises**

`SDKClientException`

### .delete_integration_credentials
```python
.delete_integration_credentials(
   credentials_id: str
)
```

---
 Delete credentials for the integration with a 3rd party
 service provider.

**Allowed Roles:**

- At least `UPDATE_PROJECT_INFORMATION` for the project
where the credentials have been configured
- `COMPANY_OWNER`
- `COMPANY_ADMIN`: cannot delete other company admins


**Args**

* **credentials_id**  : id of the integration credentials to
delete.


**Raises**

`SDKClientException`

### .set_integration_credentials_as_default
```python
.set_integration_credentials_as_default(
   credentials_id: str
)
```

---
 Set the credentials with the given id as default for 3rd party
 service provider integration.

**Allowed Roles:**

- At least `UPDATE_PROJECT_INFORMATION` for the project
where the credentials have been configured
- `COMPANY_OWNER`
- `COMPANY_ADMIN`


**Args**

* **credentials_id**  : id of the integration credentials to
set as default.


**Raises**

`SDKClientException`

### .create_aws_integration_credentials
```python
.create_aws_integration_credentials(
   name: str, default: bool, project_id: str, role_arn: str
)
```

---
Create credentials to integrate with AWS. Returns an object
that contains the external_id you will need to configure in
your trust policy.

**Allowed Roles:**

- At least `UPDATE_PROJECT_INFORMATION` for the project
- `COMPANY_OWNER`
- `COMPANY_ADMIN`


**Args**

* **name**  : a simple name to identify this set of credentials
* **default**  : whether to use these credentials by default when
    using an AWS integration
* **project_id**  : the project in which these credentials will
    be configured
* **role_arn**  : the ARN of the IAM role that will be assumed by ML
    cube Platform


**Returns**

* **credentials**  : `SecretAWSCredentials`


**Raises**

`SDKClientException`

### .create_gcp_integration_credentials
```python
.create_gcp_integration_credentials(
   name: str, default: bool, project_id: str, service_account_info_json: str
)
```

---
Create credentials to integrate with GCP.

**Allowed Roles:**

- At least `UPDATE_PROJECT_INFORMATION` for the project
- `COMPANY_OWNER`
- `COMPANY_ADMIN`


**Args**

* **name**  : a simple name to identify this set of credentials
* **default**  : whether to use these credentials by default when
    using an AWS integration
* **project_id**  : the project in which these credentials will
    be configured
* **service_account_info_json**  : the json-encoded string
    containing the key of the service account


**Returns**

* **credentials**  : `GCPCredentials`


**Raises**

`SDKClientException`

### .create_azure_integration_credentials
```python
.create_azure_integration_credentials(
   name: str, default: bool, project_id: str,
   service_principal_credentials_json: str
)
```

---
Create credentials to integrate with Azure.

**Allowed Roles:**

- At least `UPDATE_PROJECT_INFORMATION` for the project
- `COMPANY_OWNER`
- `COMPANY_ADMIN`


**Args**

* **name**  : a simple name to identify this set of credentials
* **default**  : whether to use these credentials by default when
    using an AWS integration
* **project_id**  : the project in which these credentials will
    be configured
* **service_principal_credentials_json**  : the json-encoded string
    containing the credentials of the service principal


**Returns**

* **credentials**  : `AzureCredentials`


**Raises**

`SDKClientException`

### .set_retrain_trigger
```python
.set_retrain_trigger(
   model_id: str, trigger: (RetrainTrigger|None)
)
```

---
Set the retrain trigger for a given model.

**Allowed Roles:**

- At least `WORK_ON_PROJECT` for the project
- `COMPANY_OWNER`
- `COMPANY_ADMIN`


**Args**

* **model_id**  : the id of the model
* **trigger**  : the trigger to set. If you want to remove the
    trigger, set it to None


**Raises**

`SDKClientException`

### .test_retrain_trigger
```python
.test_retrain_trigger(
   model_id: str, trigger: RetrainTrigger
)
```

---
Test the retrain trigger for a given model.


**Allowed Roles:**

- At least `WORK_ON_PROJECT` for the project
- `COMPANY_OWNER`
- `COMPANY_ADMIN`


**Args**

* **model_id**  : the id of the model
* **trigger**  : the trigger to test


**Raises**

`SDKClientException`

### .retrain_model
```python
.retrain_model(
   model_id: str
)
```

---
Retrain a model via the configured retrain trigger.

**Allowed Roles:**

- At least `WORK_ON_PROJECT` for the project
- `COMPANY_OWNER`
- `COMPANY_ADMIN`


**Args**

* **model_id**  : the id of the model


**Raises**

`SDKClientException`
