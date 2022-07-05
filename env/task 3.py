"""
Интервалы устроены следующим образом – это всегда список из четного количества элементов.
Под четными индексами (начиная с 0) время входа на урок, под нечетными - время выхода с урока.
Нужно написать функцию, которая получает на вход словарь с интервалами и возвращает время общего присутствия
ученика и учителя на уроке (в секундах).
"""


def appearance(intervals):
    lesson = set(range(intervals['lesson'][0], intervals['lesson'][1]))
    pupil = set()
    tutor = set()

    for i in range(0, len(intervals['pupil']), 2):
        for j in list(range(intervals['pupil'][i], intervals['pupil'][i+1])):
            pupil.add(j)

    for i in range(0, len(intervals['tutor']), 2):
        for j in list(range(intervals['tutor'][i], intervals['tutor'][i+1])):
            tutor.add(j)

    return len(lesson & pupil & tutor)


tests = [
    {'data': {'lesson': [1594663200, 1594666800],
              'pupil': [1594663340, 1594663389, 1594663390, 1594663395, 1594663396, 1594666472],
              'tutor': [1594663290, 1594663430, 1594663443, 1594666473]},
     'answer': 3117
    },
    {'data': {'lesson': [1594702800, 1594706400],
              'pupil': [1594702789, 1594704500, 1594702807, 1594704542, 1594704512, 1594704513, 1594704564, 1594705150,
                        1594704581, 1594704582, 1594704734, 1594705009, 1594705095, 1594705096, 1594705106, 1594706480,
                        1594705158, 1594705773, 1594705849, 1594706480, 1594706500, 1594706875, 1594706502, 1594706503,
                        1594706524, 1594706524, 1594706579, 1594706641],
              'tutor': [1594700035, 1594700364, 1594702749, 1594705148, 1594705149, 1594706463]},
     'answer': 3577
    },
    {'data': {'lesson': [1594692000, 1594695600],
              'pupil': [1594692033, 1594696347],
              'tutor': [1594692017, 1594692066, 1594692068, 1594696341]},
     'answer': 3565
    },
]

if __name__ == '__main__':
    for i, test in enumerate(tests):
       test_answer = appearance(test['data'])
       print(test_answer)
       assert test_answer == test['answer'], f'Error on test case {i}, got {test_answer}, expected {test["answer"]}'
