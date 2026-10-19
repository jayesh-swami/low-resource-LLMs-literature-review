# Topics to Study

| # | Topic | Why | Status | Notes |
|---|---|---|---|---|
| 1 | Tokens & fertility | Low-resource words get split into many pieces, so learning is less efficient | todo |  |
| 2 | Language modelling | Next-word prediction, parameters, train vs test data | todo |  |
| 3 | Causal LM vs masked LM | Decoder (GPT) generates text; encoder (BERT, AfriBERTa) understands it | todo | key for AfriBERTa |
| 4 | Pretraining & multilinguality | Self-supervised learning, cross-lingual transfer, curse of multilinguality | todo |  |
| 5 | Adaptation: from scratch, CPT, fine-tuning, LoRA | AfriBERTa trains from scratch; the usual recipe is pretrain → CPT → fine-tune | todo |  |
| 6 | Evaluation metrics | Perplexity, NER, classification, P/R/F1, accuracy, BLEU/chrF | todo |  |
| 7 | Data concepts | Corpus types, web crawls, language ID, quality problems | todo | key for Kreutzer |

<!-- Status: todo · learning · ok -->

## Check yourself
- [ ] Why is MLM good for understanding but not for generating text?
- [ ] What's the difference between CPT and fine-tuning?
- [ ] Precision 0.9, recall 0.3: is that a good NER model? What does F1 reveal?
- [ ] Why can't you compare perplexity across different tokenisers?
- [ ] How can a "Breton" dataset end up mostly French?
