import unittest

from mock import MagicMock
from pythontesting import unmarshaller

class UnmarshallerTest(unittest.TestCase):

    def test_unmarshall(self):
        db_object = MagicMock()
        db_object.get_name = MagicMock(return_value="aitor")
        db_object.get_age = MagicMock(return_value=27)

        result = unmarshaller.unmarshall(db_object)

        self.assertEqual(result, {"name": "aitor", "age": 27})
        db_object.get_name.assert_called_once_with()
        db_object.get_age.assert_called_once_with()
