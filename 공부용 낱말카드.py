import pickle
from datetime import datetime
import random


class Card:
    total_counter = 0
    total_percentage = 0

    def __init__(self, q, a, c, c1):
        now = datetime.now()
        self.question = [q]
        self.answer = [a]
        self.commentary = [c]
        self.modify_date = ['{}/{} {}:{}'.format(now.month, now.day, now.hour, now.minute)]
        self.answer_month = []
        self.answer_day = []
        self.pop_counter = 0
        self.correct_counter = 0
        self.wrong_counter = 0
        self.skip_counter = 0
        self.able_switch = 'on'
        self.correct_percentage = 0
        self.incidence_correction = 0
        self.category = c1
        self.question_type = ''
        Card.total_counter += 1

    def print_info(self):
        return '{} {} / {} ({} %) {} 스킵'.format(self.question[-1][:12], self.correct_counter, self.pop_counter,
                                                round(self.correct_percentage, 2), self.skip_counter)

    def change_things(self):  # 자체 수정기능
        while True:
            now = datetime.now()
            choice = input('무엇을 수정할까요?\n1.문제 2.정답 3.해설 4.카테고리 5.활성/비활성 : ')
            if choice == '1':
                self.question.append(input('새로운 문제를 입력해주세요 : '))
                self.modify_date.append('{}/{} {}:{}'.format(now.month, now.day, now.hour, now.minute))
                break
            elif choice == '2':
                self.answer.append(input('새로운 정답을 입력해주세요 : '))
                self.modify_date.append('{}/{} {}:{}'.format(now.month, now.day, now.hour, now.minute))
                break
            elif choice == '3':
                self.commentary.append(input('새로운 해설을 입력해주세요 : '))
                self.modify_date.append('{}/{} {}:{}'.format(now.month, now.day, now.hour, now.minute))
                break
            elif choice == '4':
                new_category = input('새로운 카테고리명을 입력해주세요 : ')
                self.category = new_category
            elif choice == '5':
                self.switcher()
                break
            elif choice == '.':
                break
            else:
                pass

    def update_info(self, c_or_w):  # 정답률 업데이트, 정답률이 바닥을 기면 보정률도 수정, 수정시 보정률이 수정된다고 출력
        now = datetime.now()
        if c_or_w == 'c':
            self.correct_counter += 1
        else:
            self.wrong_counter += 1
        today_month = now.month
        today_day = now.day
        if today_day == 1:
            self.answer_day = []
        if today_month == 1:
            self.answer_month = []
        if today_month in self.answer_month:
            pass
        else:
            self.answer_month.append(today_month)
        if today_day in self.answer_day:
            pass
        else:
            self.answer_day.append(today_month)
        self.correct_percentage = self.correct_counter / self.pop_counter * 100
        Card.total_percentage = 0
        if self.pop_counter > 10 and self.correct_percentage >= 90:
            self.pop_up()
        elif self.pop_counter > 3 and self.correct_percentage <= 30 and self.incidence_correction != 2:
            incidence_correction = 2
        elif self.pop_counter > 3 and self.correct_percentage <= 50 and self.incidence_correction != 1:
            incidence_correction = 1
        per = 0
        for i in card_data:
            per += i.correct_percentage
        Card.total_percentage = per / len(card_data)

    def switcher(self):  # 스위치 온오프
        if self.able_switch == 'on':
            self.able_switch = 'off'
            print('\n비활성화 되었습니다.\n')
        else:
            self.able_switch = 'on'
            print('\n활성화 되었습니다.\n')

    def pop_up(self):  # 10번이상 출현, 90%이상 달성시 팝업
        while True:
            choice = input('이제 이 카드는 완벽히 외운것 같습니다.\n비활성화할까요?\n1.네 2.아니오')
            if choice == '1':
                self.switcher()
                input('\n외우느라 고생하셧습니다.\n')
            else:
                break

    def show_question(self, t):  # 문제를 출력해준다.
        if t == 1:
            a = [x.answer[-1] for x in card_data if x.category == self.category and x.question_type == '객관식']
            b = [self.answer[-1]]
            while len(b) != 5:
                c = random.choice(a)
                if c in b:
                    pass
                else:
                    b.append(c)
                random.shuffle(b)
            answer = b[int(input('문제 : {}\n보기:\n1. {}\n2. {}\n3. {}\n4. {}\n5. {}'.format(self.question[-1], b[0], b[1], b[2],
                                 b[3], b[4]))) - 1]
            if answer == self.answer[-1]:
                print('\n정답입니다!\n')
                self.update_info('c')
                self.pop_counter += 1
                return 'correct'
            elif answer == '.':
                return 'break'
            else:
                print('\n오답입니다...\n')
                self.update_info('w')
                self.pop_counter += 1
                print('정답은 : {} 입니다.\n>>{}\n'.format(self.answer[-1], self.commentary[-1]))
                return 'wrong'
        else:
            answer = input('문제 : {}\n정답 : '.format(self.question[-1]))
            if answer == self.answer[-1]:
                print('\n정답입니다!\n')
                self.update_info('c')
                self.pop_counter += 1
                return 'correct'
            elif answer == '>':
                self.skip_counter += 1
                return 'skip'
            elif answer == '.':
                return 'break'
            else:
                print('\n오답입니다...\n')
                self.update_info('w')
                print('정답은 : {} 입니다.\n>>{}\n'.format(self.answer[-1], self.commentary[-1]))
                self.pop_counter += 1
                return 'wrong'

    def updater(self):
        pass


