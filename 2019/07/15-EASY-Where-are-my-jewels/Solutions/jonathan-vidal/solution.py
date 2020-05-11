def find_jewels(j, s):
    return len([stone for stone in s if s in set(j)])
