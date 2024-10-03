# Company and Subscriptions

A Company is the fundamental organizational unit inside ML cube  Platform.
Users belong to a single Company, billing, licenses, and projects are all managed and created inside a Company.

The Company has an Owner with maximum privileges and billing administration.
The owner can create new User accounts inside the Company assigning specific roles at the company and project level.

The information required that describe the Company are:

- Company name
- Address
- VAT

The Company is created by ML cube team during the onboarding, then, at the first login the owner needs to complete the remaining information.

## Subscriptions

A Subscription is the payment arrangement where a Company pays a regular fee to access ML cube Platform services.
A Subscription has a *start* and *expiration* date and contains the *modules* and *quotas* the Company can handle.

=== "Quotas"

    | Quota      | Description                          |
    | ----------- | ------------------------------------ |
    | Users       | Maximum number of Users per Company  |
    | Tasks       | Maximum number of Tasks per Company |

=== "Modules"

    | Modules      | Description                          |
    | ----------- | ------------------------------------ |
    | Monitoring       | Data drift monitoring and detection for several targets and metrics. Alerts are raised when drifts are detected allowing automating the response.  |
    | Retraining       | Generation of retraining dataset to update AI models according to new data drifts. Dataset is created according to data distributions and leverage all the past available data. |
    | Explainability       | Explainability of detected drifts to better understand what happened and how to tackle it. |


Moreover, there two types of subcriptions that depends on where ML cube Platform is used:

<div class="grid cards" markdown>
- :material-cloud:{ .lg .middle .green-icon} <span style="color:#98BE59"> **Cloud** </span>

    ---

    Standard SaaS plan to use ML cube Platform hosted on ML cube cloud infrastructure.
    With Cloud subscription the users can use Web Application and SDK to interact with ML cube Platform and to use its services.
    Data can be stored on ML cube Private Cloud Storage.

- :fontawesome-solid-computer:{ .lg .middle .green-icon} <span style="color:#98BE59"> **Edge** </span>

    ---

    Edge subscriptions are used as the name suggests, for edge devices that hosts ML cube Platform Edge.
    A common use case is industrial machinery computers that runs AI algorithms.
    Edge subscriptions are validated via Product Key and are uniquely linked to an edge device.

  </div>
