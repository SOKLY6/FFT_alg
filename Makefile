build:
	curl -LsSf https://astral.sh/uv/install.sh | sh
	uv venv
	uv sync

start:
	python3 cli.py