             #висильница
import random
def man(word):
    wrong=0
    st=[' ',
        '  ________        ',
        ' |       |        ',
        ' |       |        ',
        ' |       0        ',
        ' |      /|\       ',
        ' |      / \       ',
        '_|_______________ ' ]
    r=list(word)
    board=['__']*len(word)
    win=False
    print('Welcome to hell!')
    while wrong<len(st)-1:
        print('\n')
        msg='Vvedite bukvu: '
        char=input(msg)
        if char in r:
            cind=r.index(char)
            board[cind]=char
            r[cind]='$'
        else:
            wrong+=1
        print((' '.join(board)))
        e=wrong+1
        print('\n'.join(st[0:e]))
        if '__' not in board:
            print('You win! Slovo: ')
            print(' '.join(board))
            win=True
            break
    if not win:
        print('\n'.join(st[:wrong]))
        print('You looooose! Slovo: {}.'.format(word))
a=random.randint(0,10)
z=['дежавю','сирень','копчик','макака','тактик','зонтик','корень','сопляк','собака','лоскут']
x=str(z[a])
man(x)


             игра в кости
from random import randint
cube_1 = randint(1, 6)
cube_2 = randint(1, 6)
cube_sum = cube_1 + cube_2
if cube_sum == 7:
    print('победа')
    print(cube_1, cube_2, cube_sum)
elif cube_sum == 12:
    print('повторный бросок')
    print(cube_1, cube_2, cube_sum)
else:
    print('вы проиграли')
    print(cube_1, cube_2, cube_sum)


            крестики/нолики
board = list(range(1, 10))

def draw_board(board):
    print('-' * 13)
    for i in range(3):
        print('|', board[0+i*3], '|', board[1+i*3],'|', board[2+i*3], '|')
        print('-' * 13)

def take_input(player_token):
    valid = False
    while not valid:
        player_answer = input('Куда поставить ' + player_token + '?')
        try:
            player_answer = int(player_answer)
        except:
            print('Некоректный ввод. Введите число')
            continue
        if player_answer >= 1 and player_answer <=9:
            if (str(board[player_answer - 1]) not in 'XO'):
                board[player_answer - 1] = player_token
                valid = True
            else:
                print('Эта клетка уже занята')
        else:
            print('Введите число от 1 до 9')
def check_win(board):
    win_coord = ((0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6))
    for each in win_coord:
        if board[each[0]] == board[each[1]] == board[each[2]]:
            return board[each[0]]
    return False

def main(board):
    conter = 0
    win = False
    while not win:
        draw_board(board)
        if conter % 2 == 0:
            take_input('X')
        else:
            take_input('O')
        conter += 1
        if conter > 4:
            tmp = check_win(board)
            if tmp:
                print(tmp,'Победа!')
                win = True
                break
        if conter == 9:
            print('Ничья!')
            break
    draw_board(board)

main(board)



# подключаем модуль случайных чисел
import random

# подключаем модуль для графиков
import plotly
import plotly.graph_objs as go

# сколько денег будет на старте для каждой стратегии
startmoney = 1000000

# коэффициент ставки
c1 = 0.001

# количество побед и проигрышей
win = 0
loose = 0

# количество игр, сыгранный по первой стратегии
games = 0

# статистика для первой стратегии
balance1 = []
games1 = []

# статистика для второй стратегии
balance2 = []
games2 = []

# статистика для третьей стратегии
balance3 = []
games3 = []

# начинаем играть с полной суммой
# первая стратегия — отрицательное матожидание, как в казино
money = startmoney
# пока у нас ещё есть деньги
while money > 0:
    # ставка —  постоянная часть от первоначальной суммы
    bet = startmoney * c1
    # если ставка получилась больше, чем у нас осталось денег — ставим всё, что осталось, чтобы не уйти в минус
    if bet > money:
        bet = money
    # после ставки количество денег уменьшилось
    money -= bet

    # записываем очередную игру в статистику — деньги и номер игры
    balance1.append(money)
    games1.append(len(games1)+1)

    # крутим рулетку, на которой 18 чёрных чисел, 18 красных и одно зеро. Мы ставим на чёрное
    ball = random.randint(1,37)
    # пусть первые 18 будут чёрными — для простоты алгоритма
    # если наша ставка сыграла — мы попали в нужный диапазон
    if ball in range (1,19):
        # получаем назад нашу ставку в двойном размере
        money += bet * 2
        # увеличиваем количество побед
        win += 1
    else:
        # иначе — увеличиваем количество проигрышей
        loose += 1
