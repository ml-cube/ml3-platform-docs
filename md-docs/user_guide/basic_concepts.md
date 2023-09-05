# Basic Concepts

This page will explain you the basic concept of ML cube Platform to get familiar with the product.

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

<figure markdown>
  ![Image title](../imgs/user roles.png){ width="500" }
  <figcaption>User Roles in ML cube Platform.</figcaption>
</figure>

> Delta Energy has one dedicatd AI Team to each Task. 
> Hence, they assigned specific Project Administrator Role to each Team leader; while
> the other Data Scientists have the Project Edit Role for the project they are working on.

## Drift Detection
For each AI Task, ML cube Platform provides a set of Detectors that analyze different quantities of the Task.
**Data Detectors** look at the Task's data without considering its AI models.
They are resposible to identify input and concept drifts and more generally changes that happen in the data.

Indeed, each Model has associated a **Model Detector** that analyses its performance metrics and detect negative trends.

## Retraining
A Data drift determines a drop in the model's performance that starts providing bad estimation or predictions.
In Artificial Intelligence, Data plays a crucial role and usually, choosing the best data has higher impact in the resulting Model quality with respect to increasing the model complexity.

ML cube Platform with its Retraining Tool Module provides you the best retraining dataset to use when updating the Model after a drift reducing the reaction time after the detection.
Even if, the data has changed you can extract useful information from the past.
ML cube Platform leverages all the available data belonging to the three categories: histrical, reference and production, computing an Importance Score to every data sample you have.
These Importance Scores will be used during the training phase of your model as weights in the loss function.

## Model Life Cycle
ML cube Platform covers all the aspects of the *post-deployment life cycle* of your AI models:
<figure markdown>
  ![Image title](../imgs/model life cycle.png){ width="500" }
  <figcaption>Post-deployment AI model life cycle.</figcaption>
</figure>

> In Delta Energy data are collected every minute and are sent simultaneously to ML cube Platform.
> Ground truth data like the presence of a fault and the fault category are uploaded after they are available and therefore, they will sent with a delay compared the others.

> Drift alerting system is integrated with their Microsoft Teams and ML cube Platform sends alerts to the specified channels.
> After they receive an alerting message, they run a retraining pipeline that communicated with ML cube Platform to retrieve the retraining dataset to use.
> After that, they are ready to update the new version on ML cube Platform to start the monitoring.
