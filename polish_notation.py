from datetime import datetime


class Session:
    def __enter__(self):
        print('Время запуска {}'.format(datetime.now().time()))
        self.start_time = datetime.now()
        return self

    def __exit__(self, *args):
        print('Время окончания работы {}'.format(datetime.now().time()))
        self.end_time = datetime.now()
        self.process_time = self.end_time - self.start_time
        print('Код был выполнен за: {}'.format(self.process_time))


polish_notation = list(input('Введите выражение вида: \nОПЕРАТОР(+ - * /) ЗНАЧЕНИЕ_1 ЗНАЧЕНИЕ_2: \n').split())


def calculation():
    try:
        assert float(polish_notation[1]) >= 0 and float(polish_notation[2]) >= 0, 'Введите положительное значение'
        if polish_notation[0] == '+':
            print(float(polish_notation[1]) + float(polish_notation[2]))
        elif polish_notation[0] == '-':
            print(float(polish_notation[1]) - float(polish_notation[2]))
        elif polish_notation[0] == '*':
            print(float(polish_notation[1]) * float(polish_notation[2]))
        elif polish_notation[0] == '/':
            try:
                answ = float(polish_notation[1]) / float(polish_notation[2])
                print(answ)
            except ZeroDivisionError:
                print('На ноль делить нельзя!')
        else:
            print('Введен неизвестный оператор')
    except AssertionError:
        print('Введите положительное значение')


if __name__ == "__main__":
    with Session():
        calculation()