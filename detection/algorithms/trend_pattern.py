class TrendPattern(Pattern):
    """
    Detect an uptrend or downtrend in the financial data
    """

    def __init__(self, name: str, data: pd.DataFrame):
        super().__init__(name, data)

    def detect(self) -> Tuple[str, str]:
        if self.name == "uptrend":
            trend = self.data["close"].rolling(window=20).mean() > self.data["close"].rolling(window=200).mean()
        elif self.name == "downtrend":
            trend = self.data["close"].rolling(window=20).mean() < self.data["close"].rolling(window=200).mean()

        if trend.iloc[-1] and not trend.iloc[-2]:
            return (self.name, self.data.index[-1])
        else:
            return None