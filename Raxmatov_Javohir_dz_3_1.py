# 1. Написать функцию num_translate(), переводящую числительные от 0 до 10 c английского на русский язык.

def nums_translate(eng):
    while True :
        nums = {'zero': 'ноль',
            'one': 'один',
            'two': 'два',
            'three': 'три',
            'four': 'четыре',
            'five': 'пять',
            'six': 'шесть',
            'seven': 'семь',
            'eight': 'восемь',
            'nine': 'девять',
            'ten': 'десять'
    }
        if eng.istitle() and nums.get(eng.lower()):
            return nums.get(eng.lower()).title()
        else:
            return nums.get(eng)

# print(nums_translate('eight'))
# print(nums_translate(input('Input an English number: ')))
