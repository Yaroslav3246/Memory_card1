from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QButtonGroup, QPushButton, QLabel, QVBoxLayout,QHBoxLayout,QMessageBox,QRadioButton,QGroupBox
from random import shuffle
from random import randint

class Question():
    def __init__(self, question,right_answer,wrong1,wrong2,wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3
app = QApplication([])        
main_win = QWidget()
main_win.setWindowTitle('Memory Card')
question  = QLabel('какой национальности не существует?')
a2 = QPushButton('Ответить')
RadioGroupBox = QGroupBox('Варианты ответов ')
rbtn_1 = QRadioButton('Энцы')
rbtn_2 = QRadioButton('Смурфы')
rbtn_3 = QRadioButton('Чулымцы')
rbtn_4 = QRadioButton('Алеуты')

RadioGroup = QButtonGroup()
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)

layout_main = QVBoxLayout()
layuot_ans1 = QHBoxLayout()
layuot_ans2 = QVBoxLayout()
    
layuot_ans3 = QVBoxLayout()


layuot_ans2.addWidget(rbtn_1, alignment = Qt.AlignCenter)
layuot_ans2.addWidget(rbtn_2, alignment = Qt.AlignCenter)
layuot_ans3.addWidget(rbtn_3, alignment = Qt.AlignCenter)
layuot_ans3.addWidget(rbtn_4, alignment = Qt.AlignCenter)
layuot_ans1.addLayout(layuot_ans2)
layuot_ans1.addLayout(layuot_ans3)
RadioGroupBox.setLayout(layuot_ans1)




ansGroupBox = QGroupBox('Результаты')
lb_Question1 = QLabel('Правильно\неправильно')
lb_Question2 = QLabel('Правильный ответ')
v_line = QVBoxLayout()
v_line.addWidget(lb_Question1)
v_line.addWidget(lb_Question2)
ansGroupBox.setLayout(v_line)

ansGroupBox.hide()

layout_main.addWidget(question, alignment = Qt.AlignCenter )

layout_main.addWidget(RadioGroupBox, alignment = Qt.AlignCenter )
layout_main.addWidget(ansGroupBox)
layout_main.addWidget(a2, alignment = Qt.AlignCenter )

main_win.setLayout(layout_main)
def show_result():
    ''' показать панель ответов '''
    RadioGroupBox.hide()
    ansGroupBox.show()
    a2.setText('Следующий вопрос')

def show_qestion():
    ''' показать панель ответов '''
    RadioGroupBox.show()
    ansGroupBox.hide()
    a2.setText('Ответить')
    RadioGroup.setExclusive(False)
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True)
answers = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]
def ask(q: Question):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    question.setText(q.question)
    lb_Question2.setText(q.right_answer)
    show_qestion()

def next_question():
    main_win.total += 1
    print('Статистика\n-Всего вопросов:', main_win.total, '\n-Правильных ответов: ', main_win.score)
    cur_question = randint(0,len(questions_list) - 1)
    q = questions_list[cur_question]
    ask(q)
def click_OK():
     
    if a2.text() == 'Ответить':
        check_answer()
    else:
        next_question()
def show_correct(res):
    lb_Question1.setText(res)
    show_result()

def check_answer():
    if answers[0].isChecked():
        show_correct('Правильно!')
        main_win.score += 1
        print('Статистика\n-Всего вопросов:', main_win.total, '\n-Правильных ответов: ', main_win.score)
        print('Рейтинг: ', (main_win.score/main_win.total*100), '%')
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():

            show_correct('Неправильно')

q = Question('Государственный язык Бразилии', 'Португальский', 'Бразильский', 'Испанский', 'Итальянский')
ask(q)
main_win.score = 0
main_win.total = 0
a2.clicked.connect(click_OK)
main_win.cur_question = -1
questions_list = []
q1 = Question('В каком году был основан язык python?','1980','1960', '2000', '2015')
    
        

questions_list.append(q1)

q2 = Question('В каком году была создана игра Майнкрафт?','2009', '2015', '2000', '2010')
    
    
        

questions_list.append(q2)

q3 = Question('в каком году был создан первый компьютер?', '1927', '1950', '1990', '2000')
    
   
        

questions_list.append(q3)

q4 = Question('Сколько полос на флаге США?','13','10', '15', '5')
    
    
        
questions_list.append(q4)

q5 = Question('Где находится самая маленькая кость в теле человека?','ухо','нога', 'рука', 'палец')
    
    
        
questions_list.append(q5)

q6 = Question('Какая валюта Дании','Крона','Доллар', 'Евро', 'Динар')
    
    
        
questions_list.append(q6)

q7  = Question('Сколько элементов в переодической таблице?','118','80', '120', '100')
    
    
        

questions_list.append(q7)

q8 = Question(' Какой химический символ для серебра?', 'ag', 'Na','mg', 'ng')
questions_list.append(q8)




next_question()
main_win.show()
app.exec_()
