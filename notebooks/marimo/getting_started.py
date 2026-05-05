import marimo

__generated_with = "0.23.1"
app = marimo.App(width="full")


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Getting started

    Welcome to ML cube Platform SDK guide!

    In this notebook you will learn how to setup create your first project and taks.
    The nootebook generates a dataset for multiclass classification task to show you how to interact with ML cube Platform via the Python SDK.
    All the operations you see here in the notebook, with the exception of data uploads, can be performed directly via the [web application](https://app.platform.mlcube.com).

    > Note: you need an API key to use `MLcubePlatformClient`, the notebook assumes it is set as environment variable MLCUBE_PLATFORM_API_KEY

    **Requirements:**

    ```toml
    dependencies = [
        "ml3_platform_client>=1.0",
        "scikit-learn>=1.7",
    ]
    ```
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Variables
    """)
    return


@app.cell
def _(model_name, model_version):
    input_columns = ('x0', 'x1')
    target_column = 'target'
    prediction_column = f'{model_name}@{model_version}'
    time_id_column = 'timestamp'
    sample_id_column = 'sample_id'
    return (
        input_columns,
        prediction_column,
        sample_id_column,
        target_column,
        time_id_column,
    )


@app.cell
def _():
    model_name = 'example model'
    model_version = 'v1'
    return model_name, model_version


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Import libraries

    Everything starts by importing the required libraries, what you need is the client class and the enums and models modules that are imported with `ml3_enums` and `ml3_models` aliases.

    Then from scikit learn import dataset generation function, logistic regression classifier and other utilies
    """)
    return


@app.cell
def _():
    from ml3_platform_sdk.client import ML3PlatformClient
    from ml3_platform_sdk import enums as ml3_enums
    from ml3_platform_sdk import models as ml3_models

    from sklearn.datasets import make_blobs
    from sklearn.linear_model import LogisticRegression
    from sklearn.preprocessing import StandardScaler

    import os
    import numpy as np
    import polars as pl
    from uuid import uuid4
    import datetime as dt
    from tempfile import TemporaryDirectory
    import dotenv

    return (
        LogisticRegression,
        ML3PlatformClient,
        StandardScaler,
        TemporaryDirectory,
        dotenv,
        dt,
        make_blobs,
        ml3_enums,
        ml3_models,
        np,
        os,
        pl,
        uuid4,
    )


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Dataset preparation and model fit

    This section prepares data in training, test and production data groups, trains the model and makes prediction on unseen data. Those data will be uploaded to ML cube Platform.
    """)
    return


@app.cell
def _(
    LogisticRegression,
    StandardScaler,
    dt,
    input_columns,
    make_blobs,
    np,
    pl,
    prediction_column,
    sample_id_column,
    target_column,
    time_id_column,
    uuid4,
):
    # create data
    train_X, train_y = make_blobs(n_samples=1500, centers=3, cluster_std=0.5, random_state=0)
    test_X, test_y = make_blobs(n_samples=500, centers=3, cluster_std=0.5, random_state=0)
    production_X, production_y = make_blobs(n_samples=500, centers=3, cluster_std=0.5, random_state=0)

    # normalize data
    scaler = StandardScaler().fit(train_X)
    train_X = scaler.transform(train_X)
    test_X = scaler.transform(test_X)
    production_X = scaler.transform(production_X)

    # fit the model
    model = LogisticRegression().fit(train_X, train_y)
    train_yhat = model.predict(train_X)
    test_yhat = model.predict(test_X)
    production_yhat = model.predict(production_X)

    # define timestamps
    delta_ts = 5 * 60
    starting_timestamp = float((dt.datetime.now() - dt.timedelta(days=7)).timestamp())
    train_timestamps = list(np.arange(starting_timestamp, starting_timestamp + train_X.shape[0] * delta_ts, delta_ts))
    test_timestamps = list(np.arange(train_timestamps[-1] + delta_ts, train_timestamps[-1] + delta_ts + test_X.shape[0] * delta_ts, delta_ts))
    production_timestamps = list(np.arange(test_timestamps[-1] + delta_ts, test_timestamps[-1] + delta_ts + production_X.shape[0] * delta_ts, delta_ts))

    # define sample ids
    train_sample_ids = [str(uuid4()) for _ in range(train_X.shape[0])]
    test_sample_ids = [str(uuid4()) for _ in range(test_X.shape[0])]
    production_sample_ids = [str(uuid4()) for _ in range(production_X.shape[0])]

    # define train dataframes
    train_X = pl.DataFrame({
        sample_id_column: train_sample_ids,
        time_id_column: train_timestamps,
        input_columns[0]: train_X[:, 0],
        input_columns[1]: train_X[:, 1],
    })

    train_y = pl.DataFrame({
        sample_id_column: train_sample_ids,
        time_id_column: train_timestamps,
        target_column: train_y,
    }).with_columns((pl.lit("class_") + pl.col(target_column).cast(pl.Utf8)).alias(target_column))

    train_yhat = pl.DataFrame({
        sample_id_column: train_sample_ids,
        time_id_column: train_timestamps,
        prediction_column: train_yhat,
    }).with_columns((pl.lit("class_") + pl.col(prediction_column).cast(pl.Utf8)).alias(prediction_column))

    # define test dataframes
    test_X = pl.DataFrame({
        sample_id_column: test_sample_ids,
        time_id_column: test_timestamps,
        input_columns[0]: test_X[:, 0],
        input_columns[1]: test_X[:, 1],
    })

    test_y = pl.DataFrame({
        sample_id_column: test_sample_ids,
        time_id_column: test_timestamps,
        target_column: test_y,
    }).with_columns((pl.lit("class_") + pl.col(target_column).cast(pl.Utf8)).alias(target_column))

    test_yhat = pl.DataFrame({
        sample_id_column: test_sample_ids,
        time_id_column: test_timestamps,
        prediction_column: test_yhat,
    }).with_columns((pl.lit("class_") + pl.col(prediction_column).cast(pl.Utf8)).alias(prediction_column))

    # define production dataframes
    production_X = pl.DataFrame({
        sample_id_column: production_sample_ids,
        time_id_column: production_timestamps,
        input_columns[0]: production_X[:, 0],
        input_columns[1]: production_X[:, 1],
    })

    production_y = pl.DataFrame({
        sample_id_column: production_sample_ids,
        time_id_column: production_timestamps,
        target_column: production_y,
    }).with_columns((pl.lit("class_") + pl.col(target_column).cast(pl.Utf8)).alias(target_column))

    production_yhat = pl.DataFrame({
        sample_id_column: production_sample_ids,
        time_id_column: production_timestamps,
        prediction_column: production_yhat,
    }).with_columns((pl.lit("class_") + pl.col(prediction_column).cast(pl.Utf8)).alias(prediction_column))
    return (
        production_X,
        production_y,
        production_yhat,
        test_X,
        test_y,
        test_yhat,
        train_X,
        train_y,
        train_yhat,
    )


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Utility functions

    This section contains some utility function that are used by other cells in the notebook.
    """)
    return


