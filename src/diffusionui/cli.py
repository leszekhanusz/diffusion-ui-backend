import logging
import time
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

    parser.add_argument(
        "--share",
        help="Create a link to be able to run your model from elsewhere",
        action="store_true",
        dest="share",
    )

    parser.add_argument(
        "--auth",
        type=str,
        help='gradio authentication. "username:password" or more "user1:pass1,user2:pass2"',
        default=None,
    )

    parser.add_argument(
        "--access-code",
        type=str,
        help="Optional access code to limit access to the model without using gradio auth",
        default=None,
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
    gradio_interface = make_gradio_interface(pipe, access_code=args.access_code)

    if not args.share:
        print("\nTo create a public link, use --share")

    # Start it
    SERVER_PORT = 7860
    while True:
        try:
            gradio_interface.launch(
                server_port=SERVER_PORT,
                quiet=True,
                share=args.share,
                auth=[tuple(cred.split(":")) for cred in args.auth.strip('"').split(",")] if args.auth else None,
            )
        except OSError as e:
            if str(e).startswith(f"Port {SERVER_PORT} is in use"):
                logging.warning(f"Port {SERVER_PORT} is in use. Trying again in 5 seconds.")
                time.sleep(5)
                continue
        break
