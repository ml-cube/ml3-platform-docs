This section provides an overview of how you can setup retrain triggers for your models so that you can automatically start your retraining pipeline from ML cube Platform.
A retrain trigger can be used inside a Detection Event Rule that when specific criteria are met automatically computes the retrain report and then push the trigger, or in the retraining tool page where you can manually push the trigger for the model.

A retrain trigger is modelled as an integration to an external service and requires credentials with the right privileges to perform the action.

## Supported Triggers

The following retrain triggers are supported:

- `AWS Event Bridge`: creates an event to Event Bus with specific metadata.

### AWS Event Bridge

If you have your MLOps pipelines inside AWS ecosystem then you probably need the AWS Event Bridge retrain trigger.
The trigger consists in creating an event in a Event Bus of your AWS account with custom metadata.
You need to create an Event Bus rule that recognises the right the ML cube Platform pattern and attach the target action you want.
Examples of targets are:

- launching a Lambda function;
- launching a SageMaker pipeline;
- sending a message to a SQS Queue with a retraining request.

#### Event Bus Setup

1. From AWS console open the EventBridge service and on the left menu select the voice `Event buses`
<figure markdown>
  ![Image title](../imgs/aws event bridge/0 aws_event_bus.png){ width="800" }
</figure>
2. In the `Custom event bus` tab create a new event bus
<figure markdown>
  ![Image title](../imgs/aws event bridge/1 rule detail.png){ width="800" }
</figure>
3. Select the `Rules` section on the left menu and click the button `Create Rule`
4. Insert the rule name and in the Event Bus section the created Event Bus. Click `Next`
    1. `Event source`: select the voice *AWS events or EventBridge patner events*
    <figure markdown>
    ![Image title](../imgs/aws event bridge/2 event source.png){ width="800" }
    </figure>
    2. `Sample event`: copy and paste this:
```json
{
    "version": "0",
    "id": "fcdd87c7-f56e-c722-4f85-4cb6ba85a00a",
    "detail-type": "retrain-trigger",
    "source": "ml3_platform",
    "time": "2023-11-02T14:16:23Z",
    "resources": [],
    "detail": {
        "model_id": "fcdd87c7-f56e-c722-4f85-4cb6ba85a00a"
    }
}
```
    <figure markdown>
    ![Image title](../imgs/aws event bridge/3 sample event.png){ width="800" }
    </figure>
    3. `Creation method`: select Custom pattern (JSON editor)
    <figure markdown>
    ![Image title](../imgs/aws event bridge/4 creation method.png){ width="800" }
    </figure>
    4. `Event pattern`: copy and paste this:
    <figure markdown>
    ![Image title](../imgs/aws event bridge/5 event pattern.png){ width="800" }
    </figure>
    ```json
    {
        "source": [{
            "prefix": "ml3_platform"
        }],
        "detail-type": [{
            "prefix": "retrain_trigger"
        }]
    }
    ```
    5. click the button Test pattern to check the match and then click next

5. Select the target you want to start. If you want to test the rule, you can add a CloudWatch target that stores the event to a new Log Group.
    <figure markdown>
    ![Image title](../imgs/aws event bridge/6 select target.png){ width="800" }
    </figure>
6. Create the rule