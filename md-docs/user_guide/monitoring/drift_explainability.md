# Drift Explainability

[Monitoring]  is a crucial aspect of the machine learning lifecycle, as it enables tracking the model's performance and its data over time,
ensuring the model continues to function as expected. However, monitoring only is not enough when it comes to the adaptation phase.

In order to make the right decisions, you need to understand what were the main factors that led to the drift in the first place, so that
the correct actions can be taken to mitigate it.

The ML cube Platform supports this process by offering what we refer to as **Drift Explainability Reports**, 
automatically generated upon the detection of a drift and containing several elements that should help you diagnose the root causes 
of the change occurred.

You can access the reports by navigating to the `Drift Explainability` tab in the sidebar of the task page.

## Structure

A Drift Explainability Report consists in comparing the reference data and the portion of production data where the drift was identified, hence 
those belonging to the new data distribution. Notice that these reports are generated after a sufficient amount of samples has been collected after the drift.
This is because the elements of the report needs a significant number of samples to guarantee statistical reliability of the results.
If the distribution moves back to the reference before enough samples are collected, the report might not be generated.

Each report is composed of several entities, each providing a different perspective on the data and the drift occurred. 
Most of them are specific to a certain `Data Structure`, so they might not be available for all tasks.

These entities can take the form of tables, plots, or textual explanations. 
Observed and analyzed together, they should provide a comprehensive understanding of the drift and its underlying causes.
These are the entities currently available:

- `Feature Importance`: it's a barplot that illustrates how the significance of each feature differs between the reference 
 and the production datasets. Variations in a feature's values might suggest that its contribution to the model's predictions 
 has changed over time. This entity is available only for tasks with tabular data.
- `Variable discriminative power`: it's also a bar plot displays the influence of each feature, as well as the target, 
 in differentiating between the reference and the production datasets. 
 The values represent how strongly a given feature helps to distinguish the datasets, with higher values representing stronger 
 separating power. This entity is available only for tasks with tabular data.

[Monitoring]: index.md
