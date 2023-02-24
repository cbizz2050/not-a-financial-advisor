class PatternFactory:
    """
    Factory class for creating patterns.
    """
    def __init__(self, patterns):
        self.patterns = patterns

    def create_pattern(self, pattern_type, pattern_data):
        """
        Creates a pattern of the specified type using the given data.

        :param pattern_type: the type of the pattern to create
        :param pattern_data: the data to use to create the pattern
        :return: the created pattern
        """
        pattern = None
        for p in self.patterns:
            if p.pattern_type == pattern_type:
                pattern = p(pattern_data)
                break
        if not pattern:
            raise ValueError(f"No pattern of type {pattern_type} found.")
        return pattern
