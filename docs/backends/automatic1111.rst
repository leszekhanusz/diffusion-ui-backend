Automatic1111
=============

Installation
^^^^^^^^^^^^

- First install the automatic1111 fork by following the
  `instructions on its GitHub page <https://github.com/AUTOMATIC1111/stable-diffusion-webui>`_.
  You should be able to run its own webui interface by going to
  http://127.0.0.1:7860

- Optionally run :code:`git checkout master` and :code:`git pull -r` in the
  `stable-diffusion-webui` folder to upgrade to the latest version

- Add :code:`--cors-allow-origins=http://localhost:5173,https://diffusionui.com` to your
  commandline arguments used to start the Automatic1111 fork.
  (In the `webui-user.bat` file on Windows)

- Launch the automatic1111 webui with those arguments (on windows start the `webui.bat` script)

- Go to https://diffusionui.com

- click on the ⓘ  icon to go to the model info tab

- click on the :code:`Reset to default values` button and confirm by clicking Yes.

.. warning::

    The webui should run on the 7860 port.
    `Running on local URL:  http://127.0.0.1:7860/` appearing in the console.
    It happens that if you restart the webui too soon that the port is changed
    to 7861. In that case, wait a minute and start again until it's on port 7860

.. warning::

    It does not work with the brave browser by default and potentially some strict
    adblockers. You'll need to deactivate the brave shield for this page.
    Note that diffusion-ui does not use tracking of any kind, they just don't
    like the fact that the backend config is downloaded from http://127.0.0.1:7860/config
    I guess...
