# Data Sources

This page provides guidance on integrating external data sources into your ML cube Platform project. There are three types of data sources you can use to enable the ML cube Platform to access your data:

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
To allow the ML cube Platform to access your external data sources, you need to configure credentials for them. Once the credentials have been configured, they will be available across your entire project, so multiple tasks in the same project will be able to access the same credentials.

You can configure multiple credentials for the same provider, for example you could have two sets of credentials to access two different S3 buckets on two different AWS accounts.

Below, you can find the configuration steps required to integrate the data source of your choice

=== "Amazon S3"
    ![Amazon Web Services](../imgs/aws.svg){: style="height:50px;width:50px"}
    
    To integrate Amazon S3, you will need to create a set of AWS credentials, and add a policy that grants read access to objects in your bucket. Please refer to [this page](../credentials) to know more.

    Once you have some credentials, you will be able to specify an `S3DataSource` when adding your data to a task.

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

=== "Google Cloud Storage"
    ![Google Cloud Platform](../imgs/gcp.svg){: style="height:50px;width:50px"}

    To integrate Google Cloud Storage, you will need to create a set of GCP credentials, and add a policy that grants read access to objects in your bucket. Please refer to [this page](../credentials) to know more.

    Once you have some credentials, you will be able to specify a `GCSDataSource` when adding your data to a task.

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
