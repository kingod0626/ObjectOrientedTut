import random
import json

class Question:
    def __init__(self, description, answer):#初始函式表示物件
        #self指的皆為定義的物件
        self.description = description
        self.answer = answer

    def ask(self):#在class裡定義一個play方法/函示
        print(self.description)
        respond = input("你的答案:")
        if respond == self.answer:
            return True
        else:
            return False
class QuestionGame:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0

    def play(self):#遊玩=>定義get_question()要挑選的題數 並執行Class Question的ask()
        random_questions = self.get_question(5)
        for Question in random_questions:
            if Question.ask():
                print("答對了")
                self.score += 1
            else:
                print(f"答錯了, 答案是{Question.answer}")

        print(f"恭喜你, 總共答對{self.score}題")

    def get_question(self, num):#從題庫隨機挑題
        random_questions = random.sample(self.questions, num)
        return random_questions
        # questions_list = f.read()


with open("objectOriented.JSON", "r", encoding="utf-8") as f:#題庫的來源從json檔提取轉換成python能用的格式
    questions_list = json.loads(f.read())

questions=[]
for question in questions_list:
    des = question["description"]
    ans = question["answer"]
    q = Question(des, ans)
    questions.append(q)#在questions陣列加入題庫所有的題目

print(questions)
QuestionGame(questions).play()

