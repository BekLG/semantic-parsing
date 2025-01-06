import os

from transformers import AutoTokenizer, PreTrainedTokenizer

os.environ['HF_TOKEN'] = HF_TOKEN
LLAMA3_BASE_REPO = "meta-llama/Meta-Llama-3-70B-Instruct"


def wrap_llama3_dialog(messages: list, tokenizer: PreTrainedTokenizer = None):
    if tokenizer is None:
        tokenizer = AutoTokenizer.from_pretrained(LLAMA3_BASE_REPO, use_auth_token=HF_TOKEN)

    return tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)