games = win + loose
# выводим результат игры по первой стратегии
print("Выиграно ставок: " + str(win) + " (" + str(win/games * 100) + "%). " + " Проиграно ставок: " + str(loose)  + " (" + str(loose/games * 100) + "%). ")

# началась вторая стратегия, тоже стартуем с полной суммой
# вторая стратегия — с нулевым матожиданием
money = startmoney
# обнуляем статистику
win = 0
loose = 0

# начинаем играть с полной суммой
money = startmoney
# играем, пока есть деньги или пока мы не сыграем столько же игр, как и в первый раз
while (money > 0) and (win + loose < games):
    # ставка —  постоянная часть от первоначальной суммы
    bet = startmoney * c1
    # если ставка получилась больше, чем у нас осталось денег — ставим всё, что осталось, чтобы не уйти в минус
    if bet > money:
        bet = money
    # после ставки количество денег уменьшилось
    money -= bet

    # записываем очередную игру в статистику — деньги и номер игры
    balance2.append(money)
    games2.append(len(games2)+1)

    # крутим рулетку, на которой 18 чёрных чисел, 18 красных. Так как всего поровну, матожидание будет равно нулю.
    # Ставим, как и в прошлом случае, на чёрное
    ball = random.randint(1,36)
    # пусть первые 18 будут чёрными — для простоты алгоритма
    # если наша ставка сыграла — мы попали в нужный диапазон
    if ball in range (1,19):
        # получаем назад нашу ставку в двойном размере
        money += bet * 2
        # увеличиваем количество побед
        win += 1
    else:
        # иначе — увеличиваем количество проигрышей
        loose += 1

# выводим результат игры по второй  стратегии
print("Выиграно ставок: " + str(win) + " (" + str(win/games * 100) + "%). " + " Проиграно ставок: " + str(loose)  + " (" + str(loose/games * 100) + "%). ")



# началась третья стратегия, тоже стартуем с полной суммой
# третья стратегия — с положительным матожиданием
money = startmoney
# обнуляем статистику
win = 0
loose = 0

# начинаем играть с полной суммой
money = startmoney
# играем, пока есть деньги или пока мы не сыграем столько же игр, как и в первый раз
while (money > 0) and (win + loose < games):
    # ставка —  постоянная часть от первоначальной суммы
    bet = startmoney * c1
    # если ставка получилась больше, чем у нас осталось денег — ставим всё, что осталось, чтобы не уйти в минус
    if bet > money:
        bet = money
    # после ставки количество денег уменьшилось
    money -= bet

    # записываем очередную игру в статистику — деньги и номер игры
    balance3.append(money)
    games3.append(len(games3)+1)

    # крутим рулетку, на которой 18 чёрных чисел, 17 красных. Так как чёрных больше, а мы ставим на чёрное, то матожидание будет положительным
    # Ставим, как и в прошлом случае, на чёрное
    ball = random.randint(1,35)
    # пусть первые 18 будут чёрными — для простоты алгоритма
    # если наша ставка сыграла — мы попали в нужный диапазон
    if ball in range (1,19):
        # получаем назад нашу ставку в двойном размере
        money += bet * 2
        # увеличиваем количество побед
        win += 1
    else:
        # иначе — увеличиваем количество проигрышей
        loose += 1

# выводим результат игры по третьей  стратегии
print("Выиграно ставок: " + str(win) + " (" + str(win/games * 100) + "%). " + " Проиграно ставок: " + str(loose)  + " (" + str(loose/games * 100) + "%). ")

# строим графики
fig = go.Figure()
# для первой стратегии
fig.add_trace(go.Scatter(x=games1, y=balance1, name = "Отрицательное матожидание"))
# для второй
fig.add_trace(go.Scatter(x=games2, y=balance2, name = "Нулевое матожидание"))
# и для третьей
fig.add_trace(go.Scatter(x=games3, y=balance3, name = "Положительное матожидание"))
# выводим графики в браузер
fig.show()