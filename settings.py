import collections

class BMI:

    def __init__(self):

        self.bmi_dict = dict(
            {1: [0, 18.4, "Underweight", "Malnutrition risk"],
            2: [18.5, 24.9, "Normal weight", "Low risk"],
            3: [25, 29.9, "Overweight", "Enhanced risk"],
            4: [30, 34.9, "Moderately obese", "Medium risk"],
            5: [35, 39.9, "Severely obese", "High risk"],
            6: [40, 10000, "Very severely obese", "Very high risk"],
            })

