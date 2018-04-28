.PHONY: all
all: dependencies unit functional acceptance

TESTCMD = nosetests -sxv --with-coverage --cover-package=my_cool_library --rednose
PYTHONPATH = ${PWD}:$PYTHONPATH


export PYTHONPATH



dependencies:
	@python setup.py develop

unit:
	@$(TESTCMD) tests/unit

functional:
	@$(TESTCMD) tests/functional

acceptance:
	@steadymark README.md

clean:
	git clean -Xdf

release:
	@python setup.py sdist register upload

unit:
