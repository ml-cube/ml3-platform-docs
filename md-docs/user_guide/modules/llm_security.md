# LLM Security

Large Language Models (LLMs) are powerful human-like text generators. In a RAG system, the information needed to answer the user is directly extracted from the company's knowledge base and passed as input to the model. Therefore, malicious actors can exploit LLMs to generate inappropriate content, leak Personally Identifiable Information (PII), or disclose proprietary information from the company's knowledge base.

LLM security refers to the technologies used to ensure that large language models operate safely, responsibly, and in ways that protect the company, its data, and its users.

## LLM Security Module
The ML cube Platform LLM Security module is available for [RAG Tasks](../task.md#retrieval-augmented-generation) and generates a security assessment for a given set of samples, producing a detailed report about the security of the LLMs used in the RAG system. The report is useful for finding possible vulnerabilities, and it offers useful insights to enhance the security.

!!! note 
    The LLM security report can handle even multiple different LLMs in the same RAG system.

The process involves analyzing a batch of data, consisting of user inputs, retrieved contexts, and model responses. Additionally, to enhance the analysis, the [LLMs specifications](../model.md#llm-specifications) can also be provided to enable a more accurate analysis of the Security Guidelines in the system prompt used.

<!---
The three main components analyzed by the framework are:

| Component           | Description                                                                                                                         |
|---------------------|-------------------------------------------------------------------------------------------------------------------------------------|
| User Input          | The query or question posed by the user.                                                                                            |
| Response            | The generated answer or output provided by the model.                                                                               |
| Security guidelines | The guidelines used in the system prompt to guide the LLM in generating safe answers that align with the rules set by the provider. |
--->
!!! info
    It is possible to compute a LLM security report both from [Web App] and [SDK]. The computed report can be viewed in the Web App.

## Analysis steps

The ML cube platform's LLM Security module perform an analysis consisting of three sequential steps, with each step assigning a class to a subset of samples and passing the unassigned samples to the next step, ensuring that each sample is assigned to exactly one class.

The analysis steps are described in the following sections.

### Default analysis step

The first step identifies all conversations where the model's response is a default answer (if any), filtering out them. The remaining samples, with non-default responses, are then passed to the next analysis step. Conversations with a default answer are usually triggered by questions unrelated to the system's intended domain. 

!!! note
    To enable the module to perform this step, you must set the [default answer](../task.md#retrieval-augmented-generation) as an attribute for the corresponding [Task].

### Defense analysis step

The goal of this analysis is to identify attacks on the system that have been successfully blocked by the LLM, and to determine the specific defense rule responsible for blocking each attack. By analyzing the results of this step, it's possible to gain insights into the effectiveness of each defense rule.
<!---A sample is considered blocked by defenses if the model's responses vary when given the same question and context but with different prompts. Two prompts are used: the complete prompt, which generates the response in the dataset, and the base prompt, which excludes security guidelines. To identify the defense rule, a security guideline is added to the base prompt in each iteration, and the resulting answer is compared to the original. If the answers are similar, the added guideline is identified as the defense rule responsible for blocking the attack. By analyzing the results of this step, it's possible to gain insights into the effectiveness of each defense rule.
--->

<!---Inserire un'immagine con un esempio del risultato, preso dalla webapp, possibilmente usando uno stesso esempio del notebook che viene condiviso 
<---> 

!!! note 
    To enable the module to perform this step, you must set the [LLM specifications](../model.md#llm-specifications).

### Clustering analysis step

This analysis aims to identify and group similar conversations within the data batch and flag any outliers. Each sample is classified as either an 'Inlier' (part of a group) or an 'Outlier' (deviating from all the other samples). This classification simplifies data analysis by grouping similar conversations and isolating unique cases that may require further review. 
<!---Ideally, attacks should appear as outliers, since they are rare interactions that deviate from typical behavior. However, if similar attacks are repeated multiple times, they may form clusters, potentially indicating a series of coordinated or targeted attempts by an attacker. Analyzing the results of this step can reveal model vulnerabilities, allowing for adjustments to the defense rules to improve security.
--->
<!---Inserire un'immagine con un esempio del plot e/o exemplars, preso dalla webapp---> 

## Classes

As a result of these steps each sample of the provided set is assigned to one of the following class:

| Class              | Description                                                                                                                                                    | 
|--------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Missing            | This tag represents a sample that lacks essential information, e.g., the user input or the model response. Due to this deficit, the sample cannot be analyzed. | 
| Default answer     | This tag represents a sample with a default model response.                                                                                                    | 
| Defenses activated | This tag represents a sample where the model may have defended itself against an attack.                                                                       | 
| Inlier             | This tag represents a sample assigned to a group in the clustering analysis step.                                                                              | 
| Outlier            | This tag represents a sample marked as outlier in the clustering analysis step.                                                                                |


## Required data

Below is a summary table of the input data needed for each analysis step:

| Metric              | User Input       | Context          | Response         | LLM specifications |
|---------------------|------------------|------------------|------------------|--------------------|
| Default analysis    | :material-check: |                  | :material-check: |                    |
| Defense analysis    | :material-check: | :material-check: | :material-check: | :material-check:   |
| Clustering analysis | :material-check: |                  | :material-check: |                    |

The LLM security module performs the analysis steps for each sample based on the data availability.
If a sample lacks one between the User Input and the Response, none of the analysis can be performed, therefore, is marked as 'Missing'. Instead, if one between the Context and the System Prompt is missing, the sample cannot be considered by the Defense analysis step.

When requesting the evaluation, a **timestamp interval** must be provided to specify the time range of the data to be evaluated.

??? code-block "SDK Example"

    The following code demonstrates how to compute a rag evaluation report for a given timestamp interval.

    ```python
    # Computing the LLM security report
    llm_security_job_id = client.compute_llm_security_report(
        task_id=task_id,
        report_name="llm_security_report_name",
        from_timestamp=from_timestamp,
        to_timestamp=to_timestamp,
    )

    # Waiting for the job to complete
    client.wait_job_completion(job_id=llm_security_job_id)

    # Getting the evaluation report id
    reports = client.get_llm_security_reports(task_id=task_id)
    report_id = reports[-1].id
    ```

[Task]: ../task.md
[Web App]: https://app.platform.mlcube.com/
[SDK]: ../../api/python/index.md