from random import choice
nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

def get_jokes(time):
    for i in range(time):
        joke = [choice(nouns), choice(adverbs), choice(adjectives)]
        print(joke)

get_jokes(2)