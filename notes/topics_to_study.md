# Topics to Study

| # | Topic | Why | Status | Notes |
|---|---|---|---|---|
| 1 | Tokens & fertility | Low-resource words get split into many pieces, so learning is less efficient | done |  |
| 2 | Language modelling | Next-word prediction, parameters, train vs test data | done |  |
| 3 | Causal LM vs masked LM | Decoder (GPT) generates text; encoder (BERT, AfriBERTa) understands it | done | Also learnt about Seq2Seq |
| 4 | Pretraining & multilinguality | Self-supervised learning, cross-lingual transfer, curse of multilinguality | done |  |
| 5 | Adaptation: from scratch, CPT, fine-tuning, LoRA | AfriBERTa trains from scratch; the usual recipe is pretrain → CPT → fine-tune | done |  |
| 6 | Evaluation metrics | Perplexity, P/R/F1, accuracy, BLEU/chrF | done |  |
| 7 | Data concepts | Corpus types, web crawls, language ID, quality problems | todo |  |

<!-- Status: todo · learning · ok -->

## Resource List for Each Topic

### Tokens and Fertility

- [Understanding Token Fertility: Why It Matters for Multilingual LLMs](https://medium.com/@biswanai92/understanding-token-fertility-why-it-matters-for-multilingual-llms-38c0b9f20da2)

- Did a small check on how different tokenizers work for sentences in different languages meaning the same thing.

| Language | Sentence |
|---|---|
| English | Where are we going this evening? |
| Hindi | आज शाम को कहाँ जा रहे हैं? |
| French | Où allons-nous ce soir ? |
| Japanese | 今晩どこに行きますか？ |

| Tokenizer | English | Hindi | French | Japanese |
|---|---|---|---|---|
| mBERT | 7 | 10 | 9 | 9 |
| XLM-R | 7 | 8 | 8 | 7 |
| gpt-oss | 7 | 8 | 7 | 11 |
| Llama-4 | 7 | 9 | 6 | 8 |
| Gemma-4 | 7 | 8 | 8 | 7 |
| Qwen3.8 | 7 | 10 | 8 | 7 |
| DeepSeek-V4.1 | 7 | 14 | 9 | 8 |
| Phi-4-reasoning-vision | 7 | 26 | 9 | 11 |
| Mistral-Small-4 | 7 | 10 | 7 | 9 |
| Sarvam-30B | 7 | 8 | 8 | 25 |
| LLM-jp-4.1 | 7 | 25 | 11 | 6 |

### Language Modelling

- [Introduction to Large Language Models](https://developers.google.com/machine-learning/crash-course/llm)
- [LLMs: What's a large language model?](https://developers.google.com/machine-learning/crash-course/llm/transformers) - ♥️
- [LLMs: Fine-tuning, distillation, and prompt engineering](https://developers.google.com/machine-learning/crash-course/llm/tuning)

### Causal vs Masked LMs

- [Understanding Causal LLM’s, Masked LLM’s, and Seq2Seq: A Guide to Language Model Training Approaches](https://medium.com/@tom_21755/understanding-causal-llms-masked-llm-s-and-seq2seq-a-guide-to-language-model-training-d4457bbd07fa)

### Pretraining and Multilinguality

- [What is self-supervised learning?](https://www.ibm.com/think/topics/self-supervised-learning) - ♥️
- [Understanding LLM Pre-training: Teaching Machines to Think](https://medium.com/@tungvu_37498/understanding-llm-pre-training-teaching-machines-to-think-972dede6a560) - This one goes a bit deep into the technical aspect of transformer architecture as well (can skip safely in this context)

### Adaptation Techniques - From scratch, CPT, Fine Tuning and LoRA

- [How to train a new language model from scratch using Transformers and Tokenizers](https://huggingface.co/blog/how-to-train) - This article talks about training a small LM on Esperanto using a custom trained tokenizer, Masked LM as pretext training and then fine tuning for Part-of-Speech downstream task. Also a very nice article in this context since Esperanto is also a low resource language.
- [Characterizing Datasets and Building Better Models with Continued Pre-Training](https://www.databricks.com/blog/characterizing-datasets-and-building-better-models-continued-pre-training)
- [Pretraining vs. Fine-tuning: What Are the Differences?](https://lightly.ai/blog/pretraining-vs-finetuning) - At one point, I think the article wanted to say CPT but said pretraining. The line is "Pre-training allows the model to achieve optimal performance faster than training from scratch", it is a bit confusing since pre-training *is* starting from scratch afaiu.
- [Practical Tips for Finetuning LLMs Using LoRA (Low-Rank Adaptation)](https://magazine.sebastianraschka.com/p/practical-tips-for-finetuning-llms) - ♥️ Did not go into too much detail of implementation but got the core idea of decomposing the weight update matrix into a product of 2 low rank matrices to save space and time.

### Evaluation Metrics

- [Classification: Accuracy, recall, precision, and related metrics](https://developers.google.com/machine-learning/crash-course/classification/accuracy-precision-recall)
- [Evaluation Metrics for Language Modeling](https://thegradient.pub/understanding-evaluation-metrics-for-language-models/) ♥️ - Very nice and in-depth article
- [Traditional NLP Metrics](https://docs.ragas.io/en/stable/concepts/metrics/available_metrics/traditional/#bleu-score)
