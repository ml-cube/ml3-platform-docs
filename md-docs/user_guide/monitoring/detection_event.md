# Detection Event

A [Detection Event] is raised by the MLCube Platform when a significant change is detected in one of the entities being monitored.

An event is characterized by the following attributes:

- **event_id**: the unique identifier of the event.
- **event_type**: the [DetectionEventType] of the event.
- **severity**: the [DetectionEventSeverity] of the event. The severity should be provided only for drift events and it indicates
the criticality of the detected drift.
- **monitoring_target**: the [MonitoringTarget] being monitored.
- **monitoring_metric**: the [MonitoringMetric] that triggered the event, if the event is related to a metric.
- **model_name**: the name of the model that raised the event.
- **model_version**: the version of the model that raised the event.
- **insert_datetime**: the time when the event was raised.
- **sample_timestamp**: the timestamp of the sample that triggered the event.
- **user_feedback**: the feedback provided by the user on whether the event was expected or not.




[Detection Event]: ../../api/python/models#detectionevent
[DetectionEventType]: ../../api/python/enums#detectioneventtype
[DetectionEventSeverity]: ../../api/python/enums#detectioneventseverity
[MonitoringTarget]: ../../api/python/enums#monitoringtarget
[MonitoringMetric]: ../../api/python/enums#monitoringmetric