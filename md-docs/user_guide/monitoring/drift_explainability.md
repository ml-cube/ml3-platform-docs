# Drift Explainability

[Monitoring]  is a crucial aspect of the machine learning lifecycle, as it enables tracking the model's performance and its data over time,
ensuring the model continues to function as expected. However, monitoring only is not enough when it comes to the adaptation phase.

In order to make the right decisions, you need to understand what were the main factors that led to the drift in the first place, so that
the correct actions can be taken to mitigate it.
s
The ML cube Platform supports this process by providing what we refer to as **Drift Explainability Report**, 
automatically generated upon the detection of a drift and containing several elements that should help you diagnose the root causes 
of the change occurred.

You can access the reports in the WebApp, by navigating to the `Drift Explainability` tab in the sidebar of the [Task] page.

## Structure

A Drift Explainability Report consists in comparing the reference data and the portion of production data where the drift was identified, hence 
those belonging to the new data distribution. Notice that these reports are generated after a sufficient amount of samples has been collected 
after the drift, in order to ensure statistical reliability of the results.
If the data distribution moves back to the reference before enough samples are collected, the report might not be generated.

Each report is composed of several entities, each providing a different perspective on the data and the drift occurred. 
Most of them are specific to a certain Data Structure, so they might not be available for all Tasks.

These entities can take the form of tables, plots, or textual explanations. 
Observed and analyzed together, they should provide a comprehensive understanding of the drift and its underlying causes.
These are the entities currently available:

- **`Feature Importance`**: it's a barplot that illustrates how the significance of each feature differs between the reference 
 and the production datasets. Variations in a feature's values might suggest that its contribution to the model's predictions 
 has changed over time. This entity is available only for tasks with tabular data.

<figure markdown style="width:100%">
  ![Feature Importance](../../imgs/monitoring/drift-explainability/fi.svg)
  <figcaption>Example of a feature importance plot.</figcaption>
</figure>

- **`Variable discriminative power`**: it's also a bar plot displays the influence of each feature, as well as the target, 
 in differentiating between the reference and the production datasets. 
 The values represent how strongly a given feature helps to distinguish the datasets, with higher values representing stronger 
 separating power. This entity is available only for tasks with tabular data.

<figure markdown style="width:100%">
  ![Variable discriminative power](../../imgs/monitoring/drift-explainability/concept-fi.svg)
  <figcaption>Example of a variable discriminative power plot.</figcaption>
</figure>

- **`Drift Score`**: it's a line plot that shows the evolution of the drift score over time. The drift score is a 
  measure of the statistical distance between a sliding window of the production data and the reference data. It also shows the threshold,
  which is the value that the drift score must exceed to raise a drift alarm, and all the [Detection Events] that were triggered in
  the time frame of the report. This plot helps in understanding how the drift evolved over time and the moments in which the difference
  between the two datasets was higher. Notice that some postprocessing is applied on the events to account for the functioning of the drift detection algorithms. 
  Specifically,
  we shift back the drift on events by a certain offset, aiming to point at the precise time when the drift actually started. As a result,
  drift on events might be shown before the threshold is exceeded. This explainability entity is available for all tasks.


<figure markdown style="width: 100%">
  ![Drift score](../../imgs/monitoring/drift-explainability/score.svg)
  <figcaption style="width: 100%; text-align: center;">Example of a drift score plot with detection events of increasing severity displayed.</figcaption>
</figure>

- **`Clusters Count`**: it's an histogram plot that shows the distribution of reference and production samples across clusters created over reference data. It is obtained by fitting a clustering algorithm over the reference data and then assigning production data to these identified clusters. This plot can help understanding the nature of the drift by distinguishing between two main scenarios:

    1. `Internal dynamic change`: if all production data align with the reference clusters, with no point labeled as outlier, then the drift is likely reflecting a change in the internal dynamics of the same distribution. For instance, production data may concentrate within specific sub-domains of the reference distribution.
    2. `Distribution shift`: if most production data points are labeled as noise, which means that the clusters found defined on reference data are not able to capture the production data, then an actual distribution shift has likely occurred.

<figure markdown style="width: 100%">
  ![Drift score](../../imgs/monitoring/drift-explainability/cluster-count.svg)
  <figcaption style="width: 100%; text-align: center;">Example of a cluster count plot. In this case most production data are assigned to the reference clusters, but with different proportions, which suggests that the drift is likely due to an internal reorganization within the same distribution.</figcaption>
</figure>

- **`Clustering scatter`**: it's a scatter plot showing reference and production data in a 2 dimensional space. The color of the points represents the cluster they belong to, while the shape distinguishes between reference and production data. The clusters shown in this plot are the ones identified over the reference data (also shown in the `Clusters Count` plot). This plot can help understanding how the production data are mapped to the reference data, and how the clusters are distributed in the 2D space.

<figure markdown style="width: 100%">
  ![Drift score](../../imgs/monitoring/drift-explainability/cluster-scatter-plot.svg)
  <figcaption style="width: 100%; text-align: center;">Example of a clustering scatter plot.</figcaption>
</figure>

- **`Clustering heatmap`**: it's a heatmap which aims at showing the difference between reference and production data.
Along with the clustering over reference data, another clustering is executed, this time over production data only.
It is important to notice that the production clusters found by analyzing reference data do not necessarily map 1 to 1 with the ones found by analyzing production data.
Those two clustering outputs are then compared in this heatmap. Given a cell at row R and column C, the intensity indicates how many production samples are assigned to reference cluster R and production cluster C.
When the data distribution did not shift, the expected output is a chess-like heatmap, in which each production cluster matches with a reference cluster.
When the data distribution shifted, the expected output is that most of production data are assigned to the noise row of the reference cluster, while belonging to specific production clusters.

<figure markdown style="width: 100%">
  ![Drift score](../../imgs/monitoring/drift-explainability/cluster-heatmap.svg)
  <figcaption style="width: 100%; text-align: center;">Example of a clustering heatmap. It looks like there is a direct mapping between reference and production clusters, which suggests that the drift is likely not due to a distribution shift.</figcaption>
</figure>

[Monitoring]: index.md
[Detection Events]: detection_event.md
[Task]: ../task.md