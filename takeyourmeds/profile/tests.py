from takeyourmeds.utils.test import TestCase

class SmokeTest(TestCase):
    def test_pks_match(self):
        self.assertEqual(self.user.profile.pk, self.user.pk)

    def test_has_group(self):
        self.assert_(self.user.profile.group)
