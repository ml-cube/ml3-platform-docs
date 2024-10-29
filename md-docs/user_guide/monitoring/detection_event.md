# Detection Event

A [Detection Event] is raised by the MLCube Platform when a significant change is detected in one of the entities being monitored.

An event is characterized by the following attributes:

- `event_id`: the unique identifier of the event.
- `event_type`: the [DetectionEventType] of the event.
- `severity`: the [DetectionEventSeverity] of the event. The severity should be provided only for drift events and it indicates
the criticality of the detected drift.
- `monitoring_target`: the [MonitoringTarget] being monitored.
- `monitoring_metric`: the [MonitoringMetric] that triggered the event, if the event is related to a metric.
- `model_name`: the name of the model that raised the event.
- `model_version`: the version of the model that raised the event.
- `insert_datetime`: the time when the event was raised.
- `sample_timestamp`: the timestamp of the sample that triggered the event.
- 'sample_customer_id': the id of the customer that triggered the event.
- `user_feedback`: the feedback provided by the user on whether the event was expected or not.

## Retrieve Detection Events

You can access the detection events generated by the Platform in two ways:

- **SDK**: the [get_detection_events] method can be used to retrieve all detection events for a specific task programmatically.
- **WebApp**: navigate to the **`Detection `** section located in the task page's sidebar. Here, all detection events are displayed in a table, 
   with multiple filtering options available for useful event management.

## User Feedback

When a detection event is raised, you can provide feedback on whether the event was expected or not. This feedback is then used 
to tune the monitoring algorithms and improve their performance. The feedback can be provided through the WebApp, in the
**`Detection `** section of the task page, or through the SDK, using the [set_detection_event_user_feedback] method.


## Detection Event Rules

To automate actions upon the reception of a detection event, you can set up detection event rules. 
You can learn more about how to configure them in the [Detection Event Rules] section.

[Detection Event]: ../../api/python/models.md#detectionevent
[DetectionEventType]: ../../api/python/enums.md#detectioneventtype
[DetectionEventSeverity]: ../../api/python/enums.md#detectioneventseverity
[MonitoringTarget]: ../../api/python/enums.md#monitoringtarget
[MonitoringMetric]: ../../api/python/enums.md#monitoringmetric
[get_detection_events]: ../../api/python/client.md#get_detection_events
[set_detection_event_user_feedback]: ../../api/python/client.md#set_detection_event_user_feedback
[Detection Event Rules]: detection_event_rules.md