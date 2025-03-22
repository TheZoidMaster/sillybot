import random
from typing import List
from input_class import Input
import re
import json


class Response:
    inputs = List[Input]
    outputs = List[str]

    def __init__(self, inputs: List[Input], outputs: List[str]):
        self.inputs = inputs
        self.outputs = outputs

    def getOutput(self, input: str) -> str:
        for i in range(len(self.inputs)):
            if self.inputs[i].regex:
                if re.search(self.inputs[i].activator, input):
                    return random.choice(self.outputs)
            else:
                if self.inputs[i].activator in input:
                    return random.choice(self.outputs)
        return None

    def to_dict(self):
        return {
            "inputs": [inp.to_dict() for inp in self.inputs],
            "outputs": self.outputs
        }

    def to_json(self) -> str:
        return json.dumps(self.to_dict())

    @classmethod
    def from_dict(cls, data: dict):
        inputs = [Input.from_dict(item) for item in data.get(
            "inputs", [])]
        return cls(inputs, data.get("outputs", []))

    @classmethod
    def from_json(cls, json_str: str):
        data = json.loads(json_str)
        return cls.from_dict(data)


def load_response(file_path: str) -> "Response":
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return Response.from_dict(data)
