# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = code_from_dict(json.loads(json_string))

from typing import Any, TypeVar, Type, cast


T = TypeVar("T")


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def from_int(x: Any) -> int:
    assert isinstance(x, int) and not isinstance(x, bool)
    return x


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


class Code:
    gender: str
    height_cm: int
    weight_kg: int

    def __init__(self, gender: str, height_cm: int, weight_kg: int) -> None:
        self.gender = gender
        self.height_cm = height_cm
        self.weight_kg = weight_kg

    @staticmethod
    def from_dict(obj: Any) -> 'Code':
        assert isinstance(obj, dict)
        gender = from_str(obj.get("Gender"))
        height_cm = from_int(obj.get("HeightCm"))
        weight_kg = from_int(obj.get("WeightKg"))
        return Code(gender, height_cm, weight_kg)

    def to_dict(self) -> dict:
        result: dict = {}
        result["Gender"] = from_str(self.gender)
        result["HeightCm"] = from_int(self.height_cm)
        result["WeightKg"] = from_int(self.weight_kg)
        return result


def code_from_dict(s: Any) -> Code:
    return Code.from_dict(s)


def code_to_dict(x: Code) -> Any:
    return to_class(Code, x)
