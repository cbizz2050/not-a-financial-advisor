class BaseDetectionMethod:
    def __init__(self, pattern_params):
        self.pattern_params = pattern_params
        # TODO: add all other universal parameters here

    def detect_pattern(self, detection_event):
        # This method should be implemented by the derived classes
        raise NotImplementedError()