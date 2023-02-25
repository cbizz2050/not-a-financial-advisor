class Pattern:
    def __init__(self, pattern_type, start_date, end_date, symbol, magnitude):
        self.pattern_type = pattern_type
        self.start_date = start_date
        self.end_date = end_date
        self.symbol = symbol
        self.magnitude = magnitude

    def to_dict(self):
        return {'pattern_type': self.pattern_type,
                'start_date': self.start_date,
                'end_date': self.end_date,
                'symbol': self.symbol,
                'magnitude': self.magnitude}


class FailSwingPattern(Pattern):
    def __init__(self, highs, lows):
        self.highs = highs
        self.lows = lows

    def is_valid(self):
        if len(self.highs) < 4 or len(self.lows) < 4:
            return False

        # Check for a lower high followed by a lower low
        if self.highs[-3] > self.highs[-1] and self.lows[-3] > self.lows[-1]:
            # Check for a higher low followed by a higher high
            if self.lows[-2] < self.lows[-4] and self.highs[-2] < self.highs[-4]:
                return True

        return False
