# Monitoring

The monitoring module is a key feature of the ML cube Platform. 
It enables continuous tracking of your AI models performance over time, helping to identify potential issues. 
Additionally, it allows the monitoring of production data to preemptively detect distribution changes, ensuring
that the model continues to perform as expected and aligns with business requirements.

## Why do we need Monitoring?

Machine Learning algorithms are based on the assumption that the distribution of the data used for training is the same as the one from which
production data are drawn from. This assumption never holds in practice, as the real-world is characterized by dynamic and ever-changing conditions.
These distributional changes, if not addressed properly, can cause a drop in the model's performance, leading to bad estimations or predictions, which
in turn can have a negative impact on the business.

Monitoring, more commonly known as __Drift Detection__ in the literature, refers the process of continuously tracking the performance of a model 
and the distribution of the data it is operating on. 
Simply put, monitoring employs statistical techniques to compare the distribution characterizing the reference data (for instance, those used for training)
with the one characterizing the production data. If a significant difference is detected, the system raises an alarm, signaling that the monitored entity
is drifting away from the expected behavior and that corrective actions should be taken.

The MLCube Platform performs different types of monitoring, which will be explained in the following sections.

## Targets and Metrics

After going through the reasons why monitoring is so important in modern AI systems, and explaining how monitoring is performed in the ML cube Platform, 
we can introduce the concepts of Monitoring Targets and Monitoring Metrics. They both represent quantities that the MLCube Platform monitors, but they differ in their nature.

### Monitoring Targets

A Monitoring Target is a relevant entity involved in a [Task].

[Task]: task.md