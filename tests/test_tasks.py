from main.tasks import load_btc

import pytest


# tasks

@pytest.mark.django_db
def test_task():
    load_btc.run()
    assert True
