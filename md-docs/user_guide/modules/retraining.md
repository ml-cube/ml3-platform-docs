# Retraining
A Data drift determines a drop in the model's performance that starts providing bad estimation or predictions.
In Artificial Intelligence, Data plays a crucial role and usually, choosing the best data has higher impact in the resulting Model quality with respect to increasing the model complexity.

ML cube Platform with its Retraining Tool Module provides you the best retraining dataset to use when updating the Model after a drift reducing the reaction time after the detection.
Even if, the data has changed you can extract useful information from the past.
ML cube Platform leverages all the available data belonging to the three categories: histrical, reference and production, computing an Importance Score to every data sample you have.
These Importance Scores will be used during the training phase of your model as weights in the loss function.