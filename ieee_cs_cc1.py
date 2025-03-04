class MinMaxStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []
        self.max_stack = []

    def push(self, x):
        self.stack.append(x)
        if not self.min_stack or x <= self.min_stack[-1]:
            self.min_stack.append(x)
        if not self.max_stack or x >= self.max_stack[-1]:
            self.max_stack.append(x)

    def pop(self):
        if not self.stack:
            return None
        x = self.stack.pop()
        if x == self.min_stack[-1]:
            self.min_stack.pop()
        if x == self.max_stack[-1]:
            self.max_stack.pop()
        return x

    def top(self):
        return self.stack[-1] if self.stack else None

    def getMin(self):
        return self.min_stack[-1] if self.min_stack else None

    def getMax(self):
        return self.max_stack[-1] if self.max_stack else None

    def user_choice(self):
        while True:
            print("\n Choose the operation to be performed")
            print("1. Push an element")
            print("2. Pop an element")
            print("3. Get top element")
            print("4. Get minimum element")
            print("5. Get maximum element")
            print("6. Exit")
            choice = input("Enter your choice ")
            if choice == "1":
                x = int(input("Enter value to push "))
                self.push(x)
            elif choice == "2":
                print("Popped element ", self.pop())
            elif choice == "3":
                print("Top element ", self.top())
            elif choice == "4":
                print("Minimum element ", self.getMin())
            elif choice == "5":
                print("Maximum element ", self.getMax())
            elif choice == "6":
                break
            else:
                print("Invalid")

if __name__ == "__main__":
    stack = MinMaxStack()
    stack.user_choice()