@app.cell
def _(ml3_enums, ml3_models, os, pl):
    def build_data_objects(
        X: pl.DataFrame,
        y: pl.DataFrame,
        yhat: pl.DataFrame,
        folder: str,

    ) -> tuple[ml3_models.TabularData, ml3_models.TabularData, ml3_models.TabularData]:
        """
        Builds the data objects for the given samples, starting from the given timestamp.
        IDs are generated based on the sample IDs, and timestamps are generated based on the starting timestamp.
        The function returns the inputs, target, and predictions data objects, along with the next starting timestamp.
        """

        input_path = os.path.join(folder, 'inputs.csv')
        target_path = os.path.join(folder, 'target.csv')
        predictions_path = os.path.join(folder, 'predictions.csv')

        print('Creating input file')
        X.write_csv(input_path)

        print('Creating target file')
        y.write_csv(target_path)

        print('Creating predictions file')
        yhat.write_csv(predictions_path)

        print('Creating inputs data')
        inputs_data = ml3_models.TabularData(
            source=ml3_models.LocalDataSource(file_type=ml3_enums.FileType.CSV, is_folder=False, folder_type=None, file_path=input_path)
        )

        print('Creating target data')
        target_data = ml3_models.TabularData(
            source=ml3_models.LocalDataSource(file_type=ml3_enums.FileType.CSV, is_folder=False, folder_type=None, file_path=target_path)
        )

        print('Creating predictions data')  # If all exists and FORCE_FILE_RECREATION is False, skip the creation
        predictions_data = ml3_models.TabularData(
            source=ml3_models.LocalDataSource(file_type=ml3_enums.FileType.CSV, is_folder=False, folder_type=None, file_path=predictions_path)
        )
        return (inputs_data, target_data, predictions_data)

    return (build_data_objects,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Project and task setup

    To work on Ml cube Platform, you first need to create a project and the task specifying the attributes. After that, you need to add the dataschema and a model to monitor.
    """)
    return


@app.cell
def _(API_KEY, ML3PlatformClient, URL):
    ml3_client = ML3PlatformClient(api_key=API_KEY, url=URL)
    return (ml3_client,)


@app.cell
def _(dotenv, os):
    dotenv.load_dotenv()
    API_KEY = os.environ['MLCUBE_PLATFORM_API_KEY']
    URL = os.environ.get('MLCUBE_PLATFORM_URL', "https://api.platform.mlcube.com")
    return API_KEY, URL


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Project creation

    To create a project you need to choose a name, write a description and choose the default storage policy. MLCUBE means cloning data to ML cube's secure storage, while, CUSTOMER means keeping data in customer's storage sources (note that they must be always available).
    """)
    return


