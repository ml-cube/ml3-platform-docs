# Data Sources

This page provides guidance on integrating external data sources into your ML cube Platform project. There are three types of data sources you can use to enable the ML cube Platform to access your data:

1. Local data source
2. Remote data source with ML cube Storage
3. Remote data source with Customer Storage

## Local Data Source
This is the easiest way to send data to the ML cube Platform. You can simply specify the path to the local file you want to upload, and it will be uploaded to the ML cube Platform Secure Storage, where it is automatically processed.

!!! example

    ```py
    data = TabularData(
        source=LocalDataSource(
            data_structure=DataStructure.TABULAR,
            file_type=FileType.CSV,
            file_path=file_path,
        )
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
    ![Amazon Web Services](../../imgs/aws.svg){: style="height:50px;width:50px"}
    
    To integrate Amazon S3, you will need to create a set of AWS credentials, and add a policy that grants read access to objects in your bucket. Please refer to [this page](index.md) to know more.

    Once you have some credentials, you will be able to specify an `S3DataSource` when adding your data to a task.

    !!! example
        Note that, if you don't specify the `credentials_id`, the default ones will be used.

        ```py
        data = TabularData(
            source=S3DataSource(
                object_path='s3://my-company-data-bucket/historical/features.csv',
                credentials_id=aws_creds.credentials_id,
                data_structure=DataStructure.TABULAR,
                file_type=FileType.CSV,
            )
        )
        ```

=== "Google Cloud Storage"
    ![Google Cloud Platform](../../imgs/gcp.svg){: style="height:50px;width:50px"}

    To integrate Google Cloud Storage, you will need to create a set of GCP credentials, and add a policy that grants read access to objects in your bucket. Please refer to [this page](index.md) to know more.

    Once you have some credentials, you will be able to specify a `GCSDataSource` when adding your data to a task.

    !!! example
        Note that, if you don't specify the `credentials_id`, the default ones will be used.

        ```py
        data = TabularData(
            source=GCSDataSource(
                object_path='gs://my-company-data-bucket/historical/features.csv',
                credentials_id=gcp_creds.credentials_id,
                data_structure=DataStructure.TABULAR,
                file_type=FileType.CSV,
            )
        )
        ```

=== "Azure Blob Storage"
    ![Microsoft Azure](../../imgs/azure.svg){: style="height:50px;width:50px"}
    
    To integrate Azure Blob Storage, you will need to create a set of Azure credentials, and add a policy that grants read access to objects in your blob container. Please refer to [this page](index.md) to know more.
    
    Once you have some credentials, you will be able to specify an `AzureBlobDataSource` when adding your data to a task.

    !!! example
        Note that, if you don't specify the `credentials_id`, the default ones will be used.

        ```py
        data = TabularData(
            source=AzureBlobDataSource(
                object_path='https://mystorageaccount.blob.core.windows.net/my-container/historical/features.csv',
                credentials_id=azure_creds.credentials_id
                data_structure=DataStructure.TABULAR,
                file_type=FileType.CSV,
            )
        )
        ```

=== "MinIO"
    ![MinIO](../../imgs/minio.svg){: style="width:100px"}
    
    To integrate MinIO, follow these steps:

1. Create a set of AWS-compatible credentials:
    - Set `access_key_id` to the username of the MinIO user you want to use.
    - Set `secret_access_key` to the password of that MinIO user.
    - Set `endpoint_url` to the URL of your MinIO instance.
2. Ensure accessibility:
    - The MinIO instance must be reachable from the ML cube Platform.
    - If you're using the SaaS version, the MinIO instance must be accessible over the internet.
3. Set appropriate permissions:
    - The specified MinIO user must have read access to the bucket and its objects.

    Then, you will be able to specify an `S3DataSource` when adding your data to a task.

    !!! example
        Note that, if you don't specify the `credentials_id`, the default ones will be used.

        ```py
        data = TabularData(
            source=S3DataSource(
                object_path='s3://my-company-data-bucket/historical/features.csv',
                credentials_id=aws_creds.credentials_id,
                data_structure=DataStructure.TABULAR,
                file_type=FileType.CSV,
            )
        )
        ```
