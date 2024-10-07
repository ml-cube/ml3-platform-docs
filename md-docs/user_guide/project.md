# Project

A Project is the secondary organizational entity in ML cube Platform.
A Project groups together a set of artificial intelligence algorithms that share a common goal measured by a set of KPIs.
For this reason, it is composed of several [Tasks] that collaborate to reach the Project's goal.

Users in the [Company] can access to one or more Projects according to their [roles].

## Creation

When a Project is created, the [User] specifies its *name*, *description*, and selects the *default storage policy*.

*Storage Policy* defines the default behavior the Platform follows to access data that are shared with it.
Indeed, data shared with ML cube Platform can either be duplicated and stored in ML cube private cloud storage or stay only on customer's cloud and accessed as a remote data source.

## Demo Projects

To better explore ML cube Platform modules and features, it is possible to create *Demo Projects* that are not taken into account by subscription quotas.
ML cube Platform provides different Demo Projects that cover all the possible use cases (regression, classification, text data, image data, RAG, object detection and so on).
To create a Demo Project, you need to check the "Demo Project" checkbox and select the one you prefer.

## KPI Monitoring

A Key Performance Indicator is a measure of performance over time for a specific objective. 
While artificial intelligence algorithms try to minimize their loss function, artificial intelligence based solutions and applications look at KPIs.
Therefore, it is essential to monitor Project's KPIs along with algorithm performance to have a complete view of the current situation.

ML cube Platform offers the possibility to upload Project's KPIs to monitor them via drift detection algorithms.
That enables the detection of potentially dangerous trends in what really matters from the business point of view.
*KPI Monitoring* page in the Project sidebar shows the registered KPIs, their trends and drift events ML cube Platform detected during time.

## Integrations

ML cube Platform is part of the artificial intelligence and cloud ecosystem and provides connectors to interact with Cloud Providers and MLOps solutions.
The *Integrations* page allows to create and manage credentials that will be used by the Project's [Tasks].

For instance, if data are stored in a Google Cloud Storage bucket, adding the Google Cloud Platform credentials with the right permissions, allows ML cube Platform to read data from it.

Another example is to trigger a Sage Maker pipeline to retrain your artificial intelligence model with a dataset provided by ML cube Platform.
In this case, you can create Amazon Web Services credentials with permission to create an event on Amazon Event Bridge.
See the [Integrations] page for more information about credentials setup, data sources and retraining triggers.

## Jobs Monitoring

Operations like sharing data to ML cube Platform, submitting the creation of a retraining dataset or reports like RAG evaluation, trigger the execution of asynchronous pipelines in ML cube Platform cloud infrastructure.
Each pipeline is associated with an identifier named *job id* that can be used to monitor its execution status.
This monitoring can be done both from Web App in the *Job Status* page and, with specific SDKs method allowing automation.
A job failure can be either due to bad requests or internal errors, you can check the error message information via the same page.

[Company]: company.md
[Tasks]: task.md
[User]: user.md
[roles]: rbac.md
[Integrations]: integrations/index.md