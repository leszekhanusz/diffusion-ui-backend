# diffusion-ui-backend

[Gradio](https://gradio.app) backend for the [diffusion-ui](https://github.com/leszekhanusz/diffusion-ui) web frontend
using an [unified Stable Diffusion diffusers pipeline](src/diffusionui/pipelines/README.md)

The gradio interface provides an API to generate images with [Stable Diffusion](https://github.com/CompVis/stable-diffusion) for:

- text-to-image
- image-to-image
- inpainting

## Installation

First install [pytorch](https://pytorch.org) with cuda support (if you have a NVIDIA GPU):

```
conda install pytorch torchvision torchaudio cudatoolkit=11.6 -c pytorch -c conda-forge
```

Then install diffusionui and its dependencies:

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
# using the low-memory model (for GPUs with low VRAM)
diffusionui --low-mem --download-model

# or using the full model
diffusionui --download-model
```

## Usage

Once the model has been downloaded, you can start the backend by running:

```bash
# For the low-memory model
diffusionui --low-mem

# For the full model
diffusionui
```

It should produce an local URL for the gradio interface:

```
Running on local URL:  http://127.0.0.1:7860/
```
