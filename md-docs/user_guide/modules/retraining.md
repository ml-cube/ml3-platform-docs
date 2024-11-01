# Retraining

The Retraining module of ML cube Platform plays a fundamental role in dealing with data drifts and should be used as consequence of drift detection alarms.
Indeed, usually, a data drift determines a drop in the model's predictive capacity that starts providing bad predictions and therefore, degrading its performance.
As soon as a data drift has been detected, action must be taken to avoid excessive performance degradation and thus business issues.

## Retraining dataset

The main outcome of the Retraining module is the _retraining dataset_ that you should use to retrain your AI model adapting it to the new discovered data distributions.
The dataset computation is based on _transfer learning_ techniques and leverages all the uploaded data to maximize the available information.
In fact, after a drift has been detected, production data belonging to the new data distribution could be not sufficient for good model training.
Hence, even if previous data come from another distribution, they can be used for retraining if properly transformed.

The retraining dataset can have two formats:

- __Sample weights:__
    each sample uploaded in ML cube Platform is assigned a weight that can be used as sample weight in a weighted loss function.
    The higher the weight, the greater the importance of the sample for the new retraining.
- __Data samples:__
    a list of sample ids (using data schema column object with role ID) is provided indicating which data form the retraining dataset.
    This format can be used when the training procedure does not support weighted loss or when a fixed size retraining dataset is preferred.
    Note that samples ids can appear more than once, this could happen when a sample is particular importante for the new retraining.

The retraining report contains additional indicators and information that helps you to better understand the provided retraining dataset:

- Performance view
- Cost view
- Dataset info

## Performance view

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
