# Unified Stable Diffusion pipeline

This repository provides a unified [Stable Diffusion](https://github.com/CompVis/stable-diffusion) pipeline to generate images using the same pipeline with [diffusers](https://github.com/huggingface/diffusers) for:

- text-to-image
- image-to-image
- inpainting

This pipeline cannot be imported directly from diffusers because of the [diffusers philosophy](https://github.com/huggingface/diffusers/issues/307).

## Installation

```bash
pip install diffusionui
```

## Usage

```
from diffusionui import StableDiffusionPipeline
```

Then use any of the examples from [diffusers](https://github.com/huggingface/diffusers) by replacing `StableDiffusionImg2ImgPipeline` and `StableDiffusionInpaintPipeline` by `StableDiffusionPipeline`.
