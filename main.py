import Question

name = input("Vad heter du?")
print("Hej", name)
quiz = "Välkommen till mitt nätverksquiz"
print(quiz)

class question:
    def __init__(self):
        self.answer = None
        self.list = None

    question_list = [

    ]
    count = 0
    countfel = 0

    def init(self, answer, list):
        self.list = list
        self.answer = answer


def run_test(answers):
    score = 0
    for answer in [question]:
        answer = input(Question.question_list)
        if answer == Question.question_list:
            score += 1
    print("Du fick" + str(score) + "/" + str(len[question]) + "Rätt")
