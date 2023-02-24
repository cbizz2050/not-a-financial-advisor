class PatternStorage:
    patterns = {}

    @classmethod
    def register_pattern(cls, pattern):
        cls.patterns[pattern.name] = pattern

    @classmethod
    def get_pattern(cls, name):
        return cls.patterns[name]

    @classmethod
    def get_all_patterns(cls):
        return cls.patterns
