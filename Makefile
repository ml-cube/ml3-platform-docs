# === USER PARAMETERS

ifdef OS
   export VENV_BIN=.venv/Scripts
else
   export VENV_BIN=.venv/bin
endif

# == SETUP REPOSITORY AND DEPENDENCIES
set-hooks:
	cp .hooks/pre-commit .git/hooks/pre-commit && chmod +x .git/hooks/pre-commit

dev-sync:
	uv sync --cache-dir .uv_cache --all-extras

setup: set-hooks dev-sync

build-docs:
	. $(VENV_BIN)/activate && mkdocs build

serve-docs:
	. $(VENV_BIN)/activate && mkdocs serve
