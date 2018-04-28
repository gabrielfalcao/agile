# -*- coding: utf-8 -*-
#
from __future__ import unicode_literals
import os
import json
from .helpers import clean_fs_environment
from my_cool_library.core import JSONDatabase


@clean_fs_environment
def test_json_database_writes_file(context):
    ("JSONDatabase.save should write a file to the disc and it must contain the json data")

    # Given that there is no file named `my-db.json`
    os.path.exists(context.TEST_FILENAME).should.be.false

    # And that I create a JSONDatabase pointing to a real file
    jdb = JSONDatabase(context.TEST_FILENAME, data={
        'name': 'John Doe',
        'age': None,
    })

    # When I save the database
    jdb.save()

    # Then the file should exist
    os.path.exists(context.TEST_FILENAME).should.be.true

    # And it should contain json data
    open(context.TEST_FILENAME).read().should.equal(json.dumps({
        'name': 'John Doe',
        'age': None,
    }))
