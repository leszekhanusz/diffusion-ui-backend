import gradio as gr
from torch import autocast


def make_gradio_interface(pipe, nsfw_filter=True):
    def run_pipe(
        *,
        prompt,
        init_image,
        mask_image,
        nb_steps,
        strength,
        guidance_scale,
        pipe,
    ):

        with autocast("cuda"):
            images = pipe(
                prompt,
                init_image=init_image,
                mask_image=mask_image,
                strength=strength,
                guidance_scale=guidance_scale,
                num_inference_steps=nb_steps,
                nsfw_filter=nsfw_filter,
            )["sample"]

            return images

    def gradio_run(
        prompt,
        init_image,
        mask_image,
        nb_images=1,
        nb_steps=50,
        strength=1,
        guidance_scale=0.75,
    ):

        images = []

        for _ in range(nb_images):
            generated = run_pipe(
                prompt=prompt,
                init_image=init_image,
                mask_image=mask_image,
                nb_steps=nb_steps,
                strength=strength,
                guidance_scale=guidance_scale,
                pipe=pipe,
            )

            images.extend(generated)

        return images

    gradio_interface = gr.Interface(
        gradio_run,
        inputs=[
            gr.Textbox(),
            gr.Image(type="pil", label="Init image"),
            gr.Image(type="pil", label="Mask image"),
            gr.Slider(minimum=1, maximum=4, value=2, step=1, label="Number of images"),
            gr.Slider(minimum=1, maximum=200, value=50, label="Number of steps"),
            gr.Slider(minimum=0, maximum=1, value=0.5, label="Strength"),
            gr.Slider(minimum=0, maximum=20, value=7.5, label="Guidance scale"),
        ],
        outputs=[
            gr.Gallery(label="Images"),
        ],
    )

    return gradio_interface
