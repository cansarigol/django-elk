from django.test import TestCase
import logging
import json

logger = logging.getLogger('django')


class Test(TestCase):
    def setUp(self):
        pass

    def test(self):
        x = {
        "name": "John",
        "age": 30,
        "city": "New York"
        }

        # convert into JSON:
        y = json.dumps(x)
        print(y)
        logger.error(y)
