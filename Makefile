.PHONY: init format lint git-config

GIT_NAME ?=
GIT_EMAIL ?=

install:
	@uv sync 
	@echo
	@echo ------------------ PROJECT READY ---------------------- 
	@echo "Activate env: source .venv/bin/activate"
	@echo "Train model: make train"
	@echo

git-config:
	@if [ -z "$(GIT_NAME)" ] || [ -z "$(GIT_EMAIL)" ]; then \
		echo "Usage: make git-config GIT_NAME=\"Your Name\" GIT_EMAIL=\"your@email.com\""; \
		exit 1; \
	fi
	@git config --global user.name "$(GIT_NAME)"
	@git config --global user.email "$(GIT_EMAIL)"
	@git config --global pull.rebase false
	@git config --global pull.ff false
	@echo
	@echo ------------------ GIT CONFIGURED ---------------------
	@echo "user.name:  $(GIT_NAME)"
	@echo "user.email: $(GIT_EMAIL)"
	@echo "pull strategy: merge (no rebase, no fast-forward)"
	@echo

train:
	@python3 -m src.train

format:
	ruff src 

lint:
	ruff check src 