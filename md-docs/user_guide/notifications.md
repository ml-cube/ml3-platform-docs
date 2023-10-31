# Notifications

This section provides an overview of how you can receive notifications when a detection event occurs on the ML cube Platform.

## Detection Event Rules
When a detection event occurs, the platform evaluates your set detection event rules. If a rule matches the event, the specified actions will be triggered. These rules are specific to a task and require the following parameters for configuration:

- `name`: A descriptive label for your rule, helping you understand its purpose quickly.
- `task_id`: The unique identifier of the task to which the rule is applicable.
- `severity`: Indicates the severity level of the event - it can be `HIGH`, `MEDIUM`, or `LOW`.
- `detection_event_type`: Currently, only `DRIFT` events are available for detection.
- `monitoring_target`: Specifies what is being monitored, which can be `MODEL`, `INPUT`, or `CONCEPT`. If the value is `MODEL`, you need to provide a corresponding `model_name`.
- `actions`: A sequential list of actions to be executed when the rule is triggered.

## Supported Actions
The following actions are currently supported:

- `SlackNotificationAction`: sends a notification to a Slack channel via webhook.
- `DiscordNotificationAction`: sends a notification to a Discord channel via webhook.
- `EmailNotificationAction`: sends an email to the provided email address.
- `TeamsNotificationAction`: sends a notification to Microsoft Teams via webhook.

!!! example
    The following code snippet demonstrates how to create a rule that matches high severity drift events for a specific model. When triggered, it sends a notification to the `ml3-platform-notifications` channel on your Slack workspace using the provided webhook URL.

    ```py
    rule_id = client.create_detection_event_rule(
        name='Send Slack notification on my_model severe drift',
        task_id='my-task-id,
        model_name='my-model',
        severity=DetectionEventSeverity.HIGH,
        detection_event_type=DetectionEventType.DRIFT,
        monitoring_target=MonitoringTarget.MODEL,
        actions=[
            SlackNotificationAction(
                webhook='https://hooks.slack.com/services/...',
                channel='ml3-platform-notifications'
            ),
        ],
    )
    ```
