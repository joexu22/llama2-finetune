# llama2-finetune
![LLAMA-FIT CO.](assets/llama_in_suit.webp)
LLAMA-FIT CO.™ - Your LLaMA Will Like The Way It Looks

## Cracking the LLaMA2 Interview: A Weekend Guide to Impressing AI Startups

## Introduction

- **Goal is to finetune a LLaMA2 so that it can impress during a Tech Interview**

- **business model**
  - I got suited up llama interns waiting to work for you

- **operation model**
  - read the doc (TODO: make a doc); the joke here is that it's basically the code and I have no moat

- street cred maxxing

- impress employers/vc/people/ai

- benchmark llama2 fine-tune against base model
  - split training set against validation set (90/10?)
  - benchmark fine-tune against base
    - goal: achieve higher "cosine similarity" (between llama output and validation set) using fine-tuned version than base version
    - (exclaim - oh shit! - I'm a regmonkey)

## Quick Start Guide

[Haphazard Benchmark](./Notebooks/Haphazard_Benchmark.ipynb)
  - run all cells in notebook
  - last cell can be ran to view simple haphazard benchmark

## Basic Research

- [LLaMA2 Paper](https://arxiv.org/pdf/2307.09288.pdf)
  - definitive primary source
- [LLaMA2 Github](https://github.com/facebookresearch/llama)
  - actual code
  - not to be confused with llamacode library
    - (aside) spent way to much time trying to figure out why the download code wasn't working ...
  - 7b model
- [Deepgram Video Analysis](https://www.youtube.com/watch?v=Otb7Xi8Z0Oo)
  - good take aimed for layman
- [Karparthy is a Beast](https://github.com/karpathy/llama2.c)
  - look it's clear that I'm not legit until I make it onto the README.md page
  - but as a weekend project ... nah ... (at least right now)
- [Fiverr](https://www.fiverr.com/search/gigs?query=LLAMA2&source=top-bar&ref_ctx_id=2ab7ea78dd9c20a111a7363e13a30e50&search_in=everywhere&search-autocomplete-original-term=llama2)
  - there's academic integrity which I adhere to
  - but I'm also technically an entrepreneur ... had the look
    - these rates seems decent
    - side hustle oppurtunity?
- [Random Paper](https://people.cs.umass.edu/~simengsun/paper/rlhf_tech_report.pdf)
  - literally a random paper I pulled from arxiv talking about training and finetunning
  - insight...
    - [AlpacaFarm](https://crfm.stanford.edu/2023/05/22/alpaca-farm.html)
    - is this useful?
- [Yannic Kilcher segment](https://www.youtube.com/watch?v=xs-0cp1hSnY&ab_channel=YannicKilcher)
  - [Original LLaMA](https://www.youtube.com/watch?v=E5OnoYF2oAk&ab_channel=YannicKilcher)
  - LLaMA-Accessory (potential fine-tune tool)
    - together.ai, openchat, lmsys.org (tools that leverage llama)

## Design Experiment/Hack Minimum Viable Product/Engineering Draft

### Dataset Creation

[Kaggle](https://www.kaggle.com/datasets/sandy1811/data-science-interview-questions)
  - kaggle always have some interesting datasets (interview quetions related)
  - able to manually compile a list of interesting interview questions
    - potential OCR (future... TODO)
  - use GPT4 API to synthetically generate responses
    - potential human reinforcement here
      - scale.ai/mechanical turk stuff? (TODO)
  - 
### Implementation

#### Joke

**Discuss B4 Implementation**
![Engineering Meme](assets/SwingEngineering.webp)

#### Data Processing
  
  - acquire datasets from kaggle
  - random code in data_processing
    - Use GTP4 to do data formatting work
  - create .env with OPENAI_API_KEY=...
  - alternatively, upload/pull datasets into/from huggingface

#### Fine-Tune Framework for Pipeline

Code to be executed are found in Notebooks, which contains a bunch of colab notebooks that should be one-click solutions

[FineTune Script](https://twitter.com/Dorialexander/status/1681671177696161794)
  - good no fluff script
  - copy of code to use in pipeline in Notebooks

[Promising FineTune Framework](https://www.youtube.com/watch?v=eeM6V5aPjhk&ab_channel=1littlecoder)
  - this looks like an out of the box solution - one click colab solution
  - cons is that it uses some strange sharded model of llama 7b

##### Fine-tune Code Examples

  - [Ray Finetune](https://github.com/ray-project/ray/blob/master/doc/source/templates/04_finetuning_llms_with_deepspeed/run_llama_ft.sh)
  - [Lambda Labs Finetune](https://lambdalabs.com/blog/fine-tuning-metas-llama-2-on-lambda-gpu-cloud)

### Benchmarks

[LlamaIndex Semantic Similarity Evaluator](https://gpt-index.readthedocs.io/en/latest/examples/evaluation/semantic_similarity_eval.html)
  - compare text
  - basis for more rigorous benchmarking
    - eval-2-base_llama vs eval-2-llama_finetune

[MMLU (Massive Multitask Language Understanding)](https://paperswithcode.com/dataset/mmlu)
  - left as an excersize to better understand benchmarking

## Initial Proposal

1) choose/create fine-tuning dataset
2) prepare dataset
3) choose fine-tuning framework
4) configure fine-tuning process
5) train the model
6) evaluate the model

## Code

### Replit (MarkDown Renderer, Jupyter Env)

  - https://replit.com/@joexu22/llama2-finetune

### Github (Acutal Codebase - I hear it's on chain)

  - https://github.com/joexu22/llama2-finetune

### Executable Code in Notebook that runs on Collab
Collab Notesbooks in Repo

### Lambda Labs/Cloud Compute
  - Yo, **all instances are reserved**
    - WTF
    - need to containerize application so that it can run on any compute cloud/otherwise/etc.
      - **this is the actual product**
      - buried Alpha if you read this far

### Hugging Face
https://huggingface.co/UrbanJoe