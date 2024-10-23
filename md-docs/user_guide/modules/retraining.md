# Retraining
A Data drift determines a drop in the model's performance that starts providing bad estimation or predictions.
In Artificial Intelligence, Data plays a crucial role and usually, choosing the best data has higher impact in the resulting Model quality with respect to increasing the model complexity.

ML cube Platform with its **Retraining Tool Module** provides you the best retraining dataset to use when updating the Model after a drift reducing the reaction time after the detection.
Even if, the data has changed you can extract useful information from the past.
ML cube Platform leverages all the available data belonging to the three categories: historical, reference and production, computing an Importance Score to every data sample you have.
These Importance Scores will be used during the training phase of your model as weights in the loss function.

A **Retraining Report** is generated whenever you request it or as a consequence of a [Detection automation rules](../monitoring/detection_event_rules.md).
It contains several information and aspects that let you to decide if it is the right time to retrain your model.
It's sections are:

- Performance view
- Cost view
- Dataset info
- Data importance

Retraining report is computed for each model you have in the Task.
You can generate a retraining report whenever there are new data, moreover, if you added a [Retrain trigger](../integrations/retrain_triggers.md) to the model you can automatically execute the trigger.

## Performance view

Before retraining your model you should know how it is performing.
Performance view provides performance interval for three key moments:

- Last Concept: the performance the model has before the drift
- Current: the performance the model has after the drift
- Forecast: the estimated performance of the model if it was retrained with dataset contained in the retraining report

The performance are shown as an interval, this interval is measured from production data for *Last concept* and *Current* while is estimated for *Forecast*.
In particular, the *Forecast* upper bound is a theoretical optimistic bound that expressed the best scenario given the actual data distribution; the lower bound instead, is an empirical estimation done with a simple ML model.

## Cost view

If the Task has *cost information* it is possible to show this view.
It is similar to the *performance view* but the quantity shown is economic costs of the model with that level of performance.

## Dataset info

Information about the last training dataset and the proposed one:

- From detected drift: the number of available samples received from the last drift provides information about the amount of data available from the latest concept.
- Effective sample size: quantifies the amount of information conveyed by our suggestion. It represents the hypothetical number of independent observations in a sample that would provide the same information as the computed suggestion. As the magnitude of the drift increases, this value decreases because less information from the past can be reused.
- Last reference: the number of samples used in the last reference data.
- Whole data: the percentage of data considered in providing the suggestion relative to the total available data.

## Data importance

Retraining dataset we propose is computed by computing importance weights for each sample uploaded in ML cube Platform.
This section shows an heatmap to provide a view of the weights distribution.
When you download the retraining report we provide you a list of pairs `customer id` - `importance weight`.
In case of the suggestion type for the model is `resampled dataset` then instead of the importance weights we provide you the number of time you should consider that specific sample.