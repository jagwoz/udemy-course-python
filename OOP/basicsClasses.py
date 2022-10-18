from __future__ import annotations


class NewClass:
    attr = 5
    id = 0

    def __init__(self, parameter):
        """
        Empty class
        :param parameter: first parameter
        """
        self.list = [0 for _ in range(10)]
        self.param = parameter
        NewClass.id += 1
        self.id = NewClass.id
        pass  # constructor

    def method(self):
        return self.attr

    def method2(self, parameter: int, parameter2: bool) -> (bool, int):
        return parameter == self.param and parameter2, 2

    def method2(self, parameter: int, parameter2: bool) -> dict:
        return {"1st": parameter == self.param and parameter2, "2nd": 2}

    def future_method(self, parameter: NewClass):
        pass  # from __future__ import annotations

    def __str__(self):
        return "object in string"

    def __getitem__(self, item):
        return list[item]

    def __setitem__(self, key, value):
        self.list[key] = value

    def __len__(self):
        return len(list)

    @staticmethod
    def statMethod(value):
        pass
