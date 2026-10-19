import sys

from transformers import PreTrainedTokenizerFast

SENTENCES = {
    "English": "Where are we going this evening?",
    "Hindi": "आज शाम को कहाँ जा रहे हैं?",
    "French": "Où allons-nous ce soir ?",
    "Japanese": "今晩どこに行きますか？",
}

TOKENIZERS = {
    # Multilingual encoders (from the reading)
    "mBERT": "google-bert/bert-base-multilingual-cased",
    "XLM-R": "FacebookAI/xlm-roberta-base",
    # General LLMs (latest release of each family as of Oct 2026)
    "gpt-oss": "openai/gpt-oss-20b",
    "Llama-4": "unsloth/Llama-4-Scout-17B-16E-Instruct",  # ungated mirror of meta-llama
    "Gemma-4": "google/gemma-4-12B-it",
    "Qwen3.8": "Qwen/Qwen3.8-27B",
    "DeepSeek-V4.1": "deepseek-ai/DeepSeek-V4.1-Flash-1017",
    "Phi-4-reasoning-vision": "microsoft/Phi-4-reasoning-vision-15B",
    # Language-focused
    "Mistral-Small-4": "mistralai/Mistral-Small-4-119B-2603",  # French
    "Sarvam-30B": "sarvamai/sarvam-30b",  # Indian languages
    "LLM-jp-4.1": "llm-jp/llm-jp-4.1-8b-thinking",  # Japanese
}


def load_tokenizer(model_id):
    extra = {"fix_mistral_regex": True} if "Mistral" in model_id else {}
    return PreTrainedTokenizerFast.from_pretrained(model_id, **extra)


show_pieces = "--show" in sys.argv

print(f"{'Tokenizer':<24}" + "".join(f"{language:>14}" for language in SENTENCES))
for name, model_id in TOKENIZERS.items():
    tokenizer = load_tokenizer(model_id)
    pieces = {language: tokenizer.tokenize(text) for language, text in SENTENCES.items()}
    cells = [f"{len(p)}" for p in pieces.values()]
    print(f"{name:<24}" + "".join(f"{cell:>14}" for cell in cells))
    if show_pieces:
        for language, p in pieces.items():
            print(f"{'':<24}{language}: {p}")
