
import os.path
from django.test import TestCase

from django.core.management import call_command

from api.lib import hubstate

class HubStateTestCases(TestCase):

    def setUp(self):
        self.hs = hubstate.HubState()


    def tearDown(self):
        self.hs.delete_file()


    def test_default_state_file_is_created(self):
        """ Test that a hubstate file is created by default.
        """
        self.assertTrue(os.path.exists(self.hs._filepath))


    def test_hubstate_file_can_be_deleted(self):
        """ Test that a hubstate file can be deleted.
        """
        self.assertTrue(os.path.exists(self.hs._filepath))
        self.hs.delete_file()
        self.assertFalse(os.path.exists(self.hs._filepath))


    def test_get_value_from_hubstate(self):
        """ Test we can get a key's value
        """
        self.assertTrue(self.hs.getkey(self.hs.STATE_KEY_IS_ONLINE))


    def test_set_value_to_hubstate(self):
        """ Test we can set a key's value
        """
        self.assertTrue(self.hs.getkey(self.hs.STATE_KEY_IS_ONLINE))
        self.hs.setkey(self.hs.STATE_KEY_IS_ONLINE, False)
        self.assertFalse(self.hs.getkey(self.hs.STATE_KEY_IS_ONLINE))


    def test_django_commands_to_toggle_hubstate(self):
        """ Test we can set hubstate using django management commands.
        """
        self.assertTrue(self.hs.getkey(self.hs.STATE_KEY_IS_ONLINE))

        call_command("set_hubstate_isactive_to_false")
        self.assertFalse(self.hs.getkey(self.hs.STATE_KEY_IS_ONLINE))

        call_command("set_hubstate_isactive_to_true")
        self.assertTrue(self.hs.getkey(self.hs.STATE_KEY_IS_ONLINE))
