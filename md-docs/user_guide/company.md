# Company and Subscriptions

A **Company** is the fundamental organizational entity inside ML cube Platform.
Users belong to a single Company and billing, licenses, and projects are all managed and created inside a Company.

The Company has an **Owner** with maximum privileges including billing administration.
The owner can create new **User** accounts inside the Company assigning specific [roles] at the company and project level.

The information required that describe the Company are:

- Company name
- Address
- VAT

The Company is created by ML cube team during the onboarding, then, during first login the Owner needs to complete the remaining information.

## Subscriptions

A Subscription is the payment arrangement where a Company pays a periodical fee to access ML cube Platform services.
A Subscription has a **start** and an **expiration** date and contains the **modules** and **quotas** the Company can handle.

=== "Quotas"

    | Quota      | Description                          |
    | ----------- | ------------------------------------ |
    | Users       | Maximum number of Users per Company|
    | Tasks       | Maximum number of Tasks per Company excluding those in demo projects|
    | Data Batch Upload       | Maximum number of production data batch uploads allowed per day|

=== "Modules"

    | Module | Description |
    | :--- | :--- |
    | *Monitoring* | Data drift monitoring and detection for several targets and raw data. Alerts are raised when drifts are detected, allowing for automated responses. |
    | *Monitoring Metrics* | Extension of monitoring module with extracted metrics from raw data. |
    | *Segmented Monitoring* | Granular analysis and monitoring of specific data subsets or populations. |
    | *Retraining* | Generation of retraining datasets to update AI models based on identified data drifts and historical distributions. |
    | *Explainability* | Insights into detected drifts to support root cause analysis and mitigation strategies. |
    | *Topic Analysis* | Discovery and analysis of latent themes and semantic patterns within unstructured data. |
    | *RAG Evaluation* | Specialized evaluation frameworks and benchmarks for Retrieval-Augmented Generation pipelines. |
    | *LLM Security* | Protection, auditing, and threat detection for Large Language Model interactions. |
    | *Business* | High-level performance tracking, primarily focused on KPI monitoring and business alignment. |


Moreover, there are two types of subscriptions depending on where ML cube Platform is used:

<div class="grid cards" markdown>
- :material-cloud:{ .lg .middle .green-icon} <span style="color:#98BE59"> **Cloud** </span>

    ---

    Standard SaaS plan to use ML cube Platform hosted on ML cube cloud infrastructure.
    With Cloud subscription the users can use Web Application and SDK to interact with ML cube Platform and to use its services.
    Data can be stored on ML cube Private Cloud Storage.

- :fontawesome-solid-computer:{ .lg .middle .green-icon} <span style="color:#98BE59"> **Edge** </span>

    ---

    Edge subscriptions are used, as the name suggests, for edge devices that hosts ML cube Platform Edge.
    A common use case is an industrial machinery computer that runs AI algorithms.
    Edge subscriptions are validated via Product Key and are uniquely linked to a specific edge device.

  </div>

[roles]: rbac.md