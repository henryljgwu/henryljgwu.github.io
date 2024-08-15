---
title: "LongWriter: Unleashing 10,000+ Word Generation from Long Context LLMs"
date: 2024-08-15
priority: 2
link: https://arxiv.org/abs/2408.07055
type: Arxiv
---

This paper introduces the **LongWriter** model and associated techniques to address the limitations of current long-context large language models (LLMs) in generating ultra-long texts. Although existing long-context LLMs can process inputs up to 100,000 tokens, they typically struggle to generate outputs longer than 2,000 words. The primary reason for this limitation lies in the lack of sufficiently long output samples in supervised fine-tuning (SFT) datasets.

To tackle this issue, the paper proposes **AgentWrite**, an agent-based pipeline that breaks down ultra-long generation tasks into subtasks, enabling off-the-shelf LLMs to generate coherent outputs exceeding 20,000 words. Leveraging AgentWrite, the researchers constructed the **LongWriter-6k** dataset, containing 6,000 SFT data with output lengths ranging from 2,000 to 32,000 words. By incorporating this dataset into model training, they successfully scaled the output length of existing models to over 10,000 words while maintaining output quality.

The study also developed a comprehensive benchmark, **LongBench-Write**, for evaluating ultra-long generation capabilities. The 9B parameter model developed by the research team, further improved through Direct Preference Optimization (DPO), achieved state-of-the-art performance on this benchmark, surpassing even larger proprietary models.

The key contributions of the paper include:
1. Analyzing the generation length limits of current LLMs, revealing that these limits are primarily due to constraints in SFT dataset output lengths.
2. Proposing the AgentWrite pipeline, which uses a divide-and-conquer approach to construct ultra-long output SFT data.
3. Successfully scaling the output window size of existing LLMs to over 10,000 words without compromising output quality.
4. Demonstrating the effectiveness of DPO in further enhancing long-text generation capabilities.

# Relationship to LLM Agents and RAG Technology, and Innovations

1. **Relationship to LLM Agents**:
   - **AgentWrite** functions as an LLM Agent, breaking down the complex task of generating ultra-long text into manageable subtasks through planning and iterative generation. This is similar to the role of LLM Agents in other domains, such as problem-solving and software development, showcasing the potential of LLM Agents in handling complex tasks.

2. **Relationship to RAG Technology**:
   - Retrieval-Augmented Generation (RAG) typically involves retrieving relevant information from a knowledge base to enhance the output of a generation model. The ultra-long text generation enabled by AgentWrite can be seen as a complex generation task, where RAG technology could potentially be integrated into the AgentWrite framework in future research to generate long documents that require extensive background knowledge.

3. **Innovations**:
   - **AgentWrite** innovatively extends the text length generation capability of LLMs by controlling output length and ensuring coherence through step-by-step generation. This method not only increases output length but also maintains the quality and coherence of the text.
   - The **LongWriter-6k** dataset provides valuable resources for researching long-text generation, addressing the scarcity of long output samples in existing SFT datasets.
   - The introduction of **DPO** offers a new approach to improving the quality of long-text generation, demonstrating potential in both adhering to length constraints and enhancing output quality.

# Future Development Directions

1. **Expanding the AgentWrite Framework**: The AgentWrite framework could be expanded further to construct datasets with even longer outputs, pushing the model's output length limitations to 100,000 words or more.
2. **Integrating RAG Technology**: Integrating RAG technology into the AgentWrite framework could enable the model to dynamically retrieve relevant information during the generation of ultra-long texts, enhancing the depth and breadth of the output.
3. **Optimizing Inference Efficiency**: The generation of long texts presents challenges for inference efficiency. Future research could explore methods to improve inference efficiency while maintaining the quality of generated content.

