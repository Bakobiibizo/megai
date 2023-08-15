import json
from typing import List, Dict


class DataConverter:
    def __init__(self):
        pass

    def to_json(self, data: List[Dict[str, str]]):
        """
        Convert a list of dictionaries to a JSON string.

        Args:
            data (List[Dict[str, str]]): A list of dictionaries to be converted.

        Returns:
            A JSON string.
        """
        return json.dumps(data)

    def from_json(self, json_str: str):
        """
        Convert a JSON string to a list of dictionaries.

        Args:
            json_str (str): A JSON string to be converted.

        Returns:
            A list of dictionaries.
        """
        return json.loads(json_str)

    def validate(self, data: List[Dict[str, str]]):
        """
        Validate a list of dictionaries to check if \
            'content' and 'role' are strings.

        Args:
            data (List[Dict[str, str]]): A list of \
                dictionaries to be validated.

        Returns:
            True if all 'content' and 'role' are strings, \
                False otherwise.
        """
        return not any(
            not isinstance(item.get('content'), str)
            or not isinstance(item.get('role'), str)
            for item in data
        )

#  # Testing the DataConverter class
#  dc = DataConverter()
#
#  # Test data
#  test_data = [{"role": "user", "content": "Hello, assistant."}, {"role": "assistant", "content": "Hello, user."}]
#
#  # Test to_json
#  json_str = dc.to_json(test_data)
#  print(json_str)
#
#  # Test from_json
#  data = dc.from_json(json_str)
#  print(data)
#
#  # Test validate
#  valid = dc.validate(test_data)
#  print(valid)
#
#  # Test validate with invalid data
#  invalid_data = [{"role": "user", "content": 123}, {"role": "assistant", "content": "Hello, user."}]
#  invalid = dc.validate(invalid_data)
#  print(invalid)
#