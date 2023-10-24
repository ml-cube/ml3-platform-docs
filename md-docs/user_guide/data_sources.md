# Data Sources

This page provides guidance on integrating your data sources into your ML cube Platform project. There are three types of data sources you can use to enable the ML cube Platform to access your data:

1. Local data source
2. Remote data source with ML cube Storage
3. Remote data source with Customer Storage

## Local Data Source
This is the easiest way to send data to the ML cube Platform. You can simply specify the path to the local file you want to upload, and it will be uploaded to the ML cube Platform Secure Storage, where it is automatically processed.

!!! example

    ```py
    job_id = client.add_historical_data(
        task_id='your_task_id',
        features_data_source=LocalDataSource(
            dataset_type=DatasetType.TABULAR, file_path='historical_features.csv'
        ),
        targets_data_source=LocalDataSource(
            dataset_type=DatasetType.TABULAR, file_path='historical_targets.csv'
        ),
    )
    ```

## Remote Data Source
While using a local data source can be a good way to try out the features that the ML cube Platform can offer, in a production scenario you will usually want to integrate your remote data sources with your project. You can decide where you want your data to be stored.

### ML cube Storage
This method should be used when the ML cube Platform is allowed to perform a one-time read of the raw data from your data source, and make a copy of it inside the ML cube Platform Secure Storage. This allows the ML cube Platform to store a server-side copy of the processed dataset for quicker access and analysis. Remember that you can request the deletion of your data at any time.

### Customer Storage
This method should be used when, due to compliance requirements, the ML cube Platform is only allowed to read data from your data sources when it needs to access it, without storing any sensitive information in its systems. The ML cube Platform will only store a set of anonymous identifiers that are used for data mapping. This gives you the ability to be in full control of when the ML cube Platform can access your data, but it comes at the expense of performance and cost, since constant data transfers can be slow and expensive.

## Integration Credentials
The ML cube Platform SDK provides a way to configure credentials that can be used to access the integrated data sources of your choice. The scope of these credentials is a project, so multiple tasks in the same project will be able to access the same credentials. You can configure multiple credentials for the same provider, for example you could have two sets of credentials to access two different AWS S3 buckets.

Below, you can find the configuration steps required to integrate the data source of your choice

=== "Amazon S3"
    ![Amazon Web Services](../imgs/aws.svg){: style="height:50px;width:50px"}
    
    To integrate Amazon S3, you will need to create a set of AWS credentials. Before doing this, you need to create an **IAM Role** in your AWS Account that will be used by the ML cube Platform to read data from the S3 bucket of your choice.

    First of all, log into your AWS account and open the AWS console. Here, go to the **IAM** service, then navigate to the **Policies** section. Here, we will create an **IAM Policy**.

    !!! example
        The following policy will allow read access to objects in the `my-company-data-bucket` to the IAM entity it is attached to.

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

    Once the **IAM Policy** has been created, navigate to the **Roles** section and create a new role. When asked, select the `Custom trust policy` option and accept the default policy. Then, assign the **IAM Policy** we created previously to the role, so any entity that assumes the role will be able to access the S3 bucket.

    Now, you will need to create the credentials through the ML cube Platform SDK.

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

    Now, you will be able to specify an `S3DataSource` when adding your data to a task.

    !!! example
        Note that, if you don't specify the `credentials_id`, the default ones will be used.

        ```py
        job_id = client.add_historical_data(
            task_id='your_task_id',
            features_data_source=S3DataSource(
                dataset_type=DatasetType.TABULAR,
                object_path='s3://my-company-data-bucket/historical/features.csv',
                credentials_id=aws_creds.credentials_id
            ),
            targets_data_source=S3DataSource(
                dataset_type=DatasetType.TABULAR,
                object_path='s3://my-company-data-bucket/historical/targets.csv',
                credentials_id=aws_creds.credentials_id
            ),
        )
        ```

    Congratulations! You have successfully connected your S3 bucket to the ML cube Platform. The ML cube Platform will now be able to assume the role via STS by providing the secret `external_id` that is included in the trust policy. This way, only the ML cube Platform is able to access that specific role on your AWS account. To revoke access, simply delete the role or change the trust policy.

