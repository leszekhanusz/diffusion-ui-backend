Stable Diffusion
================

Installation
^^^^^^^^^^^^

.. tabs::

    .. tab:: Linux

        - Install `conda`_ if it is not already installed

        - Create an environment named **dui**:

        .. code-block:: bash

            conda create -n dui python=3.10

        - Activate that environment (You will need to do that every time before running the backend):

        .. code-block:: bash

            conda activate dui

        - You now should have a **(dui)** text in front of your prompt indicating that you are inside that environment.

        - Inside this environment, install `pytorch <https://pytorch.org>`_ with cuda support:

        .. code-block:: bash

            conda install pytorch torchvision torchaudio cudatoolkit=11.6 -c pytorch -c conda-forge

        - Install the diffusionui backend and its dependencies:

        .. code-block:: bash

            pip install diffusionui

    .. tab:: Windows

        - Download `Miniconda <https://docs.conda.io/en/latest/miniconda.html>`_
        - Install Miniconda. Install for all users. Uncheck "Register Miniconda as the system Python 3.9" unless you want to
        - `Activate Developer mode <https://www.wikihow.com/Enable-Developer-Mode-in-Windows-10>`_
        - Open Anaconda Prompt (miniconda3)
        - Create an environment named **dui**:

        .. code-block:: bash

            conda create -n dui python=3.10

        - Activate that environment (You will need to do that every time before running the backend):

        .. code-block:: bash

            conda activate dui

        - You now should have a **(dui)** text in front of your prompt indicating that you are inside that environment.

        - Install `pytorch <https://pytorch.org>`_ with cuda support:

        .. code-block:: bash

            conda install pytorch torchvision torchaudio cudatoolkit=11.6 -c pytorch -c conda-forge

        - Install the diffusionui backend and its dependencies:

        .. code-block:: bash

            pip install diffusionui

First Usage
^^^^^^^^^^^^

The first time, you have to download the model:

- create an account on https://huggingface.co
- `Click on this page to accept the LICENSE <https://huggingface.co/CompVis/stable-diffusion-v1-4>`_
- `generate a token in your settings <https://huggingface.co/docs/hub/security-tokens>`_
- login on your console with `huggingface-cli login`
- then download the model with:

.. tabs::

    .. tab:: Low VRAM (recommended)

        .. code-block:: bash

            diffusionui --low-mem --download-model

    .. tab:: High VRAM

        .. code-block:: bash

            diffusionui --download-model


Usage
^^^^^

Once the installation has been done, you should have a **diffusionui**
executable in the **dui** environment you created.

Every time you need to run the backend, don't forget to activate that environment:

.. code-block:: bash

    conda activate dui

You can check the current installed version by typing:

.. code-block:: bash

    diffusionui --version

To start the backend, run:

.. tabs::

    .. tab:: Low VRAM (recommended)

        .. code-block:: bash

            diffusionui --low-mem

    .. tab:: High VRAM

        .. code-block:: bash

            diffusionui

It should produce an local URL for the gradio interface:

.. code-block:: bash

    Running on local URL:  http://127.0.0.1:7860/


Once you have this local URL, congratulations 🚀 !
You can now visit https://diffusionui.com to access it with the nice interface.

.. _conda: https://docs.conda.io

Sharing
^^^^^^^

It is possible to use Diffusion-UI on your smartphone, tablet or other computer by
sharing the backend on your PC.

To share the backend:

* use :code:`--share` to get a public url that can be used from an external device
* optionaly use :code:`--access-code` to specify a required code to access the model

.. code-block:: bash

    diffusionui --low-mem --share --access-code 1234

You'll receive something like this:

.. code-block::

    Running on local URL:  http://127.0.0.1:7860/
    Running on public URL: https://16141.gradio.app

Then, from your smartphone or tablet:

* go to http://diffusionui.com
* open the left panel with the top-left icon, then open the model info tab (ⓘ)
* Click on the API URL and change it by replacing the hostname by the provided public URL
  (:code:`https://16141.gradio.app/api/predict` in this example)
* Below, insert the access code if needed

Once you've done this, you can use it on this device.
The url and access code is saved in Local Storage in your browser so you need to do this only once.

You can now show this amazing technology to all your friends!
