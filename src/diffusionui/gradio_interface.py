import logging

import gradio as gr
import torch
from torch import autocast

from .__version__ import __api_version__


def make_gradio_interface(pipe):
    def run_pipe(
        *,
        prompt,
        init_image,
        mask_image,
        nb_steps,
        strength,
        guidance_scale,
        seeds,
        pipe,
    ):

        seed = seeds[0]
        generator = torch.Generator(device="cuda")
        generator = generator.manual_seed(seed)

        with autocast("cuda"):
            images = pipe(
                prompt,
                init_image=init_image,
                mask_image=mask_image,
                strength=strength,
                guidance_scale=guidance_scale,
                num_inference_steps=nb_steps,
                generator=generator,
            ).images

            return images

    def gradio_run(
        api_version,
        prompt,
        init_image,
        mask_image,
        nb_images,
        nb_steps,
        strength,
        guidance_scale,
        seeds,
    ):

        if api_version != __api_version__:
            logging.warning(
                f"Backend API version ({__api_version__}) is different than " f"frontend API version ({api_version})."
            )

            if api_version > __api_version__:

                logging.warning("You should update the backend by running " "'pip install diffusionui --upgrade'")

        # Generate seeds if needed
        generator = torch.Generator()

        if seeds:
            seeds = [int(seed) for seed in seeds.split(",")]
        else:
            seeds = [generator.seed() for _ in range(nb_images)]

        all_generated_images = []

        for i in range(nb_images):

            # If we don't have enough seeds, stop generating images
            try:
                next_seeds = seeds[i:]
                if len(next_seeds) == 0:
                    break
            except IndexError:
                break

            generated_images = run_pipe(
                prompt=prompt,
                init_image=init_image,
                mask_image=mask_image,
                nb_steps=nb_steps,
                strength=strength,
                guidance_scale=guidance_scale,
                seeds=next_seeds,
                pipe=pipe,
            )

            all_generated_images.extend(generated_images)

        seeds_str = ",".join([str(seed) for seed in seeds])

        return all_generated_images, seeds_str

    gradio_interface = gr.Interface(
        gradio_run,
        inputs=[
            gr.Number(label="API Version", value=__api_version__, visible=False),
            gr.Textbox(label="Prompt"),
            gr.Image(type="pil", label="Init image"),
            gr.Image(type="pil", label="Mask image"),
            gr.Slider(minimum=1, maximum=4, value=2, step=1, label="Number of images"),
            gr.Slider(minimum=1, maximum=200, value=50, label="Number of steps"),
            gr.Slider(minimum=0, maximum=1, value=0.5, label="Strength"),
            gr.Slider(minimum=0, maximum=20, value=7.5, label="Guidance scale"),
            gr.Textbox(label="Seeds"),
        ],
        outputs=[
            gr.Gallery(label="Images"),
            gr.Text(label="Seeds"),
        ],
    )

    return gradio_interface
