# Detection Event Rules

This section outlines how to configure automation to receive notifications or start retraining after a [Detection Event] occurs.

When a detection event is produced, the ML cube Platform reviews all the detection event rules you have set 
and triggers those matching the event.

Rules are specific to a task and are characterized by the following attributes:

- `Name`: a descriptive label of the rule.
- `Detection Event Type`: the type of event that triggers the rule.
- `Severity`: the severity of the event that triggers the rule. It is only applicable to drift events. If not specified, the rule will be triggered by drift events of any severity.
- `Monitoring Target`: the [Monitoring Target](index.md#monitoring-targets) whose event should trigger the rule. 
- `Monitoring Metric`: the [Monitoring Metric](index.md#monitoring-metrics) whose event should trigger the rule.
- `Model name`: the name of the model to which the rule applies. This is only required when the monitoring target is related to a model
  (such as `ERROR` or `PREDICTION`).
- `Actions`: A list of actions to be executed sequentially when the rule is triggered.

## Detection Event Actions
Three types of actions are currently supported: notification, plot configuration and retrain.

### Notifications

These actions send notifications to external services when a detection event is triggered. The following notification actions are available:

- `Slack Notification`: sends a notification to a Slack channel via webhook.
- `Discord Notification`: sends a notification to a Discord channel via webhook.
- `Email Notification`: sends an email to the provided email address.
- `Teams Notification`: sends a notification to Microsoft Teams via webhook.
- `Mqtt Notification`: sends a notification to an MQTT broker.

### Plot Configuration

This action consists in creating two plot configurations when a detection event is triggered: the first one includes
data preceding the event, while the second one includes data following the event.

### Retrain

Retrain Action enables the automatic retraining of your model. Therefore, it is only available when the target of the rule is related to a model.
The retrain action does not need any parameter because it is automatically inferred from the `Model Name` attribute of the rule.
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

[Detection Event]: detection_event.md