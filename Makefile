# === USER PARAMETERS

ifdef OS
   export PYTHON_COMMAND=python
   export UV_INSTALL_CMD=powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
   export VENV_BIN=.venv/Scripts
else
   export PYTHON_COMMAND=python3.12
   export UV_INSTALL_CMD=curl -LsSf https://astral.sh/uv/install.sh | sh
   export VENV_BIN=.venv/bin
endif

export SRC_DIR=ml3_platform_docs

DEPLOY_ENVIRONMENT=$(shell if [ $(findstring main, $(BRANCH_NAME)) ]; then \
			echo 'prod'; \
		elif [ $(findstring pre, $(BRANCH_NAME)) ]; then \
			echo 'pre'; \
		else \
		 	echo 'dev'; \
		fi)
# If use deploy_environment in the tag system
# `y` => yes
# `n` => no
USE_DEPLOY_ENVIRONMENT=n

# == SETUP REPOSITORY AND DEPENDENCIES

install-uv:
	# install uv package manager
	$(UV_INSTALL_CMD)
	# create environment
	uv venv -p $(PYTHON_COMMAND)

compile:
	# install extra dev group
	uv pip compile pyproject.toml -o requirements.txt --cache-dir .uv_cache

install:
	uv pip sync requirements.txt --cache-dir .uv_cache

setup: install-uv compile install

build-docs:
	mkdocs build

serve-docs:
	mkdocs serve
