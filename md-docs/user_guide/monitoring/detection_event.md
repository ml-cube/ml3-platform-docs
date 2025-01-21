# Detection Event

A Detection Event is raised by the ML cube Platform when a significant change is detected in one of the entities being monitored.

An event is characterized by the following attributes:

| Attribute          | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | 
|--------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Eventy Type        | The type of the event. It's possible values are: <div class="nice-list"><ul><li> `Warning On`: the monitoring entity is experiencing slight changes that might lead to a drift.</li><li> `Warning Off`: the monitoring entity has returned to the reference distribution. </li><li> `Drift On`: the monitoring entity has drifted from the reference distribution.</li><li> `Drift Off`: the monitoring entity has returned to the reference distribution.</li> </ul></div> |
| Severity           | The severity of the event. It's provided only for drift events and it can be `Low`, `Medium`, or `High`.                                                                                                                                                                                                                                                                                                                                                                    |
| Monitoring Target  | The [Monitoring Target](index.md#monitoring-metrics) being monitored.                                                                                                                                                                                                                                                                                                                                                                                                       |
| Monitoring Metric  | The [Monitoring Metric](index.md#monitoring-metrics) being monitored.                                                                                                                                                                                                                                                                                                                                                                                                       |
| Model Name         | The name of the model that raised the event. It's present only if the event is related to a model.                                                                                                                                                                                                                                                                                                                                                                          |
| Model Version      | The version of the model that raised the event. It's present only if the event is related to a model.                                                                                                                                                                                                                                                                                                                                                                       |
| Insert datetime    | The time when the event was raised.                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| Sample timestamp   | The timestamp of the sample that triggered the event.                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Sample customer ID | The ID of the sample that triggered the event.                                                                                                                                                                                                                                                                                                                                                                                                                              |
| User feedback      | The feedback provided by the user on whether the event was expected or not.                                                                                                                                                                                                                                                                                                                                                                                                 |
| Segment ID         | The ID of the segment being monitored.                                                                                                                                                                                                                                                                                                                                                                                                                                      |


## Retrieve Detection Events

You can access the detection events generated by the Platform in two ways:

- **SDK**: it can be used to retrieve all detection events for a specific task programmatically.
- **WebApp**: navigate to the `Detection` section located in the task page's sidebar. Here, all detection events are displayed in a table, 
   with multiple filtering options available for useful event management. Additionally, the latest detection events identified are shown in the Task homepage,
   in the section named "Latest Detection Events".

??? code-block "SDK Example"

    The following code demonstrates how to retrieve all detection events for a specific task.

    ```python
    detection_events = client.get_detection_events(task_id='my-task-id')
    ```

## User Feedback

When a `Drift On` event is raised, you can provide feedback on whether the event was expected or not. This feedback is then used 
to tune the monitoring algorithms and improve their performance. The feedback can be provided through the WebApp, in the
`Detection` section of the task page, or through the SDK.


## Detection Event Rules

To automate actions upon the reception of a detection event, you can set up Detection Event Rules. 
You can learn more about how to configure them in the [Detection Event Rules] section.


[Monitoring]: index.md
[Detection Event Rules]: detection_event_rules.md