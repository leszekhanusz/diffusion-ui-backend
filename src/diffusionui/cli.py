from argparse import ArgumentParser

import torch

from .__version__ import __version__
from .gradio_interface import make_gradio_interface
from .pipelines import StableDiffusionPipeline


def get_parser() -> ArgumentParser:
    description = """
Generate a gradio interface providing a unified pipeline for Stable Diffusion
images generations, doing text-to-image, image-to-image and inpainting
using the same interface.
"""

    parser = ArgumentParser(
        description=description,
    )

    parser.add_argument("--version", action="version", version=f"v{__version__}")

    parser.add_argument(
        "--low-mem",
        help="Reduce GPU VRAM usage",
        action="store_true",
        dest="low_mem",
    )

    parser.add_argument(
        "--download-model",
        help="Download the Stable Diffusion model",
        action="store_true",
        dest="download_model",
    )

    parser.add_argument(
        "-m",
        "--model",
        help="choose the stable diffusion model",
        dest="model",
        default="CompVis/stable-diffusion-v1-4",
    )

    parser.add_argument(
        "--disable-nsfw-filter",
        help="Disable the NSFW filter",
        action="store_true",
        dest="disable_nsfw_filter",
    )

    return parser


def diffusionui_cli():

    # Get arguments from command line
    parser = get_parser()
    args = parser.parse_args()

    # Set the pipe arguments depending on options selected
    pipe_args = {
        "device": "cuda",
        "use_auth_token": args.download_model,
        "local_files_only": not (args.download_model),
    }

    if args.low_mem:
        pipe_args["revision"] = "fp16"
        pipe_args["torch_dtype"] = torch.float16

    # Make unified diffusers pipe
    pipe = StableDiffusionPipeline.from_pretrained(
        args.model,
        **pipe_args,
    ).to("cuda")

    # Disable the nsfw filter if requested
    if args.disable_nsfw_filter:
        pipe.disable_nsfw_filter()

    # Generate gradio interface
    gradio_interface = make_gradio_interface(pipe)

    # Start it
    gradio_interface.launch()