@app.cell
def _(ml3_client, ml3_enums):
    project_id = ml3_client.create_project(
        name="Example project",
        description="Example project created following ML cube Platform guide",
        default_storage_policy=ml3_enums.StoragePolicy.MLCUBE,
    )
    return (project_id,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Task creation

    To create a task you need to specify the project, the name, a set of tags used for filtering and the attributes that define the artificial intelligence task: task type, data structure, optional target. For more information you can go to the [documentation page](https://ml-cube.github.io/ml3-platform-docs/user_guide/task/).
    """)
    return


@app.cell
def _(ml3_client, ml3_enums, ml3_models, project_id):
    task_id = ml3_client.create_task(
        project_id=project_id,
        name='Example task',
        tags=['example'],
        task_type=ml3_enums.TaskType.CLASSIFICATION_MULTICLASS,
        data_structure=ml3_enums.DataStructure.TABULAR,
        optional_target=False,
        cost_info=ml3_models.MulticlassClassificationTaskCostInfo(
            currency=ml3_enums.Currency.EURO,
            misclassification_cost={
                'class_0': 1.2,
                'class_1': 0.3,
                'class_2': 2.1,
            }
        )
    )
    return (task_id,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Data schema

    The data schema defines the structure of the data used in this task.
    It contains features, target and a set of mandatory metadata required by the ML cube Platform.
    Each sample must have a `timestamp` and an `identifier`: the timestamp is used to sort your data chronologically and the identifier is used to share information about data without transferring them.

    The data schema is specified by the class `DataSchema` which can be found in the `models` package of our sdk.
    In the following cell you can see an example of a DataSchema. As you can notice, the model predictions are not included. The reason is that they will be automatically added when a model is created within the task.
    """)
    return


@app.cell
def _(
    input_columns,
    ml3_client,
    ml3_enums,
    ml3_models,
    sample_id_column,
    target_column,
    task_id,
    time_id_column,
):
    data_schema = ml3_models.DataSchema(
        columns=[
            # SAMPLE ID
            ml3_models.ColumnInfo(
                name=sample_id_column,
                data_type=ml3_enums.DataType.STRING,
                role=ml3_enums.ColumnRole.ID,
                is_nullable=False
            ),
            # TIMESTAMP
            ml3_models.ColumnInfo(
                name=time_id_column,
                data_type=ml3_enums.DataType.FLOAT,
                role=ml3_enums.ColumnRole.TIME_ID,
                is_nullable=False
            ),
            # FEATURES
            ml3_models.ColumnInfo(
                name=input_columns[0],
                data_type=ml3_enums.DataType.FLOAT,
                role=ml3_enums.ColumnRole.INPUT,
                is_nullable=False
            ),
            ml3_models.ColumnInfo(
                name=input_columns[1],
                data_type=ml3_enums.DataType.FLOAT,
                role=ml3_enums.ColumnRole.INPUT,
                is_nullable=False
            ),
            # TARGET
            ml3_models.ColumnInfo(
                name=target_column,
                data_type=ml3_enums.DataType.CATEGORICAL,
                role=ml3_enums.ColumnRole.TARGET,
                possible_values=['class_0', 'class_1', 'class_2'],
                is_nullable=False
            )
        ]
    )

    ml3_client.add_data_schema(task_id=task_id, data_schema=data_schema)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Model

    After the task is created, you can add AI models inside it.
    A model is uniquely identified by the pair `name` and `version`.
    The version identifies a specific trained instance of the model. Whenever you retrain your model, you will update its version on the ML cube Platform.
    The metric_name field indicates the error or performance metric used in the ML cube Platform to display the model's performance and it is also included in the retraining report.

    Before settings the reference of the model, you need to upload historical data.
    """)
    return


@app.cell
def _(ml3_client, ml3_enums, model_name, model_version, task_id):
    model_id = ml3_client.create_model(
        task_id=task_id,
        name=model_name,
        version=model_version,
        metric_name=ml3_enums.ModelMetricName.ACCURACY,
        preferred_suggestion_type=ml3_enums.SuggestionType.SAMPLE_WEIGHTS,
        with_probabilistic_output=False,
    )
    return (model_id,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Data upload

    Now, that everything is correctly setup, you can upload the data.

    There are two classes of data: *historical* and *production*.
    Historical data represent data you had before the model was in production, while production data are those coming from the production environment.
    The reference data for the model are selected from the historical data by specifying a time range.

    This is the first time you send data to ML cube Platform, therefore, we have some things to explain:

    - data are composed of features, targets, predictions and metadata. You send each category separately since data can come from multiple sources;
    - the operation of sending data belong to the category of operations that runs a pipeline inside the ML cube Platform. In this case the pipeline is composed only by the data step that reads the data, validate them and then if the storing policy is MLCUBE it stores inside the ML cube Platform's Secure Storage;
    - the pipeline is identified by a `job_id` and you can follow the execution status by asking the client its information. Additionally, you can wait for the completion of the job by calling the method `wait_job_completion(job_id)`.

    In this section, we send features using a `LocalDataSource`, since we have the file locally.
    In order to use remote data sources you need to add credentials on the ML cube Platform. You can specify them in the `DataSource` object.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Historical data

    Historical data are uploaded specifying how they were used during the model development via the `data_batch_type`, this let's ML cube Platform to handle them accordingly. In this case we upload training and test data.
    """)
    return


