import random
class Question:
    def __init__(self, question):
        self.question = question[2]
        self.options = question[3:7]
        self.answer = question[7]

    def show_question(self):
        print("\n###############################################\n")
        print(f"{self.question}\n")
        for i, option in enumerate(self.options, start=65):
            print(f"{chr(i)}. {option}\n")
    
    def show_question50(self):
        print("\n###############################################\n")
        print(f"{self.question}\n")
        print("\n###############################################\n")
        print("Opciones resultantes: \n")
        answerFlag = False
        for i, option in enumerate(self.options, start=65):
            if not self.check_answer(chr(i+32)):
                if not answerFlag:
                    print(f"{chr(i)}. {option}\n")
                answerFlag = True
            else:
                print(f"{chr(i)}. {option}\n")

    def check_answer(self, user_response):
        return user_response == self.answer