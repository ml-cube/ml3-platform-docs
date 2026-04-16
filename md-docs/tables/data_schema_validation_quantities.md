=== "Regression"

    | Task Type | Data Structure | ID | TIME ID | INPUT | METADATA | TARGET | INPUT ADDITIONAL EMBEDDING | TARGET ADDITIONAL EMBEDDING | OBJECT LABEL TARGET | OBJECT TEXT TARGET | USER INPUT | RETRIEVED CONTEXT | SEASONALITY | TREND | REGRESSOR |
    |---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
    | Regression | Tabular | 1 | 1 | $\ge$ 1 | $\ge$ 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
    | Regression | Embedding | 1 | 1 | 1 | $\ge$ 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
    | Regression | Image | 1 | 1 | 1 | $\ge$ 0 | 1 | $\le$ 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
    | Regression | Text | 1 | 1 | 1 | $\ge$ 0 | 1 | $\le$ 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |

=== "Classification Binary"

    | Task Type | Data Structure | ID | TIME ID | INPUT | METADATA | TARGET | INPUT ADDITIONAL EMBEDDING | TARGET ADDITIONAL EMBEDDING | OBJECT LABEL TARGET | OBJECT TEXT TARGET | USER INPUT | RETRIEVED CONTEXT | SEASONALITY | TREND | REGRESSOR |
    |---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
    | Classification Binary | Tabular | 1 | 1 | $\ge$ 1 | $\ge$ 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
    | Classification Binary | Embedding | 1 | 1 | 1 | $\ge$ 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
    | Classification Binary | Image | 1 | 1 | 1 | $\ge$ 0 | 1 | $\le$ 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
    | Classification Binary | Text | 1 | 1 | 1 | $\ge$ 0 | 1 | $\le$ 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |

=== "Classification Multiclass"

    | Task Type | Data Structure | ID | TIME ID | INPUT | METADATA | TARGET | INPUT ADDITIONAL EMBEDDING | TARGET ADDITIONAL EMBEDDING | OBJECT LABEL TARGET | OBJECT TEXT TARGET | USER INPUT | RETRIEVED CONTEXT | SEASONALITY | TREND | REGRESSOR |
    |---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
    | Classification Multiclass | Tabular | 1 | 1 | $\ge$ 1 | $\ge$ 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
    | Classification Multiclass | Embedding | 1 | 1 | 1 | $\ge$ 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
    | Classification Multiclass | Image | 1 | 1 | 1 | $\ge$ 0 | 1 | $\le$ 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
    | Classification Multiclass | Text | 1 | 1 | 1 | $\ge$ 0 | 1 | $\le$ 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |

=== "Classification Multilabel"

    | Task Type | Data Structure | ID | TIME ID | INPUT | METADATA | TARGET | INPUT ADDITIONAL EMBEDDING | TARGET ADDITIONAL EMBEDDING | OBJECT LABEL TARGET | OBJECT TEXT TARGET | USER INPUT | RETRIEVED CONTEXT | SEASONALITY | TREND | REGRESSOR |
    |---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
    | Classification Multilabel | Tabular | 1 | 1 | $\ge$ 1 | $\ge$ 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
    | Classification Multilabel | Embedding | 1 | 1 | 1 | $\ge$ 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
    | Classification Multilabel | Image | 1 | 1 | 1 | $\ge$ 0 | 1 | $\le$ 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
    | Classification Multilabel | Text | 1 | 1 | 1 | $\ge$ 0 | 1 | $\le$ 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |

=== "RAG"

    | Task Type | Data Structure | ID | TIME ID | INPUT | METADATA | TARGET | INPUT ADDITIONAL EMBEDDING | TARGET ADDITIONAL EMBEDDING | OBJECT LABEL TARGET | OBJECT TEXT TARGET | USER INPUT | RETRIEVED CONTEXT | SEASONALITY | TREND | REGRESSOR |
    |---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
    | RAG | Text | 1 | 1 | 2 | $\ge$ 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 0 |

=== "Object Detection"

    | Task Type | Data Structure | ID | TIME ID | INPUT | METADATA | TARGET | INPUT ADDITIONAL EMBEDDING | TARGET ADDITIONAL EMBEDDING | OBJECT LABEL TARGET | OBJECT TEXT TARGET | USER INPUT | RETRIEVED CONTEXT | SEASONALITY | TREND | REGRESSOR |
    |---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
    | Object Detection | Image | 1 | 1 | 1 | $\ge$ 0 | 1 | $\le$ 1 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 |

=== "Semantic Segmentation"

    | Task Type | Data Structure | ID | TIME ID | INPUT | METADATA | TARGET | INPUT ADDITIONAL EMBEDDING | TARGET ADDITIONAL EMBEDDING | OBJECT LABEL TARGET | OBJECT TEXT TARGET | USER INPUT | RETRIEVED CONTEXT | SEASONALITY | TREND | REGRESSOR |
    |---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
    | Semantic Segmentation | Image | 1 | 1 | 1 | $\ge$ 0 | 1 | $\le$ 1 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 |

=== "Clustering"

    | Task Type | Data Structure | ID | TIME ID | INPUT | METADATA | TARGET | INPUT ADDITIONAL EMBEDDING | TARGET ADDITIONAL EMBEDDING | OBJECT LABEL TARGET | OBJECT TEXT TARGET | USER INPUT | RETRIEVED CONTEXT | SEASONALITY | TREND | REGRESSOR |
    |---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
    | Clustering | Tabular | 1 | 1 | $\ge$ 1 | $\ge$ 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
    | Clustering | Embedding | 1 | 1 | 1 | $\ge$ 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
    | Clustering | Image | 1 | 1 | 1 | $\ge$ 0 | 1 | $\le$ 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
    | Clustering | Text | 1 | 1 | 1 | $\ge$ 0 | 1 | $\le$ 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |

=== "OCR"

    | Task Type | Data Structure | ID | TIME ID | INPUT | METADATA | TARGET | INPUT ADDITIONAL EMBEDDING | TARGET ADDITIONAL EMBEDDING | OBJECT LABEL TARGET | OBJECT TEXT TARGET | USER INPUT | RETRIEVED CONTEXT | SEASONALITY | TREND | REGRESSOR |
    |---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
    | OCR _plain_text_  | Image | 1 | 1 | 1 | $\ge$ 0 | 1 | $\le$ 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
    | OCR _with_labels_ | Image | 1 | 1 | 1 | $\ge$ 0 | 1 | $\le$ 1 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 |