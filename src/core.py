
import random
from unicode_block_map import block_list, block_map


def get_block_map():
    block_map = dict()
    for block in block_list:
        start, end = block[0].split("..")
        
        name = block[1]
        # block_map[(int(start[2:], base=16), int(end[2:], base=16))] = name
        block_map[name] = (int(start[2:], base=16), int(end[2:], base=16))
    return block_map

def get_block(char: int):
    for b_start, b_end in block_map.keys():
        if b_start <= char <= b_end:
            return b_start, b_end
    return None

def random_from_block(block: tuple, raw_value: int=None, sigma: int=None, mode: str='normal'):
    if raw_value is None:
        return random.randint(*block)
    else:
        if sigma is None:
            if mode == 'normal':
                sigma = min(list(map(lambda x: abs(raw_value - x), block))) / 3
            else:
                sigma = 0

        return round(random.Random().gauss(raw_value, sigma))

def decay(data:str, half_life: float=None)->str:
    def func(value):
        code = ord(value)
        sigma = 1 / half_life if half_life and half_life > 0  else None
        result = chr(random_from_block(get_block(code), code, sigma=sigma))
        return result
    return "".join(list(map(func, list(data))))

def test(data: list)->None:
    for value in data:
        print(f"原始值为: {value}")
        print(f"变异值为: {decay(value, 1)}")

if __name__ == "__main__":
    from faker import Faker
    from collections import OrderedDict
    locales = OrderedDict([
        ('en_US', 1),
        ('zh_CN', 2),
        ('ja_JP', 3)
    ])
    fake = Faker(locales)
    # block_map = get_block_map()

    # old_texts = [fake.name() for i in range(10)]
    old_texts = [fake.address() for i in range(10)]
    test(old_texts)
