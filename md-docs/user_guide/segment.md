
# Segment

A Segment is a subset of the data distribution that identifies a sub-domain inside the data.
It is defined by a set of rules over data dimensions and metadata.
A [Task] can include several Segments and there are no constrains about how they are specified.
Indeed, two Segments can have some intersections in the data space.

When Segments are specified for a [Task], monitoring is performed both on the whole data, called _all population_, and for each Segment.
The objective of a Segment is to allow the analysis of specific groups of data, whose variations might go unnoticed if only the whole population is monitored.

Segments, similarly to the [Data schema], must be defined before sending any data to the Platform.
They must to be created all at once, as they can't be modified upon creation. Additionally, their definition needs to happen after the creation of the Data Schema, as the rules for the Segment are based on the columns defined there. 


## Segment Structure

The Segment structure is very simple, as it only requires the definition of two fields:

| Field  | Description | 
| --------- | ------- |
| Name | The name of the Segment. It is used to display information related to the segment in the Web App. |
| Rules | A list of rules defining the subset of the population. These rules are applied in AND between them, which means that a sample belongs to the Segment if all the conditions expressed by the rules are satisfied. To prevent possible conflicts, there can't be two rules in a segment defined over the same column.  |

Segments can be created both through the Web App and the SDK.
    
## Segment Rules

A rule is a condition over a single data dimension that a specific sample must match to be considered part of the Segment.
Each Segment has from one to several rules, which are applied in AND between them.
A rule is defined by the following fields:

| Field  | Description |
| --------- | ------- |
| Column name | The name of the column in the Data Schema that the rule is applied to. A rule can be applied only on columns of role INPUT, TARGET and METADATA|
| Operator | The operator defining the rule. It can be either `IN` or `OUT`  |
| Values | This field can have two possible meaning, according to the data type of the column specified in the rule: <br><ul><li>The data type is float: Values is a series of ranges [a, b] that define the numeric intervals over which the operator is applied. The range is closed, meaning that the extremes are always considered in it. When operator is `IN`, the ranges are in OR, whereas, when the operator is `OUT` they are in AND.</li><li>The data type is categorical or string: Values is a list which elements must match the content of the column. When operator is `IN`, the column value must be one of the specified elements, while, when operator is `OUT` it must not be one of them. </li></ul> |

## Examples

Let's consider a simple example where we have a dataset with the following columns:

| Sample ID | X_0 | X_1 | Y | Metadata_1 | Metadata_2 |
| --------- | --- | --- | - | --------- | --------- |
| id_0 | 10 | 20 | class_0 | A1 | B2 |
| id_1 | 11 | 21 | class_0 | A2 | B1 |
| id_2 | 12 | 22 | class_1 | A1 | B2 |
| id_3 | 13 | 23 | class_1 | A2 | B1 |
| id_4 | 14 | 24 | class_0 | A1 | B2 |

It represents a binary classification problem where the target is the column `Y` and the input features are `X_0` and `X_1`. Columns `Metadata_1` and `Metadata_2` are metadata columns.

Let's now define some possible segments of increasing complexity.

- A Segment that includes all samples where the value of the column `X_0` is between 10 and 12:
  
| Field  | Value | 
| --------- | ------- |
| Name | Segment_1 |
| Rules | Only 1 rule is needed: <br><ol><li> <ul> <li>Column name: X_0</li> <li>Operator: IN </li> <li>Values: [10, 12] </li> </ul> </li></ol> |

This segment would include the samples with `Sample ID` equal to `id_0`, `id_1` and `id_2`.

??? code-block "SDK Example"

    You can define the previous segment using the SDK with the following code:

    ``` py
    client.create_task_segments(
                task_id=task_id,
                segments=[
                    Segment(name=f'Segment 1',
                            rules=[
                                NumericSegmentRule(
                                    column_name='X_0',
                                    operator=SegmentOperator.IN,
                                    values=[SegmentRuleNumericRange(start_value=10, end_value=12)]
                                )
                            ]
                    )
                ]
            )
    ```

- A Segment that includes all samples where the value of the column `X_0` is greater or equal than 13 and the value of the column `X_1` is strictly less than 24:
  
