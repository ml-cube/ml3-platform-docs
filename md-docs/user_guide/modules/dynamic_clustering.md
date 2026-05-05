# Dynamic Clustering


## Overview

The Dynamic Clustering page provides an interactive exploration interface for analyzing clustered data through multiple coordinated views. This tool helps you understand patterns, relationships, and quality metrics across your clustered samples.



## Understand Cluster Evolution with the History Graph

The timeline visualization at the top shows how samples progress through different clusters over time or across dimensions:

- **Multiple cluster tracks**: Each row represents a different cluster (Cluster 0, Cluster 1, Cluster 2, etc.)
- **Connected nodes**: Circles connected by lines show the progression and relationships between samples

![Metro Graph](../../imgs/dynamic_clustering/metro_graph.png)

### Transition Types

Cluster evolution is characterized using explicit transition types that describe how clusters change between consecutive iterations:

- Survival: A cluster persists with largely the same members across iterations, indicating stability.
- Appearance: A new cluster emerges that did not exist in the previous iteration.
- Disappearance: A cluster ceases to exist because its samples are reassigned or absorbed elsewhere.
- Merge: Two or more clusters combine into a single cluster, suggesting increased similarity or reduced separation.
- Split: A single cluster divides into multiple distinct clusters, often revealing finer-grained structure.
- Merge–Split: Multiple clusters merge and then reorganize into multiple new clusters within the same transition, indicating significant structural reconfiguration.
- Reappearance: A previously disappeared cluster re-emerges after one or more iterations, potentially with similar composition.
- Remerge: Clusters that were previously separate and merged once again after intermediate changes.
- Resplit: A cluster that had previously split undergoes another splitting event, further refining its internal structure.

## Explore Clusters in Embedding Space

Explore your data in 2D embedding space:

- **Color-coded clusters**: Each cluster is represented by a distinct color for easy identification
- **Interactive selection**: Draw selections directly on the scatter plot to filter and examine specific groups of samples

![Scatter](../../imgs/dynamic_clustering/scatter.png)

## Interpret Clusters with Cluster Cards

In order to give an immediate interpretation on what the clusters represent, each cluster card contains the following information:

- **Silhouette scores**: A bar chart showing the cohesion quality for each sample within the cluster
    - Higher scores (closer to 1.0) indicate samples that are well-matched to their cluster
    - Lower scores suggest samples that might be borderline or belong to multiple clusters


- **Micro-cluster percentage**: A gauge visualization showing what portion of samples belong to micro-clusters
    - Shows how much of the data is captured by dominant clusters
    - Helps to determining the distribution of clusters at current iteration

- **Sample gallery**: Visual thumbnails of the most relevant samples in the cluster
    - Provides qualitative insight into cluster composition
    - Helps validate that similar items are grouped together

![Cards](../../imgs/dynamic_clustering/cards.png)

## Measure Clustering Quality with Advanced Statistics

Monitor clustering quality metrics:

- **Silhouette score**: Line chart showing how the overall clustering quality changes
    - X-axis represents different clustering iterations
    - Y-axis shows the silhouette coefficient (higher is better)
- - For a detailed explanation, refer to [this link](https://en.wikipedia.org/wiki/Silhouette_(clustering)).

![Silhouette Score](../../imgs/dynamic_clustering/silhouette.png)

- **Davies-Bouldin index**: Alternative clustering quality metric (available via tab)
    - Lower scores indicate better cluster separation
    - Useful for comparing different clustering approaches
    - For a detailed explanation, refer to [this link](https://en.wikipedia.org/wiki/Davies%E2%80%93Bouldin_index).

## Analyze transition

The **Analyze Transition** view allows you to shift focus from a single clustering snapshot to the **changes occurring between two iterations**. Instead of analyzing clusters in isolation, this mode helps you understand how the clustering structure evolves.

When this mode is activated, the interface is split into two side-by-side panels, each representing a different iteration. This layout enables direct comparison and highlights how clusters and samples move from one state to another.

While the History-Graph now allow you to select the transition, all the visualization components available in the standard view (embedding scatter plot and cluster cards) are duplicated across both panels to ensure a consistent comparison experience.

### What you can explore

- **Side-by-side comparison**: View two iterations simultaneously to easily spot structural differences in clusters.
- **Cluster transitions**: Identify how clusters evolve between iterations, including merges, splits, appearances, and disappearances.
- **Change focus**: Quickly pinpoint which clusters underwent the most significant transformations.

By focusing on transitions rather than static states, you gain a deeper understanding of the dynamics behind the dynamic clustering results.

![DB Score](../../imgs/dynamic_clustering/analyze_transition.png)