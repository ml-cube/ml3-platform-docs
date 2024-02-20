# Data Schema

Data schema is the core attribute of a Machine Learning **Task**.
It specifies the name of the quantities, their data type and role.
A Data Schema is a collection of *Column* entity that has the following attributes:

- `name`: name of the quantity. For Tabular data is the name of the column in the table.
- `data type`: as the name suggests, it is the type data of the quantity: float, integer, categorical, array, ...
- `nullable`: if the quantity is allowed to be missing
- `role`: specifies what this quantity represents, it can be: 
    - INPUT
    - PREDICTION
    - TARGET
    - ID
    - TIME_ID
- `dims`: if the data type is array, it represents its dimensions, for instance an image is an ARRAY_3 with dimensions (1920, 1080, 3)

The data schema must always have:

- one Column with role ID that is the unique identifier of samples used to recognize them
- one Column with role TIME_ID that is used to temporally order the samples
- at least one Column with role INPUT
- one Column with role TARGET
- one Column for each model created in the Task (this Column is added automatically by the application and have the following name `MODEL_NAME@MODEL_VERSION`)