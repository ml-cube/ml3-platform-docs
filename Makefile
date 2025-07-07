# == SETUP REPOSITORY AND DEPENDENCIES
set-hooks:
	cp .hooks/pre-commit .git/hooks/pre-commit && chmod +x .git/hooks/pre-commit

dev-sync:
	uv sync --cache-dir .uv_cache --all-extras

setup: set-hooks dev-sync

build-docs:
	uv run mkdocs build

serve-docs:
	uv run mkdocs serve
