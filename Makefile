default: install

all: install build

.PHONY: install
install:
	cd docs && ./install.sh

.PHONY: build
build:
	cd docs && ./build.sh

.PHONY: serve
s serve:
	cd docs && mdbook serve
