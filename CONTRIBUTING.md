# Contributing

Thanks for helping to make Diffusion-UI awesome!

We welcome all kinds of contributions:

- Bug fixes
- Documentation improvements
- New features
- Refactoring & tidying

## Getting started

If you have a specific contribution in mind, be sure to check the
[issues](https://github.com/leszekhanusz/diffusion-ui-backend/issues)
and [pull requests](https://github.com/leszekhanusz/diffusion-ui-backend/pulls)
in progress - someone could already be working on something similar
and you can help out.

## Coding guidelines

Some tools are used to ensure a coherent coding style.
You need to make sure that your code satisfy those requirements
or the automated tests will fail.

- [black code formatter](https://github.com/psf/black)
- [flake8 style enforcement](https://flake8.pycqa.org/en/latest/index.html)
- [isort to sort imports alphabetically](https://isort.readthedocs.io/en/stable/)

On Linux or MacOS, you can fix and check your code style by running
the Makefile command `make check` (this is also checked by running
the automated tests with tox but it is much faster with make)

## How to create a good Pull Request

1. Make a fork of the main branch on github
2. Clone your forked repo on your computer
3. Create a feature branch `git checkout -b feature_my_awesome_feature`
4. Modify the code
5. Verify that the [Coding guidelines](#coding-guidelines) are respected
7. Make a commit and push it to your fork
8. From github, create the pull request. Automated tests from GitHub actions
will then automatically check the code
9. If other modifications are needed, you are free to create more commits and
push them on your branch. They'll get added to the PR automatically.

Once the Pull Request is accepted and merged, you can safely
delete the branch (and the forked repo if no more development is needed).
