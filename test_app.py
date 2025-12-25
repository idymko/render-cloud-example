# test_app.py

import os
import pytest
from app import dymko_fun

# Set the DATABASE_URL environment variable
os.environ['DATABASE_URL'] = 'your_database_url_here'

def test_dymko_fun():
    assert dymko_fun() == "This page is created by dymko!!!"
