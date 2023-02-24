# Pattern Detector

The `PatternDetector` class is a market analysis tool that identifies various chart patterns in stock market data. It is designed to work with the `MarketDataIngestor` class and the `Database` class to retrieve and store market data and detection results.

## Design

The `PatternDetector` class uses a modular design that allows for easy extension with new pattern detection algorithms. The core functionality of the class revolves around the `Pattern` class, which provides a framework for defining and detecting chart patterns. Each `Pattern` subclass implements its own detection algorithm and overrides the `detect` method.

The `PatternDetector` class provides a `detect` method that takes in a `MarketData` object and applies all of its defined patterns to the data. The detected patterns are stored in a dictionary that maps pattern names to a list of detection results.

## Usage

To use the `PatternDetector` class, first create an instance and then define any patterns that should be used for detection. For example, to detect a double bottom pattern:

```
detector = PatternDetector()
detector.add_pattern(DoubleBottomPattern())
data = MarketDataIngestor.download_data('AAPL', '1y')
detections = detector.detect(data)
```