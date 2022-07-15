

def flat_generator(list):
    i = 0
    while i < len(list):
        for item in list[i]:
            yield item
        i += 1