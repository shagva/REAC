""" 
Module for counting tokens and splitting text into chunks
"""
from typing import List
from langchain_openai import ChatOpenAI
from langchain_ollama import ChatOllama
from langchain_mistralai import ChatMistralAI
from langchain_core.language_models.chat_models import BaseChatModel
from transformers import GPT2TokenizerFast

def num_tokens_calculus(string: str, llm_model: BaseChatModel) -> int:
    """
    Returns the number of tokens in a text string.
    """
    if isinstance(llm_model, ChatOpenAI):
        from .tokenizers.tokenizer_openai import num_tokens_openai
        num_tokens_fn = num_tokens_openai

    elif isinstance(llm_model, ChatMistralAI):
        from .tokenizers.tokenizer_mistral import num_tokens_mistral
        num_tokens_fn = num_tokens_mistral

    elif isinstance(llm_model, ChatOllama):
        from .tokenizers.tokenizer_ollama import num_tokens_ollama
        num_tokens_fn = num_tokens_ollama

    elif isinstance(llm_model, GPT2TokenizerFast):
        def num_tokens_gpt2(text: str, model: BaseChatModel) -> int:
            tokenizer = GPT2TokenizerFast.from_pretrained("gpt2")
            tokens = tokenizer.encode(text)
            return len(tokens)
        num_tokens_fn = num_tokens_gpt2

    else:
        from .tokenizers.tokenizer_openai import num_tokens_openai
        num_tokens_fn = num_tokens_openai

    num_tokens = num_tokens_fn(string, llm_model)
    return num_tokens