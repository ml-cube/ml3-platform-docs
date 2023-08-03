#
 

## ML3PlatformClient
```python 
ML3PlatformClient(
   url: str = '', api_key: str = ''
)
```


---
Client for interacting with ML3Platform APIs


**Methods:**


### .create_company
```python
.create_company(
   name: str, address: str, vat: str
)
```

---
Create a company


**Args**

* **name**  : the name of the company
* **address**  : the address of the company
* **vat**  : the vat of the company


**Returns**

the company id associated with the new company (string)

### .get_company
```python
.get_company()
```

---
# TODO sistemare doc
Get company


**Returns**

the company

### .update_company
```python
.update_company(
   name: Optional[str], address: Optional[str], vat: Optional[str]
)
```

---
#TODO sistemare doc
Update company


**Args**

#TODO

**Returns**

None

### .create_project
```python
.create_project(
   name: str, description: Optional[str]
)
```

---
Create a project


**Args**

* **name**  : the name of the project
* **description**  : optional description of the project


**Returns**

the project id associated with the created project (string)

### .get_projects
```python
.get_projects()
```

---
Get the list of all projects

### .get_project
```python
.get_project(
   project_id: str
)
```

---
Get the list of all projects

### .update_project
```python
.update_project(
   project_id: str, name: Optional[str], description: Optional[str]
)
```

---
Update project details

### .show_projects
```python
.show_projects()
```

---
Show a list all projects

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
Create a task


**Args**

* **project_id**  : the identifier of the project that includes the task
* **name**  : the name of the task
* **tags**  : a list of tags associated with the task
* **task_type**  : the type of the task


**Returns**

the task id associated with the created task (string)

### .get_tasks
```python
.get_tasks(
   project_id: str
)
```

---
Get all project tasks

### .get_task
```python
.get_task(
   task_id: str
)
```

---
Get task by id

### .show_tasks
```python
.show_tasks(
   project_id: str
)
```

---
Show a list of tasks included in a project


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
Create a model.


**Args**

* **task_id**  : the identifier of the task
* **name**  : the name of the model
* **version**  : the current version of the model


**Returns**

the model id associated with the created model (string)

### .get_models
```python
.get_models(
   task_id: str
)
```

---
Get all models of a task

### .get_model
```python
.get_model(
   model_id: str
)
```

---
Get model by id

### .show_models
```python
.show_models(
   task_id: str
)
```

---
Show a list of models included in a task.


**Args**

* **task_id**  : the identifier of the task

---
**Example output:**
```
Model ID                  Name        Version    Status     Status start date
------------------------  ----------  ---------  --------   -----------------
64760430583201813ab4ad1e  model_name  v1.0       OK         03-02-2023 10:14:06
```

### .update_model_version
```python
.update_model_version(
   model_id: str, new_model_version: str, suggestion_id: Optional[str] = None,
   raw_data_storing_process_id: Optional[str] = None
)
```

---
Update model version

### .add_data_schema
```python
.add_data_schema(
   task_id: str, data_schema: DataSchema
)
```

---
Associate a data schema to a task


**Args**

* **task_id**  : the identifier of the task
* **data_schema**  : the data schema that characterize your task


### .get_data_schema
```python
.get_data_schema(
   task_id: str
)
```

---
Get task data schema

### .show_data_schema
```python
.show_data_schema(
   task_id: str
)
```

---
Show data schema of associated with a task

**Example output:**
```
Column name       Role     Type      Nullable
----------------  -------  --------  ----------
sample_id         id       string    False
timestamp         time_id  string    False
sepallength       input    float     False
sepalwidth        input    float     False
petallength       input    float     False
petalwidth        input    float     False
class             target   category  False
```

### .update_data_schema
```python
.update_data_schema(
   task_id: str, data_schema: DataSchema
)
```

---
Update an existing data schema


**Args**

* **task_id**  : the identifier of the task
* **data_schema**  : the set of new columns that should be added to the data schema


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


### .wait_job_completion
```python
.wait_job_completion(
   job_id: str, max_wait_timeout: int = 600
)
```

