# User Guide

ML cube Platform is built following the API first principle, by which it can be used both via Web Application and REST API.

In order to find easily every information we suggest you to use the search bar, moreover, you can go to [Glossary] to find the key concepts and definition we use along this site.

[Glossary]: glossary

To help you to better understand the concepts and the entities in ML cube Platform we will use a fictional company called *Delta Energy*.
It is a producer of Photovoltaic Modules that own Photovoltaic fields and trades the producted energy to the market.

!!! tip "Example Company"

    Every time you find a section like this you will find a examples with a fictional company that will help you to better understand the concepts and the entities in ML cube Platform.
    We will use a fictional company called *Delta Energy* that is a producer of Photovoltaic Modules that own Photovoltaic fields and trades the producted energy to the market.

To use ML cube Platform you need to belong to a **Company** that is created during your first login in the Web Application.
Everything will be done inside it, for example, if you want your collegues to work with you in ML cube Platform you need to create new **Users** inside the company.
Users has assigned a specific **Role** that defines their privileges and what they are able to do (refer to [User Roles] for more information).

[User Roles]: rbac

Your work on ML cube Platform is organized through the creation of **Projects**, **Task** and **Models**.
A Project is an artificial intelligence application that uses a set of algorithms to reach a common set of **KPIs**.

!!! tip "Delta Energy inc"

    Delta Energy, created the *Energy Revenue* Project to enhance their revenue from energy trading. They invested in four AI algorithms:

    - Fault detection
    - Fault diagnosis
    - Soiling detection
    - Trading

    In ML cube Platform, these four algorithms define four Tasks inside the Project Energy Revenue.
    They have been placed into the same Project because they share the business goal i.e., the net revenue, the data and are interdependent.

As you may have guessed, in ML cube Platform a Task corresponds to an AI Algorithm.
To be more precise, a Task is an AI Problem with a dataset composed of input features and a target.
A Task can have more than one AI Model that uses the input features estimates the target.

!!! tip "Delta Energy inc"

    In out example company, the Fault Detection Task has as input features the PV moduels and weather data and the target is the presence of a fault. 
    The Task has two Models: logistic regression and random forest. 
    Both models use the same data and predict the same target but are different in the techniques used to perform the estimation.

The last entity is the Model that is the actual AI model that predicts the target.
A Model has a Version that defines the training data used to train it. All model's data will be uploaded specifying the model version in order to track each prediction with the right model instance. 
The model version is updated whenever a new training of the model is done.

!!! note

    It's worth nothing to note that in ML cube Platform you do not actually need to upload the model on the application. 
    We just need to know its training data and its predictions for the production data. 
    In this way, ML cube Platform is considered as model agnostic.
