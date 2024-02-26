# Modules

ML cube Platform covers all the aspects of the *post-deployment life cycle* of your AI models.
The expected usage flow with ML cube Platform is depicted in the Figure below: the model is updated by specifying its reference dataset, then production data are logged and analyzed, if a drift is detected an alarm is raised, then a retraining dataset is computed to retrain the model that will be updated on the application.

<figure markdown>
  ![Image title](../../imgs/model life cycle.png){ width="400" }
  <figcaption>Post-deployment AI model life cycle.</figcaption>
</figure>



!!! note "Delta Energy inc"
    In Delta Energy data are collected every minute and are sent simultaneously to ML cube Platform.
    Ground truth data like the presence of a fault and the fault category are uploaded after they are available and therefore, they will sent with a delay compared the others.
    Drift alerting system is integrated with their Microsoft Teams and ML cube Platform sends alerts to the specified channels.
    After they receive an alerting message, they run a retraining pipeline that communicated with ML cube Platform to retrieve the retraining dataset to use.
    After that, they are ready to update the new version on ML cube Platform to start the monitoring.


Each step of this journey is covered by a module:

<div class="grid cards" markdown>

-   :material-text-search-variant:{ .lg .middle } **Monitoring**

    ---

    Monitor data and model, detect drifts and receive alerts.

    [:octicons-arrow-right-24: More info](monitoring.md)

-   :fontawesome-solid-gears:{ .lg .middle } **Retraining**

    ---

    Adapt your models to the current concept with new retraining dataset.

    [:octicons-arrow-right-24: More info](retraining.md)

-   :material-label:{ .lg .middle } **Labeling**

    ---

    Find which data to label to improve the overall performance.

    [:octicons-arrow-right-24: More info](labeling.md)

-   :material-briefcase:{ .lg .middle } **Business**

    ---

    Monitor business KPI to validate the impact of your models.

    [:octicons-arrow-right-24: More info](business.md)

</div>
