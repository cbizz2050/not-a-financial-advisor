class Pattern:
    patterns = {}

    def __init__(self, name):
        self.name = name
        self.strategies = []

    def add_strategy(self, strategy):
        self.strategies.append(strategy)

    def get_strategies(self):
        return self.strategies

    def detect(self, data):
        for strategy in self.strategies:
            result = strategy.detect(data)
            if result is not None:
                return {"name": self.name, "strategy": strategy.__class__.__name__, "result": result}

    @classmethod
    def register_pattern(cls, pattern):
        cls.patterns[pattern.name] = pattern

    @classmethod
    def get_pattern(cls, name):
        return cls.patterns[name]

    @classmethod
    def get_all_patterns(cls):
        return cls.patterns
