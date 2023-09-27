# 🤗 Hugging Face Model Hub with OpenVINO™

The Hugging Face (HF) Model Hub is a central repository for pre-trained deep learning models. It allows exploration and provides access to thousands of models for a wide range of tasks, including text classification, question answering, and image classification.
Hugging Face provides Python packages that serve as APIs and tools to easily download and finetune state-of-the-art pretrained models, namely [transformers] and [diffusers] packages.

![](https://github.com/huggingface/optimum-intel/raw/main/readme_logo.png)

## Contents: 
Throughout this notebook we will learn:
1. How to load a HF pipeline using the `transformers` package and then convert it to OpenVINO.
2. How to load the same pipeline using Optimum Intel package.

## Installation instructions
This is a self-contained example that relies solely on its own code.</br>
We recommend running the notebook in a virtual environment. You only need a Jupyter server to start.
For details, please refer to [Installation Guide](../../README.md).
