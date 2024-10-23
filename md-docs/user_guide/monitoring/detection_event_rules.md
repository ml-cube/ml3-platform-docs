# Detection Event Rules

This section outlines how to configure automation to receive notifications or start retraining after a [Detection Event] occurs.

When a detection event is produced, the MLCube Platform reviews all the detection event rules you have set 
and triggers those matching the event.

Rules are specific to a task and require the following parameters:

- `name`: a descriptive label of the rule.
- `task_id`: the unique identifier of the task to which the rule belongs.
- `detection_event_type`: the [DetectionEventType] that the rule matches.
- `severity`: the [DetectionEventSeverity] of the event.
- `monitoring_target`: the monitoring target whose event should trigger the rule. 
- `model_name`: the name of the model to which the rule applies. This is only required when the monitoring target is related to a model
  (such as `ERROR` or `PREDICTION`).
- `actions`: A sequential list of actions to be executed when the rule is triggered.

## Detection Event Actions
Two types of actions are currently supported: notification and retrain.

### Notifications
- `SlackNotificationAction`: sends a notification to a Slack channel via webhook.
- `DiscordNotificationAction`: sends a notification to a Discord channel via webhook.
- `EmailNotificationAction`: sends an email to the provided email address.
- `TeamsNotificationAction`: sends a notification to Microsoft Teams via webhook.
- `MqttNotificationAction`: sends a notification to an MQTT broker.

### Retrain Action

Retrain action lets you retrain your model. Therefore, it is only available when the monitoring target of the rule is related to a model.
The retrain action does not need any parameter because it is automatically inferred from the `model_name` attribute of the rule.
Of course, the model must already have a retrain trigger associated before setting up this action.

!!! example
    The following code snippet demonstrates how to create a rule that matches high severity drift events on the error of a model. 
    When triggered, it first sends a notification to the `ml3-platform-notifications` channel on your Slack workspace, using the 
    provided webhook URL, and then starts the retraining of the model.

    ```py
    rule_id = client.create_detection_event_rule(
        name='Retrain model with notification',
        task_id='my-task-id',
        model_name='my-model',
        severity=DetectionEventSeverity.HIGH,
        detection_event_type=DetectionEventType.DRIFT_ON,
        monitoring_target=MonitoringTarget.ERROR,
        actions=[
            SlackNotificationAction(
                webhook='https://hooks.slack.com/services/...',
                channel='ml3-platform-notifications'
            ),
            RetrainAction()
        ],
    )
    ```

[add_historical_data]: ../../api/python/client.md#add_historical_data
[Detection Event]: detection_event.md
[DetectionEventType]: ../../api/python/enums.md#detectioneventtype
[DetectionEventSeverity]: ../../api/python/enums.md#detectioneventseverity