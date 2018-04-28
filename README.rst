Agile
=====

.. image:: https://travis-ci.org/gabrielfalcao/agile.svg?branch=master
   :target: https://travis-ci.org/gabrielfalcao/agile

.. image:: https://codecov.io/gh/gabrielfalcao/agile/branch/master/graph/badge.svg
   :target: https://codecov.io/gh/gabrielfalcao/agile


Meta-package for python with tools for an agile development workflow.


add it to your project
----------------------

.. code:: bash

    pip install agile


what is in it?
--------------

mock
^^^^

The `mock <http://www.voidspace.org.uk/python/mock/>`__ library is the
easiest and most expressive way to mock in python.

example: mocking I/O calls:


.. code:: python

    # cool-git-project/my_cool_library/core.py
    import io
    import json


    class JSONDatabase(object):
        def __init__(self, filename=None, data={}):
            self.filename = filename
            self.data = data

        def state_to_json(self):
            return json.dumps(self.data)

        def save(self):
            # open file
            fd = io.open(self.filename, 'wb')
            fd.write(self.state_to_json())
            fd.close()

.. code:: python

    # cool-git-project/tests/unit/test_core.py
    from mock import patch
    from my_cool_library.core import JSONDatabase


    @patch('my_cool_library.core.io')
    @patch('my_cool_library.core.JSONDatabase.state_to_json')
    def test_json_database_save(state_to_json, io):
        ("JSONDatabase.save() should open the database file, "
         "and write the latest json state of the data")

        # Given that the call to io.open returns a mock
        mocked_fd = io.open.return_value

        # And that I create an instance of JSONDatabase with some data
        jdb = JSONDatabase('my-database.json', data={'foo': 'bar'})

        # When I call .save()
        jdb.save()

        # Then the file descriptor should have been opened in write mode,
        # and pointing to the right file
        io.open.assert_called_once_with('my-database.json', 'wb')

        # And the returned file descriptor should have been used
        # to write the return value from state_to_json
        mocked_fd.write.assert_called_once_with(state_to_json.return_value)

        # And then the file descriptor should have been closed
        mocked_fd.close.assert_called_once_with()

The mock documentation can be found
`here <http://www.voidspace.org.uk/python/mock/>`__

sure
^^^^

Sure modifies the all the python objects in memory, adding a special
property ``should``, that allows you to test aspects of the given
object.

Let's see it in practice.

Still considering the project from the *mock* example above, now let's
test that ``state_to_json`` returns a json string.

.. code:: python

    def test_json_database_state_to_json():
        ("JSONDatabase.state_to_json() should return a valid json string")
        # Given that I have an instance of the database containing some data
        jdb = JSONDatabase(data={'name': 'Foo Bar'})

        # When I call .state_to_json
        result = jdb.state_to_json()

        # Then it should return a valid JSON
        result.should.equal('{"name": "Foo Bar"}')

The sure documentation is available
`here <https://github.com/gabrielfalcao/sure>`__

nose + coverage + rednose
^^^^^^^^^^^^^^^^^^^^^^^^^

.. code:: bash

    nosetests -vsx --rednose --with-coverage --cover-package=my_cool_library tests/unit
    # or
    nosetests -vsx --rednose --with-coverage --cover-package=my_cool_library tests/functional

Nose is a great test runner, recursively scans for files that start with
``test_`` and and with ``.py``. It supports plugins and agile installs
two cool plugins:

coverage


coverage is a module that collects test coverage data so that nose can
show a summary of what lines of python code don't have test coverage.

rednose


Rednose is a plugin that prints a prettier output when running the
tests, and show bad things in **red** which highlights problems and make
it easier to see where is the problem, pretty awesome.

More over, **as long as you write single-line docstrings to describe
your tests** rednose will show the whole sentence, pretty and with no
chops.

.. code:: bash

    JSONDatabase.save() should open the database file, and write the latest json state of the data ... passed
    JSONDatabase.state_to_json() should return a valid json string ... passed

    -----------------------------------------------------------------------------
    2 tests run in 0.0 seconds (2 tests passed)

ps.: nose actually matches files that contain ``test`` in the name and
can also find ``TestCase`` classes, but I recommend using function-based
tests, for clarity, expressiveness and to enforce simplicity. We
developers tend to add too much logic to setup and teardown functions
when writing test-based class.

Gists:
------

creating a basic python test infrastructure
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code:: bash

    mkdir -p tests/{unit,functional}
    touch tests/{unit,functional,}/__init__.py
    printf 'import sure\nsure\n' > tests/unit/__init__.py
    printf 'import sure\nsure\n' > tests/functional/__init__.py

now go ahead and add a unit test file, try to name your test file such
that it resembles module being tested, for example, let's say you are
testing ``my_cool_library/engine.py``, you could create a test file like
this

.. code:: bash

    printf "# -*- coding: utf-8 -*-\n\n" > tests/unit/test_engine.py

.. |Build Status| image:: https://travis-ci.org/gabrielfalcao/agile.svg
   :target: https://travis-ci.org/gabrielfalcao/agile
