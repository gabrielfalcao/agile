#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
from sure import scenario
import os


def prepare_db_file(context):
    """setup function for the clean_fs_environment scenario, removes
    the file if already exists"""
    # setting the filename in one central place, and use in many tests when necessary
    context.TEST_FILENAME = 'my-db.json'
    remove_db_file(context)


def remove_db_file(context):
    """teardown function of the clean_fs_environment scenario, removes
    the TEST_FILENAME file if it exists"""
    if os.path.exists(context.TEST_FILENAME):
        os.unlink(context.TEST_FILENAME)


clean_fs_environment = scenario(prepare_db_file, remove_db_file)
