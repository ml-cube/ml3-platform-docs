# User Guide

ML cube Platform is built following the API first principle, by which it can be used both via Web Application and REST API.
In this first guide, we explain the basic concepts in ML cube Platform.
In order to find easily every information we suggest you to use the search bar, moreover, you can go to [Glossary] to find the key concepts and definition we use along this site.

[Glossary]: glossary.md

!!! tip "Example Company"

    Every time you find a section like this you will see a examples with a fictional company that will help you to better understand the concepts and the entities in ML cube Platform.
    We will use a fictional company called *Delta Energy* that is a producer of Photovoltaic Modules that own Photovoltaic fields and trades the produced energy to the market.

## Company

To use ML cube Platform you need to belong to a **Company** that is created during your first login in the Web Application.
Everything will be done inside it, for example, if you want your colleagues to work with you in ML cube Platform you need to create new **Users** inside the company.
Users has assigned a specific **Role** that defines their privileges and what they are able to do (refer to [User Roles] for more information).

[User Roles]: rbac.md


## Project

Your work on ML cube Platform is organized through **Projects**, **Task** and **Models**.
A **Project** is an artificial intelligence application that uses a set of algorithms to reach a common set of **KPIs**, usually a **Project** contains several **Tasks**.

!!! tip "Delta Energy inc"

    Delta Energy, created the *Energy Revenue* Project to enhance their revenue from energy trading. They invested in four AI algorithms:

    - Fault detection
    - Fault diagnosis
    - Soiling detection
    - Trading

    In ML cube Platform, these four algorithms define four Tasks inside the Project Energy Revenue.
    They have been placed into the same Project because they share the business goal i.e., the net revenue, the data and are interdependent.

## Task

As you may have guessed, in ML cube Platform a **Task** corresponds to an AI Algorithm.
To be more precise, a **Task** is an AI Problem with a dataset composed of input features and a target.
**A Task** can have more than one AI **Model** that uses the input features estimates the target.

!!! tip "Delta Energy inc"

    In out example company, the Fault Detection Task has as input features the PV modules and weather data and the target is the presence of a fault. 
    The Task has two Models: logistic regression and random forest. 
    Both models use the same data and predict the same target but are different in the techniques used to perform the estimation.

A **Task** is specified by several attributes, the most important are:

- `type`: regression, classification, object detection ...
- `data structure`: tabular data, image data, ...
- `optional target`: if the target is not always available. This happens when input samples are labeled and the most part of production data do not have a label
- `data schema`: specifies the inputs and the target of the task, see [Data Schema](data_schema.md) section for more details
- `cost info`: information about the economic costs of the error on the target

!!! tip "Delta Energy inc"

    The Task of Fault Detection has clear costs due to false positives or false negatives. 
    Every time a fault is not detected the false negative cost is proportional to the power reduction.
    While, false positives determine costs for the maintenance team that will go on the field for nothing.

## Model

The last entity is the **Model** that is the actual AI model that predicts the target.
A **Model** has a Version that defines the training data used to train it.
All model's data will be uploaded specifying the model version in order to track each prediction with the right model instance. 
The model version is updated whenever a new training of the model is done.

A **Model** has the following attributes:

- `name`: uniquely identifies the model inside the **Task**
- `version`: specifies different trained instance of the model
- `metric name`: metric to use to measure the model performance
- `suggestion type`: type of retraining action to use for that model, see [Retraining](modules/retraining.md) section for more details
- `retraining cost`: how much model training cost. This information is used by the [Business](modules/business.md) module

!!! note

    It's worth nothing to note that in ML cube Platform you do not actually need to upload the model on the application. 
    We just need to know its training data and its predictions for the production data. 
    In this way, ML cube Platform is considered as model agnostic.

Now that you have clear the basic concepts we invite you to explore the other ML cube Platform pages:

<div class="grid cards" markdown>

-   :simple-hive_blockchain:{ .lg .middle } **Modules**

    ---

    Explore available features in ML cube Platform

    [:octicons-arrow-right-24: More info](modules/index.md)

-   :material-connection:{ .lg .middle } **Integrations**

    ---

    We are part of MLOps ecosystem and natively integrated with other solutions.

    [:octicons-arrow-right-24: More info](integrations/index.md)

-   :material-flash-auto:{ .lg .middle } **Automation rules**

    ---

    Discover how to setup automation rules to increase your reactivity.

    [:octicons-arrow-right-24: More info](monitoring/detection_event_rules.md)

-   :material-lock:{ .lg .middle } **Roles and access**

    ---

    Get more info about RBAC inside ML cube Platform

    [:octicons-arrow-right-24: More info](rbac.md)

</div>