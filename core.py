from abc import ABC

from consecution import Node


class Transform(Node, ABC):
    def transform(self, row: dict):
        raise NotImplementedError

    def process(self, row):
        transformed = self.transform(row)
        self._push(transformed)


class Load(Node, ABC):

    def process(self, row):
        self.load(row)

    def load(self, row: dict):
        raise NotImplementedError
