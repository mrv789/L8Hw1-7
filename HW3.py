class Listinput(Exception):
    def __init__(self, some_inp):
        self.some_inp = some_inp

list = []
while True:
    some_i = input('Введите число для добавления в список или stop для выхода: ')

    if some_i == 'stop':
        print(f'Список на момент выхода{list}')
        break

    try:
        if not some_i.isnumeric():
            raise Listinput('NaN!')
        list.append(int(some_i))
    except Listinput as error:
        print('Вы ввели не число')