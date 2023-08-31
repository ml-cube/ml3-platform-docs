# Basic Concepts

## Company, Project, Task and Model

Everything starts with a **Company**, when you register on ML cube Platform, you are asked to create a Company.
A Company has a **Subscription Plan** that defines how many Projects, Tasks, Data you can create.
Moreover, billing and payments are done at Company level.

After you created your Company you become the *company owner*, and as company owner, you can create new **Users**, assigning them the right **Role**.

> To help you to better understand the concepts and the entities in ML cube Platform we use a fictional company: it is called *Delta Energy*, and it is a producer of Photovoltaic Modules that own Photovoltaic fields and trades the energy to the market.

After the Company is created, you can create a **Project** and AI Tasks inside it.
Think of a Project as an application of Artificial Intelligence algorithms and techniques to optimize a KPI.

> Delta Energy created the Project *Energy Revenue* for increasing the revenue from trading the produced energy.
> They invested in four AI algorithms:
> 
> 1. Fault detection
> 2. Fault diagnosis
> 3. Soiling detection
> 4. Trading

> In ML cube Platform, these four algorithms define four Tasks inside the Project *Energy Revenue*.
> They have been placed into the same Project because they share the business goal i.e., the net revenue,
> the data and are interdependent.

Putting Tasks inside the same Project allows to leverage Tasks and data correlation having a comprehensive view of the problem.

As you may have guessed, in ML cube Platform a **Task** corresponds to an AI Algorithm.
To be more precise, a Task is an AI Problem with a dataset composed of input features and a target.
A Task can have more than one AI Model that uses the input features estimates the target.

> In out example company, the Fault Detection Task has as input features the PV moduels and weather data and the target is the presence of a fault.
> The Task has two Models: logistic regression and random forest.
> Both models use the same data and predict the same target but are different in the techniques used to perform the estimation.

The last entity is the **Model** that is the actual AI model that predicts the target.
A Model has a Version that defines the training data used to train it.
All model's data will be uploaded specifying the model version in order to track each prediction with the right model instance.
The model version is updated whenever a new training of the model is done.

It's worth nothing to note that in ML cube Platform you do not actually need to upload the model on the application.
We just need to know its training data and its predictions for the production data.
In this way, ML cube Platform is considered as *model agnostic*.

## Data Tassonomy
A Batch of data is composed of four types of data:

- **metadata:** additional information that AI models do not use as input but that are important to define the data or the samples.
Mandatory for this category are the `sample-id`, a unique identifier for each sample used to avoid confusion and misinterpretation; and the
`sample-timestamp`, a timestamp associated with each sample used for ordering.
Moreover, the User can provide additional data used to segment the data space. 
For instance, sensitive information like zip code or country are not used by AI models to prevent bias, however, ML cube Platform can use them to 
check and prevent bias in the suggested retraining dataset or to perform segmented drift detection.
- **input:** set of input features the AI model uses to predict the output. 
ML cube Platform uses the input data that come at the end of the processing data pipeline and not the raw data.
This is due to the fact that ML cube Platform detects drifts in what the AI model uses and not in the general data the customer has.
- **output:** target quantity predicted by the AI models.
It is present in the training data but can be not available for production data.
- **models' predictions:** predicted target for each AI model in the AI Task.


### Data Categories
ML cube Platform are present three categories of data:

- **Reference:** represents the dataset used to train the model.
Each model version has a reference dataset.
Detection algorithms use reference data during their initialization.
- **Production:** represents data that comes from the production environment in which the AI model is operating.
Detection algorithms analise production data to detect the presence of drifts.
- **Historical:** represents additional data that ML cube Platform can use to define the retraining dataset after a drift.

<figure markdown>
  ![Image title](../imgs/data_categories.png){ width="1000" }
  <figcaption>ML cube Platform data categories.</figcaption>
</figure>

> Delta Energy company trained its models using the data in the year 2022 and used the algorithms starting from the 2023.
> This means that the data in the 2022 are the reference data and every data from the january first 2023 are considered as production data.
> Data previous 2022 are historical data instead.

## User Roles
Before to dive into details about the functionalities and modules covered, let's talk about the Role Based Access Control in ML cube Platform.
As mentioned above, the company owner can create new Users assigning to them a Role.
The Role defines the set of actions a User has inside the ML cube Platform.
There are two levels of roles:

-  **Company:** each User has a role inside the company. 
The roles are Owner, Admin, Standard User.
- **Project:** by default a User does not have roles in a Project. 
The Company Owner or Admin will assign a Project Role to User when needed.
The roles are Admin, Edit User, View User.

## Model Life Cycle
It's possible to identify an usage cycle of ML cube Platform that covers the main aspects of the life cycle management of a AI model.

1. Define new model version uploading a reference data
2. Log production data containing input, target and model prediction
3. Receive drift alarms when they occur
4. Get the retraining dataset
5. Train model locally and uplaod new model version with the new reference data

## Drift Detection
For each AI Task, ML cube Platform provides a set of Detectors that analyze different quantities of the Task.
**Data Detectors** are look at the Task data without considering its AI models.
Data detectors are resposible to identify input and concept drifts.
Each Model has associated a **Model Detector** that analyses the its performance metric and detect negative trends.

## Retraining
A Data drift determines a drop in the model's performance that require to update it with new and fresh data.
The retraining module of ML cube Platform provides the best dataset to train the model using as much data as possible.
In particular, using the data after the drifts as reference, it computes an importance score
