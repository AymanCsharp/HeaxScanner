.PHONY: help install test clean run demo quick-start lint format security-check build release

help:
	@echo "HEAX Scanner"
	@echo "=============================================="
	@echo ""
	@echo "Available targets:"
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "  %-15s %s\n", $$1, $$2}' $(MAKEFILE_LIST)

install:
	@echo "Installing requirements..."
	pip install -r requirements.txt
	@echo "Installation completed!"

install-dev:
	@echo "Installing development requirements..."
	pip install -r requirements-dev.txt
	pip install -e .
	@echo "Development installation completed!"

test:
	@echo "Running all tests..."
	pytest tests/ -v --cov=src --cov-report=html --cov-report=term

test-unit:
	@echo "Running unit tests..."
	pytest tests/unit/ -v

test-integration:
	@echo "Running integration tests..."
	pytest tests/integration/ -v

test-system:
	@echo "Running system tests..."
	pytest tests/system/ -v

test-coverage:
	@echo "Running tests with coverage report..."
	pytest tests/ -v --cov=src --cov-report=html --cov-report=term --cov-report=xml

test-performance:
	@echo "Running performance tests..."
	pytest tests/system/performance/ -v --benchmark-only

test-security:
	@echo "Running security tests..."
	pytest tests/system/security/ -v

lint:
	@echo "Running code linting..."
	flake8 src/ tests/
	pylint src/ tests/
	bandit -r src/

format:
	@echo "Formatting code..."
	black src/ tests/
	isort src/ tests/
	autopep8 --in-place --recursive src/ tests/

format-check:
	@echo "Checking code format..."
	black --check src/ tests/
	isort --check-only src/ tests/

security-check:
	@echo "Running security checks..."
	bandit -r src/
	safety check
	pip-audit

build:
	@echo "Building project..."
	python -m build

release:
	@echo "Creating new release..."
	bump2version patch
	git push --tags
	git push origin main

run:
	@echo "Starting HEAX Scanner..."
	python heax_scanner.py

demo:
	@echo "Running demo..."
	python demo.py

quick-start:
	@echo "Running quick start..."
	python quick_start.py

start:
	@echo "Direct launch..."
	python start.py

dev-setup:
	@echo "Setting up development environment..."
	python -m venv venv
	@echo "Virtual environment created. Activate it with:"
	@echo "  source venv/bin/activate  # Linux/macOS"
	@echo "  venv\\Scripts\\activate     # Windows"

dev-install:
	@echo "Installing in development mode..."
	pip install -e .

db-init:
	@echo "Initializing database..."
	python -c "from heax_scanner import HeaxScanner; scanner = HeaxScanner(); scanner.setup_database()"

db-reset:
	@echo "Resetting database..."
	rm -f heax_vulnerabilities.db
	@echo "Database reset completed!"

config-init:
	@echo "Creating default configuration..."
	@if [ ! -f heax_config.ini ]; then \
		echo "Configuration file already exists. Skipping..."; \
	else \
		python -c "from heax_scanner import HeaxScanner; scanner = HeaxScanner()"; \
		echo "Configuration file created!"; \
	fi

config-edit:
	@echo "Opening configuration file for editing..."
	@if command -v code >/dev/null 2>&1; then \
		code heax_config.ini; \
	elif command -v nano >/dev/null 2>&1; then \
		nano heax_config.ini; \
	elif command -v vim >/dev/null 2>&1; then \
		vim heax_config.ini; \
	else \
		echo "Please edit heax_config.ini manually"; \
	fi

docs-build:
	@echo "Building documentation..."
	@if command -v mkdocs >/dev/null 2>&1; then \
		mkdocs build; \
	else \
		echo "MkDocs not installed. Installing..."; \
		pip install mkdocs; \
		mkdocs build; \
	fi

docs-serve:
	@echo "Starting documentation server..."
	@if command -v mkdocs >/dev/null 2>&1; then \
		mkdocs serve; \
	else \
		echo "MkDocs not installed. Please run 'make docs-build' first"; \
	fi

clean:
	@echo "Cleaning temporary files..."
	find . -type f -name "*.pyc" -delete
	find . -type d -name "__pycache__" -delete
	find . -type f -name "*.log" -delete
	find . -type f -name "*.db" -delete
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info/
	rm -rf htmlcov/
	rm -rf .pytest_cache/
	rm -rf .coverage
	@echo "Cleaning completed!"

clean-all: clean
	@echo "Performing deep clean..."
	rm -rf venv/
	rm -rf .venv/
	rm -rf node_modules/
	@echo "Deep cleaning completed!"

deps-update:
	@echo "Updating dependencies..."
	pip install --upgrade pip
	pip install --upgrade -r requirements.txt
	@echo "Dependencies updated!"

deps-check:
	@echo "Checking dependencies..."
	pip list --outdated
	safety check

git-status:
	@echo "Git status:"
	git status

git-commit:
	@echo "Committing changes..."
	git add .
	git commit -m "Update: $(shell date)"

git-push:
	@echo "Pushing changes..."
	git push origin main

install-windows:
	@echo "Installing on Windows..."
	python -m pip install --upgrade pip
	pip install -r requirements.txt
	@echo "Windows installation completed!"

install-linux:
	@echo "Installing on Linux..."
	sudo apt-get update
	sudo apt-get install -y python3-pip python3-venv
	pip3 install -r requirements.txt
	@echo "Linux installation completed!"

install-macos:
	@echo "Installing on macOS..."
	brew install python3
	pip3 install -r requirements.txt
	@echo "macOS installation completed!"

all: install test lint format security-check
	@echo "All operations completed!"

quick: install run
	@echo "Quick setup and run completed!"

test-help:
	@echo "Test targets:"
	@echo "  test           - Run all tests"
	@echo "  test-unit      - Run unit tests only"
	@echo "  test-integration - Run integration tests only"
	@echo "  test-system    - Run system tests only"
	@echo "  test-coverage  - Run tests with coverage report"
	@echo "  test-performance - Run performance tests"
	@echo "  test-security  - Run security tests"

run-help:
	@echo "Run targets:"
	@echo "  run           - Run main application"
	@echo "  demo          - Run demo"
	@echo "  quick-start   - Run quick start"
	@echo "  start         - Direct launch"

dev-help:
	@echo "Development targets:"
	@echo "  dev-setup     - Setup development environment"
	@echo "  dev-install   - Install in development mode"
	@echo "  lint          - Code linting"
	@echo "  format        - Code formatting"
	@echo "  security-check - Security checks"

.DEFAULT_GOAL := help


