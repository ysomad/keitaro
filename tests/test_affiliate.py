import random

from unittest import TestCase
from .client import get_client


class AffiliateTestCase(TestCase):
    api = get_client()

    def test_get_all(self):
        self.affiliate_all = AffiliateTestCase.api.affiliate.get()

        self.assertEqual(self.affiliate_all.status_code, 200)
        self.assertIsInstance(self.affiliate_all, list)
        self.assertIsInstance(self.affiliate_all[0], dict)

    def get_random_affiliate(self):
        return random.choice(self.affiliate_all)

    def test_get_by_id(self):
        affiliate_id = self.get_random_affiliate()['id']
        self.affiliate = AffiliateTestCase.api.affiliate.get(affiliate_id)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['id'], affiliate_id)

