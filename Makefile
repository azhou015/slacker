PACKAGE_NAME := slacker

.PHONY: install
install:
	pip install -e .

.PHONY: install-dev 
install-dev:
	pip install -e .

.PHONY: uninstall
uninstall:
	pip uninstall -y $(PACKAGE_NAME)

.PHONY: setup-build
setup-build:
	pip install -e .'[build]'

.PHONY: build
build:
	python -m build

