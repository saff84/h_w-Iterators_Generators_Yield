
from flatiterator import FlatIterator
from flat_generator import flat_generator


nested_list = [
	['a', 'b', 'c'],
	['d', 'e', 'f', 'h', False],
	[1, 2, None],
]

if __name__ == '__main__':
    option = int(input('''1 - итератор
2 - генератор
ваш выбор: '''))
    if option == 1:
        for item in FlatIterator(nested_list):
            print(item)
        flat_list = [item for item in FlatIterator(nested_list)]
        print(flat_list)
    elif option == 2:
        for item in flat_generator(nested_list):
            print(item)

