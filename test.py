class HelloWorld:
    def __init__(self):
        self.message = "Hello, World!"
    
    def greet(self):
        print(self.message)


if __name__ == "__main__":
    hw = HelloWorld()
    hw.greet()