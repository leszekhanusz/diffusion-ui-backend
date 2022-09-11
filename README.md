# diffusion-ui-backend

[Gradio](https://gradio.app) backend for the [diffusion-ui](https://github.com/leszekhanusz/diffusion-ui) web frontend
using an [unified Stable Diffusion diffusers pipeline](src/diffusionui/pipelines/README.md)

The gradio interface provides an API to generate images with [Stable Diffusion](https://github.com/CompVis/stable-diffusion) for:

- text-to-image
- image-to-image
- inpainting

## Installation

```bash
pip install diffusionui
```

## First Usage

The first time, you have to download the model:

- create an account on https://huggingface.co
- [generate a token in your settings](https://huggingface.co/docs/hub/security-tokens)
- login on your console with `huggingface-cli login`
- then download the model with:

```bash
diffusionui --download-model
```

## Usage

Once the model has been downloaded, you can start the backend by running:

```bash
diffusionui --low-mem
```

It should produce an local URL for the gradio interface:

```
Running on local URL:  http://127.0.0.1:7860/
```
