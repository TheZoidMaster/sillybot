import random
from typing import List
import re
import json


class Response:
    inputs = List[str]
    outputs = List[str]

    def __init__(self, inputs: List[str], outputs: List[str]):
        self.inputs = inputs
        self.outputs = outputs

    def getOutput(self, input: str) -> str:
        for i in range(len(self.inputs)):
            if self.inputs[i] in input:
                return random.choice(self.outputs)
        return None

    def to_dict(self):
        return {
            "inputs": self.inputs,
            "outputs": self.outputs
        }

    def to_json(self) -> str:
        return json.dumps(self.to_dict())

    @classmethod
    def from_dict(cls, data: dict):
        return cls(data.get("inputs", []), data.get("outputs", []))

    @classmethod
    def from_json(cls, json_str: str):
        data = json.loads(json_str)
        return cls.from_dict(data)


def load_response(file_path: str) -> "Response":
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return Response.from_dict(data)
