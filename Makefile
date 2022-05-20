# Build

.PHONY: FORCE

clean: py-clean
.PHONY: clean

install: py-install
.PHONY: install

lint: py-lint
.PHONY: lint

test: py-test
.PHONY: test


# Non-PHONY targets (real files)

py-clean: FORCE
	./script/clean.sh

py-install: FORCE
	./script/install.sh

py-lint: FORCE
	./script/lint.sh

py-test: FORCE
	./script/test.sh