@app.cell
def _(
    TemporaryDirectory,
    build_data_objects,
    ml3_client,
    ml3_enums,
    model_id,
    task_id,
    test_X,
    test_y,
    test_yhat,
    train_X,
    train_y,
    train_yhat,
):
    with TemporaryDirectory() as _folder:
        _input_data, _target_data, _prediction_data = build_data_objects(
            train_X, train_y, train_yhat, _folder
        )

        _job_id = ml3_client.add_historical_data(
            task_id=task_id,
            inputs=_input_data,
            target=_target_data,
            predictions=[(model_id, _prediction_data)],
            data_batch_type=ml3_enums.DataBatchType.TRAINING
        )
        print('job submitted, waiting')
        ml3_client.wait_job_completion(job_id=_job_id)
        print('job completed')

        _input_data, _target_data, _prediction_data = build_data_objects(
            test_X, test_y, test_yhat, _folder
        )

        _job_id = ml3_client.add_historical_data(
            task_id=task_id,
            inputs=_input_data,
            target=_target_data,
            predictions=[(model_id, _prediction_data)],
            data_batch_type=ml3_enums.DataBatchType.TEST
        )
        print('job submitted, waiting')
        ml3_client.wait_job_completion(job_id=_job_id)
        print('job completed')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Model reference

    Before uploading production data, you need to define the reference for your model. Reference should reflect the data you are expecting in production. For this reason you can use test data.
    """)
    return


@app.cell
def _(ml3_client, ml3_models, model_id, test_X, time_id_column):
    _job_id = ml3_client.set_model_reference(
        model_id=model_id,
        default_reference=ml3_models.ReferenceInfo(time_intervals=[(test_X[time_id_column].min(), test_X[time_id_column].max())])
    )
    print('job submitted, waiting')
    ml3_client.wait_job_completion(job_id=_job_id)
    print('job completed')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Production data

    Production data can be uploaded one data category at a time following an incremental approach, allowing, for instance, target data to arrive with a delay.
    """)
    return


@app.cell
def _(
    TemporaryDirectory,
    build_data_objects,
    ml3_client,
    model_id,
    production_X,
    production_y,
    production_yhat,
    task_id,
):
    with TemporaryDirectory() as _folder:
        _input_data, _target_data, _prediction_data = build_data_objects(
            production_X, production_y, production_yhat, _folder
        )

        _job_id = ml3_client.add_production_data(
            task_id=task_id,
            inputs=_input_data,
            target=None,
            predictions=[(model_id, _prediction_data)],
        )
        print('job submitted, waiting')
        ml3_client.wait_job_completion(job_id=_job_id)
        print('job completed')

        _job_id = ml3_client.add_production_data(
            task_id=task_id,
            inputs=None,
            target=_target_data,
            predictions=None,
        )
        print('job submitted, waiting')
        ml3_client.wait_job_completion(job_id=_job_id)
        print('job completed')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Web Application

    Now that you setup everything and uploaded data, you can open the [web application](https://app.platform.mlcube.com) to see the results. In particular, you can open the following pages:

    - Data Explorer - Dashboards
    - Dynamic Clustering
    """)
    return


if __name__ == "__main__":
    app.run()
