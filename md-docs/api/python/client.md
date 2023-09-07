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
The there are the following types of methods:

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
   name: Optional[str], address: Optional[str], vat: Optional[str]
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
   name: str, description: Optional[str]
)
```

---
Create a project inside the company. You don't need to specify
the company because a User belong only to one company and it
is retrieved automatically.

**Allowed Roles**

- `COMPANY_OWNER`
- `COMPANY_ADMIN`

**Args**

* **name**  : the name of the project
* **description**  : optional description of the project


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
   project_id: str, name: Optional[str], description: Optional[str]
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
   project_id: str, name: str, tags: List[str], task_type: TaskType
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


**Returns**

* **task_id**  : `str`


**Raises**

`CreateTaskException`

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
   task_id: str, name: str, version: str
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
Model ID                  Name        Version    Status     Status start date
------------------------  ----------  ---------  --------   -----------------
64760430583201813ab4ad1e  model_name  v1.0       OK         03-02-2023 10:14:06
```

### .get_suggestions
```python
.get_suggestions(
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

* **suggestion_list**  : `List[Suggestion]`


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

### .update_model_version_by_suggestion_id
```python
.update_model_version_by_suggestion_id(
   model_id: str, new_model_version: str, suggestion_id: str
)
```

---
Update model version by suggestion id.
To retrain the Model, ML cube Platform provides importance
weights through a `Suggestion`.
After the retraining is completed, you use this method to
create the new model version in ML cube Platform.
By specifying the `suggestion_id`, ML cube Platform
automatically knows which is the reference data the model is
trained on.

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

### .update_model_version_from_raw_data
```python
.update_model_version_from_raw_data(
   model_id: str, new_model_version: str, dataset_type: DatasetType, data_path: str
)
```

---
Update model version by suggestion id.
To retrain the Model, ML cube Platform provides importance
weights through a `Suggestion`.
However, it is possible to train the model with new data that
has been not already upload to ML cube Platform.
After the retraining is completed, you use this method to
create the new model version in ML cube Platform by
specifying the data to load.

**Allowed Roles:**

- At least `PROJECT_EDIT` for that project
- `COMPANY_OWNER`
- `COMPANY_ADMIN`


**Args**

* **model_id**  : the identifier of the model
* **new_model_version**  : the new version of the model
* **dataset_type**  :  Dataset type describes the nature
               of data stored (DatasetType)
* **data_path**  : path to the csv file containing the data
           which will be used as new reference


**Returns**

* **job_id**  : `str` job identifier of the pipeline in execution


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

### .update_data_schema
```python
.update_data_schema(
   task_id: str, data_schema: DataSchema
)
```

---
Update an existing data schema

**Allowed Roles:**

- At least `PROJECT_EDIT` for that project
- `COMPANY_OWNER`
- `COMPANY_ADMIN`



**Args**

* **task_id**  : the identifier of the task
* **data_schema**  : the set of new columns that should be added to the data schema


**Raises**

`UpdateDataSchemaException`

### .add_historical_data
```python
.add_historical_data(
   task_id: str, dataset_type: DatasetType, data_path: str
)
```

---
Add a batch of historical data


**Args**

* **task_id**  : the identifier of the task
* **dataset_type**  :  Dataset type describes the nature of data stored (DatasetType)
* **data_path**  : path to the csv file containing the historical data

---
Returns the job_id associated to the pipeline

### .add_model_reference
```python
.add_model_reference(
   model_id: str, dataset_type: DatasetType, data_path: str
)
```

---
Add a batch of reference data associated with a given model


**Args**

* **model_id**  : the identifier of the model
* **dataset_type**  :  Dataset type describes the nature of data stored (DatasetType)
* **data_path**  : path to the csv file containing the reference data

---
Returns the job_id associated to the pipeline

### .add_production_data
```python
.add_production_data(
   task_id: str, dataset_type: DatasetType, data_path: str
)
```

---
Add a batch of production data associated with a given task


**Args**

* **task_id**  : the identifier of the task
* **dataset_type**  :  Dataset type describes the nature of data stored (DatasetType)
* **data_path**  : path to the csv file containing the production data

---
Returns the job_id associated to the pipeline

### .compute_importance_weights
```python
.compute_importance_weights(
   model_id: str, model_version: str
)
```

---
For a given model version, get the importance weights
with the possibility to specify a retrain_event_id.


**Args**

* **model_id**  : the identifier of the task
* **model_version**  : the version of the model

---
It returns the job_id associated to the job that computes the
weights

### .get_importance_weights
```python
.get_importance_weights(
   model_id: str, model_version: str
)
```

---
For a given model version, get the importance weights
with the possibility to specify a retrain_event_id.


**Args**

* **model_id**  : the identifier of the task
* **model_version**  : the version of the model


### .get_jobs
```python
.get_jobs(
   project_id: Optional[str] = None, task_id: Optional[str] = None,
   model_id: Optional[str] = None, status: Optional[JobStatus] = None,
   job_id: Optional[str] = None
)
```

---
Get current jobs information.
Jobs can be filtered by project_id, task_id, model_id or status


**Args**

* **project_id**  : the project_id to filter job. If ``None`` job of every project will be returned
* **task_id**  : the task_id to filter job. If ``None`` job of every task will be returned
* **model_id**  : the model_id to filter job. If ``None`` job of every model will be returned
* **status**  : the status to filter job. If ``None`` job with every status will be retrieved
* **job_id**  : id of the job to filter. If ``None`` job with every id will be retrieved


### .get_job
```python
.get_job(
   job_id: str
)
```

---
Get current job information.


**Args**

* **job_id**  : id of the job to retrieve


### .show_jobs
```python
.show_jobs()
```

---
Show current job information.
Jobs can be filtered by project_id, task_id, model_id or status


**Args**

* **project_id**  : the project_id to filter job. If ``None`` job of every project will be returned
* **task_id**  : the task_id to filter job. If ``None`` job of every task will be returned
* **model_id**  : the model_id to filter job. If ``None`` job of every model will be returned
* **status**  : the status to filter job. If ``None`` job with every status will be retrieved
* **job_id**  : id of the job to filter. If ``None`` job with every id will be retrieved


### .get_detection_event_rules
```python
.get_detection_event_rules(
   task_id: str
)
```

---
Get all detection event rules of a given task.


**Args**

* **task_id**  : id of the task for which you want to retrieve
the detection event rules

### .get_detection_event_rule
```python
.get_detection_event_rule(
   rule_id: str
)
```

---
Get a detection event rule by id.


**Args**

* **rule_id**  : id of the rule


### .create_detection_event_rule
```python
.create_detection_event_rule(
   name: str, task_id: str, model_id: str, severity: DetectionEventSeverity,
   detection_event_type: DetectionEventType, monitoring_target: MonitoringTarget,
   actions: List[Union[DiscordNotificationAction, SlackNotificationAction]]
)
```

---
Create a detection event rule.


**Args**

* **name**  : the name of the rule
* **task_id**  : the id of the task to which the rule belongs.
* **model_id**  : the id of the model, only required if event_type
* **detection_event_type**  : the type of detection event that this
* **monitoring_target**  : the type of monitoring target that this
* **severity**  : the level of severity of the detection event that
* **actions**  : the list of actions to execute, in order, when the

The rule will only respond to detection events generated by
this task.

is set to PERFORMANCE.

rule should respond to.

rule should respond to.

this rule should respond to.

conditions of the rule are matched.

### .update_detection_event_rule
```python
.update_detection_event_rule(
   rule_id: str, name: Optional[str] = None, model_id: Optional[str] = None,
   severity: Optional[DetectionEventSeverity] = None,
   detection_event_type: Optional[DetectionEventType] = None,
   monitoring_target: Optional[MonitoringTarget] = None,
   actions: Optional[List[Union[DiscordNotificationAction,
   SlackNotificationAction]]] = None
)
```

---
Update a detection event rule.


**Args**

* **rule_id**  : the id of the rule to update
* **name**  : the name of the rule.
* **model_id**  : the id of the model, only required if event_type
* **detection_event_type**  : the type of detection event that this
* **monitoring_target**  : the type of monitoring target that this
* **severity**  : the level of severity of the detection event that
* **actions**  : the list of actions to execute, in order, when the

If None, keeps the existing value.

is set to PERFORMANCE. If None, keeps the existing value.

rule should respond to. If None, keeps the existing value.

rule should respond to. If None, keeps the existing value.

this rule should respond to. If None, keeps the existing
value.

conditions of the rule are matched. If None, keeps the
existing value.

### .delete_detection_event_rule
```python
.delete_detection_event_rule(
   rule_id: str
)
```

---
Delete a detection event rule by id.


**Args**

* **rule_id**  : id of the rule to delete


### .wait_job_completion
```python
.wait_job_completion(
   job_id: str, max_wait_timeout: int = 600
)
```


### .delete_company
```python
.delete_company()
```


### .create_company_user
```python
.create_company_user(
   name: str, surname: str, username: str, password: str, email: str,
   company_role: UserCompanyRole
)
```

---
TODO

### .remove_user_from_company
```python
.remove_user_from_company(
   user_id: str
)
```

---
TODO

### .add_user_to_company
```python
.add_user_to_company(
   user_id: str
)
```

---
TODO

### .get_company_users
```python
.get_company_users()
```

---
TODO

### .change_user_company_role
```python
.change_user_company_role(
   user_id: str, company_role: UserCompanyRole
)
```

---
TODO

### .show_company_users
```python
.show_company_users()
```

---
TODO

### .get_user_projects
```python
.get_user_projects(
   user_id: str
)
```

---
TODO

### .show_user_projects
```python
.show_user_projects(
   user_id: str
)
```

---
TODO

### .add_user_project_role
```python
.add_user_project_role(
   user_id: str, project_id: str, project_role: UserProjectRole
)
```

---
TODO

### .delete_project_role
```python
.delete_project_role(
   user_id: str, project_id: str
)
```

---
TODO

### .get_api_keys
```python
.get_api_keys()
```

---
TODO

### .show_api_keys
```python
.show_api_keys()
```

---
TODO

### .create_api_key
```python
.create_api_key()
```

---
TODO

### .delete_api_key
```python
.delete_api_key(
   api_key: str
)
```

---
TODO

### .get_user_api_keys
```python
.get_user_api_keys(
   user_id: str
)
```

---
TODO

### .show_user_api_keys
```python
.show_user_api_keys(
   user_id: str
)
```

---
TODO

### .create_user_api_key
```python
.create_user_api_key(
   user_id: str
)
```

---
TODO

### .delete_user_api_key
```python
.delete_user_api_key(
   user_id: str, api_key: str
)
```

---
TODO

### .change_company_owner
```python
.change_company_owner(
   user_id: str
)
```

---
TODO

### .delete_company_user
```python
.delete_company_user(
   user_id: str
)
```

---
TODO
