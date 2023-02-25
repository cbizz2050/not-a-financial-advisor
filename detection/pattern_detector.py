class PatternDetector:
    def __init__(self):
        self.detectors = []

    def add_detector(self, detector):
        self.detectors.append(detector)

    def detect_patterns(self, intraday_data, historical_data):
        detected_patterns = []
        for detector in self.detectors:
            detector.detect(intraday_data, historical_data)
            if detector.has_unstored_detections():
                detected_patterns += detector.get_unstored_detections()
        return detected_patterns
