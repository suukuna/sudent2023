from typing import Any

trash_list = ['abc',
              12,
              24.5,
              [12341, 89689.86],
              {'key': 'value'},
              ('after', 'before'), 'egoista',
              'isagiYoichi',
              111,
              14,
              1,
              16,
              {'wild_card': 'renoske'},
              ('Isae', 'Rin'),
              ['blue lock'],
              4.5,
              2523523643262.24,
              'jujutsu kaisen',
              ['alcohol'],
              {'sukuna': 'Itadori'},
              ['Gojo', 'six path'],
              ('shrimps', 'pasta', 'carbonara', 'desert'),
              {'George Hotz': 'programming'},
              'Harry Potter',
              'Dota 2',
              23423,
              1515326251161.1,
              7777777,
              666,
              'ElfBar',
              {'Rum1': 'Capitan Morgan'},
              ['mma', 'muay tai', 'jiu jitsu', 'box', ' '],
              ('Odessa', 'Ukraine'),
              ]


def is_str(item: Any) -> bool:
    if type(item) == str:
        return True
    else:
        return False


def add_phrase_two_filtered_list(item):
    return item + ' tigr ne tot kto tigr, a tot kto v poloskah'


o_str2 = list(filter(is_str, trash_list))

o_str_lambda = filter(lambda item: type(item) == str, trash_list)

add_phrase = list(map(add_phrase_two_filtered_list, o_str2))

add_phrase_lambda = list(map(lambda item: item + ' tigr ne tot kto tigr, a tot kto v poloskah', o_str_lambda))
for item in add_phrase_lambda:
    print(item)