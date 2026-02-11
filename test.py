class HelloWorld:
    def __init__(self):
        self.message = "Hello, World! I am here to test GitHub!"
    
    def greet(self):
        print(self.message)
    
    def update_message(self, new_msg):
        self.message = new_msg
        
    def del_message(self):
        self.message = ""
        


if __name__ == "__main__":
    hw = HelloWorld()
    hw.greet()
    hw.update_message("Hello, GitHub")
    hw.greet()
    hw.del_message()
    hw.greet()