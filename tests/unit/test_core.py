# -*- coding: utf-8 -*-
#

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


def test_json_database_state_to_json():
    ("JSONDatabase.state_to_json() should return a valid json string")
    # Given that I have an instance of the database containing some data
    jdb = JSONDatabase(data={'name': 'Foo Bar'})

    # When I call .state_to_json
    result = jdb.state_to_json()

    # Then it should return a valid JSON
    result.should.equal('{"name": "Foo Bar"}')
