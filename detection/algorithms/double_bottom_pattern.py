class DoubleBottomPattern(Pattern):
    def __init__(self, data, min_distance=50, percentage_drop=0.3, depth=20):
        super().__init__(data)
        self.min_distance = min_distance
        self.percentage_drop = percentage_drop
        self.depth = depth
        
    def identify(self):
        """
        Identifies double bottom patterns in the given data.
        """
        bottom1 = None
        bottom2 = None
        last_bottom = None
        
        for i in range(self.min_distance, len(self.data)-self.min_distance):
            window = self.data[i-self.min_distance:i+self.min_distance]
            min_val = min(window)
            max_val = max(window)
            if abs(min_val - max_val) > abs(max_val) * self.percentage_drop:
                if last_bottom is None or min_val < last_bottom:
                    if bottom1 is None:
                        bottom1 = min_val
                    else:
                        if bottom2 is None:
                            if min_val > bottom1:
                                bottom2 = min_val
                            else:
                                bottom1 = min_val
                        else:
                            if min_val > bottom2:
                                last_bottom = bottom2
                                bottom1 = None
                                bottom2 = None
                                self.matches.append((i-self.min_distance, i+self.min_distance))
        
    def plot(self, ax):
        """
        Plots the identified double bottom patterns in the given axis.
        """
        super().plot(ax)
        for match in self.matches:
            start, end = match
            ax.plot(self.data.index[start:end], self.data['Close'][start:end], color='r')
