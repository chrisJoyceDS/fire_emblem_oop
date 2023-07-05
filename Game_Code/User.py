class User:
    
    def __init__(self):
        self.name = self.user_name_input()
        
    def user_name_input(self):
        print('Enter your name:')
        self.name = input()
        print('Hello, ' + self.name)
            