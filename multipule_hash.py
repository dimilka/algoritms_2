def processing(name): # обработка информации, определение размерности хэш таблицы
    f = open(name, 'r', encoding='utf-8')
    lines = f.readlines()
    f.close()
    words = []
    for line in lines:
        words += line.strip().split()
    return words


def key_compiling(word):
    key = 0
    for i, val in enumerate(word):
        letter_ord = ord(val)
        if i % 2 == 0:
            letter_ord **= 2
        else:
            letter_ord **= 3
        key += letter_ord
    return key


def multiple_hash(word, m): # хэширование умножением
    key = key_compiling(word)
    c = 0.115555
    id = int(m * ((key * c) % 1))
    return id

# dictionary[new_key] = dictionary.pop(old_key)
def run():
    array_a = processing('input.txt')
    m = len(array_a)
    hash_tab = dict()
    for j in array_a:
        new_id = multiple_hash(j, m)
        if new_id in hash_tab:
            old = hash_tab[new_id]
            old.append(j)
            hash_tab[new_id] = list(set(old))
        else:
            hash_tab[new_id] = [j]

    array_b = processing('words.txt')
    for word in array_b:
        word_id = multiple_hash(word, m)
        if (word_id in hash_tab) and (word in hash_tab[word_id]):
            print(word)

run()
