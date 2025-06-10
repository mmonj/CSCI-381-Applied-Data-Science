.PHONY: notebook register

notebook:
	uv run jupyter notebook
register:
	uv run ipython kernel install --user --env VIRTUAL_ENV $(pwd)/.venv --name=pythontestttt
