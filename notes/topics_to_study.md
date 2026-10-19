# Topics to Study

| # | Topic | Why | Status | Notes |
|---|---|---|---|---|
| 1 | Tokens & fertility | Low-resource words get split into many pieces, so learning is less efficient | done |  |
| 2 | Language modelling | Next-word prediction, parameters, train vs test data | done |  |
| 3 | Causal LM vs masked LM | Decoder (GPT) generates text; encoder (BERT, AfriBERTa) understands it | done | Also learnt about Seq2Seq |
| 4 | Pretraining & multilinguality | Self-supervised learning, cross-lingual transfer, curse of multilinguality | learning |  |
| 5 | Adaptation: from scratch, CPT, fine-tuning, LoRA | AfriBERTa trains from scratch; the usual recipe is pretrain → CPT → fine-tune | todo |  |
| 6 | Evaluation metrics | Perplexity, NER, classification, P/R/F1, accuracy, BLEU/chrF | todo |  |
| 7 | Data concepts | Corpus types, web crawls, language ID, quality problems | todo | key for Kreutzer |

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
- [LLMs: What's a large language model?](https://developers.google.com/machine-learning/crash-course/llm/transformers)
- [LLMs: Fine-tuning, distillation, and prompt engineering](https://developers.google.com/machine-learning/crash-course/llm/tuning)

### Causal vs Masked LMs

- [Understanding Causal LLM’s, Masked LLM’s, and Seq2Seq: A Guide to Language Model Training Approaches](https://medium.com/@tom_21755/understanding-causal-llms-masked-llm-s-and-seq2seq-a-guide-to-language-model-training-d4457bbd07fa)