=== "Google Cloud Storage"
    ![Google Cloud Platform](../imgs/gcp.svg){: style="height:50px;width:50px"}

    To integrate Google Cloud Storage, you will need to create a set of GCP credentials. Before doing this, you need to create a **Service Account** in your GCP Account that will be used by the ML cube Platform to read data from the GCS bucket of your choice.

    First of all, log into your GCP account, select the correct project and open the **Cloud Shell**. You can find the button to open it in the upper-right corner of the page. Now we will enter some commands that will create the **Service Account** with the required permissions. A description of each command is provided to help you understand its purpose.

    ```bash
    # Change these according to your project and bucket
    export GCP_PROJECT=my-project
    export GCP_BUCKET=my-company-data-bucket

    # Creates an IAM Role called ml3PlatformServiceRole for your project, with read permissions on buckets and objects in the storage service
    gcloud iam roles create ml3PlatformServiceRole --project=$GCP_PROJECT --title="ML3 Platform Service Role" --description="Role that allows the ML cube Platform to access resources in a project" --permissions=storage.buckets.get,storage.buckets.list,storage.objects.get,storage.objects.list --stage=ALPHA

    # Creates a service account called ml3PlatformServiceAccount
    gcloud iam service-accounts create ml3PlatformServiceAccount --display-name "ML3 Platform Service Account"

    # Adds the previously created IAM Role to the service account
    gcloud projects add-iam-policy-binding $GCP_PROJECT --member=serviceAccount:ml3PlatformServiceAccount@$GCP_PROJECT.iam.gserviceaccount.com --role=projects/$GCP_PROJECT/roles/ml3PlatformServiceRole

    # Allows the service account we created to access the given bucket with the objectViewer role
    gsutil iam ch serviceAccount:ml3PlatformServiceAccount@$GCP_PROJECT.iam.gserviceaccount.com:roles/storage.objectViewer gs://$GCP_BUCKET

    # Generates the access key that will be used to authenticate as the service account
    gcloud iam service-accounts keys create ml3-platform-key.json --iam-account=ml3PlatformServiceAccount@$GCP_PROJECT.iam.gserviceaccount.com

    # Displays the access key to the terminal screen
    cat ml3-platform-key.json
    ```

    Copy the JSON object containing the key and save it to a file with the same name on your disk.

    Now, you will need to create the credentials through the ML cube Platform SDK.

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

    Now, you will be able to specify a `GCSDataSource` when adding your data to a task.

    !!! example
        Note that, if you don't specify the `credentials_id`, the default ones will be used.

        ```py
        job_id = client.add_historical_data(
            task_id='your_task_id',
            features_data_source=GCSDataSource(
                dataset_type=DatasetType.TABULAR,
                object_path='gs://my-company-data-bucket/historical/features.csv',
                credentials_id=gcp_creds.credentials_id
            ),
            targets_data_source=GCSDataSource(
                dataset_type=DatasetType.TABULAR,
                object_path='gs://my-company-data-bucket/historical/targets.csv',
                credentials_id=gcp_creds.credentials_id
            ),
        )
        ```

    Congratulations! You have successfully connected your GCS bucket to the ML cube Platform. The ML cube Platform will now be able to authenticate to the service account you created via the generated key. To revoke access, simply delete the key.

=== "Azure Blob Storage"
    ![Microsoft Azure](../imgs/azure.svg){: style="height:50px;width:50px"}
    
    To integrate Azure Blob Storage, you will need to create a set of Azure credentials. Before doing this, you need to create a **Service Principal** in your Azure Account that will be used by the ML cube Platform to read data from the specified Container in the Storage Account of your choice.

    First of all, log into your Azure account, select the correct project and open the **Cloud Shell**. You can find the button to open it in the upper-right corner of the page. Set the Cloud Shell to use bash instead of powershell. Now we will enter the following commands that will create the **Service Principal** with the required permissions to read blobs from your container.

    ```bash
    # Change these according to your Azure resources
    export SUBSCRIPTION_ID=your-subscription-id
    export RESOURCE_GROUP=your-resource-group
    export STORAGE_ACCOUNT=your-storage-account
    export BLOB_CONTAINER=your-blob-container

    az ad sp create-for-rbac --name ML3PlatformSP --role "Storage Blob Data Reader" --scopes /subscriptions/$SUBSCRIPTION_ID/resourceGroups/$RESOURCE_GROUP/providers/Microsoft.Storage/storageAccounts/$STORAGE_ACCOUNT/blobServices/default/containers/$BLOB_CONTAINER
    ```
    
    If you would like to use a custom role, for example to restrict the reads to a specific subfolder, create it and then replace "Storage Blob Data Reader" with the name of your role.

    Once the operation finishes running, it will output a JSON object with the following fields: `appId`, `displayName`, `password` and `tenant`. Copy this object and save it to a file on your disk, for example `azure-credentials.json`.

    Now, you will need to create the credentials through the ML cube Platform SDK.

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

    Now, you will be able to specify an `AzureBlobDataSource` when adding your data to a task.

    !!! example
        Note that, if you don't specify the `credentials_id`, the default ones will be used.

        ```py
        job_id = client.add_historical_data(
            task_id='your_task_id',
            features_data_source=AzureBlobDataSource(
                dataset_type=DatasetType.TABULAR,
                object_path='https://mystorageaccount.blob.core.windows.net/my-container/historical/features.csv',
                credentials_id=azure_creds.credentials_id
            ),
            targets_data_source=AzureBlobDataSource(
                dataset_type=DatasetType.TABULAR,
                object_path='https://mystorageaccount.blob.core.windows.net/my-container/historical/targets.csv',
                credentials_id=azure_creds.credentials_id
            ),
        )
        ```

    Congratulations! You have successfully connected your Azure blob container to the ML cube Platform. The ML cube Platform will now be able to authenticate to the service principal you created via the generated key. To revoke access, search for 'App Registrations' in the Azure Console, then navigate to the 'All Applications' tab, select 'ML3PlatformSP' and delete it.

=== "Databricks"
    ![Databricks](../imgs/databricks.svg){: style="height:50px;width:50px"}

    *Coming Soon...*
