# Context Length Visualized - How much is 128k tokens

To visualize how big the context windows are for the current LLMs I currated a list of different token lengths.

## Context Length Terminology

Since we started intially with a context length of 4096 I assumed that the follow up context lengths are multiples of 4096.

But to keep it simple the big companies shortend it to 32k, 64k and 128k respectivelly.

Hoever I kept it to the multiples of 4096.

### Tokenizer

The tokenizer used is [tiktoken](https://github.com/openai/tiktoken) from [OpenAI](https://platform.openai.com/tokenizer)

Every company is using their own tokenizer but in principal they are all working the same

The tokenizer base for those files is `o200k_base` which means that the vocabulary used to create those tokens is 200k big!

### Tokenizer base file

You can find two additional files

One represents the encoded base `o200k_base.tiktoken`

And one the decoded base with base64/utf-8 encoding `o200k_base.txt`

I had troubles to decode it. Some decodes didn't work properly.

Does someone knows how to decode it propperly?

You can run the decode with `python decode.py`