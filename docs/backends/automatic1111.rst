Automatic1111 fork
==================

Installation
^^^^^^^^^^^^

- First install the automatic1111 fork by following the
  `instructions on its GitHub page <https://github.com/AUTOMATIC1111/stable-diffusion-webui>`_.
  You should be able to run its own webui interface by going to
  http://127.0.0.1:7860

- Run :code:`git checkout master` and :code:`git pull -r` in the
  `stable-diffusion-webui` folder to upgrade to the latest version

- Launch the automatic1111 webui (on windows start the `webui.bat` script)

- Go to https://diffusionui.com

- select :code:`Automatic1111` in the dropdown at the top of the left panel

- click on the ⓘ  icon to go to the model info tab

- click on the :code:`Reset to default values` button and confirm by clicking Yes.

.. warning::

    The webui should run on the 7860 port.
    `Running on local URL:  http://127.0.0.1:7860/` appearing in the console.
    It happens that if you restart the webui too soon that the port is changed
    to 7861. In that case, wait a minute and start again until it's on port 7860
