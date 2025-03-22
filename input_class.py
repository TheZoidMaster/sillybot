class Input:
    def __init__(self, activator: str, regex: bool = False):
        self.activator = activator
        self.regex = regex

    def to_dict(self):
        return {
            "activator": self.activator,
            "regex": self.regex
        }

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            activator=data.get("activator"),
            regex=data.get("regex")
        )
