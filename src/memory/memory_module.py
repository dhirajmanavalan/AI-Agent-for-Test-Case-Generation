class MemoryModule:

    def __init__(self):
        self.storage = {}

    def save(self, requirement: str, testcases: list):
        key = requirement.strip().lower()
        self.storage[key] = testcases

    def retrieve(self, requirement: str):
        key = requirement.strip().lower()
        return self.storage.get(key, None)