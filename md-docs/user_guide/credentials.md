# Credentials
Below, you will find a guide that will help you create the credentials and configure the permissions that ML cube will use to access your resources on the supported cloud providers.

## Creating the credentials

=== "Amazon Web Services"
    ![Amazon Web Services](../imgs/aws.svg){: style="height:50px;width:50px"}

    The ML cube Platform can assume an **IAM Role** on your AWS Account, that can be used to authorize actions on specific resources.
    To create this, log into your AWS account and open the AWS console. Here, go to the **IAM** service, navigate to the **Roles** section and create a new role. When asked, select the **Custom trust policy** option and paste the following json:

    ```json
    {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Sid": "Statement1",
                "Effect": "Allow",
                "Principal": {
                    "AWS": "arn:aws:iam::883313729965:root"
                },
                "Action": "sts:AssumeRole",
                "Condition": {
                    "StringEquals": {
                        "sts:ExternalId": "<EXTERNAL_ID>"
                    }
                }
            }
        ]
    }
    ```

    `883313729965` is the ID of the AWS Account used by the ML cube Platform. It is important that this value is not changed. We will populate the value of `<EXTERNAL_ID>` in a later step. Give your role a name and save it.

    Now, you will need to create the credentials through the ML cube Platform SDK or the web application.

    !!! example
        The following code will create a set of AWS credentials from the IAM Role we just created.

        ```py
        aws_creds = client.create_aws_integration_credentials(
            name='AWS_01',
            default=True,  # Set these credentials as the default to use when not specified
            project_id='your_project_id',
            role_arn='arn:aws:iam::{{YOUR_AWS_ACCOUNT_ID}}:role/{{YOUR_ROLE_NAME}}',
        )

        trust_policy = aws_creds.generate_trust_policy()
        print(trust_policy)
        ```

    You can call the `generate_trust_policy` function on the created credentials to obtain the **trust policy**.
    Edit your IAM Role and change the **trust policy** to the one you just obtained.

    Right now, your **IAM Role** grants no permissions. Please refer to the next sections that will explain how to set up **IAM Policies** for S3, Event Bridge and so on.

    To revoke access, simply delete the role or change the trust policy.

=== "Google Cloud Platform"
    ![Google Cloud Platform](../imgs/gcp.svg){: style="height:50px;width:50px"}

    The ML cube Platform can operate in your GCP Account through the creation of a dedicated **Service Account**. You will then be able to assign one or more **IAM Roles** to this Service Account, to allow the ML cube Platform to perform specific actions.

    To configure a Service Account for ML cube Platform, log into your GCP account, select the correct project and open the **Cloud Shell**. You can find the button to open it in the upper-right corner of the page. Now we will enter some commands that will create the **Service Account** with the required permissions. A description of each command is provided to help you understand its purpose.

    ```bash
    # Change this according to your project
    export GCP_PROJECT=my-project

    # Creates a service account called ml3PlatformServiceAccount
    gcloud iam service-accounts create ml3PlatformServiceAccount --display-name "ML3 Platform Service Account"

    # Generates the access key that will be used to authenticate as the service account
    gcloud iam service-accounts keys create ml3-platform-key.json --iam-account=ml3PlatformServiceAccount@$GCP_PROJECT.iam.gserviceaccount.com

    # Displays the access key to the terminal screen
    cat ml3-platform-key.json
    ```

    Copy the JSON object containing the key and save it to a file with the same name on your disk.
    Now, you will need to create the GCP credentials, either through the SDK or the web application, and provide the contents of the JSON file you just created.

    !!! example
        The following code will create a set of GCP credentials that will be able to access the service account.

        ```py
        with open('path/to/ml3-platform-key.json', 'r') as f:
            creds_json = f.read()

            gcp_creds = client.create_gcp_integration_credentials(
                name='GCP_01',
                default=True,  # Set these credentials as the default to use when not specified
                project_id='your_project_id',
                service_account_info_json=creds_json
            )
        ```

    Right now, your **IAM Role** grants no permissions. Please refer to the next sections that will explain how to set up **IAM Policies** for Google Cloud Storage, Pub/Sub and so on.

