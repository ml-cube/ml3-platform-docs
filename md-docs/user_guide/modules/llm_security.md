# LLM Security

## What is LLM Security?

Large Language Model (LLM) security refers to the strategies, practices, and technologies used to ensure that large language models operate safely, responsibly, and in ways that protect the company, its data, and users. 

This module can be used in all systems that incorporate an LLM as a building block. Therefore, it can also be used with a RAG system to protect all the data contained in documents that make up the company knowledge base. It provides an assessment of the system security, and offers useful insights to enhance it. 

## Why do we need LLM Security?

Large Language Models are powerful because they are trained, or source from large amount of textual data. As a result, they can process vast amounts of data to generate human-like text, answer questions, summarize information, and much more. However, this capability poses security risks. Malicious actors can exploit LLMs to generate harmful content, leak Personal Identifiable Information (PII), or disclose proprietary information. LLM security focuses on identifying and preventing these risks, ensuring that models are used responsibly and ethically. The main threats to the system are:

1. **Preventing Harmful Content**: LLMs are pre-trained on large datasets that contains also harmful and toxic information, and a model can inadvertently generate harmful content. Security measures help monitor and limit these outputs.

2. **Leakage of PII**:  When a LLM is deployed in an industrial settings, it often accesses some company-provided informarion (or it may be fine-tuned on it). Some documents in the knowledge base may contain PII. Security measures ensure that these models do not violates the privacy of individuals referenced in the dataset, preserving their privacy and adhering to regulatory standards like GDPR.

3. **Disclosure of proprietary information**: Similarly, the knowledge base may contain sentive or proprietaty information that a company prefers to keep hidden from its employees. Security measures ensure that these models do not inadvertently expose private data.

## How does the MLCube Platform perform an analysis of the LLM security?

The MLCube platform's LLM Security module involves analyzing a batch of data, composed of user inputs, retrieved contexts, and model responses, to assess both the security of the LLM when used as a building block in a RAG system and the safety of the conversation with the system. The analysis consists of three sequential steps, with each step assigning a class to a subset of samples and passing the unassigned samples to the next step, ensuring that each sample is assigned to exactly one class.

### Analysis steps

 The analysis steps performed are:

1. **Default analysis step**: This first step is performed only when the RAG system uses a default answer for questions that retrieve no documents from the knowledge base. The analysis identifies all conversations where the model's response is a default answer, filtering out those with non-default responses. Samples with non-default answers are then passed to the next analysis step. Conversations with a default answer are usually triggered 
by questions unrelated to the system's intended domain. Such conversations may also correspond to requests for harmful content.

1. **Defense analysis step**: This step is performed only if specifications for the LLM underlying the RAG system are provided. Its goal is to identify attacks on the system that have been successfully blocked and to determine the specific defense rule responsible for each blocked attack. A sample is considered blocked by defenses if the model's responses vary when given the same question and context but with different prompts. Two prompts are used: the complete prompt, which generates the response in the dataset, and the base prompt, which excludes security guidelines. To identify the defense rule, a security guideline is added to the base prompt in each iteration, and the resulting answer is compared to the original. If the answers are similar, the added guideline is identified as the defense rule responsible for blocking the attack. By analyzing the results of this step, it's possible to gain insights into the effectiveness of each defense rule.


1. **Clustering analysis step**: It's the final step, this analysis identifies clusters of similar conversations within the data batch and flags any outliers. Each sample is classified as either an 'Inlier' (part of a group) or an 'Outlier' (deviating from all clusters). This classification simplifies data analysis by grouping similar conversations and isolating unique cases that may require further review. Ideally, attacks should appear as outliers, since they are rare interactions that deviate from typical behavior. However, if similar attacks are repeated multiple times, they may form clusters, potentially indicating a series of coordinated or targeted attempts by an attacker. Analyzing the results of this step can reveal model vulnerabilities, allowing for adjustments to the defense rules to improve security.

### Classes

As a result of these steps each sample of the provided batch is assigned to one of the following class:

- **Missing**:  This tag represents a sample that lacks essential information, such as the user input or the model output. Due to this deficit, the sample cannot be analyzed by the analysis.
- **Default answer**: This tag represents a sample with a default model answer, if such an answer is used and provided by the system.
- **Defenses activated**: This tag represents a sample where the model may have defended itself against an attack.
- **Inlier**: This tag represents a sample assigned to a cluster in the clustering analysis step.
- **Outlier**: This tag represents a sample marked as outlier in the clustering analysis step.
