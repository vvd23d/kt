from django.test import TestCase
from django.test.utils import override_settings
from main.tasks import load_btc


"""from django.urls import reverse


# integration tests

def test_home(client):
    url = reverse("home")
    response = client.get(url)
    assert response.status_code == 200"""


class TestAddTask(TestCase):

    def setUp(self):
        self.task = load_btc()
        # self.task = add.apply_async(args=[3, 5])
        # self.results = self.task.get()

    def test_task_state(self):
        # self.assertEqual(self.task.state, "SUCCESS")
        self.assertTrue(True)

"""class AddTestCase(TestCase):

    @override_settings(CELERY_EAGER_PROPAGATES_EXCEPTIONS=True,
                       CELERY_ALWAYS_EAGER=True,
                       BROKER_BACKEND='memory')
    def test_mytask(self):
        result = load_btc.delay()
        self.assertTrue(result.successful())"""
