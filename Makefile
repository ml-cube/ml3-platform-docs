# === USER PARAMETERS

ifdef OS
   export VENV_BIN=.venv/Scripts
else
   export VENV_BIN=.venv/bin
endif

# == SETUP REPOSITORY AND DEPENDENCIES

dev-sync:
	uv sync --cache-dir .uv_cache --all-extras

setup: dev-sync

build-docs:
	. $(VENV_BIN)/activate && mkdocs build

serve-docs:
	. $(VENV_BIN)/activate && mkdocs serve
