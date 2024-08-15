---
title: "Amuro & Char: Analyzing the Relationship between Pre-Training and Fine-Tuning of Large Language Models"
date: 2024-08-14
priority: 2
link: https://arxiv.org/abs/2408.06663
type: Arxiv
---

# Abstract
The development of LLMs has led to a "pre-train-then-align" paradigm, where models are pre-trained on large text corpora and fine-tuned for specific tasks. This paper investigates the relationship between pre-training and fine-tuning by analyzing multiple intermediate pre-trained model checkpoints. The key findings are:
- Continual pre-training improves the model in ways that are only revealed after fine-tuning.
- Tasks where the model performs poorly during pre-training benefit more from fine-tuning than tasks where it already performs well.
- Supervised fine-tuning can lead to forgetting of domain knowledge and tasks not seen during fine-tuning.
- Sensitivity to evaluation prompts after supervised fine-tuning can be reduced by more pre-training.

# Introduction
The emergence of LLMs has transformed NLP, introducing new data collection and model training paradigms. While pre-training and fine-tuning have been studied extensively, their interaction is not well understood. This paper explores this interaction by fine-tuning multiple intermediate pre-trained checkpoints and evaluating their performance.

# Experimental Setup
The paper uses the  [OLMo-1B model](https://github.com/allenai/OLMo/tree/main/checkpoints) and evaluates its performance on various NLP tasks, including  [summary generation](https://aclanthology.org/P18-1156/) [1],  [question generation](https://aclanthology.org/C19-1371/) [2],  [natural language inference](https://aclanthology.org/W18-5537/) [3], and  [paraphrase detection](https://aclanthology.org/Z19-5563/) [4].

# Results
The results show a dichotomy in task performance during pre-training: some tasks are learned, while others are not. Fine-tuning improves performance on tasks not learned during pre-training, but not on tasks already learned. Sensitivity to task format is also observed, with early pre-training steps struggling to adapt to different formats.

# Discussion and Conclusion
The study highlights the dynamics of pre-training and fine-tuning, suggesting that early stopping of pre-training may not hurt downstream performance. It also emphasizes the importance of analyzing training dynamics and calls for the release of pre-training checkpoints for further research.

# Technical Details
**Model Choice**: Due to computational constraints, the paper focuses on the OLMo-1B model, which is one of the few models that release individual pre-training checkpoints. This model has several desirable properties, including full openness and a smaller size, allowing for efficient training on a single GPU.

**Training Procedure**: The paper uses two fine-tuning procedures: supervised fine-tuning and instruction tuning. Supervised fine-tuning is conducted separately for each model checkpoint and dataset, while instruction tuning is done once using the [TÜLU dataset](https://aclanthology.org/2023.tulu-1.20/) [5].

**Evaluation**: The evaluation includes both in-domain and out-of-domain datasets for each task. Accuracy is used as the evaluation metric for classification tasks, and  [ROUGE-L](https://aclanthology.org/W04-1013/) [6] is used for generation tasks. The paper also explores different prediction generation methods and task formats.

# Model Changes during Pre-Training
The paper evaluates the pre-trained checkpoints with few-shot examples, as models without alignment tend to perform poorly in a zero-shot context. Results show that some tasks are learned during early pre-training steps, while others show no improvement. This suggests a dichotomy in task performance during pre-training.

# Impact of More Pre-Training on Fine-Tuning
The paper investigates whether more pre-training improves fine-tuning performance. Results indicate that tasks not learned during pre-training benefit significantly from fine-tuning, while tasks already learned during pre-training do not. This suggests that early stopping of pre-training may not be detrimental to downstream performance.

# What Does the Model Learn and Forget during Supervised Fine-Tuning?
The paper analyzes three dimensions: task format, task transfer, and domain knowledge.
- **Task Format**: The model is sensitive to task format during early pre-training steps, but becomes more flexible with more pre-training and fine-tuning.
- **Task Transfer**: Fine-tuning on classification tasks leads to a decrease in performance on generation tasks, but fine-tuning on generation tasks does not affect classification performance.
- **Domain Knowledge**: Fine-tuning on a specific dataset can lead to improvements on similar datasets but may cause forgetting on unrelated tasks.

# Discussion
The study provides insights into the dynamics of pre-training and fine-tuning, suggesting that some tasks are presented in a manner that aligns with pre-training, while others require fine-tuning to be learned. The paper also highlights the potential for cost-effective training paradigms and the importance of analyzing training dynamics.
