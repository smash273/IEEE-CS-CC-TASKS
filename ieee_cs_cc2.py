class IntervalMerger:
    def __init__(self):
        self.intervals = []

    def addInterval(self, start, end):
        self.intervals.append((start, end))
        self.intervals.sort()
        merged = []
        for interval in self.intervals:
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                merged[-1] = (merged[-1][0], max(merged[-1][1], interval[1]))
        self.intervals = merged

    def getIntervals(self):
        return self.intervals

    def user_choice(self):
        while True:
            print("\n Select the operation to be performed")
            print("1. Add interval")
            print("2. Display merged intervals")
            print("3. Exit")
            choice = input("Enter your choice ")
            if choice == "1":
                start = int(input("Enter start of interval "))
                end = int(input("Enter end of interval "))
                self.addInterval(start, end)
            elif choice == "2":
                print("Intervals after merging ", self.getIntervals())
            elif choice == "3":
                break
            else:
                print("Invalid choice")

if __name__ == "__main__":
    merger = IntervalMerger()
    merger.user_choice()