=== "Microsoft Azure"
    ![Microsoft Azure](../imgs/azure.svg){: style="height:50px;width:50px"}
    
    The ML cube Platform can operate in your Azure Account through the creation of a dedicated **Service Principal**. You will then be able to assign one or more **Roles** to this Service Principal, to allow the ML cube Platform to perform specific actions.

    To configure a Service Principal for ML cube Platform, log into your Azure account, select the correct project and open the **Cloud Shell**. You can find the button to open it in the upper-right corner of the page. Set the Cloud Shell to use bash instead of powershell. Now we will enter the following command that will create the **Service Principal**.

    ```bash
    az ad sp create-for-rbac --name ML3PlatformSP --skip-assignment
    ```

    Once the operation finishes running, it will output a JSON object with the following fields: `appId`, `displayName`, `password` and `tenant`. Copy this object and save it to a file on your disk, for example `azure-credentials.json`.

    Now, you will need to create the Azure credentials, either through the SDK or the web application, and provide the contents of the JSON file you just created.

    !!! example
        The following code will create a set of Azure credentials that will be able to access the service account.

        ```py
        with open('path/to/azure-credentials.json', 'r') as f:
            creds_json = f.read()

            azure_creds = client.create_azure_integration_credentials(
                name='AZURE_01',
                default=True,  # Set these credentials as the default to use when not specified
                project_id='your_project_id',
                service_principal_credentials_json=creds_json
            )
        ```

## Storage integration

=== "AWS S3"
    ![Amazon Web Services](../imgs/aws.svg){: style="height:50px;width:50px"}

    Log into your AWS account and open the AWS console, then go to the **IAM** service and navigate to the **Policies** section. Here, we will create an **IAM Policy**.

    !!! example
        The following policy will grant read access to objects in the `my-company-data-bucket` to the IAM entity it is attached to.

        ```json
        {
            "Version": "2012-10-17",
            "Statement": [
                {
                    "Sid": "Statement1",
                    "Effect": "Allow",
                    "Action": [
                        "s3:GetBucketTagging",
                        "s3:GetObject",
                        "s3:ListBucket"
                    ],
                    "Resource": [
                        "arn:aws:s3:::my-company-data-bucket",
                        "arn:aws:s3:::my-company-data-bucket/*"
                    ]
                }
            ]
        }
        ```

    Once the **IAM Policy** has been created, navigate to the **Roles** section, select the **IAM Role** you previously created and finally attach the **IAM Policy** to it.

=== "Google Cloud Storage"
    ![Google Cloud Platform](../imgs/gcp.svg){: style="height:50px;width:50px"}

    Log into your GCP account, select the correct project and open the **Cloud Shell**. You can find the button to open it in the upper-right corner of the page. Now we will enter some commands that will create an **IAM Role** with the required permissions, bind it to the service account you previously created, and grant access to the bucket. A description of each command is provided to help you understand its purpose.

    ```bash
    # Change these according to your project and bucket
    export GCP_PROJECT=my-project
    export GCP_BUCKET=my-company-data-bucket

    # Creates an IAM Role called ml3PlatformStorageRole for your project, with read permissions on buckets and objects in the storage service
    gcloud iam roles create ml3PlatformStorageRole --project=$GCP_PROJECT --title="ML3 Platform Storage Role" --description="Role that allows the ML cube Platform to access storage resources in a project" --permissions=storage.buckets.get,storage.buckets.list,storage.objects.get,storage.objects.list --stage=ALPHA

    # Adds the IAM Role to the previously created service account
    gcloud projects add-iam-policy-binding $GCP_PROJECT --member=serviceAccount:ml3PlatformServiceAccount@$GCP_PROJECT.iam.gserviceaccount.com --role=projects/$GCP_PROJECT/roles/ml3PlatformStorageRole

    # Allows the service account we created to access the given bucket with the objectViewer role
    gsutil iam ch serviceAccount:ml3PlatformServiceAccount@$GCP_PROJECT.iam.gserviceaccount.com:roles/storage.objectViewer gs://$GCP_BUCKET
    ```

