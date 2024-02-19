# Monitoring

## Data Taxonomy
A Batch of data is composed of four types of data:

- **metadata:** additional information that AI models do not use as input but that is important to define the data or the samples.
Mandatory for this category are the `sample-id`, a unique identifier for each sample used to avoid confusion and misinterpretation; and the
`sample-timestamp`, a timestamp associated with each sample used for ordering.
Moreover, the User can provide additional data used to segment the data space. 
For instance, sensitive information like zip code or country are not used by AI models to prevent bias, however, ML cube Platform can use them to 
check and prevent bias in the suggested retraining dataset or to perform segmented drift detection.
- **input:** set of input features the AI model uses to predict the output. 
ML cube Platform uses the input data that comes at the end of the processing data pipeline and not the raw data.
This is due to the fact that ML cube Platform detects drifts in what the AI model uses and not in the general data the customer has.
- **output:** target quantity predicted by the AI models.
It is present in the training data but can be not available for production data.
- **models' predictions:** predicted target for each AI model in the AI Task.


### Data Categories
ML cube Platform are present three categories of data:

- **Reference:** represents the dataset used to train the model.
Each model version has a reference dataset.
Detection algorithms use reference data during their initialization.
- **Production:** represents data that comes from the production environment in which the AI model is operating.
Detection algorithms analise production data to detect the presence of drifts.
- **Historical:** represents additional data that ML cube Platform can use to define the retraining dataset after a drift.

<figure markdown>
  ![Image title](../imgs/data_categories.png){ width="1000" }
  <figcaption>ML cube Platform data categories.</figcaption>
</figure>

!!! note "Delta Energy inc"

    Delta Energy company trained its models using the data in the year 2022 and used the algorithms starting from the 2023. This means that the data in the 2022 are the reference data and every data from the january first 2023 are considered as production data. Data previous 2022 are historical data instead.


## Drift Detection
ML cube Platform provides a set of Detectors for each AI Task. These detectors are used to monitor the task according 
to different levels. The choice over the types of detectors to be instantiated depends on the type of task (classification or regression) and on 
the type of data available for that task (input, output, model predictions).   
There are mainly two classes of detectors:  

- **Data Detectors:** they take into account data associated with the task. They may be *input only* 
data or *input and ground truth* data. These detectors are independent from the models trained on the 
task as they do not either consider their predictions or performances. These detectors are responsible for the identification of 
input and concept drifts. According to the type of the used detector, changes in data are either monitored at feature 
level or using a multivariate monitoring strategy.
- **Model Detectors:** they monitor the performances associated with the models related to the task.
In cases where the user has multiple models trained for a single task, a single detector is created for each model.

Each detector is initially created using **Reference data** provided by the user. Every time a new batch of data 
is uploaded, the detectors observe the batch and update their statistics.  
Each detector updates its statistics independently from the others and each of them presents a double-level alarm scheme in 
order to either signal a **Warning** or a **Drift** for the monitored task. Each of these levels are identified by properly 
setting specific thresholds for each detector. The choice over the sensibility associated with the alarms can be chosen 
by the user.  
The detectors may be in three different states: 

- **Regular:** the detector is monitoring data that are similar to the reference data, 
- **Warning:** the detector has fired a Warning alarm since the data has started to change. From this zone, it is possible 
to either go into the Drift status or to go back to the Regular one, depending on the monitored data.
- **Drift:** the detector has fired a Drift alarm and a change has been established between the reference data and the last 
ones. After a drift, the detector is usually reset by defining a new set of reference data. The reset process is different 
according to what has been monitored by the detector.  
<When a detector 
enters the warning zone, it generates a warning alert. It is possible to exit from the it if the new data gets more similar 
to the reference data. If instead, data exhibit significant differences with respect to the original ones, the detectors 
may enter the drift zone and fire a drift alarm.>

All the alarms generated during this process are combined and a final set of alarms is shown to the user. The alarms generated 
during this process will be helpful to define the division into **Concepts**.
<After having raised drift alarms, the detectors can be reset in different ways, according to what the detector is actually monitoring.>