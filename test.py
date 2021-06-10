import unittest
import json
import sys
import logging
from main import validating_json_with_schema, calculate_bmi

unittest.TestLoader.sortTestMethodsUsing = None
logging.basicConfig(stream=sys.stderr)
logger = logging.getLogger("TestBMI")
logger.setLevel(logging.ERROR)

class utils:

    sample_json = {
        "Gender": "Male",
        "HeightCm": 171,
        "WeightKg": 96
        }

    sample_json2 = {"random_text"}

    sample_json3 = {"Gender": "Male"}

    risk= dict({
            "Malnutrition risk": [167, 40, {"Gender": "Male", "HeightCm": 167, "WeightKg": 40}],
            "Low risk": [167, 60, {"Gender": "Female", "HeightCm": 167, "WeightKg": 60}],
            "Enhanced risk": [167 , 70, {"Gender": "Male", "HeightCm": 167, "WeightKg": 70}],
            "Medium risk": [170 , 90, {"Gender": "Female", "HeightCm": 170, "WeightKg": 90}],
            "High risk": [175, 110, {"Gender": "Male", "HeightCm": 175, "WeightKg": 110}],
            "Very high risk": [165, 120, {"Gender": "Male", "HeightCm": 165, "WeightKg": 120}]
        })

class TestBMI(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        # json schema path
        self.json_schema_path = "data/schema/input_schema.json"

    def test_101_validate_json(self):
        self.assertTrue(validating_json_with_schema(
            utils.sample_json, self.json_schema_path))

    def test_102_validate_json_error_case(self):
        error_json_files = ((utils.sample_json2, 'error json input'), (utils.sample_json3, 'error json input'))

        for sample_json, description in error_json_files:
            with self.subTest(description):
                self.assertFalse(validating_json_with_schema(
                    sample_json, self.json_schema_path))

    def test_103_malnutrition_ris(self):

        for key, value in utils.risk.items():
            with self.subTest():
                result = calculate_bmi(value[0], value[1], value[2])
                self.assertEqual(key, result['Health Risk'])

if __name__ == "__main__":
    unittest.main(verbosity=2)