=== "Azure Blob Storage"
    ![Microsoft Azure](../imgs/azure.svg){: style="height:50px;width:50px"}

    Log into your Azure account and open the **Cloud Shell**. You can find the button to open it in the upper-right corner of the page. The following command will associate the previously created Service Principal with a role that is able to read data from a given blob container.

    ```bash
    # Change these according to your project and storage configuration
    export SERVICE_PRINCIPAL_APP_ID=my-sp-app-id
    export SUBSCRIPTION_ID=my-azure-subscription-id
    export RESOURCE_GROUP=my-azure-resource-group
    export STORAGE_ACCOUNT=my-storage-account
    export BLOB_CONTAINER=my-blob-container

    az role assignment create --assignee $SERVICE_PRINCIPAL_APP_ID --role "Storage Blob Data Reader" --scope /subscriptions/$SUBSCRIPTION_ID/resourceGroups/$RESOURCE_GROUP/providers/Microsoft.Storage/storageAccounts/$STORAGE_ACCOUNT/blobServices/default/containers/$BLOB_CONTAINER
    ```

## Retrain events integration

=== "Amazon EventBridge"
    ![Amazon Web Services](../imgs/aws.svg){: style="height:50px;width:50px"}

    Log into your AWS account and open the AWS console, then go to the **IAM** service and navigate to the **Policies** section. Here, we will create an **IAM Policy**.

    !!! example
        The following policy will allow an **IAM Entity** to put events in a specific event bus.

        ```json
        {
            "Version": "2012-10-17",
            "Statement": [
                {
                    "Sid": "Statement1",
                    "Effect": "Allow",
                    "Action": [
                        "events:PutEvents"
                    ],
                    "Resource": [
                        "arn:aws:events:<REGION>:<ACCOUNT_ID>:event-bus/<EVENT_BUS_NAME>"
                    ]
                }
            ]
        }
        ```

        Replace `<REGION>`, `<ACCOUNT_ID>` and `<EVENT_BUS_NAME>` with your desired values.

    Once the **IAM Policy** has been created, navigate to the **Roles** section, select the **IAM Role** you previously created and finally attach the **IAM Policy** to it.

=== "GCP Pub/Sub"
    ![Google Cloud Platform](../imgs/gcp.svg){: style="height:50px;width:50px"}

    Log into your GCP account, select the correct project and open the **Cloud Shell**. You can find the button to open it in the upper-right corner of the page. Now we will enter some commands that will create an **IAM Policy** with the required permissions, bind it to the service account you previously created, and grant access to the Pub/Sub topic. A description of each command is provided to help you understand its purpose.

    ```bash
    # Change these according to your project and topic
    export GCP_PROJECT=my-project
    export GCP_TOPIC=my-topic

    # Adds a new IAM Policy to the previously created service account, granting publish access to the Pub/Sub topic
    gcloud pubsub topics add-iam-policy-binding $GCP_TOPIC --member=serviceAccount:ml3PlatformServiceAccount@$GCP_PROJECT.iam.gserviceaccount.com --role=roles/pubsub.publisher
    ```

=== "Azure Event Grid"
    ![Microsoft Azure](../imgs/azure.svg){: style="height:50px;width:50px"}

    Log into your Azure account and open the **Cloud Shell**. You can find the button to open it in the upper-right corner of the page. The following command will associate the previously created Service Principal with a role that is able to publish events to an Event Grid topic.

    ```bash
    # Change these according to your project and storage configuration
    export SERVICE_PRINCIPAL_APP_ID=my-sp-app-id
    export SUBSCRIPTION_ID=my-azure-subscription-id
    export RESOURCE_GROUP=my-azure-resource-group
    export TOPIC_ID=my-topic

    az role assignment create --assignee $SERVICE_PRINCIPAL_APP_ID --role "EventGrid Data Sender" --scope /subscriptions/$SUBSCRIPTION_ID/resourceGroups/$RESOURCE_GROUP/providers/Microsoft.EventGrid/topics/$TOPIC_ID
    ```
