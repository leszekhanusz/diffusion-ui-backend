.PHONY: clean tests docs

SRC_PYTHON := src/diffusionui

check:
	isort -v $(SRC_PYTHON)
	black $(SRC_PYTHON)
	flake8 $(SRC_PYTHON)
	check-manifest

clean:
	find . -name "*.pyc" -delete
	find . -name "__pycache__" | xargs -I {} rm -rf {}
	find . -name "*.egg-info" | xargs -I {} rm -rf {}
	rm -rf ./.mypy_cache
	rm -rf ./dist
	rm -rf ./build
	rm -rf ./.tox
	rm -rf ./docs/_build
	rm -rf ./flagged

docs:
	rm -rf ./docs/_build
	cd docs; make html
	xdg-open ./docs/_build/html/index.html
