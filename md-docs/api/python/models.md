#


## Company
```python 
Company()
```


---
Company model

----


## Project
```python 
Project()
```


---
Project model

----


## Task
```python 
Task()
```


---
Task model

----


## Model
```python 
Model()
```


---
Base model to define model item

----


## Job
```python 
Job()
```


---
Job information item model

----


## ColumnInfo
```python 
ColumnInfo()
```


---
Column base model

----


## DataSchema
```python 
DataSchema()
```


---
Data schema base model

----


## Suggestion
```python 
Suggestion()
```


---
Suggestion base model

----


## ImportanceWeightsSuggestion
```python 
ImportanceWeightsSuggestion()
```


---
base model for importance weights suggestion

----


## CompanyUser
```python 
CompanyUser()
```


---
base model for company user

----


## ApiKey
```python 
ApiKey()
```


---
base model for api key

----


## DetectionEventAction
```python 
DetectionEventAction()
```


---
Generic action that can be performed

----


## DiscordNotificationAction
```python 
DiscordNotificationAction()
```


---
Action that sends a notification to a Discord server through
a webhook that you configure

----


## SlackNotificationAction
```python 
SlackNotificationAction()
```


---
Action that sends a notification to a Slack channel through
a webhook that you configure.

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