| Field  | Value | 
| --------- | ------- |
| Name | Segment_2 |
| Rules | We need 2 rules: <br><ol><li> <ul> <li>Column name: X_0</li> <li>Operator: IN </li> <li>Values: [13, +inf] </li> </ul> </li><li> <ul> <li>Column name: X_1</li> <li>Operator: IN </li> <li>Values: [-inf, 23] </li> </ul> </li></ol> |

This segment would include the sample with `Sample ID` equal to `id_3`.

??? code-block "SDK Example"

    You can define the previous segment using the SDK with the following code:

    ``` py
    client.create_task_segments(
                task_id=task_id,
                segments=[
                    Segment(name=f'Segment 2',
                            rules=[
                                NumericSegmentRule(
                                    column_name='X_0',
                                    operator=SegmentOperator.IN,
                                    values=[SegmentRuleNumericRange(start_value=13)]
                                ),
                                NumericSegmentRule(
                                    column_name='X_1',
                                    operator=SegmentOperator.IN,
                                    values=[SegmentRuleNumericRange(end_value=23)]
                                )
                            ]
                    )
                ]
            )
    ```

    Notice how leaving one end of the interval empty means that the interval is unbounded in that direction.

- A Segment that includes all samples where the value of the column `X_0` either lower or equal than 10 or greater or equal than 14 and the value of the metadata column `Metadata_1` is equal to `A1` or `A3`:
  
| Field  | Value | 
| --------- | ------- |
| Name | Segment_3 |
| Rules | We need 2 rules: <br><ol><li> <ul> <li>Column name: X_0</li> <li>Operator: IN </li> <li>Values: [-inf, 10], [14, +inf] </li> </ul> </li><li> <ul> <li>Column name: Metadata_1</li> <li>Operator: IN </li> <li>Values: [A1, A3] </li> </ul> </li></ol> |

This segment would include the samples with `Sample ID` equal to `id_0` and `id_4`. Notice that, even though there is no sample with the value of `Metadata_1` equal to `A3`, there are still samples belonging to the segment because the values of the rules are applied in OR between them.

??? code-block "SDK Example"

    You can define the previous segment using the SDK with the following code:

    ``` py
    client.create_task_segments(
                task_id=task_id,
                segments=[
                    Segment(name=f'Segment 3',
                            rules=[
                                NumericSegmentRule(
                                    column_name='X_0',
                                    operator=SegmentOperator.IN,
                                    values=[SegmentRuleNumericRange(end_value=10), SegmentRuleNumericRange(start_value=14)]
                                ),
                                CategoricalSegmentRule(
                                    column_name='Metadata_1',
                                    operator=SegmentOperator.IN,
                                    values=['A1', 'A3']
                                )
                            ]
                    )
                ]
            )
    ```

- A Segment that includes all samples where the value of the column `X_1` is not between 21 and 23, the value of the target `y_0` is equal to `class_0` and the value of the metadata column `Metadata_2` is different from `B1`:
  
| Field  | Value | 
| --------- | ------- |
| Name | Segment_4 |
| Rules | We need 3 rules: <br><ol><li><ul>Column name: X_1</li> <li>Operator: OUT </li> <li>Values: [21, 23] </li> </ul> </li><li> <ul> <li>Column name: y_0</li> <li>Operator: IN </li> <li>Values: [class_0] </li> </ul> </li><li> <ul> <li>Column name: Metadata_2</li> <li>Operator: OUT </li> <li>Values: [B1] </li> </ul> </li></ol> |

This segment would include the samples with `Sample ID` equal to `id_2` and `id_4`.

??? code-block "SDK Example"

    You can define the previous segment using the SDK with the following code:

    ``` py
    client.create_task_segments(
                task_id=task_id,
                segments=[
                    Segment(name=f'Segment 3',
                            rules=[
                                NumericSegmentRule(
                                    column_name='X_1',
                                    operator=SegmentOperator.OUT,
                                    values=[SegmentRuleNumericRange(end_value=21), SegmentRuleNumericRange(start_value=23)]
                                ),
                                CategoricalSegmentRule(
                                    column_name='y_0',
                                    operator=SegmentOperator.IN,
                                    values=['class_0']
                                ),
                                CategoricalSegmentRule(
                                    column_name='Metadata_1',
                                    operator=SegmentOperator.IN,
                                    values=['A1']
                                )
                            ]
                    )
                ]
            )
    ```

[Task]: task.md
[Data schema]: data_schema.md