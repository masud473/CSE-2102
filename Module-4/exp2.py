from exp1 import isfunction
def isInjective(pair:list[tuple[int]]):
    return isfunction(pair) and len(pair)==len(set([i[1] for i in pair]))

def isSurjective(pair:list[tuple[int]],codomain:set[int]):
    return isfunction(pair) and set([i[1] for i in pair])==codomain

def isBijective(pair:list[tuple[int]],codomain:set[int]):
    return isInjective(pair) and isSurjective(pair,codomain)