class Statistics:
    def __init__(self):
        now = datetime.now()
        year = now.year
        month = now.month
        day = now.day
        weekday = now.weekday()
        answered_card_counter = 0
        correct_counter = 0
        wrong_counter = 0
        correct_rate = 0
        category = ''
        lowest_card = ''
        lowest_rate = 100





def main(card_data, statistics_data):
    now = datetime.now()
    if len(card_data) == 0:
        print('등록된 카드가 없습니다.\n문제추가하기 메뉴로 문제를 추가해보세요.')
    else:
        pass
    already = []
    first = input('1.문제풀기 2.낮은 정답률 문제풀기 3.메뉴보기 : ')
    if first == '1' or first == '2':
        second = int(input('1.객관식문제 2.주관식문제 : '))
    if first == '1':
        limit = [x for x in card_data if x.able_switch == 'on']
        while len(already) != len(limit):
            selected = random.choice(card_data)
            if selected in already or selected.able_switch == 'off':
                pass
            else:
                a = selected.show_question(second)
                if a == 'skip':
                    pass
                elif a == 'break':
                    break
                else:
                    already.append(selected)
        print('카드 학습을 종료합니다.')
    elif first == '2':
        difficult = [x for x in card_data if x.incidence_correction > 0 and x.able_switch == 'on']
        while len(already) != len(difficult):
            selected = random.choice(difficult)
            if selected in already:
                pass
            else:
                a = selected.show_question()
                if a == 'skip:':
                    pass
                else:
                    already.append(selected)
        print('카드 학습을 종료합니다.')
    while True:
        menu = input('\n1.모든카드보기 2.카드추가 3.카드수정 4.카드삭제 5.통계 6.종료 : ')
        if menu == '1':
            idx = 0
            print('')
            for i in card_data:
                idx += 1
                print('{}) '.format(idx) + i.print_info())
        elif menu == '2':
            q = input('\n문제를 입력하세요 : ')
            if q == '.':
                pass
            else:
                a = input('\n정답을 입력하세요 : ')
                if a == '.':
                    pass
                else:
                    c = input('\n해설을 입력하세요. 입력하지 않으려면 " . "을 입력하세요 : ')
                    c1 = input('\n문제의 카테고리를 입력하세요 : ')
                    card_data.append(Card(q, a, c, c1))
                    input('카드가 등록 되었습니다.')
        elif menu == '3':
            choice = int(input('몇번 문제를 수정 할까요? : ')) - 1
            if choice == '.':
                pass
            else:
                card_data[choice].change_things()
                print('\n성공적으로 변경 되었습니다.\n')
        elif menu == '4':
            choice = int(input('몇번 문제를 삭제할까요? : ')) - 1
            if choice == '.':
                pass
            else:
                choice2 = input('정말 삭제하시겠습니까?\n1.예 2.아니오 : ')
                if choice2 == '1':
                    del card_data[choice]
                    print('\n성공적으로 삭제 되었습니다.')
                else:
                    pass
        elif menu == '5':
            print('일간 정답률: {}% / 푼문제: {}')
        elif menu == '6':
            break
        else:
            pass
        with open('Card_data.bin', 'wb') as f:
            pickle.dump(card_data, f)
            pickle.dump(statistics_data, f)



def show_statistics():
    while True:
        pass
if __name__ == '__main__':
    try:
        with open('Card_data.bin', 'rb') as f:
            card_data = pickle.load(f)
            #statistics_data = pickle.load((f))
    except:
        card_data = []
        statistics_data = []
    for i in card_data:
        i.updater()
    statistics_data = []
    main(card_data, statistics_data)
