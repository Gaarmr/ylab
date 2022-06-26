from itertools import combinations


def bananas(s) -> set:
    res = set()
    word = 'banana'
    numb_count = len(s) - len(word)
    pool = combinations(range(len(s)), numb_count)
    for i in pool:
        temp = list(s)
        for a in i:
            temp[a] = '-'
        updated_str = ''.join(temp)
        if updated_str.replace('-', '') == word:
            res.add(updated_str)
    return res


assert bananas("banann") == set()
assert bananas("banana") == {"banana"}
assert bananas("bbananana") == {"b-an--ana", "-banana--", "-b--anana", "b-a--nana", "-banan--a",
                     "b-ana--na", "b---anana", "-bana--na", "-ba--nana", "b-anan--a",
                     "-ban--ana", "b-anana--"}
assert bananas("bananaaa") == {"banan-a-", "banana--", "banan--a"}
assert bananas("bananana") == {"ban--ana", "ba--nana", "bana--na", "b--anana", "banana--", "banan--a"}
