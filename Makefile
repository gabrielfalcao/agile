export TESTCMD		:= nosetests -sxv --with-coverage --cover-package=my_cool_library --rednose
export PYTHONPATH	:= ${PWD}:$PYTHONPATH

tests: dependencies unit functional

dependencies:
	@python setup.py develop

unit functional:
	@$(TESTCMD) tests/$@

clean:
	git clean -Xdf

release: tests
	@./.release
	@rm -rf dist
	@pipenv run python setup.py sdist
	@pipenv run twine upload dist/*.tar.gz


.PHONY: tests
