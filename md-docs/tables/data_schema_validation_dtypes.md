=== "Regression"

    | Task Type | Data Structure | ID | TIME ID | INPUT | METADATA | TARGET | INPUT ADDITIONAL EMBEDDING | TARGET ADDITIONAL EMBEDDING | OBJECT LABEL TARGET | OBJECT TEXT TARGET | USER INPUT | RETRIEVED CONTEXT | SEASONALITY | TREND | REGRESSOR |
    |---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
    | Regression | Tabular | STRING | FLOAT | FLOAT, CATEGORY | FLOAT, CATEGORY, STRING | FLOAT | - | - | - | - | - | - | - | - | - |
    | Regression | Embedding | STRING | FLOAT | ARRAY_1 | FLOAT, CATEGORY, STRING | FLOAT | - | - | - | - | - | - | - | - | - |
    | Regression | Image | STRING | FLOAT | ARRAY_3 | FLOAT, CATEGORY, STRING | FLOAT | ARRAY_1 | - | - | - | - | - | - | - | - |
    | Regression | Text | STRING | FLOAT | STRING | FLOAT, CATEGORY, STRING | FLOAT | ARRAY_1 | - | - | - | - | - | - | - | - |

=== "Classification Binary"

    | Task Type | Data Structure | ID | TIME ID | INPUT | METADATA | TARGET | INPUT ADDITIONAL EMBEDDING | TARGET ADDITIONAL EMBEDDING | OBJECT LABEL TARGET | OBJECT TEXT TARGET | USER INPUT | RETRIEVED CONTEXT | SEASONALITY | TREND | REGRESSOR |
    |---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
    | Classification Binary | Tabular | STRING | FLOAT | FLOAT, CATEGORY | FLOAT, CATEGORY, STRING | CATEGORY | - | - | - | - | - | - | - | - | - |
    | Classification Binary | Embedding | STRING | FLOAT | ARRAY_1 | FLOAT, CATEGORY, STRING | CATEGORY | - | - | - | - | - | - | - | - | - |
    | Classification Binary | Image | STRING | FLOAT | ARRAY_3 | FLOAT, CATEGORY, STRING | CATEGORY | ARRAY_1 | - | - | - | - | - | - | - | - |
    | Classification Binary | Text | STRING | FLOAT | STRING | FLOAT, CATEGORY, STRING | CATEGORY | ARRAY_1 | - | - | - | - | - | - | - | - |

=== "Classification Multiclass"

    | Task Type | Data Structure | ID | TIME ID | INPUT | METADATA | TARGET | INPUT ADDITIONAL EMBEDDING | TARGET ADDITIONAL EMBEDDING | OBJECT LABEL TARGET | OBJECT TEXT TARGET | USER INPUT | RETRIEVED CONTEXT | SEASONALITY | TREND | REGRESSOR |
    |---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
    | Classification Multiclass | Tabular | STRING | FLOAT | FLOAT, CATEGORY | FLOAT, CATEGORY, STRING | CATEGORY | - | - | - | - | - | - | - | - | - |
    | Classification Multiclass | Embedding | STRING | FLOAT | ARRAY_1 | FLOAT, CATEGORY, STRING | CATEGORY | - | - | - | - | - | - | - | - | - |
    | Classification Multiclass | Image | STRING | FLOAT | ARRAY_3 | FLOAT, CATEGORY, STRING | CATEGORY | ARRAY_1 | - | - | - | - | - | - | - | - |
    | Classification Multiclass | Text | STRING | FLOAT | STRING | FLOAT, CATEGORY, STRING | CATEGORY | ARRAY_1 | - | - | - | - | - | - | - | - |

=== "Classification Multilabel"

    | Task Type | Data Structure | ID | TIME ID | INPUT | METADATA | TARGET | INPUT ADDITIONAL EMBEDDING | TARGET ADDITIONAL EMBEDDING | OBJECT LABEL TARGET | OBJECT TEXT TARGET | USER INPUT | RETRIEVED CONTEXT | SEASONALITY | TREND | REGRESSOR |
    |---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
    | Classification Multilabel | Tabular | STRING | FLOAT | FLOAT, CATEGORY | FLOAT, CATEGORY, STRING | ARRAY_1 | - | - | - | - | - | - | - | - | - |
    | Classification Multilabel | Embedding | STRING | FLOAT | ARRAY_1 | FLOAT, CATEGORY, STRING | ARRAY_1 | - | - | - | - | - | - | - | - | - |
    | Classification Multilabel | Image | STRING | FLOAT | ARRAY_3 | FLOAT, CATEGORY, STRING | ARRAY_1 | ARRAY_1 | - | - | - | - | - | - | - | - |
    | Classification Multilabel | Text | STRING | FLOAT | STRING | FLOAT, CATEGORY, STRING | ARRAY_1 | ARRAY_1 | - | - | - | - | - | - | - | - |

=== "RAG"

    | Task Type | Data Structure | ID | TIME ID | INPUT | METADATA | TARGET | INPUT ADDITIONAL EMBEDDING | TARGET ADDITIONAL EMBEDDING | OBJECT LABEL TARGET | OBJECT TEXT TARGET | USER INPUT | RETRIEVED CONTEXT | SEASONALITY | TREND | REGRESSOR |
    |---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
    | RAG | Text | STRING | FLOAT | STRING | FLOAT, CATEGORY, STRING | - | ARRAY_1 | - | - | - | STRING | STRING | - | - | - |

=== "Object Detection"

    | Task Type | Data Structure | ID | TIME ID | INPUT | METADATA | TARGET | INPUT ADDITIONAL EMBEDDING | TARGET ADDITIONAL EMBEDDING | OBJECT LABEL TARGET | OBJECT TEXT TARGET | USER INPUT | RETRIEVED CONTEXT | SEASONALITY | TREND | REGRESSOR |
    |---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
    | Object Detection | Image | STRING | FLOAT | ARRAY_3 | FLOAT, CATEGORY, STRING | ARRAY_2 | ARRAY_1 | - | ARRAY_1 | - | - | - | - | - | - |

=== "Semantic Segmentation"

    | Task Type | Data Structure | ID | TIME ID | INPUT | METADATA | TARGET | INPUT ADDITIONAL EMBEDDING | TARGET ADDITIONAL EMBEDDING | OBJECT LABEL TARGET | OBJECT TEXT TARGET | USER INPUT | RETRIEVED CONTEXT | SEASONALITY | TREND | REGRESSOR |
    |---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
    | Semantic Segmentation | Image | STRING | FLOAT | ARRAY_3 | FLOAT, CATEGORY, STRING | ARRAY_3 | ARRAY_1 | - |ARRAY_1 | - | - | - | - | - | - |

=== "Timeseries"

    | Task Type | Data Structure | ID | TIME ID | INPUT | METADATA | TARGET | INPUT ADDITIONAL EMBEDDING | TARGET ADDITIONAL EMBEDDING | OBJECT LABEL TARGET | OBJECT TEXT TARGET | USER INPUT | RETRIEVED CONTEXT | SEASONALITY | TREND | REGRESSOR |
    |---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
    | Timeseries | Tabular | STRING | FLOAT | FLOAT, CATEGORY | FLOAT, CATEGORY, STRING | FLOAT | - | - | - | - | - | - | FLOAT | FLOAT | FLOAT | - |

=== "Clustering"

    | Task Type | Data Structure | ID | TIME ID | INPUT | METADATA | TARGET | INPUT ADDITIONAL EMBEDDING | TARGET ADDITIONAL EMBEDDING | OBJECT LABEL TARGET | OBJECT TEXT TARGET | USER INPUT | RETRIEVED CONTEXT | SEASONALITY | TREND | REGRESSOR |
    |---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
    | Clustering | Tabular | STRING | FLOAT | FLOAT, CATEGORY | FLOAT, CATEGORY, STRING | STRING | - | - | - | - | - | - | - | - | - |
    | Clustering | Embedding | STRING | FLOAT | ARRAY_1 | FLOAT, CATEGORY, STRING | STRING | - | - | - | - | - | - | - | - | - |
    | Clustering | Image | STRING | FLOAT | ARRAY_3 | FLOAT, CATEGORY, STRING | STRING | ARRAY_1 | - | - | - | - | - | - | - | - |
    | Clustering | Text | STRING | FLOAT | STRING | FLOAT, CATEGORY, STRING | STRING | ARRAY_1 | - | - | - | - | - | - | - | - |

=== "OCR"

    | Task Type | Data Structure | ID | TIME ID | INPUT | METADATA | TARGET | INPUT ADDITIONAL EMBEDDING | TARGET ADDITIONAL EMBEDDING | OBJECT LABEL TARGET | OBJECT TEXT TARGET | USER INPUT | RETRIEVED CONTEXT | SEASONALITY | TREND | REGRESSOR |
    |---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
    | OCR _plain_text_  | Image | STRING | FLOAT | ARRAY_3 | FLOAT, CATEGORY, STRING | STRING  | ARRAY_1 | - | - | - | - | - | - | - | - |
    | OCR _with_labels_ | Image | STRING | FLOAT | ARRAY_3 | FLOAT, CATEGORY, STRING | ARRAY_3 | ARRAY_1 | - | ARRAY_1 | ARRAY_1 | - | - | - | - | - |